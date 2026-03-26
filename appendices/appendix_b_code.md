# Appendix B: Code Walkthrough for Legal Analysis Tools

This appendix provides a walkthrough of the computational tools that implement the geometric legal framework. The codebase is organized as a Python library (`eris-law`) that constructs the judicial complex from case data, computes the legal metric, evaluates gauge invariance, and performs topological analysis. Full source code and documentation are available in the companion repository.

The walkthrough assumes familiarity with Python and basic numerical computing (NumPy, SciPy). Mathematical background is covered in Appendix A.

---

## B.1 Constructing the Judicial Complex

The judicial complex $\mathcal{K}$ is a weighted directed simplicial complex. Construction requires three inputs: a corpus of decided cases, an NLP pipeline for extracting legal dimensions, and a citation graph.

```python
import numpy as np
from eris_law import JudicialComplex, LegalDimensionExtractor

# Step 1: Load the case corpus
# Each case has: id, text, citations, metadata
cases = load_case_corpus("path/to/courtlistener_data/")

# Step 2: Extract 8-dimensional attribute vectors
# Uses linear probes on language-agnostic embeddings (LaBSE)
extractor = LegalDimensionExtractor(model="labse-v2")
for case in cases:
    case.attribute_vector = extractor.extract(case.text)
    # Returns np.array of shape (8,):
    # [d1_entitlement, d2_factual, d3_procedural, d4_statutory,
    #  d5_constitutional, d6_precedential, d7_remedial, d8_public]

# Step 3: Build the simplicial complex
complex = JudicialComplex()
for case in cases:
    complex.add_vertex(case.id, attributes=case.attribute_vector)
for case in cases:
    for cited_id in case.citations:
        complex.add_directed_edge(case.id, cited_id)
```

The `LegalDimensionExtractor` uses linear probes trained on annotated legal data (Chapter 3, Section 3.4). Each probe is a logistic regression classifier that maps the 768-dimensional LaBSE embedding to a scalar score on one of the eight legal dimensions. The probes are trained on a hand-annotated dataset of 2,000 case passages, validated at 82% mean accuracy across dimensions.

---

## B.2 Computing the Legal Metric

The legal metric combines the Mahalanobis distance with boundary penalties.

```python
from eris_law import LegalMetric

# Step 1: Estimate the covariance matrix from the corpus
Sigma = np.cov(
    np.array([c.attribute_vector for c in cases]).T
)  # shape: (8, 8)

# Step 2: Define boundary penalties
# Boundaries encode regime transitions (criminal/civil, federal/state)
boundaries = {
    "criminal_civil": {"dimensions": [0, 2, 6], "penalty": 2.0},
    "federal_state":  {"dimensions": [3, 4],    "penalty": 1.5},
    "constitutional": {"dimensions": [4],       "penalty": np.inf},
}

# Step 3: Create the metric
metric = LegalMetric(Sigma, boundaries)

# Step 4: Compute distances
d = metric.distance(case_a.attribute_vector, case_b.attribute_vector)
# Returns: sqrt((a-b)^T Sigma^{-1} (a-b)) + sum of boundary penalties
```

The covariance matrix $\Sigma$ is estimated from the corpus of decided cases. Different legal traditions produce different covariance structures: common law systems exhibit strong covariance between $d_6$ (precedential constraint) and $d_1$ (entitlement structure), while civil law systems exhibit weaker covariance on these dimensions but stronger covariance between $d_4$ (statutory authority) and $d_5$ (constitutional conformity).

---

## B.3 Gauge Invariance and the Legal Bond Index

The Legal Bond Index measures how far the legal system deviates from gauge invariance.

```python
from eris_law import GaugeTransformer, LegalBondIndex

# Step 1: Define gauge transformations
# Each transformation changes a protected characteristic
# while preserving legally relevant attributes
transformer = GaugeTransformer(
    transformations={
        "race":   lambda x: swap_demographic(x, "race"),
        "gender": lambda x: swap_demographic(x, "gender"),
        "ses":    lambda x: swap_demographic(x, "socioeconomic_status"),
    }
)

# Step 2: Compute the gauge violation tensor
# V[i, j] = J_j(tau_i(x)) - J_j(x)
# where i indexes the transformation, j indexes the outcome
V = np.zeros((len(transformer.transformations), n_outcome_dims))
for i, (name, tau) in enumerate(transformer.transformations.items()):
    for case in test_cases:
        original_outcome = model.predict(case)
        transformed_case = tau(case)
        transformed_outcome = model.predict(transformed_case)
        V[i] += (transformed_outcome - original_outcome)
    V[i] /= len(test_cases)

# Step 3: Compute the Legal Bond Index
lbi = LegalBondIndex(V)
print(f"Legal Bond Index: {lbi.total:.3f}")
print(f"  Race-sentence component: {V[0, 0]:.3f}")
print(f"  Gender-sentence component: {V[1, 0]:.3f}")
```

The `swap_demographic` function performs a counterfactual transformation: it modifies the demographic attributes of a case while preserving all legally relevant features. This is the computational implementation of Judge Rivera's mental experiment from Chapter 8. The gauge violation tensor $V_{ij}$ measures whether the transformation changes the predicted outcome.

A perfectly gauge-invariant system has $\|V\| = 0$. The baseline Legal Bond Index of 0.155 (from the Geometric Ethics experiments) indicates moderate gauge violation in the legal systems studied.

---

## B.4 Path Homology for Constitutional Review

The constitutional review algorithm checks whether adding a statute to the judicial complex preserves the path homology of the constitutional subcomplex.

```python
from eris_law import PathHomology, ConstitutionalReview

# Step 1: Extract the constitutional subcomplex
C = complex.subcomplex(
    vertex_filter=lambda v: v.attributes[4] > 0.5  # d5 > 0.5
)

# Step 2: Compute baseline path homology
H_before = PathHomology(C)
print(f"H_0: {H_before.betti(0)}")  # Connected components
print(f"H_1: {H_before.betti(1)}")  # Cycles (potential circuit splits)

# Step 3: Add the proposed statute as a new vertex + edges
C_new = C.copy()
C_new.add_vertex("proposed_statute", attributes=statute_vector)
for related_case in find_related_cases(statute_vector, C):
    C_new.add_directed_edge("proposed_statute", related_case)

# Step 4: Compute new path homology
H_after = PathHomology(C_new)

# Step 5: Constitutional review
review = ConstitutionalReview(H_before, H_after)
if review.homology_preserved():
    print("Statute is topologically consistent with Constitution")
else:
    print(f"Statute creates topological defect:")
    print(f"  New holes: {review.new_cycles()}")
    print(f"  Broken paths: {review.broken_paths()}")
```

The `PathHomology` class implements the path homology computation for directed graphs as described in Chapter 7. The key insight is that constitutional review reduces to a comparison: does the proposed statute change the topological structure of the constitutional subcomplex? If $\widetilde{H}_n^{\text{path}}(C_{\text{new}}) \neq \widetilde{H}_n^{\text{path}}(C)$ for any $n$, the statute has created or destroyed a topological feature.

---

## B.5 Precedent Search via A*

Legal reasoning is modeled as A* search on the judicial complex, with precedent as the heuristic field.

```python
from eris_law import LegalAstar, DoctrinalHeuristic

# Step 1: Define the heuristic field
# h(n) estimates cost-to-goal based on doctrinal similarity
heuristic = DoctrinalHeuristic(
    complex=complex,
    metric=metric,
    goal_attributes=target_case.attribute_vector
)

# Step 2: Run A* search
searcher = LegalAstar(complex, metric, heuristic)
path = searcher.search(
    start=current_case.id,
    goal=lambda v: metric.distance(v.attributes, target) < threshold
)

# Step 3: Analyze the path
print(f"Path length: {len(path.vertices)}")
print(f"Total legal friction: {path.total_cost:.3f}")
print(f"Is geodesic: {path.is_near_optimal(tolerance=0.05)}")
for edge in path.edges:
    print(f"  {edge.source} -> {edge.target}: cost={edge.weight:.3f}")
```

The doctrinal heuristic $h_D(n)$ estimates the cost-to-goal from the current case $n$ to the target legal state. An admissible heuristic --- one that never overestimates the true cost --- guarantees optimal pathfinding (A* optimality theorem, Appendix A). Well-developed areas of law have strong heuristics (the precedent clearly guides the analysis). Novel legal questions have weak heuristics (sparse precedent, flat guidance field).

---

## B.6 Stare Decisis as Parallel Transport

The parallel transport of legal rules along precedent paths.

```python
from eris_law import ParallelTransport

# Define a legal rule from the precedent case
rule = precedent_case.holding  # The rule established by the case

# Transport the rule along the citation path
transporter = ParallelTransport(complex, metric)
transported_rule = transporter.transport(
    rule=rule,
    path=[precedent_id, intermediate_1, intermediate_2, current_id]
)

# Measure holonomy (rotation accumulated along the path)
holonomy = transporter.holonomy(
    rule=rule,
    loop=[case_a, case_b, case_c, case_a]  # Closed loop
)
print(f"Holonomy magnitude: {holonomy.magnitude:.3f}")
# Non-zero holonomy indicates doctrinal evolution along the loop
```

---

## B.7 Dependencies and Environment

The `eris-law` library requires:

```
python >= 3.10
numpy >= 1.24
scipy >= 1.10
scikit-learn >= 1.3
torch >= 2.0          # For LaBSE embeddings
sentence-transformers  # For LaBSE model
networkx >= 3.0       # For graph operations
gudhi >= 3.8          # For persistent homology (optional)
```

Installation: `pip install eris-law`

The library runs on CPU for all operations except embedding extraction, which benefits from GPU acceleration. A T4 GPU processes approximately 1,000 case passages per minute through the LaBSE embedding pipeline.

---

## B.8 Limitations

The current implementation has several limitations, discussed in Chapter 16:

1. **Dimension extraction accuracy.** The linear probes achieve 82% mean accuracy. Errors in dimension extraction propagate to all downstream computations.

2. **Covariance estimation.** The $8 \times 8$ covariance matrix requires a large corpus for stable estimation. Small or domain-specific corpora may produce degenerate estimates.

3. **Boundary penalties.** The boundary penalty values ($\beta_k$) are set by expert judgment rather than learned from data. Sensitivity analysis is recommended.

4. **Scalability.** The path homology computation has worst-case complexity exponential in the number of vertices. The practical implementation uses filtration-based approximations that scale to corpora of approximately 100,000 cases.

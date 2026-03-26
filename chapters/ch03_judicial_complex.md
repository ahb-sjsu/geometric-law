# Chapter 3: The Judicial Reasoning Space

> *"The law is not a brooding omnipresence in the sky, but the articulate voice of some sovereign or quasi-sovereign that can be identified."*
> — Oliver Wendell Holmes Jr., *Southern Pacific Co. v. Jensen* (1917)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera's voting rights case has landed. A coalition of civil rights organizations challenges a state law that eliminates three days of early voting and requires a specific form of photo identification that, the plaintiffs allege, minority voters disproportionately lack. The state argues the law prevents fraud and streamlines election administration.*
>
> *Rivera must analyze this case. But what does "analyze" mean, precisely? She will consider the constitutional text (Equal Protection Clause, Fifteenth Amendment), the statutory framework (Voting Rights Act), the factual record (statistical evidence of disparate impact), the procedural posture (preliminary injunction hearing), the relevant precedent (Shelby County, Brnovich, Crawford), the available remedies (injunction, declaratory relief), and the public interest (democratic participation, election integrity).*
>
> *These are not random considerations. They are dimensions of a space — the space of legal states. Every case Rivera has ever decided occupies a point in this space, characterized by its position along each dimension. Her task is to locate the current case in this space, identify the nearest precedents, and navigate from the current legal state to the appropriate legal outcome.*
>
> *This chapter constructs that space.*

---

## The Need for a Legal Space

Chapter 1 argued that legal evaluation has geometric structure — that the binary verdict destroys information about the multi-dimensional reality of legal reasoning. Chapter 2 showed that the fundamental unit of legal analysis, the Hohfeldian relation, has the algebraic structure of the dihedral group $D_4$. Now we need a space in which these structures live.

What would such a space look like? We need three things:

1. **Points.** Each point should represent a legal state — a decided case, a pending dispute, a hypothetical configuration of rights and duties. The space must be large enough to contain every legal state that has existed or could exist.

2. **Structure.** The points cannot be unrelated. Legal states are connected by doctrinal relationships (one case cites another), by factual similarity (two cases involve the same type of dispute), and by hierarchical authority (a Supreme Court decision controls district court outcomes). The space must encode these connections.

3. **Measurement.** We need to be able to say that two legal states are "close" or "far apart." Two cases involving the same statute and similar facts are close. Two cases involving different areas of law, different jurisdictions, and different types of parties are far apart. The space must carry a notion of distance.

The mathematical object that provides all three — points, structure, and measurement — is a *weighted simplicial complex*. This chapter constructs the judicial complex $\mathcal{K}$ from the ground up.

## The Eight Legal Dimensions

### Why Dimensions?

A legal case is not a point on a line. It is a point in a multi-dimensional space, characterized by its position along several independent axes of analysis. When Judge Rivera analyzes the voting rights case, she does not ask a single question and arrive at a single answer. She asks at least eight distinct questions, each corresponding to a dimension of the legal space:

*What rights and duties are at stake? What are the causal and evidentiary facts? Does the court have jurisdiction? What statutes apply? Are constitutional provisions implicated? What do the precedents say? What remedies are available? What is the public interest?*

These questions are not reducible to one another. The constitutional question (does the law violate equal protection?) is logically independent of the procedural question (does the plaintiff have standing?). The statutory question (does the Voting Rights Act apply?) is independent of the remedial question (should the court issue an injunction or a declaratory judgment?). Each question defines an independent axis of variation — a dimension of the legal space.

### The Eight Dimensions

Legal analysis, across both common-law and civil-law traditions, has converged on a finite set of fundamental categories. We identify eight *legal dimensions*, each representing an axis along which a legal state can be characterized:

**Dimension $d_1$: Entitlement Structure.** The configuration of Hohfeldian positions — rights, duties, liberties, no-rights, powers, immunities, liabilities, disabilities — among the parties. This is the dimension that Chapter 2 analyzed. It answers the question: *who holds what legal positions relative to whom?*

In the voting rights case, the entitlement structure includes: voters' right to vote (Fifteenth Amendment), the state's power to regulate elections (Article I, Section 4), voters' potential immunity from burdensome restrictions (as a constitutional right), and the legislature's potential disability from enacting discriminatory restrictions.

**Dimension $d_2$: Factual Nexus.** The causal, evidentiary, and material connections between parties, actions, and harms. This is the empirical dimension — the facts of the case, the evidence supporting them, and the causal relationships they establish.

In the voting rights case: statistical evidence of disparate impact (what percentage of minority voters lack the required ID?), the legislature's stated purpose (fraud prevention), the factual record regarding actual fraud (how many documented cases exist?), and the causal link between the law and the alleged harm (does the ID requirement actually prevent eligible voters from voting?).

**Dimension $d_3$: Procedural Posture.** Standing, jurisdiction (personal, subject-matter, territorial), timeliness, exhaustion of remedies. This is the gatekeeper dimension — it determines whether the court can hear the case at all, before reaching the merits.

In the voting rights case: do the plaintiffs have standing (have they suffered an injury-in-fact, traceable to the challenged law, redressable by judicial relief)? Is the case ripe (has the law been enforced, or is the challenge premature)? Is the court the right forum (federal court for a federal constitutional challenge)? Has any applicable exhaustion requirement been met?

**Dimension $d_4$: Statutory Authority.** The legislative basis for claims and defenses; the statutory framework governing the dispute. This dimension identifies which statutes apply and how they interact.

In the voting rights case: the Voting Rights Act of 1965 (as amended), the state's election code, the Help America Vote Act, and any state constitutional provisions regarding voting. The interplay among these statutes — preemption, supplementation, conflict — is a critical analytical dimension.

**Dimension $d_5$: Constitutional Conformity.** The degree to which the legal configuration respects fundamental rights, structural provisions, and separation-of-powers constraints. This is the dimension that connects to the topological analysis of Chapter 7.

In the voting rights case: the Equal Protection Clause of the Fourteenth Amendment, the Fifteenth Amendment's prohibition on racial discrimination in voting, the First Amendment's protection of the right to political participation, and the structural question of whether the judiciary may override legislative judgments about election administration.

**Dimension $d_6$: Precedential Constraint.** The weight of stare decisis; binding versus persuasive authority; degree of factual similarity to controlling precedent. This dimension measures how tightly the case is constrained by prior decisions.

In the voting rights case: *Crawford v. Marion County* (2008, upholding a voter ID law under rational basis review), *Shelby County v. Holder* (2013, invalidating the VRA's coverage formula), *Brnovich v. DNC* (2021, narrowing Section 2 of the VRA). These precedents constrain Rivera's analysis — they set the edge weights in the judicial complex, making some legal paths cheap (consistent with precedent) and others expensive (requiring distinguishing or overruling).

**Dimension $d_7$: Remedial Scope.** The available relief — compensatory damages, injunctive relief, specific performance, declaratory judgment, punitive damages. This dimension captures what the court can actually *do* if it rules for one party.

In the voting rights case: preliminary injunction (blocking the law before the election), permanent injunction (striking the law permanently), declaratory judgment (declaring the law unconstitutional without enjoining it), or denial of relief (upholding the law). Each remedy has different legal requirements, different practical effects, and different precedential implications.

**Dimension $d_8$: Public Interest.** Societal implications, third-party effects, institutional consequences, regulatory impact. This dimension captures the broader context — the effects of the decision beyond the immediate parties.

In the voting rights case: the interest in democratic participation (every eligible citizen should be able to vote), the interest in election integrity (preventing fraud protects the value of every vote), the institutional implications (how much deference should courts give legislatures on election administration?), and the third-party effects (other states are watching — the decision will affect voting laws nationwide).

### Dimensionality as a Modeling Choice

The choice of eight dimensions is a modeling decision, not a derivation from first principles. It is empirically motivated — legal analysis across traditions and jurisdictions consistently employs these eight categories — but it is not the unique correct decomposition.

The framework accommodates modifications without altering the core theory. Additional dimensions (international law compliance, indigenous law considerations, environmental impact) can be added by extending the attribute vector from $\mathbb{R}^8$ to $\mathbb{R}^{8+k}$. Dimensions can be merged if empirical analysis shows they are redundant. The theorems of subsequent chapters hold for any finite-dimensional attribute space.

The key requirement is not a specific number of dimensions but the existence of *multiple, non-redundant axes of legal variation*. The eight-dimensional model is our best current empirical estimate. It may be refined by the NLP calibration pipeline described later in this chapter.

---

> **RUNNING EXAMPLE — MAPPING THE VOTING RIGHTS CASE**
>
> *Judge Rivera can now characterize her voting rights case as a point in eight-dimensional legal space. Using a scale from 0 to 1 on each dimension:*
>
> *$d_1$ (Entitlement): **0.9** — Strong entitlement structure. Voters have a fundamental right to vote; the state has limited power to restrict it.*
>
> *$d_2$ (Factual nexus): **0.7** — Substantial statistical evidence of disparate impact, but the causal chain (law $\to$ inability to vote) requires analysis of individual circumstances.*
>
> *$d_3$ (Procedural posture): **0.8** — Clear standing (voters who lack the required ID), ripe claim (law has been enacted), proper forum (federal court for federal constitutional challenge). Preliminary injunction posture adds urgency.*
>
> *$d_4$ (Statutory authority): **0.6** — Mixed. The VRA provides strong statutory authority, but post-Shelby County and post-Brnovich, the scope of Section 2 is narrower than pre-2013.*
>
> *$d_5$ (Constitutional conformity): **0.8** — Strong constitutional dimension. Equal Protection and Fifteenth Amendment are directly implicated.*
>
> *$d_6$ (Precedential constraint): **0.5** — Mixed precedent. Crawford supports the state; but the specific facts (disparate impact on minorities) may distinguish Crawford. The precedent does not cleanly resolve the case in either direction.*
>
> *$d_7$ (Remedial scope): **0.7** — Multiple remedies available (injunction, declaratory relief). Preliminary injunction standard (likelihood of success, irreparable harm, balance of equities, public interest) is well-established.*
>
> *$d_8$ (Public interest): **0.9** — Extremely high. Democratic participation is the paradigmatic public interest. Election integrity is also a legitimate public interest. The court must balance these.*
>
> *The attribute vector is $\mathbf{v} = (0.9, 0.7, 0.8, 0.6, 0.8, 0.5, 0.7, 0.9)$. This vector locates the case in eight-dimensional legal space.*

---

## The Judicial Complex: Construction

### Why a Simplicial Complex?

The space of legal states is fundamentally *discrete*. There are finitely many decided cases, finitely many statutes, and finitely many constitutional provisions. Legal states do not form a continuum — you cannot "continuously vary" a case from *Brown v. Board of Education* to *Plessy v. Ferguson*. Cases are discrete points, and the connections between them (citations, doctrinal relationships) are discrete edges.

The mathematical structure that captures discrete points with connections is a *simplicial complex* — a collection of vertices (points), edges (connections between pairs), triangles (connections among triples), and higher-dimensional simplices (connections among larger groups). A simplicial complex is a combinatorial object: it is defined by listing which subsets of vertices are connected, without any reference to a continuous ambient space.

But the legal simplicial complex has additional structure that a generic complex does not: it is *directed* (citations go from later cases to earlier cases, and authority flows from higher courts to lower courts) and *weighted* (some connections are stronger or cheaper to traverse than others). We therefore work with a *directed weighted simplicial complex*.

### Formal Construction

**Definition (Judicial Complex).** The *judicial complex* $\mathcal{K}$ is a directed weighted simplicial complex constructed as follows:

**Vertices (0-simplices).** Each decided case $c_i$ is a vertex. The vertex carries an *attribute vector* $\mathbf{v}(c_i) \in \mathbb{R}^8$, whose components are scores along the eight legal dimensions, and metadata including the deciding court's level $\ell(c_i) \in \{\text{trial}, \text{appellate}, \text{supreme}\}$ and the decision date $\tau(c_i)$.

**Directed edges (1-simplices).** A directed edge $c_i \to c_j$ exists when case $c_j$ cites case $c_i$ (the later case relies on the earlier one). Directionality encodes two asymmetries:

- *Temporal precedence:* $\tau(c_i) < \tau(c_j)$, since a case cannot cite a future decision. The citation graph is a directed acyclic graph (DAG) with respect to time.

- *Hierarchical authority:* $\ell(c_i) \geq \ell(c_j)$ for binding precedent. A district court must follow a Supreme Court precedent (low traversal cost), but the Supreme Court is not bound by the district court (high or infinite cost in the reverse direction).

The edge carries an *asymmetric* weight $w(c_i \to c_j) \geq 0$. The asymmetry is essential: the cost of traveling from a binding precedent to the current case is low (the precedent controls), while the cost of traveling in the reverse direction — from a lower court case to a higher court case — is high or infinite (the lower court does not bind the higher court).

**Higher simplices.** A $k$-simplex $[c_0, \ldots, c_k]$ exists when the cases form a *doctrinal cluster* — a set of mutually citing cases that collectively establish a legal doctrine. The simplex inherits a partial order from the temporal and hierarchical ordering of its vertices.

### Why Directionality Is Essential

The directionality of the judicial complex is not a technical nicety. It encodes the two most fundamental asymmetries of legal reasoning:

**Temporal asymmetry.** A case decided in 2024 can cite a 1954 precedent, but not vice versa. The citation graph is a DAG with respect to time. This means that legal reasoning is inherently *historical*: the path from a precedent to the current case follows the arrow of time, and the legal significance of the path depends on the temporal order.

If we forgot the directions — if we treated the citation graph as undirected — we would lose this temporal structure. We would treat "the current case cites *Brown*" and "*Brown* cites the current case" as equivalent, which is absurd: *Brown* was decided in 1954 and cannot cite a 2024 case.

**Hierarchical asymmetry.** A district court *must* follow a Supreme Court precedent (binding authority, low traversal cost), but the Supreme Court is not bound by any district court (no binding authority in the reverse direction, high or infinite traversal cost). The weight of an edge depends on its direction: $w(c_{\text{Supreme}} \to c_{\text{District}}) \neq w(c_{\text{District}} \to c_{\text{Supreme}})$.

If we forgot the directions, we would treat "the Supreme Court binds the district court" and "the district court binds the Supreme Court" as equivalent, which is constitutionally impossible.

The judicial complex is therefore inherently directed. This is not a choice — it is a structural feature of legal reasoning itself.

### The Judicial Complex Is a Concrete Object

Unlike the continuous manifolds of differential geometry, which are abstract mathematical constructions, the judicial complex $\mathcal{K}$ is a *concrete, constructible object*:

- **Vertices** come from case databases. In the United States, databases like Westlaw, LexisNexis, CourtListener, and the Caselaw Access Project contain every published federal and state court decision. Each decision is a vertex.

- **Directed edges** come from citation networks. Every judicial opinion cites prior cases, and these citations are catalogued in the databases. The citation is inherently directed: case $B$ cites case $A$, creating an edge $A \to B$.

- **Attribute vectors** come from the NLP scoring procedure. Each case's text is embedded using a language-agnostic model and scored on the eight dimensions by trained linear probes. The procedure is deterministic: the same case text always produces the same attribute vector.

- **Edge weights** are computed from the attribute vectors, the regime boundary structure, and the hierarchical cost function. The computation is a finite arithmetic operation.

The judicial complex is therefore not a theoretical abstraction that might someday be built. It is a data structure that can be constructed today from existing resources. The theoretical framework tells us *what to build*; the existing infrastructure provides *the materials*.

## Regime Boundaries

### Sharp Legal Transitions

Not all transitions between legal states are smooth. Some are discontinuous — sharp boundaries where the legal regime changes qualitatively:

- The shift from "no liability" to "strict liability" when a statutory threshold is crossed.
- The jurisdictional boundary between state and federal court.
- The constitutional line between protected and unprotected speech.
- The statute of limitations, which separates timely claims from time-barred claims.
- The "meeting of the minds" that converts negotiation into binding contract.

These boundaries are not gradual transitions. They are *phase boundaries* — sharp discontinuities where the rules change. A claim filed one day before the limitations period expires is timely; a claim filed one day after is barred. There is no continuous interpolation.

### Regime Filtration

In the simplicial complex framework, regime boundaries appear naturally as a *filtration* — a nested sequence of subcomplexes, each corresponding to a distinct legal regime.

**Definition (Regime Filtration).** The judicial complex admits a filtration

$$\emptyset = \mathcal{K}_0 \subset \mathcal{K}_1 \subset \cdots \subset \mathcal{K}_m = \mathcal{K}$$

where each $\mathcal{K}_\alpha$ is a subcomplex corresponding to a distinct legal regime. The inclusion $\mathcal{K}_\alpha \hookrightarrow \mathcal{K}_{\alpha+1}$ introduces edges that cross a regime boundary:

- **Jurisdictional boundaries** — edges between state-court and federal-court vertices.
- **Statutory thresholds** — edges between vertices on opposite sides of a statutory trigger (e.g., the "meeting of the minds" that converts negotiation into contract).
- **Constitutional limits** — edges between vertices inside and outside the domain of a fundamental right.
- **Precedential boundaries** — edges between vertices inside and outside the factual scope of a controlling holding.

The boundary penalty $\beta$ in the edge weight formula makes crossing these boundaries costly, modeling the sharp legal transitions that characterize regime shifts.

### Persistent Homology

The filtration structure enables *persistent homology* analysis: by varying the boundary penalty $\beta$, we can identify which topological features of the legal landscape are robust (persist across a range of penalties) and which are artifacts of a particular threshold choice.

A topological feature that persists as $\beta$ varies from 0 to a large value is a *structural* feature of the legal landscape — it reflects a genuine discontinuity in the law. A feature that appears only for a narrow range of $\beta$ values is an *artifact* — it depends on the specific penalty chosen and may not correspond to a real legal boundary.

This distinction is legally important. Some regime boundaries are sharp and universally recognized (the statute of limitations is either expired or it is not). Others are fuzzy and contested (where exactly is the line between commercial speech and political speech?). Persistent homology provides a formal tool for measuring the sharpness of legal boundaries.

---

> **RUNNING EXAMPLE — REGIME BOUNDARIES IN THE VOTING RIGHTS CASE**
>
> *Judge Rivera identifies three regime boundaries relevant to her case:*
>
> *1. **The constitutional boundary.** The Equal Protection Clause creates a boundary between permissible and impermissible voting restrictions. A law that classifies by race faces strict scrutiny (extremely costly to justify); a law that does not classify by race but has disparate impact faces a lower standard (the Brnovich factors). Rivera's first task is to determine which side of this boundary the challenged law occupies.*
>
> *2. **The statutory boundary.** Section 2 of the VRA creates its own boundary: a law that "results in" the denial of equal voting opportunity is prohibited. This boundary is distinct from the constitutional boundary — a law can be constitutional (surviving rational basis review) but still violate Section 2 (resulting in disparate impact). The two boundaries create a filtration: $\mathcal{K}_{\text{constitutional}} \subset \mathcal{K}_{\text{statutory}} \subset \mathcal{K}$.*
>
> *3. **The procedural boundary.** The preliminary injunction standard creates a boundary between cases where relief is warranted and cases where it is not. The four-factor test (likelihood of success, irreparable harm, balance of equities, public interest) defines a surface in the legal space: cases on one side get the injunction, cases on the other side do not.*
>
> *Each boundary imposes a penalty $\beta$ on edges that cross it. An argument that crosses the constitutional boundary — claiming, for instance, that a facially neutral law is actually a racial classification — incurs a heavy penalty because crossing that boundary requires establishing discriminatory intent, which is difficult to prove. An argument that stays within the statutory boundary (Section 2 disparate impact) avoids the constitutional crossing but faces the Brnovich factors.*
>
> *Rivera's analysis is, in geometric terms, a search for the least-costly path from the plaintiffs' position to the desired remedy — the path that crosses the fewest regime boundaries and incurs the lowest total penalties.*

---

## From Complex to Continuum

### The Approximation Theorem

In the limit of dense case law — when decided cases tile the space of legal configurations finely — the weighted simplicial complex $\mathcal{K}$ approximates a continuous Riemannian manifold $\mathcal{J}$ with metric $g_{ij}$. The edge weights $w(c_i, c_j)$ converge to geodesic distances $ds^2 = g_{ij} \, dx^i \, dx^j$, and the simplicial homology $H_n(\mathcal{K}; \mathbb{Z})$ converges to the singular homology $H_n(\mathcal{J}; \mathbb{Z})$.

We use the continuous notation where it clarifies the theoretical structure (for stating Noether-type balance principles, for instance), but the computational framework is discrete throughout. The judicial complex is a finite object, and all computations on it are finite.

The continuum limit is useful as a *theoretical tool*, not as a computational method. It tells us that the concepts we borrow from differential geometry — curvature, geodesics, parallel transport, holonomy — have well-defined analogues in the discrete setting. The discrete complex is primary; the continuous manifold is its asymptotic approximation.

### Why Not Start with a Manifold?

One might ask: why not define the legal space as a continuous manifold from the start, and treat decided cases as sample points on it? This is the approach taken by some machine learning models of legal reasoning, which embed cases in a continuous vector space and compute distances using standard metrics.

The answer is that continuity is a *fiction* in the legal domain. Legal states are discrete: there are finitely many decided cases, and each case is a distinct point. The transition between "liable" and "not liable" is a sharp boundary, not a continuous gradient. The hierarchical authority structure is a discrete lattice (trial $<$ appellate $<$ supreme), not a continuous ordering.

Starting with a simplicial complex respects the discrete nature of legal data. The continuum limit is then a *theorem* — a result that tells us when continuous methods provide good approximations — not an *assumption* that forces us to smooth over the sharp boundaries that are essential to legal reasoning.

## Constructing the Attribute Vectors

### From Case Text to Legal Coordinates

The attribute vector $\mathbf{v}(c_i) \in \mathbb{R}^8$ is the fundamental datum of the judicial complex: it locates each decided case in eight-dimensional legal space. But how do we compute it?

The answer is an NLP pipeline that mirrors the methodology validated in the Geometric Ethics programme:

**Step 1: Embedding.** Given the text $t_i$ of a judicial opinion, compute a multilingual embedding $\mathbf{e}(t_i) \in \mathbb{R}^d$ using a pre-trained sentence encoder such as LaBSE. LaBSE produces 768-dimensional embeddings that are language-invariant — the same legal concept in English, Spanish, or Mandarin maps to the same region of embedding space.

**Step 2: Dimension scoring.** Train eight linear probes $f_k: \mathbb{R}^d \to [0, 1]$ ($k = 1, \ldots, 8$), one for each legal dimension $d_k$. Each probe is a logistic regression classifier trained on a labeled corpus of legal texts annotated for the presence or absence of each dimension. The output is the attribute vector:

$$\mathbf{v}(c_i) = \bigl(f_1(\mathbf{e}(t_i)), \; f_2(\mathbf{e}(t_i)), \; \ldots, \; f_8(\mathbf{e}(t_i))\bigr) \in [0,1]^8$$

This architecture directly replicates the methodology validated in the parent framework, where nine moral-dimension probes achieved $F_1 = 0.74\text{--}0.91$.

**Step 3: Covariance estimation.** From the full corpus of $N$ scored cases, estimate the $8 \times 8$ covariance matrix $\hat{\Sigma}$ of the attribute vectors:

$$\hat{\Sigma} = \frac{1}{N-1} \sum_{i=1}^{N} (\mathbf{v}(c_i) - \bar{\mathbf{v}})(\mathbf{v}(c_i) - \bar{\mathbf{v}})^T$$

This matrix captures cross-dimensional dependencies and is used in the Mahalanobis edge-weight formula developed in Chapter 4.

### Determinism and Reproducibility

A legally authoritative scoring system must be *deterministic*: the same case text must produce the same attribute vector every time. The pipeline achieves this through two design choices:

1. **Fixed embeddings.** The embedding model is frozen at a specific version. Its weights are not updated during or after deployment. The same input text always produces the same embedding vector $\mathbf{e}(t_i)$.

2. **Linear probes.** Logistic regression is a deterministic function: given fixed weights $\mathbf{w}_k$ and a fixed embedding $\mathbf{e}$, the score $f_k(\mathbf{e}) = \sigma(\mathbf{w}_k^T \mathbf{e} + b_k)$ is uniquely determined. There is no sampling, temperature parameter, or non-deterministic decoding.

This contrasts sharply with LLM-based scoring, where the same prompt can produce different outputs across runs (due to sampling), across model versions (due to weight updates), and across providers (due to different fine-tuning). An LLM-scored attribute vector is a *random variable*; a probe-scored attribute vector is a *fixed function* of the input text. For a system whose outputs may inform legal decisions, this distinction is dispositive.

### Validation: Preventing Probe Hallucination

A critical concern for any NLP-based scoring pipeline is *probe hallucination*: the risk that the linear probes assign confident but incorrect dimension scores. We address this through four mechanisms:

1. **Ground-truth calibration.** A validation set of approximately 200 cases is scored by legal experts (law professors or experienced practitioners) on all eight dimensions. The probes' $F_1$ scores against this ground truth provide the quality floor.

2. **Confidence thresholding.** Scores near 0.5 (low confidence) are flagged as uncertain. Only cases where all eight probes exceed a confidence threshold $|p_k - 0.5| > \delta$ are used for metric calibration.

3. **Consistency checks.** Legal dimensions have known structural constraints: procedural posture ($d_3$) should be high in cases that turn on standing or jurisdiction; remedial scope ($d_7$) should correlate with the presence of damages language.

4. **Ablation.** Remove each probe in turn and measure the effect on downstream tasks. Probes that contribute noise rather than signal are detected by ablation.

## The Legal Space in Practice

### What the Judicial Complex Looks Like

Imagine the judicial complex for a single area of law — say, employment discrimination under Title VII. The complex would contain:

- **Vertices:** Thousands of decided cases, from the Supreme Court's foundational decisions (*Griggs v. Duke Power*, *McDonnell Douglas v. Green*, *Texas Department of Housing v. Inclusive Communities Project*) down to individual district court rulings.

- **Edges:** Tens of thousands of citation links, each directed from the cited case to the citing case. The edges form a dense network in some regions (frequently litigated issues like burden-shifting) and sparse in others (novel questions like AI-driven discrimination).

- **Attribute vectors:** Each case scored on eight dimensions. *McDonnell Douglas* scores high on statutory authority ($d_4$) and precedential constraint ($d_6$), moderate on factual nexus ($d_2$), and relatively low on constitutional conformity ($d_5$) because it is a statutory rather than constitutional case.

- **Regime boundaries:** The boundary between disparate treatment and disparate impact; the boundary between Title VII and Section 1981; the boundary between individual and pattern-or-practice claims.

- **Edge weights:** Low for edges connecting closely related cases within the same doctrine (traversing from one McDonnell Douglas case to another is easy), high for edges crossing doctrinal boundaries (traversing from a disparate treatment case to a disparate impact case requires establishing different elements).

The complex is a concrete computational object. It can be visualized as a directed graph with weighted edges, where the layout reflects the attribute-vector distances and the edge thickness reflects the weight.

### How Judges Navigate the Complex

When Judge Rivera analyzes the voting rights case, she is — in the framework's terms — performing a search through the judicial complex:

1. She locates the current case in eight-dimensional space (the attribute vector $\mathbf{v}$).
2. She identifies nearby vertices (precedents with similar attribute vectors).
3. She evaluates directed paths from the precedents to the current case (doctrinal arguments).
4. She assesses which paths cross regime boundaries (constitutional challenges, statutory thresholds).
5. She selects the path with the lowest total cost (the most legally persuasive argument).

This is precisely the $A^*$ pathfinding algorithm, which Chapter 6 will develop formally. The judicial complex is the graph on which the search operates.

---

> **RUNNING EXAMPLE — NEIGHBORING CASES IN THE VOTING RIGHTS COMPLEX**
>
> *Judge Rivera identifies the nearest precedents to her voting rights case — the vertices in $\mathcal{K}$ closest to her case's attribute vector $(0.9, 0.7, 0.8, 0.6, 0.8, 0.5, 0.7, 0.9)$:*
>
> *1. **Crawford v. Marion County (2008):** Attribute vector approximately $(0.7, 0.5, 0.9, 0.5, 0.7, 0.8, 0.6, 0.7)$. High procedural posture (case went to the Supreme Court with full factual record), high precedential constraint (it is a controlling precedent). But the factual nexus is weaker (less evidence of disparate impact), and the entitlement structure scores lower (the Court applied a more deferential standard). Distance from Rivera's case: moderate.*
>
> *2. **Shelby County v. Holder (2013):** Attribute vector approximately $(0.8, 0.4, 0.9, 0.8, 0.9, 0.9, 0.7, 0.9)$. Very high on constitutional conformity and precedential constraint (it is a landmark decision), but the factual nexus differs significantly (Shelby County challenged the coverage formula, not a specific voter ID law). Distance: relatively large on $d_2$ but small on $d_5$.*
>
> *3. **Brnovich v. DNC (2021):** Attribute vector approximately $(0.8, 0.6, 0.9, 0.7, 0.6, 0.9, 0.6, 0.8)$. The most recent precedent, with the highest precedential constraint. The factual nexus is moderately close (voting restrictions with alleged disparate impact). But the constitutional conformity dimension is lower (the Court analyzed Section 2 rather than the Constitution directly).*
>
> *Rivera can now compute the edge weights between her case and each precedent. The cheapest path — the path of least legal resistance — is the one she should follow if the precedents are correctly decided. If the cheapest path leads to a different outcome than her analysis of the constitutional text suggests, she faces a tension between precedential constraint ($d_6$) and constitutional conformity ($d_5$) — a tension that is now visible in the geometry of the complex rather than hidden in the ambiguity of prose.*

---

## The Judicial Complex and Legal Theory

### The Framework Is Neither Formalist Nor Realist

The oldest debate in jurisprudence is the tension between legal formalism (legal outcomes are determined by logical application of rules) and legal realism (legal outcomes are determined by human judgment, policy, and social context).

The judicial complex is *neither* formalist *nor* realist but *structuralist*: it is the space in which both formal rules (regime boundaries, constitutional constraints) and contextual factors (edge weights, precedential deformation) operate.

The formalist insight — that legal reasoning has structure — is preserved. The complex has a definite topology, a filtration of regime boundaries, and a gauge group of Hohfeldian symmetries.

The realist insight — that context, policy, and judgment shape outcomes — is captured by the *edge weights*, which are context-dependent and calibrated by human practice. Different judges may assign different weights. Different legal traditions may use different metrics. The framework does not determine the metric; it provides the space within which different metrics compete.

### Hart's Core and Penumbra

H.L.A. Hart distinguished between the "core" of a legal rule (where its application is clear and uncontested) and the "penumbra" (where its application is uncertain). This distinction maps naturally onto the stratified structure of the judicial complex:

- The **core** of a legal rule corresponds to the *interior* of a stratum — a region where the rule's application is smooth and the metric is well-calibrated.
- The **penumbra** corresponds to the *neighborhood of a stratum boundary* — a region where the rule's application is uncertain and the metric is poorly calibrated.

Cases in the core are easy: they are well inside a stratum, surrounded by consistent precedents, with clear attribute vectors. Cases in the penumbra are hard: they are near a boundary, where small changes in the facts can move the case from one stratum to another, and the precedents point in different directions.

### Sunstein's Incompletely Theorized Agreements

Cass Sunstein argued that legal systems function through "incompletely theorized agreements" — situations where parties agree on the outcome but disagree on the reasons. In the framework's terms, these are regions where parties agree on the *stratum structure* but disagree on the *metric*: they agree on which legal dimensions are relevant but disagree on how much each matters.

The framework makes this disagreement precise. Two judges who agree that the voting rights case involves entitlement structure, constitutional conformity, and public interest, but disagree on their relative weights, are using different metrics on the same space. Their disagreement is not about the structure of the problem but about how to measure distances within it.

### Dworkin's Law as Integrity

Ronald Dworkin argued that law should be interpreted according to the principles that best "fit and justify" existing legal practice. In the framework's terms, "integrity" is *topological consistency*: the legal system satisfies integrity when its constitutional constraint manifold has the expected path homology and all Wilson loops are trivial. A body of law that has non-trivial Wilson loops — hidden contradictions detectable by traversing cycles of precedent — lacks integrity in Dworkin's sense.

## Chapter Summary

1. Legal analysis operates in an eight-dimensional space, with each dimension corresponding to a fundamental category of legal analysis: entitlement structure, factual nexus, procedural posture, statutory authority, constitutional conformity, precedential constraint, remedial scope, and public interest.

2. The judicial complex $\mathcal{K}$ is a directed weighted simplicial complex whose vertices are decided cases, whose directed edges are citations, and whose attribute vectors encode positions along the eight legal dimensions.

3. Directionality is essential: it encodes temporal asymmetry (cases cannot cite future decisions) and hierarchical asymmetry (higher courts bind lower courts, not vice versa).

4. Regime boundaries — jurisdictional limits, statutory thresholds, constitutional boundaries — appear as a filtration of the complex. Crossing a boundary incurs a penalty, modeling the sharp transitions of legal regime changes.

5. The complex is a concrete, constructible object: vertices come from case databases, edges from citation networks, and attribute vectors from an NLP scoring pipeline.

6. In the dense-case limit, the complex approximates a continuous Riemannian manifold, connecting the discrete framework to the tools of differential geometry.

---

## Worked Example: Constructing a Mini-Complex

Consider a simplified judicial complex containing five cases in the area of voter ID law:

| Case | Court | Year | $d_1$ | $d_2$ | $d_3$ | $d_4$ | $d_5$ | $d_6$ | $d_7$ | $d_8$ |
|------|-------|------|--------|--------|--------|--------|--------|--------|--------|--------|
| $c_1$: *Harper v. Virginia* | Supreme | 1966 | 0.9 | 0.6 | 0.9 | 0.3 | 0.9 | 0.7 | 0.8 | 0.9 |
| $c_2$: *Crawford v. Marion County* | Supreme | 2008 | 0.7 | 0.5 | 0.9 | 0.5 | 0.7 | 0.8 | 0.6 | 0.7 |
| $c_3$: *Shelby County v. Holder* | Supreme | 2013 | 0.8 | 0.4 | 0.9 | 0.8 | 0.9 | 0.9 | 0.7 | 0.9 |
| $c_4$: *Brnovich v. DNC* | Supreme | 2021 | 0.8 | 0.6 | 0.9 | 0.7 | 0.6 | 0.9 | 0.6 | 0.8 |
| $c_5$: Rivera's case | District | 2026 | 0.9 | 0.7 | 0.8 | 0.6 | 0.8 | 0.5 | 0.7 | 0.9 |

**Citation edges (directed):**
- $c_1 \to c_2$ (*Crawford* cites *Harper*): hierarchical cost $h = 0$ (same level, Supreme to Supreme).
- $c_1 \to c_3$ (*Shelby County* cites *Harper*): $h = 0$.
- $c_2 \to c_4$ (*Brnovich* cites *Crawford*): $h = 0$.
- $c_3 \to c_4$ (*Brnovich* cites *Shelby County*): $h = 0$.
- $c_2 \to c_5$ (Rivera's case cites *Crawford*): $h = 0$ (binding: Supreme Court to district court).
- $c_4 \to c_5$ (Rivera's case cites *Brnovich*): $h = 0$ (binding).

**Edge weights.** For the edge $c_2 \to c_5$ (*Crawford* to Rivera's case):
- Attribute-vector difference: $\Delta \mathbf{v} = (0.2, 0.2, -0.1, 0.1, 0.1, -0.3, 0.1, 0.2)$
- Mahalanobis distance: $\Delta \mathbf{v}^T \Sigma^{-1} \Delta \mathbf{v}$ (requires the covariance matrix)
- Regime boundary: no boundary crossing (same area of law, same constitutional framework)
- Hierarchical cost: $h = 0$ (binding precedent)
- Total weight: the Mahalanobis distance plus any boundary penalties

For the edge $c_4 \to c_5$ (*Brnovich* to Rivera's case):
- $\Delta \mathbf{v} = (0.1, 0.1, -0.1, -0.1, 0.2, -0.4, 0.1, 0.1)$
- The large negative component on $d_6$ (precedential constraint drops from 0.9 to 0.5) reflects that Rivera's case is less constrained by precedent than *Brnovich* was.
- Total weight: comparable to the *Crawford* edge, but the dimensional profile differs.

This mini-complex illustrates the basic structure: cases as vertices, citations as directed edges, attribute vectors as coordinates, and edge weights as costs of doctrinal traversal. The full judicial complex for voting rights law would contain thousands of cases and tens of thousands of edges, but the structure is the same.

---

## Technical Appendix

**Definition (Directed Weighted Simplicial Complex).** A *directed weighted simplicial complex* is a tuple $\mathcal{K} = (V, E, S, \mathbf{v}, w)$ where:
- $V$ is a finite set of vertices.
- $E \subset V \times V$ is a set of directed edges (ordered pairs).
- $S$ is a set of higher simplices, each a subset of $V$ with a compatible partial order.
- $\mathbf{v}: V \to \mathbb{R}^n$ assigns an attribute vector to each vertex.
- $w: E \to \mathbb{R}_{\geq 0}$ assigns a non-negative weight to each directed edge. The weight function is asymmetric: $w(u \to v) \neq w(v \to u)$ in general.

**Definition (Regime Filtration).** A *regime filtration* of $\mathcal{K}$ is a sequence $\emptyset = \mathcal{K}_0 \subset \mathcal{K}_1 \subset \cdots \subset \mathcal{K}_m = \mathcal{K}$ of subcomplexes such that the inclusion $\mathcal{K}_\alpha \hookrightarrow \mathcal{K}_{\alpha+1}$ introduces edges crossing a regime boundary. The boundary penalty $\beta_\alpha$ for crossing boundary $\alpha$ is added to the edge weight.

**Proposition (DAG Property).** The citation subgraph of $\mathcal{K}$, restricted to edges encoding temporal citation (later case cites earlier case), is a directed acyclic graph (DAG). This follows from the impossibility of citing a future decision.

**Proposition (Convergence to the Continuum).** Let $\mathcal{K}_N$ be a sequence of judicial complexes with $N \to \infty$ vertices whose attribute vectors tile $[0,1]^8$ with mesh size $\epsilon_N \to 0$, and whose edge weights are given by the Mahalanobis formula. Then the metric space $(V(\mathcal{K}_N), w)$ Gromov-Hausdorff converges to a Riemannian manifold $(\mathcal{J}, g)$ where $g_{ij} = (\Sigma^{-1})_{ij}$ is the inverse covariance metric.

**Definition (Attribute Vector via NLP).** Given case text $t_i$, the attribute vector is:

$$\mathbf{v}(c_i) = \bigl(\sigma(\mathbf{w}_1^T \mathbf{e}(t_i) + b_1), \; \ldots, \; \sigma(\mathbf{w}_8^T \mathbf{e}(t_i) + b_8)\bigr)$$

where $\mathbf{e}(t_i)$ is the LaBSE embedding, $\sigma$ is the sigmoid function, and $(\mathbf{w}_k, b_k)$ are the trained probe parameters for dimension $k$.

---

## Notes on Sources

The simplicial complex construction draws on Hatcher (2002) for algebraic topology, Edelsbrunner and Harer (2010) for persistent homology, and Grigor'yan, Lin, Muranov, and Yau (2012, 2014) for path homology on directed graphs. The eight legal dimensions are synthesized from Hart (1961), Posner (1990), and the Restatements of Law, cross-referenced with the nine moral dimensions of Bond (2026a, *Geometric Ethics*). The NLP calibration pipeline adapts the methodology of Bond (2026a), independently replicated by Thiele (2026). The voter ID case law includes *Harper v. Virginia Board of Elections* (1966), *Crawford v. Marion County Election Board* (2008), *Shelby County v. Holder* (2013), and *Brnovich v. Democratic National Committee* (2021). Hart's core/penumbra distinction appears in *The Concept of Law* (1961). Sunstein's incompletely theorized agreements appear in *Legal Reasoning and Political Conflict* (1996). Dworkin's integrity thesis appears in *Law's Empire* (1986).

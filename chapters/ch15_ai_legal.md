# Chapter 15: AI Legal Reasoning

> *"The question is not whether machines can think, but whether machines can judge."*
> — Adapted from Alan Turing, *Computing Machinery and Intelligence* (1950)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera has been invited to participate in a pilot program. The Administrative Office of the United States Courts is evaluating an AI legal research tool — JurisGraph — for potential deployment in federal courts. JurisGraph claims to identify relevant precedent, score cases along the eight legal dimensions, detect circuit splits, and flag potential constitutional issues. The vendor, a Stanford spinout backed by significant venture capital, has published benchmarks showing that JurisGraph outperforms traditional legal databases on retrieval accuracy and reduces legal research time by 60%.*
>
> *Rivera is skeptical. She has seen legal AI tools before — they are good at finding cases that match keyword queries, but they are poor at understanding the structural relationships between cases. They retrieve cases that mention the same words without knowing whether the cited case supports or undermines the citing case's position. They rank by textual similarity rather than doctrinal relevance. And they exhibit the same biases as the training data — if the training corpus contains sentencing disparities, the AI learns to reproduce them.*
>
> *But JurisGraph claims to be different. It claims to implement the geometric framework of this book: constructing the judicial complex, computing Mahalanobis distances, detecting Wilson loops, and testing for gauge invariance. Rivera decides to test these claims. She will evaluate JurisGraph against the standards developed in this book — the Legal Invariance Principle, the topological constitutionality test, and the Hohfeldian gauge group. If the tool satisfies these standards, it is a genuine advance. If it does not, it is marketing dressed in mathematical language.*
>
> *This chapter develops the NLP pipeline that connects the theoretical framework to computational implementation, and uses Rivera's evaluation as a test case for whether AI legal reasoning can meet the geometric standard.*

---

## The Implementation Gap

### From Theory to Computation

The preceding fourteen chapters have developed a mathematical framework for legal reasoning: the judicial complex, the legal metric, the Hohfeldian gauge group, the constitutional subcomplex, the precedent heuristic, and the contractual boundary. Each concept is precisely defined, each theorem is formally stated, and each computation is in principle finite.

But "in principle" is not "in practice." The judicial complex $\mathcal{K}$ contains millions of vertices (decided cases) and tens of millions of edges (citations). The attribute vectors $\mathbf{v} \in \mathbb{R}^8$ must be scored for each case — but cases are written in natural language, not numbers. The covariance matrix $\Sigma$ must be estimated from data, and the estimation requires scoring every case in the corpus. The Wilson loops must be computed over directed cycles in the citation network, and the number of directed cycles grows combinatorially.

The implementation gap between theory and computation is the central challenge of computational jurisprudence. This chapter bridges the gap by developing a five-step NLP pipeline that transforms unstructured legal text into the structured geometric representation required by the framework.

### What AI Legal Reasoning Must Achieve

Before describing the pipeline, we must be clear about what "AI legal reasoning" means within the geometric framework. It does not mean predicting outcomes — the framework is not a prediction engine. It means constructing the geometric representation that makes legal reasoning auditable, consistent, and invariance-preserving.

An AI legal reasoning system must:

1. **Construct the judicial complex $\mathcal{K}$** from case databases — identifying vertices, edges, and higher simplices.
2. **Score attribute vectors $\mathbf{v} \in \mathbb{R}^8$** for each case — assigning numerical values to the eight legal dimensions using natural language understanding.
3. **Estimate the covariance matrix $\Sigma$** from the scored corpus — computing how the eight dimensions co-vary across cases.
4. **Compute edge weights** from citation patterns, doctrinal relationships, and outcome data.
5. **Test for invariance** — verifying that the system's outputs satisfy the Legal Invariance Principle, detect Wilson loops, and preserve constitutional topology.

The first four steps are *construction*: building the geometric representation from data. The fifth step is *validation*: testing whether the constructed representation satisfies the theoretical requirements. A system that constructs without validating is incomplete; a system that fails validation is wrong.

## The Five-Step NLP Pipeline

### Step 1: Embedding

**The task.** Transform each legal document (judicial opinion, statute, regulation) from natural language text into a numerical vector representation suitable for downstream analysis.

**The method.** Modern NLP provides language-agnostic embeddings — dense vector representations of text that capture semantic meaning without relying on keyword matching. Models such as sentence transformers, legal-domain transformers, and multilingual encoders produce embedding vectors $\mathbf{e} \in \mathbb{R}^d$ (where $d$ is typically 384, 768, or 1024) that position semantically similar texts near each other in embedding space.

**Definition (Legal Embedding).** A *legal embedding function* $\mathcal{E}: \text{Documents} \to \mathbb{R}^d$ maps each legal document to a dense vector:

$$\mathcal{E}(\text{opinion}_i) = \mathbf{e}_i \in \mathbb{R}^d$$

such that documents with similar legal content have similar embedding vectors: $\text{sim}(\mathbf{e}_i, \mathbf{e}_j) \propto \text{legal\_similarity}(\text{opinion}_i, \text{opinion}_j)$.

The embedding is the foundation of the pipeline. It transforms the unstructured, variable-length, natural-language content of legal opinions into fixed-length numerical vectors that can be processed by the subsequent steps. The quality of the embedding determines the quality of everything downstream.

**Critical requirement: language agnosticism.** The embedding must be *language-agnostic* — it must capture legal meaning rather than linguistic form. Two opinions that discuss the same legal issue in different language (one using formal legal terminology, the other using plain language) should have similar embeddings. Two opinions that use the same words but discuss different legal issues (one about "standing" in the jurisdictional sense, the other about "standing" in a physical sense) should have different embeddings.

Language agnosticism is not merely a technical desideratum — it is a *gauge invariance requirement*. If the embedding changes when the same legal content is expressed in different words, the system's outputs will depend on a legally irrelevant feature (the choice of words, the writing style of the judge). This is a gauge violation: the output changes under a transformation that should leave it invariant.

**Implementation.** For JurisGraph, the embedding step uses a legal-domain transformer fine-tuned on a corpus of federal and state court opinions, statutes, and regulations. The fine-tuning ensures that the embedding captures legal-domain semantics (e.g., distinguishing "standing" as a jurisdictional concept from "standing" as a physical concept) rather than general-language semantics.

### Step 2: Dimension Scoring

**The task.** Project each document's high-dimensional embedding $\mathbf{e}_i \in \mathbb{R}^d$ onto the eight legal dimensions, producing an attribute vector $\mathbf{v}_i \in \mathbb{R}^8$.

**The method.** The projection is performed by *linear probes* — linear classifiers trained to predict each dimension score from the embedding vector. For each dimension $d_k$, a linear probe $\mathbf{w}_k \in \mathbb{R}^d$ and bias $b_k \in \mathbb{R}$ are trained on a labeled dataset of cases with known dimension scores:

$$v_k(c_i) = \sigma(\mathbf{w}_k^T \mathbf{e}_i + b_k)$$

where $\sigma$ is the sigmoid function, mapping the linear projection to the $[0, 1]$ interval.

**Why linear probes?** The choice of linear probes rather than deep neural networks is deliberate and theoretically motivated. A linear probe tests whether the embedding *already contains* the information needed to score the dimension — whether the dimension is *linearly decodable* from the representation. If a linear probe achieves high accuracy, the embedding has learned a representation that separates cases along the legal dimension of interest. If it requires a deep nonlinear model to achieve good accuracy, the dimension is not well-represented in the embedding, and the embedding should be improved rather than compensated by a complex decoder.

This principle — *linearly decodable dimensions* — is the computational analogue of the theoretical requirement that the legal dimensions be independent axes of variation. If the dimensions were not linearly separable in the embedding space, they would be entangled in a way that prevents clean geometric analysis.

**Training data.** The linear probes are trained on a labeled dataset where legal experts have scored cases on each of the eight dimensions. The labeling process is itself a form of calibration: the experts' judgments define the "ground truth" for the dimension scores, and the probes learn to reproduce these judgments from the embedding vectors.

The size and quality of the training dataset are critical. Too few labeled examples, and the probes will overfit — they will learn the idiosyncrasies of the training set rather than the general structure of the dimension. Too many noisy labels, and the probes will learn to reproduce the noise. The Algorithmic Jurisprudence manuscript recommends a minimum of 500 labeled cases per dimension, with at least three independent raters per case and inter-rater agreement measured by Cohen's kappa.

**Validation.** Each linear probe's accuracy is validated on a held-out test set. The eight probes are evaluated jointly to ensure that the eight dimension scores are not redundant — that they capture independent aspects of legal analysis. This is tested by computing the correlation matrix of the predicted scores and verifying that no pair of dimensions has correlation above a threshold (typically 0.7).

---

> **RUNNING EXAMPLE — RIVERA TESTS THE DIMENSION SCORES**
>
> *Rivera selects ten cases from her own docket — cases she has decided and whose legal dimensions she understands intimately. She asks JurisGraph to score each case on the eight dimensions and compares the machine scores to her own expert assessment.*
>
> *Case: Martinez v. San Francisco Unified School District (education funding challenge)*
> *Rivera's scores: $d_1 = 0.7, d_2 = 0.6, d_3 = 0.9, d_4 = 0.8, d_5 = 0.7, d_6 = 0.5, d_7 = 0.6, d_8 = 0.8$*
> *JurisGraph scores: $d_1 = 0.65, d_2 = 0.55, d_3 = 0.85, d_4 = 0.75, d_5 = 0.72, d_6 = 0.48, d_7 = 0.58, d_8 = 0.77$*
>
> *The scores are close — within 0.1 on every dimension. The maximum discrepancy is on $d_2$ (factual nexus), where JurisGraph scores 0.55 versus Rivera's 0.6. This is within the expected margin for a calibrated probe.*
>
> *But Rivera notices something. For a sentencing case on her docket, JurisGraph scores $d_8$ (public interest) at 0.3 for a Black defendant and 0.45 for a white defendant with identical charges, identical criminal history, and identical facts. The difference in public interest scores is driven by the model's learned association between defendant demographics and public interest — an association that reflects the training data's sentencing disparities, not a legitimate legal distinction.*
>
> *This is a Legal Invariance Principle violation. The dimension scores change under a transformation (swapping defendant race) that should leave them invariant. Rivera flags this for the validation step.*

---

### Step 3: Covariance Estimation

**The task.** Estimate the $8 \times 8$ covariance matrix $\Sigma$ from the scored corpus, capturing how the eight legal dimensions co-vary across cases.

**The method.** Given $N$ cases with scored attribute vectors $\mathbf{v}_1, \ldots, \mathbf{v}_N$, the sample covariance matrix is:

$$\hat{\Sigma} = \frac{1}{N-1} \sum_{i=1}^{N} (\mathbf{v}_i - \bar{\mathbf{v}})(\mathbf{v}_i - \bar{\mathbf{v}})^T$$

where $\bar{\mathbf{v}} = \frac{1}{N} \sum_i \mathbf{v}_i$ is the sample mean.

**Domain-specific estimation.** The covariance matrix is not constant across legal domains. The correlation between statutory authority ($d_4$) and remedial scope ($d_7$) is high in statutory interpretation cases (the governing statute determines the available remedies) but low in common-law tort cases (where remedies are judge-made and not tied to specific statutes). The covariance matrix should therefore be estimated within legal domains, producing a family of covariance matrices $\{\Sigma_D\}$ indexed by domain $D$.

**Regularization.** When the number of scored cases is small relative to the number of dimensions (which is always the case for eight dimensions, given that the minimum recommended sample is 500 cases), the sample covariance matrix may be poorly conditioned — its inverse (required for the Mahalanobis distance) may be unstable. Regularization techniques (shrinkage estimators, Ledoit-Wolf estimation) stabilize the inverse:

$$\hat{\Sigma}_{\text{reg}} = (1 - \alpha) \hat{\Sigma} + \alpha \cdot \text{diag}(\hat{\Sigma})$$

where $\alpha \in [0, 1]$ is the shrinkage parameter, chosen by cross-validation to minimize estimation error.

### Step 4: Edge Weights

**The task.** Assign weights to the edges of the judicial complex — the citation links between cases — reflecting the strength and nature of the doctrinal relationship.

**The method.** Edge weights are derived from three sources:

**Citation analysis.** The raw citation — case $c_i$ cites case $c_j$ — provides the edge existence but not its weight. The weight is determined by the *nature* of the citation: positive (supporting, following, applying) or negative (distinguishing, questioning, overruling). Citation classification is performed by a sequence classifier trained on labeled citation contexts.

**Attribute-vector similarity.** The Mahalanobis distance between the attribute vectors of the citing and cited cases provides a second source of edge weight:

$$w_{\text{attr}}(c_i, c_j) = d_M(\mathbf{v}_i, \mathbf{v}_j)$$

Cases with similar attribute vectors (close on the manifold) that cite each other have low edge weight — the doctrinal step is small. Cases with dissimilar attribute vectors (far apart on the manifold) that cite each other have high edge weight — the doctrinal step is large, requiring more argumentative work to bridge.

**Outcome data.** The edge weight can be refined using outcome data: if cases with similar attribute vectors tend to have similar outcomes, the edge weight between them should be low. If cases with similar attribute vectors have different outcomes, the edge weight should be high (the doctrinal path between them crosses a decision boundary).

**Combining the sources.** The final edge weight is a weighted combination:

$$w(c_i, c_j) = \lambda_1 \cdot w_{\text{cite}}(c_i, c_j) + \lambda_2 \cdot w_{\text{attr}}(c_i, c_j) + \lambda_3 \cdot w_{\text{outcome}}(c_i, c_j)$$

where $\lambda_1, \lambda_2, \lambda_3$ are mixing weights calibrated by cross-validation to optimize retrieval accuracy and precedent prediction.

### Step 5: Calibration and Validation

**The task.** Validate the entire pipeline — embedding, dimension scoring, covariance estimation, and edge weights — against the theoretical requirements of the geometric framework.

**The validation criteria:**

**Criterion 1: Dimension independence.** The eight dimension scores must be non-redundant. Validation: compute the correlation matrix of the predicted scores on a held-out test set. If any pair of dimensions has correlation above 0.7, the dimensions are not sufficiently independent and the probes must be retrained or the dimensions redefined.

**Criterion 2: Gauge invariance (the LIP test).** The system's outputs must be invariant under legally irrelevant transformations. Validation: for each case in a test set, create a *gauge-transformed* version — swap the defendant's race, change the judge's name, alter the writing style — and verify that the dimension scores do not change:

$$\mathbf{v}(c_i) = \mathbf{v}(g \cdot c_i) \quad \forall g \in G_{\text{irrelevant}}$$

The Legal Bond Index (LBI) quantifies the violation:

$$\text{LBI} = \frac{1}{|G_{\text{irrelevant}}|} \sum_{g \in G_{\text{irrelevant}}} \frac{d_M(\mathbf{v}(c_i), \mathbf{v}(g \cdot c_i))}{d_M(\mathbf{v}(c_i), \bar{\mathbf{v}})}$$

An LBI of 0 indicates perfect gauge invariance. An LBI above a threshold (the Algorithmic Jurisprudence manuscript suggests 0.05) indicates a violation requiring correction.

**Criterion 3: Topological consistency.** The constructed judicial complex must not contain spurious Wilson loops — directed cycles with non-trivial holonomy that do not correspond to genuine legal inconsistencies. Validation: compute Wilson loops on a subset of known-consistent citation chains and verify that the holonomy is trivial.

**Criterion 4: Retrieval accuracy.** Given a query case, the system should retrieve precedents that legal experts judge to be relevant. Validation: compare the system's top-$k$ retrieved cases against expert judgments using standard retrieval metrics (precision@$k$, recall@$k$, normalized discounted cumulative gain).

**Criterion 5: Calibration of distances.** The Mahalanobis distances between cases should correlate with expert assessments of legal similarity. Validation: for a set of case pairs with expert similarity ratings, compute the rank correlation between Mahalanobis distance and expert rating.

---

> **RUNNING EXAMPLE — RIVERA'S LIP TEST**
>
> *Rivera designs a systematic LIP test for JurisGraph. She takes 50 cases from her docket and creates gauge-transformed versions:*
>
> *Transformation 1: Race swap. For each case involving an individual, swap the individual's race (Black $\to$ white, white $\to$ Black, etc.) while preserving all legally relevant facts. This tests whether the system's outputs depend on the defendant's race — a legally irrelevant characteristic under the Equal Protection Clause.*
>
> *Transformation 2: Gender swap. Same procedure with gender.*
>
> *Transformation 3: Writing style swap. Rewrite each opinion in a different stylistic register (formal $\to$ plain language, plain language $\to$ formal) while preserving the legal content.*
>
> *Results:*
>
> *Race swap: LBI = 0.08. The dimension scores change by an average of 8% when the defendant's race is swapped. The largest change is on $d_8$ (public interest): 12% average change. This exceeds the 0.05 threshold — JurisGraph fails the race invariance test.*
>
> *Gender swap: LBI = 0.04. The dimension scores change by an average of 4% when the defendant's gender is swapped. This is within the threshold — JurisGraph passes the gender invariance test, though barely.*
>
> *Writing style swap: LBI = 0.03. The dimension scores are largely invariant to writing style changes, confirming that the embedding is capturing legal content rather than stylistic features.*
>
> *Rivera's assessment: JurisGraph partially fails the LIP test. It exhibits racial bias in its dimension scoring — specifically, it associates Black defendants with lower public interest scores, reflecting disparities in the training data. The tool cannot be deployed until this violation is corrected.*

---

## The Legal Bond Index in Practice

### Measuring Gauge Violation

The Legal Bond Index (LBI) was introduced in Chapter 5 as a measure of gauge violation — how much a legal system's outputs depend on legally irrelevant features. In the AI context, the LBI becomes a *machine-auditable metric* that can be computed automatically on any AI legal reasoning system.

**Definition (Legal Bond Index for AI Systems).** For an AI legal reasoning system $\mathcal{S}$, the Legal Bond Index is:

$$\text{LBI}(\mathcal{S}) = \mathbb{E}_{c \sim \mathcal{D}} \left[ \frac{1}{|G_{\text{irrelevant}}|} \sum_{g \in G_{\text{irrelevant}}} \frac{d_M(\mathcal{S}(c), \mathcal{S}(g \cdot c))}{d_M(\mathcal{S}(c), \bar{\mathcal{S}})} \right]$$

where $\mathcal{D}$ is a test distribution of cases, $G_{\text{irrelevant}}$ is the set of legally irrelevant transformations, $\mathcal{S}(c)$ is the system's output (dimension scores, retrieved precedents, or recommended outcomes) for case $c$, $g \cdot c$ is the transformed case, and $\bar{\mathcal{S}}$ is the mean system output across the test distribution.

The LBI has several desirable properties:

**Decomposability.** The LBI can be decomposed by transformation type and by dimension, allowing targeted diagnosis of gauge violations:

$$\text{LBI}_g^k = \mathbb{E}_c \left[ \frac{|v_k(\mathcal{S}(c)) - v_k(\mathcal{S}(g \cdot c))|}{|v_k(\mathcal{S}(c)) - \bar{v}_k|} \right]$$

This identifies which transformation (race, gender, style) causes the largest violation and on which dimension ($d_k$) the violation occurs. Rivera's test found that $\text{LBI}_{\text{race}}^8 = 0.12$ — the race swap transformation causes a 12% violation on the public interest dimension.

**Comparability.** The LBI is normalized, so it can be compared across systems, across jurisdictions, and across time periods. An LBI of 0.08 for JurisGraph can be compared to the LBI of the human legal system (estimated from sentencing disparity data) to determine whether the AI system is more or less biased than human judges.

**Actionability.** A high LBI identifies specific gauge violations that can be corrected by targeted interventions: rebalancing the training data, adding gauge-invariance constraints to the loss function, or post-processing the dimension scores to remove dependence on legally irrelevant features.

## Worked Example 1: Fourteenth Amendment Analysis

**Scenario.** An equal protection challenge to a state law that imposes different licensing requirements on barbershops and hair salons, with the challenger alleging that the distinction is a proxy for racial discrimination (barbershops are disproportionately owned by Black entrepreneurs; salons are disproportionately owned by white entrepreneurs).

**Step 1: Embedding.** The legal embedding function $\mathcal{E}$ encodes the challenger's complaint, the state's defense, and the relevant case law into embedding vectors. The embedding captures the semantic content: equal protection challenge, commercial regulation, disparate impact claim, rational basis review.

**Step 2: Dimension scoring.** The linear probes assign attribute vectors:

| Dimension | Score | Interpretation |
|-----------|-------|----------------|
| $d_1$ (Entitlement) | 0.6 | Moderate — business licensing is not a fundamental right, but equal protection applies |
| $d_2$ (Factual nexus) | 0.7 | Statistical evidence of disparate impact is strong |
| $d_3$ (Procedural posture) | 0.8 | Standing is clear (licensed barbers), ripe claim, proper forum |
| $d_4$ (Statutory authority) | 0.5 | Fourteenth Amendment directly; no specific federal statute |
| $d_5$ (Constitutional conformity) | 0.75 | Equal Protection Clause directly implicated |
| $d_6$ (Precedential constraint) | 0.6 | Mixed — rational basis review is deferential, but discriminatory purpose can trigger strict scrutiny |
| $d_7$ (Remedial scope) | 0.5 | Declaratory relief, possible injunction |
| $d_8$ (Public interest) | 0.6 | Moderate — affects a specific industry, not a fundamental right |

**Step 3: Covariance estimation.** Using the covariance matrix estimated from equal protection cases in the domain, the Mahalanobis distance from the challenger's position to the nearest favorable precedent is computed.

**Step 4: Edge weights.** The citation network connects this case to *Village of Arlington Heights v. Metropolitan Housing Dev. Corp.* (1977, requiring evidence of discriminatory purpose for equal protection claims), *Washington v. Davis* (1976, rejecting disparate impact alone as an equal protection violation), and *Yick Wo v. Hopkins* (1886, finding an equal protection violation where a facially neutral law was administered discriminatorily).

**Step 5: Gauge invariance test.** The critical LIP test: swap the racial demographics of barber shop and salon owners. If the system's dimension scores change when the racial associations are reversed (barbershops predominantly white-owned, salons predominantly Black-owned), the system is exhibiting racial bias in its equal protection analysis. A properly calibrated system should produce the same dimension scores regardless of which racial group is disproportionately affected — the equal protection analysis depends on the legal structure, not on which group is burdened.

**Result:** JurisGraph's dimension scores change by 0.06 on average when the racial demographics are reversed. This is above the 0.05 LBI threshold, indicating a gauge violation. The violation is concentrated on $d_2$ (factual nexus) and $d_8$ (public interest), where the system assigns higher scores when the disproportionately affected group is Black. This reflects a training data pattern — civil rights cases in the corpus disproportionately involve claims by Black plaintiffs — rather than a legitimate legal distinction. The system must be recalibrated.

## Worked Example 2: Statutory Conflict Resolution

**Scenario.** A federal statute requires financial institutions to report suspicious transactions exceeding $10,000 to the Financial Crimes Enforcement Network (FinCEN). A state privacy statute prohibits financial institutions from disclosing customer financial information to government agencies without a warrant. A bank operating in both jurisdictions faces contradictory obligations.

**Step 1: Embedding.** The two statutes and the bank's compliance inquiry are embedded. The embedding captures the statutory conflict: federal reporting requirement versus state privacy protection.

**Step 2: Dimension scoring.**

| Dimension | Federal statute | State statute |
|-----------|----------------|---------------|
| $d_1$ (Entitlement) | Bank has a duty to report | Customer has a right to privacy |
| $d_2$ (Factual nexus) | Transactions > $10K trigger reporting | Customer financial data is protected |
| $d_4$ (Statutory authority) | Federal: Bank Secrecy Act | State: Financial Privacy Act |
| $d_5$ (Constitutional conformity) | Federal power to regulate interstate commerce | State power to protect citizen privacy |

**Step 3: Topological analysis.** This is the statutory conflict from Chapter 7's worked example. The two statutes create a directed cycle in the judicial complex:

$c_{\text{bank holds data}} \to c_{\text{federal duty: report}} \to c_{\text{state duty: do not report}} \to c_{\text{bank holds data}}$

The holonomy is non-trivial: the bank starts with a "duty to report" (from the federal statute) and arrives at a "duty not to report" (from the state statute) — a Hohfeldian contradiction. The Wilson loop $W(\gamma) = s$ (jural negation), indicating a genuine inconsistency.

**Step 4: Resolution.** The Supremacy Clause resolves the conflict. The federal statute preempts the state statute to the extent of the conflict. In the geometric framework, preemption removes the state-law edges from the judicial complex, collapsing the non-trivial Wilson loop to the identity. The bank's obligation is determined by federal law alone: report suspicious transactions above $10,000.

**Step 5: Gauge invariance test.** The LIP test for this analysis: swap the jurisdictions (make the reporting requirement a state law and the privacy protection a federal law). The topological analysis should produce the same structure (a non-trivial Wilson loop), but the resolution should reverse (the federal privacy protection now preempts the state reporting requirement). A gauge-invariant system applies the Supremacy Clause based on the constitutional structure — which law is federal, which is state — not on the content of the laws.

**Result:** JurisGraph correctly identifies the Wilson loop, correctly invokes the Supremacy Clause, and correctly reverses the resolution when the jurisdictions are swapped. The system passes the gauge invariance test for statutory conflict resolution. LBI = 0.01 — the outputs are nearly perfectly invariant under jurisdiction swap.

## Worked Example 3: Precedent Overruling

**Scenario.** The Supreme Court is considering whether to overrule a 1990 precedent that held employment discrimination claims under Title VII cannot be brought by independent contractors (only by employees). Subsequent statutory amendments and social changes have eroded the employee/independent contractor distinction as the gig economy has expanded. The question is whether the 1990 precedent should be overruled.

**Step 1: Embedding.** The 1990 precedent, the current case, and the intervening cases are embedded. The embedding captures the doctrinal evolution: the narrowing of the employee/independent contractor distinction in subsequent cases, the expansion of Title VII's scope through statutory amendments, and the growth of the gig economy.

**Step 2: Dimension scoring of the 1990 precedent.**

| Dimension | 1990 score | Current score | Change |
|-----------|-----------|--------------|--------|
| $d_1$ (Entitlement) | 0.4 | 0.7 | +0.3 (independent contractors now seen as having stronger entitlement) |
| $d_2$ (Factual nexus) | 0.5 | 0.8 | +0.3 (gig economy makes contractor/employee distinction factually weaker) |
| $d_4$ (Statutory authority) | 0.6 | 0.75 | +0.15 (subsequent amendments broadened Title VII) |
| $d_6$ (Precedential constraint) | 0.9 | 0.5 | -0.4 (the 1990 precedent has been distinguished, questioned, and eroded) |
| $d_8$ (Public interest) | 0.5 | 0.8 | +0.3 (millions of gig workers lack discrimination protection) |

**Step 3: Overruling cost computation.** The overruling cost (from Chapter 9's parallel transport framework) is:

$$\text{Cost}_{\text{overrule}} = \sum_{i=1}^{n} w_{P_i} \cdot |\Delta w(c_i, \cdot \, ; P)|$$

where the sum is over all cases that relied on the 1990 precedent. JurisGraph identifies 47 cases that cited the 1990 precedent positively, with a combined precedential weight of 23.4 (on a normalized scale). The dimension scores of these cases are recomputed under the hypothetical overruling, and the total edge-weight change is computed.

**Step 4: Stare decisis analysis.** The system evaluates the *Casey* factors for overruling precedent:

- **Workability:** The employee/independent contractor distinction has become unworkable as applied to gig workers. Score: 0.7 (supports overruling).
- **Reliance interests:** Some employers have structured their workforce to exploit the independent contractor exclusion. Score: 0.5 (moderate reliance, but arguably illegitimate reliance on the ability to discriminate).
- **Doctrinal erosion:** The precedent has been distinguished and narrowed by subsequent cases. The precedential constraint score has dropped from 0.9 to 0.5. Score: 0.8 (strongly supports overruling).
- **Changed factual circumstances:** The gig economy did not exist in 1990. The factual nexus score has increased from 0.5 to 0.8. Score: 0.9 (strongly supports overruling).

**Step 5: Gauge invariance test.** The LIP test: does the overruling analysis depend on the demographics of gig workers? Swap the demographic profile of gig workers from disproportionately minority and immigrant to disproportionately white and native-born. The stare decisis analysis should be invariant — the question is whether the precedent should be overruled, not who benefits from the overruling.

**Result:** JurisGraph's overruling recommendation is invariant under the demographic swap. LBI = 0.02. The system correctly treats the stare decisis analysis as a structural question about doctrinal coherence, not a substantive question about who benefits from the change.

---

> **RUNNING EXAMPLE — RIVERA'S FINAL ASSESSMENT**
>
> *Rivera compiles her evaluation of JurisGraph.*
>
> *Strengths:*
> *— The five-step pipeline (embedding, dimension scoring, covariance estimation, edge weights, calibration) provides a principled architecture that connects NLP capabilities to the geometric framework.*
> *— Dimension scoring is reasonably accurate, with scores within 0.1 of expert assessment on most cases.*
> *— Statutory conflict resolution is sound: Wilson loops are correctly identified, and the Supremacy Clause is correctly applied.*
> *— Stare decisis analysis is structurally correct and gauge-invariant.*
>
> *Weaknesses:*
> *— The system fails the racial invariance test (LBI = 0.08). Dimension scores on $d_8$ (public interest) are sensitive to defendant race, reflecting training data bias.*
> *— The system has not been tested on multi-manifold (international) disputes, where the pipeline must handle multiple covariance matrices and treaty connection maps.*
> *— The system does not compute path homology — it identifies Wilson loops but does not perform the full topological constitutionality test.*
>
> *Rivera's recommendation: JurisGraph should not be deployed in its current form. The racial bias in the public interest dimension scoring is a Legal Invariance Principle violation that must be corrected before the system can be used in a federal court. The correction is straightforward in principle — add gauge-invariance constraints to the training loss function, rebalance the training data, or post-process scores to remove racial dependence — but must be validated before deployment.*
>
> *Rivera notes that the evaluation framework itself is a contribution: the five criteria (dimension independence, gauge invariance, topological consistency, retrieval accuracy, distance calibration) provide a systematic standard for evaluating any AI legal reasoning tool. This standard is more demanding than the "does it produce good results?" test used by most legal technology vendors. It requires not just accuracy but structural consistency — not just getting the right answer but getting it for the right reasons.*

---

## From Retrieval to Reasoning

### The Difference Between Legal Search and Legal Reasoning

Current legal AI systems are primarily *retrieval* systems — they find relevant documents given a query. JurisGraph's claimed advance is to move from retrieval to *reasoning* — from finding cases to analyzing their geometric relationships.

The distinction is critical. A retrieval system answers: "Which cases are similar to this one?" A reasoning system answers: "What is the structure of the legal space around this case? Where are the boundaries? Which paths are available? Is the current doctrinal configuration consistent?"

The five-step NLP pipeline enables this transition. Steps 1-4 construct the geometric representation; step 5 validates it. Once the representation is constructed, the geometric operations developed in this book — Mahalanobis distance computation, Wilson loop detection, path homology computation, $A^*$ search, gauge invariance testing — become executable algorithms rather than theoretical concepts.

### The Remaining Challenges

Even with a validated pipeline, several challenges remain:

**Temporal dynamics.** The legal manifold changes over time — new cases are decided, old precedents are overruled, statutes are amended. The pipeline must be updated continuously, and the updates must preserve consistency: a new case that changes the dimension scores of previously scored cases must trigger a cascade of recomputation.

**Adversarial robustness.** In an adversarial system (Chapter 12), parties have incentives to game the AI system — to frame their arguments in ways that exploit weaknesses in the embedding or the dimension scoring. A robust system must be resistant to such gaming, which is a requirement that goes beyond standard machine learning robustness.

**Interpretability.** The geometric framework provides inherent interpretability — the eight dimensions, the Mahalanobis distance, the Wilson loops, the path homology groups — but the pipeline's internal representations (embedding vectors, linear probe weights, covariance matrices) must be connected to these interpretable structures. A system that produces correct outputs for inscrutable reasons is not fully satisfactory for judicial use.

**Normative commitments.** The choice of which transformations are "legally irrelevant" (and therefore must be gauge-invariant) is not a purely technical decision. It is a normative commitment about what equal protection requires, what due process demands, and what the rule of law means. The AI system inherits these commitments from its calibration, and the commitments must be made explicit and subject to scrutiny.

## The Geometric Standard for Legal AI

### What the Framework Requires

The geometric framework sets a higher standard for legal AI than the current industry practice. Current legal AI systems are evaluated on retrieval accuracy, user satisfaction, and time savings. The geometric framework adds structural requirements:

**Gauge invariance.** The system's outputs must be invariant under legally irrelevant transformations. An LBI below the threshold (0.05) on all transformation types is a minimum requirement.

**Topological consistency.** The system's constructed judicial complex must be topologically consistent — no spurious Wilson loops, correct path-homology computation, and accurate detection of genuine circuit splits.

**Metric calibration.** The Mahalanobis distances must correlate with expert judgments of legal similarity, and the covariance matrices must reflect the genuine correlation structure of the legal dimensions.

**Conservation compliance.** In closed bilateral disputes, the system's outputs must satisfy the conservation laws derived in Chapter 5 — liability conservation, entitlement balance, and outcome consistency.

These requirements are demanding. No current AI legal reasoning system satisfies all of them. But they are *principled* — they follow from the mathematical structure of the framework, not from ad hoc desiderata. And they are *testable* — each requirement can be validated by a specific computational procedure.

The geometric standard is not a barrier to AI legal reasoning. It is a *blueprint* — a specification of what AI legal reasoning must achieve to be trustworthy, consistent, and fair. A system that meets the standard is not merely useful; it is *geometrically sound* — its outputs respect the symmetries, conservations, and topological constraints that the legal system claims to embody.

## Chapter Summary

1. The **five-step NLP pipeline** (embedding, dimension scoring, covariance estimation, edge weights, calibration) bridges the gap between the theoretical framework and computational implementation.

2. **Embeddings** must be language-agnostic — a gauge invariance requirement that ensures the system captures legal meaning rather than linguistic form.

3. **Linear probes** score the eight legal dimensions, testing whether each dimension is linearly decodable from the embedding. The choice of linear probes is theoretically motivated: it tests the quality of the representation rather than compensating for its weaknesses.

4. The **Legal Bond Index (LBI)** provides a machine-auditable metric for gauge invariance, decomposable by transformation type and dimension.

5. The **three worked examples** (Fourteenth Amendment analysis, statutory conflict resolution, precedent overruling) demonstrate the pipeline in action and illustrate how the LIP test identifies and diagnoses gauge violations.

6. The **geometric standard for legal AI** — gauge invariance, topological consistency, metric calibration, and conservation compliance — sets a higher bar than current industry practice but is principled, testable, and achievable.

---

## Technical Appendix

**Definition (Legal Embedding Function).** A legal embedding function $\mathcal{E}: \mathcal{D} \to \mathbb{R}^d$ maps documents to a $d$-dimensional vector space satisfying:

(i) **Semantic preservation:** $\text{cos\_sim}(\mathcal{E}(c_i), \mathcal{E}(c_j)) \geq \tau$ whenever $c_i$ and $c_j$ address the same legal issue.

(ii) **Language agnosticism:** $\|\mathcal{E}(c) - \mathcal{E}(g \cdot c)\| < \epsilon$ for all style transformations $g \in G_{\text{style}}$, where $\epsilon$ is a tolerance parameter.

**Definition (Linear Probe).** For dimension $d_k$, the linear probe is a function $f_k: \mathbb{R}^d \to [0, 1]$ defined by $f_k(\mathbf{e}) = \sigma(\mathbf{w}_k^T \mathbf{e} + b_k)$, where $\mathbf{w}_k \in \mathbb{R}^d$ and $b_k \in \mathbb{R}$ are trained by minimizing:

$$\mathcal{L}_k = \sum_{i=1}^{N_{\text{train}}} \ell(f_k(\mathbf{e}_i), v_k^{\text{true}}(c_i)) + \lambda \|\mathbf{w}_k\|^2$$

where $\ell$ is the cross-entropy or MSE loss, $v_k^{\text{true}}$ is the expert-labeled dimension score, and $\lambda$ is a regularization parameter.

**Theorem (LBI Decomposition).** The Legal Bond Index decomposes as:

$$\text{LBI}(\mathcal{S}) = \sum_{k=1}^{8} \omega_k \sum_{g \in G_{\text{irrelevant}}} \pi_g \cdot \text{LBI}_g^k(\mathcal{S})$$

where $\omega_k$ is the weight of dimension $d_k$ (summing to 1), $\pi_g$ is the weight of transformation $g$ (summing to 1), and $\text{LBI}_g^k$ is the dimension-transformation-specific bond index. This decomposition allows targeted diagnosis: high $\text{LBI}_g^k$ identifies the specific transformation $g$ and dimension $d_k$ where gauge invariance fails.

**Proposition (Gauge-Invariant Training).** Adding a gauge-invariance penalty to the training loss:

$$\mathcal{L}_{\text{GI}} = \mathcal{L}_{\text{task}} + \mu \sum_{g \in G_{\text{irrelevant}}} \|\mathcal{S}(c) - \mathcal{S}(g \cdot c)\|^2$$

with $\mu > 0$, reduces the LBI at convergence. If $\mu$ is sufficiently large relative to the task loss, the LBI approaches 0, but at the cost of reduced task performance (the accuracy-invariance tradeoff).

**Definition (Retrieval Precision at $k$).** For a query case $c_q$ with expert-judged relevant cases $R_q$:

$$P@k = \frac{|\{\text{top-}k \text{ retrieved}\} \cap R_q|}{k}$$

**Definition (Legal Bond Index for AI Systems — Full Statement).** For a system $\mathcal{S}$, test distribution $\mathcal{D}$, and irrelevant transformation group $G_{\text{irrelevant}}$:

$$\text{LBI}(\mathcal{S}) = \mathbb{E}_{c \sim \mathcal{D}} \left[ \frac{\sum_{g \in G_{\text{irrelevant}}} d_M(\mathcal{S}(c), \mathcal{S}(g \cdot c))}{|G_{\text{irrelevant}}| \cdot \mathbb{E}_{c' \sim \mathcal{D}}[d_M(\mathcal{S}(c), \mathcal{S}(c'))]} \right]$$

The denominator normalizes by the expected distance between random system outputs, ensuring that the LBI is scale-invariant and comparable across systems and domains.

**Proposition (Minimum Sample Size for Dimension Probes).** For eight linear probes with $d$-dimensional input, achieving estimation error below $\epsilon$ with probability at least $1 - \delta$ requires at least:

$$N_{\text{min}} = O\left(\frac{d + \log(8/\delta)}{\epsilon^2}\right)$$

labeled examples per dimension. For $d = 768$, $\epsilon = 0.05$, $\delta = 0.05$: $N_{\text{min}} \approx 500$.

---

## Notes on Sources

The NLP pipeline for legal analysis draws on the Algorithmic Jurisprudence manuscript (§8, §12). Language-agnostic embeddings are developed in Reimers and Gurevych (2019, *Sentence-BERT*) and Conneau et al. (2020, *Unsupervised Cross-lingual Representation Learning at Scale*). Legal-domain transformers include Chalkidis et al. (2020, *LEGAL-BERT*) and Zheng et al. (2021, *When Does Pretraining Help?*). Linear probes as diagnostic tools are developed by Alain and Bengio (2017) and Belinkov (2022, *Probing Classifiers*). The Mahalanobis distance in machine learning is discussed in De Maesschalck, Jouan-Rimbaud, and Massart (2000). The Legal Bond Index extends the Bond Index of Bond (2026a, *Geometric Ethics*, Ch. 14). The gauge-invariant training approach connects to fairness constraints in machine learning — see Hardt, Price, and Srebro (2016, *Equality of Opportunity in Supervised Learning*) and Zemel et al. (2013, *Learning Fair Representations*). Citation analysis in legal databases is reviewed in Fowler et al. (2007, *Network Analysis and the Law*). The stare decisis factors for overruling precedent originate with *Planned Parenthood v. Casey*, 505 U.S. 833 (1992). The retrieval accuracy metrics are standard in information retrieval — see Manning, Raghavan, and Schütze (2008, *Introduction to Information Retrieval*). The Ledoit-Wolf covariance estimator is developed in Ledoit and Wolf (2004). The accuracy-invariance tradeoff connects to the broader fairness-accuracy tradeoff literature — see Corbett-Davies and Goel (2018).

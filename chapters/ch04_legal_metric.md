# Chapter 4: The Legal Metric

> *"Hard cases make bad law — because they are so close to the boundary that the distance between competing outcomes is smaller than the measurement error of the legal system."*
> — Adapted from the Geometric Ethics programme

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera has two employment discrimination cases on her docket this week. Both involve claims under Title VII. Both allege that the employer terminated the plaintiff because of race. The facts are superficially similar: long-tenured employee, positive performance reviews, terminated after a new supervisor arrived.*
>
> *But one case is "easy" and the other is "hard." Why?*
>
> *In Case A, the plaintiff was replaced by a white employee, the new supervisor made documented racial remarks, and three other minority employees were terminated in the same month. The path from the plaintiff's legal position to a finding of discrimination is short — a few doctrinal steps with strong factual support at each step.*
>
> *In Case B, the plaintiff was replaced by another minority employee, the supervisor's motives are ambiguous, and the employer has articulated a reorganization rationale that may or may not be pretextual. The path from the plaintiff's position to a finding of discrimination is long — it requires establishing pretext, which means undermining the employer's stated rationale, which requires either direct evidence of discriminatory intent or a convincing pattern of circumstantial evidence.*
>
> *The difference between "easy" and "hard" is not subjective. It is a difference in **distance** — in how far apart the plaintiff's legal position is from the desired outcome, measured in doctrinal steps, evidentiary burdens, and regime boundary crossings. This chapter defines that distance.*

---

## Why Law Needs a Metric

Chapter 3 constructed the judicial complex $\mathcal{K}$ — a directed weighted simplicial complex whose vertices are decided cases and whose attribute vectors encode positions along eight legal dimensions. But a space without a notion of distance is a space without structure. We need to measure how "close" two legal states are, and the measurement must capture what lawyers mean when they say that one case is "on point" while another is "distinguishable."

The metric serves three purposes:

1. **Precedent selection.** A case is relevant precedent if it is "close" to the current case. But close in what sense? Not just factual similarity, and not just legal similarity — both, weighted by their cross-dimensional correlations. The metric defines "close."

2. **Argument evaluation.** A legal argument is a path through the complex. The cost of the argument — its persuasive burden — is the total distance traveled along the path. A shorter path is a more compelling argument. The metric defines "shorter."

3. **Burden of proof.** The burden of proof is the minimum distance from the plaintiff's position to the goal region. Different standards of proof (preponderance, clear and convincing, beyond reasonable doubt) correspond to different distance thresholds. The metric defines the thresholds.

## The Mahalanobis Distance

### Why Not Euclidean Distance?

The naive approach would be to measure the distance between two cases as the Euclidean distance between their attribute vectors:

$$d_{\text{Euclid}}(c_i, c_j) = \sqrt{\sum_{k=1}^{8} (v_k(c_i) - v_k(c_j))^2}$$

This treats each legal dimension as independent and equally weighted. It says that a difference of 0.3 on the entitlement dimension is the same "distance" as a difference of 0.3 on the procedural posture dimension.

But legal dimensions are *not* independent. Statutory authority ($d_4$) heavily constrains remedial scope ($d_7$): the available remedies depend on the governing statute. Procedural posture ($d_3$) gates access to the merits ($d_2$): a case dismissed for lack of standing never reaches the factual analysis. Constitutional conformity ($d_5$) interacts with entitlement structure ($d_1$): constitutional rights constrain which Hohfeldian positions are permissible.

An independent-dimension metric treats these cross-dimensional dependencies as noise. If two cases differ on both statutory authority and remedial scope — dimensions that are highly correlated — the Euclidean distance counts the difference twice. This overcounts the distance, because the two dimensions are not contributing independent information.

### The Mahalanobis Solution

The Mahalanobis distance corrects this by accounting for the covariance structure of the dimensions:

**Definition (Legal Mahalanobis Distance).** The Mahalanobis distance between two legal states with attribute vectors $\mathbf{v}(c_i)$ and $\mathbf{v}(c_j)$ is:

$$d_M(c_i, c_j) = \sqrt{\Delta \mathbf{v}^T \, \Sigma^{-1} \, \Delta \mathbf{v}}$$

where $\Delta \mathbf{v} = \mathbf{v}(c_j) - \mathbf{v}(c_i)$ is the attribute-vector difference and $\Sigma \in \mathbb{R}^{8 \times 8}$ is the *dimensional covariance matrix*.

The covariance matrix $\Sigma$ captures how the eight dimensions co-vary across the case corpus. Its diagonal entries $\Sigma_{kk}$ are the variances of each dimension (how much each dimension varies across cases), and its off-diagonal entries $\Sigma_{kl}$ encode how much dimensions $d_k$ and $d_l$ co-vary.

The inverse $\Sigma^{-1}$ appears in the formula because we want to *de-correlate* the dimensions before measuring distance. When two dimensions are highly correlated (large $\Sigma_{kl}$), the inverse downweights differences along the correlated directions, preventing double-counting.

### The Covariance Matrix

The covariance matrix is estimated empirically from the case corpus:

$$\hat{\Sigma} = \frac{1}{N-1} \sum_{i=1}^{N} (\mathbf{v}(c_i) - \bar{\mathbf{v}})(\mathbf{v}(c_i) - \bar{\mathbf{v}})^T$$

where $\bar{\mathbf{v}} = \frac{1}{N} \sum_i \mathbf{v}(c_i)$ is the mean attribute vector over the corpus.

The off-diagonal entries of $\hat{\Sigma}$ are empirically testable predictions of the framework. For example:

- $\hat{\Sigma}_{4,7}$ (statutory authority -- remedial scope): predicted to be significantly positive, reflecting the coupling between which statute governs and which remedies are available.
- $\hat{\Sigma}_{3,2}$ (procedural posture -- factual nexus): predicted to be moderately positive, reflecting the gating effect of procedure on access to the merits.
- $\hat{\Sigma}_{1,5}$ (entitlement structure -- constitutional conformity): predicted to be significantly positive, reflecting the constraint that constitutional provisions impose on the Hohfeldian structure.

If these predictions are falsified — if the off-diagonal entries are near zero — then the dimensions are empirically independent, and the Mahalanobis distance reduces to a weighted Euclidean distance.

### Special Case: Independent Dimensions

When $\Sigma$ is diagonal — $\Sigma = \text{diag}(\sigma_1^2, \ldots, \sigma_8^2)$ — the Mahalanobis distance simplifies to a weighted $L_2$ norm:

$$d_M(c_i, c_j) = \sqrt{\sum_{k=1}^{8} \frac{(v_k(c_i) - v_k(c_j))^2}{\sigma_k^2}}$$

This weights each dimension inversely by its variance: dimensions with high variance (which vary a lot across cases) contribute less per unit of difference, while dimensions with low variance (which are more stable) contribute more. The intuition is that a difference on a stable dimension is more legally meaningful than a difference on a highly variable one.

The general (non-diagonal) case allows the data to determine whether and how the dimensions interact. This is the correct approach: we should not assume independence and then be surprised when the metric overcounts; we should let the empirical covariance structure determine the metric.

---

> **RUNNING EXAMPLE — WHY CASE B IS HARDER THAN CASE A**
>
> *Rivera can now quantify the difference between her two employment discrimination cases.*
>
> *Case A: Attribute vector $\mathbf{v}_A = (0.9, 0.9, 0.8, 0.7, 0.3, 0.7, 0.7, 0.5)$. Strong entitlement structure (clear right to non-discrimination), strong factual nexus (direct evidence of racial animus), good procedural posture (timely filing, proper jurisdiction), adequate statutory authority (Title VII), low constitutional dimension (statutory case), solid precedent (McDonnell Douglas with direct evidence), standard remedial scope (reinstatement, back pay, damages), moderate public interest.*
>
> *Case B: Attribute vector $\mathbf{v}_B = (0.9, 0.4, 0.8, 0.7, 0.3, 0.5, 0.6, 0.4)$. Identical entitlement structure, but weak factual nexus (circumstantial evidence only), weaker precedential fit (the case is in the murky zone between prima facie case and pretext), and narrower remedial scope (reinstatement may not be feasible if the position was eliminated in reorganization).*
>
> *Goal region $G$: Cases where the plaintiff prevailed in Title VII race discrimination claims. Representative attribute vector: $\mathbf{v}_G = (0.95, 0.8, 0.9, 0.8, 0.3, 0.8, 0.8, 0.5)$.*
>
> *Mahalanobis distance from Case A to $G$: small. The attribute vectors are close along all dimensions.*
>
> *Mahalanobis distance from Case B to $G$: large. The factual nexus gap ($0.4$ vs. $0.8$) is the dominant contribution, and because $d_2$ and $d_6$ are positively correlated (stronger facts lead to stronger precedential fit), the Mahalanobis distance accounts for this coupling without double-counting.*
>
> *The quantitative difference between "easy case" and "hard case" is simply the Mahalanobis distance to the goal region.*

---

## Edge Weights: The Full Formula

### The Three Components

The Mahalanobis distance between attribute vectors is only the first component of the edge weight. The full weight of a directed edge $c_i \to c_j$ in the judicial complex is:

**Definition (Asymmetric Edge Weights).** The weight of a directed edge $c_i \to c_j$ in $\mathcal{K}$ is:

$$w(c_i \to c_j) = \underbrace{\Delta \mathbf{v}(c_i, c_j)^T \, \Sigma^{-1} \, \Delta \mathbf{v}(c_i, c_j)}_{\text{Mahalanobis distance}} + \underbrace{\beta \cdot \mathbf{1}[\text{regime boundary}]}_{\text{boundary penalty}} + \underbrace{h(\ell(c_i), \ell(c_j))}_{\text{hierarchical cost}}$$

The three terms correspond to three distinct sources of legal "friction" — costs that make legal arguments harder to traverse:

### Component 1: Doctrinal Distance

The Mahalanobis term $\Delta \mathbf{v}^T \Sigma^{-1} \Delta \mathbf{v}$ measures the *doctrinal distance* between two cases — how different they are along the eight legal dimensions, accounting for cross-dimensional correlations.

Cases with similar attribute vectors are doctrinally close: they involve similar entitlement structures, similar factual patterns, similar statutory frameworks, and so on. Traversing from one to the other is easy — the legal argument that "this case is like that case" is straightforward.

Cases with very different attribute vectors are doctrinally distant: they involve different areas of law, different types of facts, and different legal frameworks. Traversing from one to the other requires extensive argument — the legal equivalent of a long and winding road.

### Component 2: Boundary Penalties

The boundary penalty $\beta \cdot \mathbf{1}[\text{regime boundary}]$ adds a discrete cost whenever a legal argument crosses a regime boundary. This is not a continuous cost — it is a *step function* that activates (or does not) when the argument moves from one legal regime to another.

Examples of boundary crossings:

- **Jurisdictional crossing.** Moving from a state-court precedent to a federal-court argument (or vice versa) incurs a penalty because the authority structure differs.
- **Doctrinal crossing.** Moving from a contract-law analysis to a tort-law analysis incurs a penalty because the elements of the claims differ.
- **Statutory crossing.** Moving from a Title VII analysis to a Section 1983 analysis incurs a penalty because the statutory frameworks impose different requirements.
- **Constitutional crossing.** Moving from a statutory claim to a constitutional claim (or vice versa) incurs a penalty because the burden of proof and the available remedies change discontinuously.

Different boundaries have different penalties: $\beta_{\text{jurisdiction}}$ may be large (crossing jurisdictional boundaries is legally difficult), while $\beta_{\text{doctrine}}$ may be smaller (courts routinely analyze claims under multiple doctrines).

### Component 3: Hierarchical Cost

The hierarchical cost function $h(\ell(c_i), \ell(c_j))$ encodes the asymmetry of legal authority:

$$h(\ell_i, \ell_j) = \begin{cases}
0 & \text{if } \ell_i > \ell_j \text{ (binding: higher court to lower)} \\
\eta & \text{if } \ell_i = \ell_j \text{ (persuasive: same level)} \\
\infty & \text{if } \ell_i < \ell_j \text{ (reverse direction: lower to higher)}
\end{cases}$$

where $\eta > 0$ is a persuasive-authority penalty.

This makes the edge weight *asymmetric*: $w(c_i \to c_j) \neq w(c_j \to c_i)$ in general. A Supreme Court precedent binds a district court at zero cost (the district court must follow it). A district court opinion is merely persuasive to a circuit court at cost $\eta$ (the circuit court may consider it but is not bound). And a district court opinion has no binding authority at the Supreme Court level — the reverse edge has infinite cost.

The asymmetry is not a modeling choice. It is a structural feature of the legal system, encoded in the Constitution (Article III) and in the doctrine of stare decisis.

## Legal Friction

### Definition

A legal argument is a path through the judicial complex — a sequence of edges connecting a starting case to a goal case. The *legal friction* of an argument is the total edge weight along the path:

**Definition (Legal Friction).** For a path $\gamma = (c_0, c_1, \ldots, c_m)$ through the judicial complex $\mathcal{K}$:

$$\text{BF}_{\text{law}}(\gamma) = \underbrace{\sum_{i=0}^{m-1} w(c_i, c_{i+1})}_{\text{argument complexity}} + \underbrace{\sum_k \beta_k \cdot \mathbf{1}[(c_i, c_{i+1}) \text{ crosses regime } k]}_{\text{boundary penalties}} + \underbrace{\sum_j \omega_j \cdot \delta_j(\gamma)}_{\text{burden of proof}}$$

The three terms correspond to:

1. **Argument complexity** — the total edge weight along the path. More doctrinal steps and larger dimensional differences cost more. A brief that cites twenty cases to establish a point has higher argument complexity than a brief that cites three closely related cases.

2. **Boundary penalties** — the cost of crossing regime boundaries. Changing legal regimes, establishing jurisdiction, overcoming presumptions — each crossing adds a discrete cost.

3. **Burden of proof** — the cost of establishing facts along the path. $\omega_j$ is the weight of the $j$-th evidentiary requirement; $\delta_j(\gamma)$ measures how far the path's evidence falls short of the threshold.

### What Makes an Argument "Longer"

In everyday legal practice, lawyers and judges have strong intuitions about which arguments are "stronger" or "weaker," which cases are "easy" or "hard," which paths to a legal conclusion are "direct" or "circuitous." Legal friction formalizes these intuitions:

- **A strong argument has low friction.** The path is short (few doctrinal steps), the edges are cheap (the cited cases are closely related), and no regime boundaries are crossed.

- **A weak argument has high friction.** The path is long (many doctrinal steps), the edges are expensive (the cited cases are factually or doctrinally distant), and regime boundaries must be crossed.

- **An impossible argument has infinite friction.** The path requires traversing an edge with infinite cost — citing a lower court to bind a higher court, for instance, or relying on overruled precedent.

---

> **RUNNING EXAMPLE — ARGUMENT PATHS IN CASE B**
>
> *In Case B, the plaintiff's attorney has two possible argument paths to the goal region (successful discrimination claim):*
>
> ***Path 1: Direct evidence.** If the plaintiff can produce direct evidence of discriminatory intent — a smoking-gun email, a witness to a discriminatory statement — the path is short. Direct evidence takes you directly from the plaintiff's position to the goal region without traversing the McDonnell Douglas burden-shifting framework. Legal friction: low (assuming the evidence exists), because the doctrinal distance is small and no burden-shifting boundary must be crossed.*
>
> *But the plaintiff in Case B does not have direct evidence. This path has high burden-of-proof cost ($\delta_j$ is large), making the total friction prohibitive.*
>
> ***Path 2: McDonnell Douglas burden-shifting.** The plaintiff establishes a prima facie case (member of protected class, qualified, adverse action, replacement or differential treatment), the employer articulates a legitimate non-discriminatory reason, and the plaintiff shows pretext. This path is longer — three doctrinal steps instead of one — but the burden-of-proof cost at each step is lower because the evidentiary requirements are less demanding.*
>
> *Legal friction along Path 2:*
> *- Step 1 (prima facie case): edge weight moderate, burden of proof low (prima facie elements are easy to establish).*
> *- Step 2 (employer's rebuttal): edge weight low (the burden shifts to the employer, reducing the plaintiff's friction on this segment).*
> *- Step 3 (pretext): edge weight high, burden of proof moderate (the plaintiff must show the stated reason is pretextual, which requires attacking the employer's credibility).*
>
> *Total friction: the sum of the three segments. Higher than Path 1 (if Path 1 were feasible), but finite and traversable.*
>
> *This is why Rivera considers Case B "hard": the available path to the goal region has higher total friction than the available path in Case A. The difficulty is not subjective — it is the graph distance, measured in Mahalanobis units with boundary penalties and burden-of-proof costs.*

---

## Burden of Proof as Distance

### The Formal Statement

The burden of proof in a legal proceeding is the shortest-path distance from the plaintiff's initial vertex to the nearest vertex in the goal region:

**Proposition (Burden of Proof as Graph Distance).** The *burden of proof* in a legal proceeding is:

$$\text{Burden}(c_0, G) = \min_{\gamma} \text{BF}_{\text{law}}(\gamma) \quad \text{subject to } \gamma \text{ starts at } c_0, \; \gamma \text{ ends in } G$$

where $G$ is the set of goal vertices (cases where plaintiffs prevailed on similar claims).

This is the shortest-path distance from $c_0$ to $G$ in the weighted directed graph $\mathcal{K}$.

### Standards of Proof as Distance Thresholds

Different standards of proof correspond to different thresholds on this distance. The standard of proof determines how much shorter the plaintiff's optimal path must be relative to the defendant's optimal path:

**Preponderance of the evidence:** $\text{BF}_{\text{law}}(\gamma^*_\pi) < \text{BF}_{\text{law}}(\gamma^*_\delta)$. The plaintiff's optimal path is shorter than the defendant's. In graph terms: the distance from the facts to the plaintiff's goal is less than the distance from the facts to the defendant's goal. This is the standard in civil cases.

**Clear and convincing evidence:** $\text{BF}_{\text{law}}(\gamma^*_\pi) < \alpha \cdot \text{BF}_{\text{law}}(\gamma^*_\delta)$ for some $\alpha < 1$. The plaintiff's path must be *substantially* shorter — not just shorter, but shorter by a margin. This is the standard for fraud claims, some involuntary commitment proceedings, and other cases where the stakes are high.

**Beyond reasonable doubt:** $\text{BF}_{\text{law}}(\gamma^*_\pi) < \epsilon$ for small $\epsilon$. The path to guilt is so short — the evidence so overwhelming — that no reasonable alternative path exists. The threshold $\epsilon$ is not zero (absolute certainty is not required) but it is very small. This is the criminal standard.

The geometric interpretation makes the relationship among these standards precise. They are not three different "levels of confidence" (a psychological notion that resists formalization). They are three different *distance thresholds* on the same graph (a mathematical notion that admits computation).

### Burden-Shifting as Weight Reassignment

When the burden shifts — as in the McDonnell Douglas framework — the edge weights change: dimensions that the plaintiff previously had to traverse become the defendant's responsibility.

**Remark (Burden-Shifting as Weight Reassignment).** Burden-shifting re-assigns which party bears the cost of movement along each dimension. The total path cost is conserved — only the allocation between parties changes. This is consistent with the Liability-Damages Conservation theorem of Chapter 5.

In the McDonnell Douglas framework:
- **Step 1:** The plaintiff bears the burden of establishing a prima facie case. The edge weights on the plaintiff's path are at their default values.
- **Step 2:** The burden shifts to the employer. The edge weights on this segment are borne by the defendant — the plaintiff's friction temporarily drops to near zero on this segment, while the defendant's friction increases.
- **Step 3:** The burden returns to the plaintiff, who must show pretext. The edge weights return to their default values for the plaintiff.

The total friction across all three steps, summed over both parties, is conserved. Burden-shifting does not create or destroy legal work — it redistributes it.

## The Metric in Different Legal Traditions

### Common Law vs. Civil Law

Different legal traditions correspond to different metrics on the same space. The eight dimensions are (we hypothesize) universal — they appear across legal traditions because they capture structural features of normative reasoning. But the *metric* — how differences along these dimensions are weighted, which cross-dimensional correlations matter — varies by tradition.

**Common law** gives heavy weight to precedential constraint ($d_6$). The common-law metric makes it cheap to traverse edges to factually similar precedents and expensive to distinguish or overrule them. The covariance matrix in a common-law jurisdiction will have large diagonal entries for $d_6$, reflecting the high variance (and high importance) of precedential constraint.

**Civil law** gives heavy weight to statutory authority ($d_4$) and relatively less weight to precedential constraint. The civil-law metric makes it cheap to traverse edges between cases governed by the same code provision and expensive to cross between code sections. The covariance matrix in a civil-law jurisdiction will emphasize the coupling between statutory authority and remedial scope ($\Sigma_{4,7}$).

**Religious law** (Islamic *fiqh*, Jewish *halakha*, Hindu *dharmashastra*) gives heavy weight to entitlement structure ($d_1$) as derived from sacred texts, with the textual authority dimension effectively substituting for $d_4$. The metric in religious legal traditions reflects the primacy of textual interpretation over precedential reasoning.

The framework does not privilege one metric over another. It provides the *space* on which all legal traditions operate and allows the *metric* to vary — just as Riemannian geometry provides a single manifold that can carry different metrics depending on the physical context.

### The Legal Metric Is Not Given — It Is Calibrated

This is the central insight of the legal metric: *the metric is not a priori*. It is *calibrated from data*.

The covariance matrix $\Sigma$ is estimated from the attribute vectors of the case corpus. The boundary penalties $\beta_k$ are estimated from the observed cost of crossing regime boundaries (how often do arguments that cross jurisdictional boundaries succeed? how much more evidence is required?). The hierarchical costs $h$ are determined by the constitutional and institutional structure.

The metric can therefore be *wrong* — miscalibrated. If the covariance matrix is estimated from a biased corpus (say, one that overrepresents a particular type of case), the resulting metric will distort the distance measurements. If the boundary penalties are set too high, the metric will make regime crossings appear more difficult than they actually are, discouraging novel legal arguments that combine doctrines from different regimes.

Calibrating the metric correctly is an empirical programme, not a theoretical exercise. It requires scoring a large corpus of cases on the eight dimensions, estimating the covariance structure, and validating the resulting distances against judicial practice. This programme has not yet been executed on legal data — the analogous programme for moral dimensions has been validated on 20,030 texts with independent replication — but the methodology is established.

### Outcome-Weighted Calibration

The covariance matrix $\hat{\Sigma}$ can be further refined by *outcome-weighted estimation*. Given a corpus of $N$ decided cases with known outcomes $y_i \in \{0, 1\}$ (plaintiff wins/loses), fit a regularized logistic regression:

$$P(y_i = 1 \mid \mathbf{v}(c_i)) = \sigma\!\left(\mathbf{v}(c_i)^T W \mathbf{v}(c_i) + \mathbf{b}^T \mathbf{v}(c_i) + b_0\right)$$

where $W \in \mathbb{R}^{8 \times 8}$ is a symmetric weight matrix and $\mathbf{b} \in \mathbb{R}^8$ captures linear effects. The fitted $W$ is an *outcome-calibrated* inverse covariance matrix: it encodes not just the statistical co-occurrence of dimensions but their *predictive* interaction.

The effective metric becomes $\Sigma_{\text{eff}}^{-1} = \lambda \hat{\Sigma}^{-1} + (1 - \lambda) W$, blending the corpus-derived covariance with outcome-derived predictive structure. The mixing parameter $\lambda$ is set by cross-validation.

This outcome-weighted calibration ensures that the metric reflects not only how dimensions co-vary statistically but how they interact *causally* in determining legal outcomes.

---

> **RUNNING EXAMPLE — THE METRIC IN JUDGE RIVERA'S COURTROOM**
>
> *Rivera handles both employment discrimination cases and voting rights cases. The metrics for these two areas of law differ because the covariance structures differ.*
>
> *In employment discrimination, the strongest cross-dimensional correlation is between factual nexus ($d_2$) and precedential constraint ($d_6$): cases with strong facts tend to have strong precedential support, because the well-established doctrines (McDonnell Douglas, direct evidence) were developed from factually strong cases. The metric in this area is shaped by the $\Sigma_{2,6}$ correlation.*
>
> *In voting rights, the strongest cross-dimensional correlation is between constitutional conformity ($d_5$) and public interest ($d_8$): constitutional voting rights cases almost always involve significant public interest considerations, because the right to vote is inherently collective. The metric in this area is shaped by the $\Sigma_{5,8}$ correlation.*
>
> *Rivera does not consciously think about covariance matrices. But her legal intuition — her sense of which cases are "close" and which are "far" — reflects the implicit metric she has internalized through twenty years of practice. The framework makes this intuition explicit and, in principle, testable: does Rivera's implicit metric match the empirically calibrated metric, or does it diverge in systematic ways?*

---

## Worked Example: Computing Edge Weights

Consider two Title VII cases connected by citation:

**Case A ($c_A$):** *McDonnell Douglas v. Green* (Supreme Court, 1973)
- Attribute vector: $\mathbf{v}_A = (0.8, 0.7, 0.9, 0.9, 0.3, 1.0, 0.7, 0.6)$
- Court level: Supreme
- Year: 1973

**Case B ($c_B$):** A recent district court case applying McDonnell Douglas (District Court, 2025)
- Attribute vector: $\mathbf{v}_B = (0.85, 0.5, 0.8, 0.8, 0.2, 0.7, 0.6, 0.4)$
- Court level: District
- Year: 2025

**Step 1: Attribute-vector difference.**

$$\Delta \mathbf{v} = \mathbf{v}_B - \mathbf{v}_A = (0.05, -0.2, -0.1, -0.1, -0.1, -0.3, -0.1, -0.2)$$

**Step 2: Mahalanobis distance.** Assume a simplified covariance matrix (for illustration) that is diagonal with variances $\sigma_k^2 = 0.04$ for each dimension:

$$d_M^2 = \frac{0.05^2}{0.04} + \frac{0.2^2}{0.04} + \frac{0.1^2}{0.04} + \frac{0.1^2}{0.04} + \frac{0.1^2}{0.04} + \frac{0.3^2}{0.04} + \frac{0.1^2}{0.04} + \frac{0.2^2}{0.04}$$

$$= 0.0625 + 1.0 + 0.25 + 0.25 + 0.25 + 2.25 + 0.25 + 1.0 = 5.3125$$

The dominant contribution is from $d_6$ (precedential constraint), which dropped from 1.0 to 0.7 — reflecting that the district court case has less precedential authority than the foundational Supreme Court case. The second-largest contribution is from $d_2$ (factual nexus), which dropped from 0.7 to 0.5.

**Step 3: Boundary penalty.** Both cases are in the same area of law (Title VII employment discrimination), so there is no regime boundary crossing: $\beta = 0$.

**Step 4: Hierarchical cost.** The edge goes from the Supreme Court ($\ell_A = \text{supreme}$) to the district court ($\ell_B = \text{trial}$): binding authority. Hierarchical cost: $h = 0$.

**Step 5: Total edge weight.** $w(c_A \to c_B) = 5.3125 + 0 + 0 = 5.3125$.

**Reverse edge weight.** $w(c_B \to c_A)$ would have $h = \infty$ (a district court cannot bind the Supreme Court), so this edge is impassable in the reverse direction. The asymmetry is extreme: the edge from the Supreme Court to the district court is costless (in hierarchical terms), while the reverse edge has infinite cost.

## Cross-Dimensional Correlations: What the Data Should Show

### Predicted Correlations

The covariance matrix $\Sigma$ is not merely a statistical artifact. Its off-diagonal entries make *testable predictions* about the structure of legal reasoning. The framework predicts specific patterns of cross-dimensional correlation that should emerge from any well-scored corpus of legal cases.

**The Statute-Remedy Coupling ($\Sigma_{4,7}$).** The correlation between statutory authority ($d_4$) and remedial scope ($d_7$) should be strongly positive. This is because the available remedies are largely determined by the governing statute: Title VII authorizes back pay and reinstatement; Section 1983 authorizes damages; the APA authorizes remand to the agency. A case with high statutory authority (a clear statutory basis for the claim) will typically have well-defined remedial scope, while a case with weak statutory authority (a novel claim without a clear statutory home) will have uncertain remedial scope.

**The Procedure-Merits Gating ($\Sigma_{3,2}$).** The correlation between procedural posture ($d_3$) and factual nexus ($d_2$) should be moderately positive. This reflects the gating function of procedure: a case that survives procedural challenges (high $d_3$) is more likely to have strong factual support (high $d_2$), because weak factual cases are typically dismissed on procedural grounds before reaching the merits.

**The Entitlement-Constitution Coupling ($\Sigma_{1,5}$).** The correlation between entitlement structure ($d_1$) and constitutional conformity ($d_5$) should be strongly positive. Constitutional provisions define the structure of entitlements: the Equal Protection Clause constrains which Hohfeldian configurations are permissible, the Due Process Clause constrains how entitlements can be altered, and the Bill of Rights creates specific immunities. Cases with strong constitutional dimensions necessarily have complex entitlement structures.

**The Precedent-Public Interest Anticorrelation ($\Sigma_{6,8}$).** There may be a *negative* correlation between precedential constraint ($d_6$) and public interest ($d_8$). Cases with high precedential constraint (well-settled law, many controlling precedents) tend to involve low public interest (routine applications of established doctrine), while cases with high public interest (novel questions with broad implications) tend to have weaker precedential constraint (because the novelty means fewer controlling precedents exist). If this anticorrelation is confirmed, it has practical implications: the legal metric would measure a case as "closer" to novel high-impact cases and "farther" from routine applications, even if the two cases share similar factual profiles on other dimensions.

### Falsifiability

Each of these predictions is falsifiable. If $\hat{\Sigma}_{4,7}$ is near zero, the framework's assumption of statute-remedy coupling is wrong. If $\hat{\Sigma}_{3,2}$ is negative (cases that survive procedure have *weaker* facts), the gating hypothesis is wrong. The Mahalanobis distance would still be well-defined, but its interpretation would need revision.

This falsifiability is a strength of the framework. Unlike purely conceptual models of legal reasoning, the legal metric makes quantitative predictions about the correlation structure of legal dimensions that can be tested against data.

### A Proof-of-Concept: Title VII Metric Calibration

To make the calibration concrete, consider the procedure for a specific area of law. In Title VII disparate-treatment claims:

1. Collect approximately 1,000 Title VII opinions from a freely available case database (CourtListener or the Caselaw Access Project).
2. Embed each opinion using LaBSE: $\mathbf{e}(t_i) \in \mathbb{R}^{768}$.
3. Score each opinion on eight dimensions using trained probes: $\mathbf{v}(c_i) \in [0,1]^8$.
4. Estimate $\hat{\Sigma}$ from the scored corpus. Prediction: $\hat{\Sigma}_{4,7}$ (statutory authority -- remedial scope) will be significantly positive.
5. Fit the outcome-weighted matrix $W$ to predict case outcomes. Prediction: the $(2,2)$ entry (factual nexus, quadratic term) and the $(2,4)$ cross-term (factual nexus $\times$ statutory authority) will be the dominant predictive components.
6. Construct directed edges from the citation network, compute Mahalanobis edge weights, and add hierarchical costs.

Both predictions are falsifiable, and the entire pipeline can be executed with existing tools and data.

## The Metric and Judicial Discretion

### Where Discretion Lives

The framework does not eliminate judicial discretion. It *locates* discretion in the metric.

Two judges may agree on the structure of the judicial complex — the same vertices, the same edges, the same attribute vectors. But they may disagree on the covariance matrix $\Sigma$, the boundary penalties $\beta_k$, or the burden-of-proof thresholds. This disagreement is not a failure of the framework. It is a precise formalization of the disagreement that exists in practice.

A judge who gives heavy weight to precedential constraint (large $\sigma_6^{-2}$) will produce short distances to factually similar precedents and long distances to novel arguments. This judge will tend to follow precedent closely and resist novel theories.

A judge who gives heavy weight to public interest (large $\sigma_8^{-2}$) will produce short distances to cases with similar public-interest profiles and may weight public consequences more heavily in her analysis.

The framework makes these differences visible. Instead of debating whether two judges are "conservative" or "liberal" — labels that obscure more than they reveal — we can compare their metrics. Two judges' disagreements can be localized to specific entries of the covariance matrix or specific boundary penalties. The disagreement is no longer about "values" in the abstract; it is about the relative weights of legal dimensions in the concrete.

### The Metric Is the Judge's Implicit Theory

Every experienced judge has an implicit metric — a sense of which cases are close and which are far, which arguments are strong and which are weak, which boundaries are hard to cross and which are routine. This implicit metric is the product of legal education, judicial experience, and intellectual temperament.

The framework does not claim to replace this implicit metric with a computed one. It claims that the implicit metric *exists* — that judicial reasoning has a metric structure, whether or not anyone has measured it — and that making it explicit enables analysis, comparison, and critique.

## Chapter Summary

1. The legal metric measures distance between legal states using the Mahalanobis distance, which accounts for cross-dimensional correlations.

2. Edge weights in the judicial complex have three components: Mahalanobis doctrinal distance, boundary penalties for regime crossings, and hierarchical costs reflecting the authority structure.

3. Legal friction is the total edge weight along a legal argument path. A strong argument has low friction; a weak argument has high friction; an impossible argument has infinite friction.

4. The burden of proof is the shortest-path distance from the plaintiff's position to the goal region. Different standards of proof correspond to different distance thresholds.

5. Burden-shifting redistributes friction between parties without changing the total. The conservation of total friction is consistent with the Liability-Damages Conservation theorem.

6. The metric is not given a priori. It is calibrated from data — from the covariance structure of case attribute vectors and from outcome-weighted regression. Different legal traditions correspond to different metrics on the same space.

---

## Technical Appendix

**Definition (Mahalanobis Distance on the Judicial Complex).** Given the covariance matrix $\Sigma \in \mathbb{R}^{8 \times 8}$ (positive definite), the Mahalanobis distance between vertices $c_i, c_j \in \mathcal{K}$ is:

$$d_M(c_i, c_j) = \sqrt{(\mathbf{v}(c_j) - \mathbf{v}(c_i))^T \Sigma^{-1} (\mathbf{v}(c_j) - \mathbf{v}(c_i))}$$

This defines a Riemannian metric on $\mathbb{R}^8$ with metric tensor $g_{ij} = (\Sigma^{-1})_{ij}$.

**Definition (Asymmetric Edge Weight).** The full edge weight is:

$$w(c_i \to c_j) = \Delta \mathbf{v}^T \Sigma^{-1} \Delta \mathbf{v} + \sum_k \beta_k \cdot \mathbf{1}[\text{crossing regime } k] + h(\ell(c_i), \ell(c_j))$$

The weight is asymmetric: $w(c_i \to c_j) \neq w(c_j \to c_i)$ whenever $h(\ell(c_i), \ell(c_j)) \neq h(\ell(c_j), \ell(c_i))$.

**Definition (Legal Friction).** For a directed path $\gamma = (c_0, c_1, \ldots, c_m)$:

$$\text{BF}_{\text{law}}(\gamma) = \sum_{i=0}^{m-1} w(c_i \to c_{i+1}) + \sum_j \omega_j \cdot \delta_j(\gamma)$$

where $\omega_j$ are evidentiary weights and $\delta_j(\gamma) = \max(0, \theta_j - e_j(\gamma))$ measures the shortfall of evidence $e_j(\gamma)$ below the threshold $\theta_j$.

**Proposition (Metric Consistency).** The Mahalanobis distance is a valid metric (non-negativity, identity of indiscernibles, symmetry, triangle inequality) when restricted to the doctrinal component. The full edge weight is not a metric in the mathematical sense — it is asymmetric — but it defines a valid cost function for shortest-path computation on a directed graph.

**Proposition (Outcome-Weighted Metric).** The effective inverse covariance matrix $\Sigma_{\text{eff}}^{-1} = \lambda \hat{\Sigma}^{-1} + (1 - \lambda)W$ is positive definite when $\hat{\Sigma}^{-1}$ is positive definite, $W$ is positive semi-definite, and $\lambda \in (0, 1]$. The resulting Mahalanobis distance is a valid metric.

---

## Notes on Sources

The Mahalanobis distance was introduced by P. C. Mahalanobis (1936) for cluster analysis in statistics. Its application to case similarity in legal settings is new to this framework. The burden-of-proof formalization builds on the legal literature surveyed by Allen and Pardo (2019). The McDonnell Douglas burden-shifting framework was established in *McDonnell Douglas Corp. v. Green* (1973), with subsequent refinement in *Texas Department of Community Affairs v. Burdine* (1981) and *St. Mary's Honor Center v. Hicks* (1993). The distinction between common-law and civil-law metrics builds on comparative law scholarship by Zweigert and Kotz (1998). The concept of legal friction extends the "burden friction" concept of Bond (2026a, *Geometric Ethics*). Outcome-weighted calibration adapts the supervised metric learning literature surveyed by Kulis (2012).

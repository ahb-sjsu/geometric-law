# Chapter 11: Sentencing Disparities as Gauge Violation Tensors

> *"The quality of mercy is not strain'd, / It droppeth as the gentle rain from heaven / Upon the place beneath."*
> — William Shakespeare, *The Merchant of Venice*, Act IV, Scene I

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera has seen the aggregate statistics: racial disparities in sentencing, gender disparities in bail, socioeconomic disparities in conviction rates. She knows these numbers. Every federal judge knows them. But knowing that the system is unfair in the aggregate is not the same as knowing **where** it is unfair, **how much** it is unfair, and **in which dimensions** the unfairness manifests.*
>
> *This chapter gives Rivera a tool for answering those questions: the gauge violation tensor. The tensor $V_{ij}$ is a matrix whose rows index the type of transformation (race swap, gender swap, socioeconomic swap) and whose columns index the type of outcome (sentence length, bail amount, conviction rate). Each entry $V_{ij}$ measures how much the outcome in dimension $j$ changes under transformation $i$ — the degree to which the legal system violates gauge invariance along that specific axis.*
>
> *The tensor is not a metaphor. It is a computable quantity, derivable from the same sentencing data that the U.S. Sentencing Commission already collects. Rivera intends to compute it for her own district — and for her own courtroom. The results, she suspects, will be uncomfortable. But discomfort is a feature, not a bug: the tensor makes visible what was previously hidden, and what is visible can be measured, monitored, and corrected.*

---

## The Gauge Violation Tensor

### From Scalar to Tensor

Chapter 8 introduced the Legal Bond Index (LBI) as a scalar measure of gauge violation — a single number that quantifies how much the legal evaluation changes under protected-class transformations. The LBI is a useful summary statistic, but it is a *scalar*: it collapses the multi-dimensional structure of legal injustice into a single number.

Injustice is not one-dimensional. A legal system might be gauge-invariant in its conviction rates but gauge-variant in its sentencing. It might treat men and women equally in bail decisions but unequally in plea negotiations. It might be fair to defendants of all races but systematically biased against defendants of low socioeconomic status.

To capture this multi-dimensional structure, we need a tensor — a mathematical object that indexes gauge violations along multiple axes simultaneously.

**Definition (Gauge Violation Tensor).** The *gauge violation tensor* $V_{ij}$ is a matrix where:

- $i$ indexes the **gauge transformation** (the type of protected-characteristic swap):
  - $i = 1$: racial transformation (swap defendant's race)
  - $i = 2$: gender transformation (swap defendant's gender)
  - $i = 3$: socioeconomic transformation (swap defendant's socioeconomic status)
  - $i = 4$: age transformation (swap defendant's age bracket)
  - $i = 5$: citizenship transformation (swap defendant's citizenship status)

- $j$ indexes the **outcome dimension** (the type of legal outcome):
  - $j = 1$: sentence length (months of incarceration)
  - $j = 2$: bail/bond amount (dollars)
  - $j = 3$: conviction rate (probability of conviction)
  - $j = 4$: charge severity (maximum statutory penalty for charged offense)
  - $j = 5$: departure rate (probability of departing from guidelines)

Each entry is:

$$V_{ij} = \frac{1}{|S|} \sum_{s \in S} \frac{|O_j(\tau_i(s)) - O_j(s)|}{O_j(s)}$$

where $S$ is the set of cases, $\tau_i$ is the $i$-th gauge transformation, and $O_j(s)$ is the $j$-th outcome measure for case $s$.

### Reading the Tensor

The gauge violation tensor is a $5 \times 5$ matrix (or whatever dimensions are chosen for transformations and outcomes). Each entry tells a specific story about a specific type of injustice.

$V_{11}$ (race $\times$ sentence length): How much does the sentence change when you swap the defendant's race? This is the most-studied gauge violation in the empirical sentencing literature.

$V_{22}$ (gender $\times$ bail amount): How much does the bail amount change when you swap the defendant's gender? This captures the "gender gap" in pretrial detention.

$V_{13}$ (race $\times$ conviction rate): How much does the probability of conviction change when you swap the defendant's race? This captures racial bias in the adjudication process itself, separate from sentencing.

$V_{31}$ (socioeconomic status $\times$ sentence length): How much does the sentence change when you swap the defendant's socioeconomic status? This captures class bias in sentencing — the degree to which wealth or poverty, education or lack of it, affect the punishment.

The tensor has several useful properties:

**Decomposability.** The total LBI from Chapter 8 is the trace (or norm) of the tensor:

$$\text{LBI} = \frac{1}{n_i \cdot n_j} \sum_i \sum_j V_{ij}$$

The scalar LBI is recovered from the tensor by summing over all transformation and outcome dimensions. The tensor decomposes the scalar into its components.

**Asymmetry detection.** If $V_{ij} \gg V_{kl}$ for $(i,j) \neq (k,l)$, the system's gauge violation is concentrated along specific axes. This guides remediation: focus reform on the high-violation cells of the tensor.

**Cross-dimensional correlations.** The off-diagonal pattern of the tensor reveals how different types of discrimination correlate with different types of outcomes. A system where racial bias affects sentencing ($V_{11}$ high) but not conviction rates ($V_{13}$ low) has a different pathology from one where racial bias affects conviction rates ($V_{13}$ high) but not sentencing ($V_{11}$ low).

---

> **RUNNING EXAMPLE — RIVERA COMPUTES THE TENSOR**
>
> *Rivera's clerk, a former data scientist, helps her compute the gauge violation tensor for the Northern District of California using the Sentencing Commission's data. They use matched-pair analysis: for each case, they identify the closest match in the dataset that differs only on the transformation variable (race, gender, etc.) and compare outcomes.*
>
> *The results, for federal drug cases in the Northern District over the past five years:*
>
> | | Sentence | Bail | Conviction Rate | Charge Severity | Departure Rate |
> |---|---|---|---|---|---|
> | **Race** | 0.191 | 0.224 | 0.043 | 0.087 | 0.112 |
> | **Gender** | 0.142 | 0.098 | 0.031 | 0.056 | 0.178 |
> | **SES** | 0.167 | 0.312 | 0.062 | 0.041 | 0.089 |
> | **Age** | 0.034 | 0.047 | 0.018 | 0.023 | 0.051 |
> | **Citizenship** | 0.071 | 0.189 | 0.039 | 0.102 | 0.067 |
>
> *Rivera reads the tensor. The largest entry is $V_{32} = 0.312$: socioeconomic status has the biggest effect on bail. This makes sense — bail is set partly based on "ability to pay" and "community ties," both of which correlate strongly with socioeconomic status. But the LIP requires that outcomes not depend on socioeconomic status when it is not legally relevant to the offense conduct. Bail is supposed to ensure the defendant's appearance at trial, not to punish poverty.*
>
> *The second-largest entry is $V_{12} = 0.224$: race has a substantial effect on bail. Black defendants receive bail amounts 22.4% higher than comparable white defendants. This is a pure gauge violation — there is no legal justification for racial variation in bail.*
>
> *The third-largest entry is $V_{11} = 0.191$: the well-known racial sentencing disparity. But the tensor reveals that the racial disparity is actually **smaller** in sentencing than in bail. The system is more gauge-variant in pretrial decisions than in post-conviction decisions — a finding that the scalar LBI would have missed.*
>
> *Rivera also notices a pattern in the rows: the gender row has a high departure rate entry ($V_{25} = 0.178$) — female defendants are much more likely to receive downward departures from the guidelines than comparable male defendants. This suggests that the gender disparity in sentencing operates primarily through departures rather than through within-guidelines variation. The tensor not only measures the disparity but identifies the mechanism.*

---

## Computing the Tensor from Data

### The Matching Problem

The fundamental challenge in computing $V_{ij}$ is the *matching problem*: you cannot observe the same defendant with two different races. You must approximate the counterfactual by finding pairs of defendants who are as similar as possible on all legally relevant variables but differ on the transformation variable.

Several statistical methods are available:

**Propensity score matching.** Estimate the probability of group membership (e.g., the probability of being Black given the defendant's offense, criminal history, and other characteristics) and match defendants with similar propensity scores across groups. The difference in outcomes between matched pairs estimates $V_{ij}$.

**Regression adjustment.** Regress the outcome on all legally relevant variables and the transformation variable. The coefficient on the transformation variable estimates $V_{ij}$, controlling for all included covariates.

**Blinder-Oaxaca decomposition.** Decompose the outcome gap between groups into a "explained" component (due to differences in legally relevant characteristics) and an "unexplained" component (due to differences in how the same characteristics are evaluated). The unexplained component estimates the gauge violation.

Each method has limitations. Propensity score matching requires a well-specified model of group membership. Regression adjustment requires correct functional form specification. Blinder-Oaxaca decomposition requires the assumption that the explained and unexplained components are separable. No single method is definitive; convergence across methods strengthens the conclusions.

### The Ideal Experiment

The gauge violation tensor is, conceptually, the output of an experiment that cannot be run: take the same case, change one protected characteristic, re-adjudicate, and compare outcomes. The statistical methods above approximate this experiment using observational data.

A closer approximation is the *audit study*: present decision-makers with identical case files that differ only in the defendant's name (a racially or gender-coded name). The difference in recommendations is a direct estimate of $V_{ij}$, uncontaminated by differences in case characteristics.

Audit studies of bail recommendations, sentencing recommendations, and plea offers have been conducted, typically finding significant gauge violations. The tensor framework systematizes these studies by organizing the results into a single mathematical object that can be analyzed, decomposed, and tracked over time.

### Temporal Dynamics

The gauge violation tensor is not static. It changes over time as laws, norms, and institutional practices evolve. Computing $V_{ij}(t)$ at multiple time points reveals the *dynamics* of legal injustice:

$$\frac{dV_{ij}}{dt} = \text{rate of change of gauge violation along axis } (i,j)$$

A decreasing $V_{ij}$ indicates progress toward gauge invariance along that axis. An increasing $V_{ij}$ indicates regression. A stable $V_{ij}$ indicates a persistent structural violation that is resistant to reform.

The temporal derivative also reveals *reform effectiveness*: after a policy intervention (new sentencing guidelines, implicit bias training, bail reform), does $V_{ij}$ decrease? By how much? How quickly? The tensor provides a quantitative evaluation framework for reform efforts.

## The Structure of the Tensor

### Symmetry Properties

The gauge violation tensor has structural properties that constrain its form and reveal the geometry of the underlying injustice.

**Non-negativity.** Each entry $V_{ij} \geq 0$, because the tensor measures the absolute magnitude of the gauge violation, not its direction. A system that systematically sentences Black defendants more harshly and a system that systematically sentences Black defendants more leniently both have $V_{11} > 0$. The direction of the violation is captured by a *signed* version of the tensor:

$$V_{ij}^{\text{signed}} = \frac{1}{|S|} \sum_{s \in S} \frac{O_j(\tau_i(s)) - O_j(s)}{O_j(s)}$$

The signed tensor reveals which group is disadvantaged: $V_{ij}^{\text{signed}} > 0$ means group $A$ receives harsher treatment; $V_{ij}^{\text{signed}} < 0$ means group $B$ does.

**Row structure.** Each row of the tensor corresponds to a single transformation (e.g., race swap). The row sum is the total gauge violation due to that transformation across all outcome dimensions:

$$V_{i \cdot} = \sum_j V_{ij}$$

A high row sum means that the transformation produces large gauge violations across many outcome dimensions — the system is comprehensively biased along that axis.

**Column structure.** Each column corresponds to a single outcome dimension (e.g., sentence length). The column sum is the total gauge violation in that dimension across all transformations:

$$V_{\cdot j} = \sum_i V_{ij}$$

A high column sum means that the outcome dimension is susceptible to gauge violations from many different transformations — it is a "fragile" dimension where bias easily enters.

### The Eigendecomposition

The gauge violation tensor can be decomposed using singular value decomposition (SVD):

$$V = U \Sigma W^T$$

where $U$ is an orthogonal matrix of "violation modes" (linear combinations of transformations), $\Sigma$ is a diagonal matrix of singular values (violation magnitudes), and $W$ is an orthogonal matrix of "outcome modes" (linear combinations of outcome dimensions).

The first singular value $\sigma_1$ and its associated vectors $u_1, w_1$ identify the *dominant mode of injustice*: the combination of transformations and outcomes that accounts for the largest share of the total gauge violation. The second singular value identifies the next-largest mode, and so on.

This decomposition reveals whether the gauge violations are *structured* (a few dominant modes account for most of the violation) or *diffuse* (many modes contribute roughly equally). A structured violation suggests a single underlying cause (e.g., a specific institutional practice that drives multiple types of bias). A diffuse violation suggests multiple independent causes.

---

> **RUNNING EXAMPLE — RIVERA DECOMPOSES THE TENSOR**
>
> *Rivera's clerk performs the SVD on the district's gauge violation tensor. The results:*
>
> *First singular value: $\sigma_1 = 0.42$, accounting for 58% of total violation.*
> *Associated transformation mode: $u_1 \approx (0.71, 0.45, 0.52, 0.12, 0.15)$ — a weighted combination dominated by race (0.71) and SES (0.52).*
> *Associated outcome mode: $w_1 \approx (0.53, 0.68, 0.18, 0.31, 0.35)$ — dominated by bail (0.68) and sentence (0.53).*
>
> *Second singular value: $\sigma_2 = 0.19$, accounting for 22% of total violation.*
> *Associated transformation mode: $u_2 \approx (0.22, 0.78, 0.15, 0.38, 0.42)$ — dominated by gender (0.78).*
> *Associated outcome mode: $w_2 \approx (0.41, 0.12, 0.15, 0.22, 0.86)$ — dominated by departure rate (0.86).*
>
> *The decomposition tells a clear story. The dominant mode of injustice in the Northern District is **race/SES-driven bail and sentencing disparity**: the combination of racial and socioeconomic bias in pretrial and post-conviction decisions accounts for 58% of the total gauge violation. The second mode is **gender-driven departure disparity**: female defendants receive downward departures at much higher rates, accounting for 22% of total violation.*
>
> *The two modes are nearly independent (the singular vectors are approximately orthogonal), suggesting two distinct mechanisms. The first mode likely reflects systemic biases in risk assessment and "dangerousness" evaluation — processes that correlate with race and SES. The second mode likely reflects a specific judicial norm — a widespread but uncodified belief that female defendants are less dangerous or more deserving of leniency — that operates through the discretionary departure mechanism.*
>
> *Rivera now has actionable intelligence. To reduce gauge violation in the district, the most effective interventions are: (1) reform bail practices to reduce race/SES dependence (addressing the dominant mode), and (2) audit downward departures for gender consistency (addressing the second mode). These two interventions, if successful, would eliminate 80% of the measurable gauge violation.*

---

## Intersectional Analysis

### Beyond Single-Axis Violations

The basic gauge violation tensor indexes violations along single axes: race, gender, SES, age, citizenship. But discrimination often operates *intersectionally*: the treatment of a Black woman may differ from what you would predict by combining the treatment of Black people and the treatment of women separately.

Intersectionality, formalized by Kimberle Crenshaw in 1989, has a natural expression in the tensor framework: it corresponds to *interaction terms* in the gauge violation.

**Definition (Intersectional Gauge Violation).** The *intersectional gauge violation* for transformations $i$ and $k$ in outcome dimension $j$ is:

$$V_{(ik)j} = V_{ij}^{\text{combined}} - V_{ij}^{\text{separate}} - V_{kj}^{\text{separate}}$$

where $V_{ij}^{\text{combined}}$ is the gauge violation when both characteristics $i$ and $k$ are transformed simultaneously, and $V_{ij}^{\text{separate}}$ and $V_{kj}^{\text{separate}}$ are the violations when each is transformed alone.

If $V_{(ik)j} = 0$, the gauge violations are *additive*: the combined violation equals the sum of the individual violations. There is no intersectional effect.

If $V_{(ik)j} > 0$, the gauge violations are *superadditive*: the combined violation exceeds the sum of the individual violations. The intersection creates *additional* discrimination beyond what either axis produces alone.

If $V_{(ik)j} < 0$, the gauge violations are *subadditive*: the combined violation is less than the sum of the individual violations. The intersection provides a *protective* effect — discrimination along one axis is partially offset by the other.

### The Intersectional Tensor

The full intersectional analysis extends the gauge violation tensor from a matrix to a higher-order tensor. The second-order intersectional tensor $V_{ikj}$ has three indices: transformation $i$, transformation $k$, and outcome $j$. Each entry measures the *interaction effect* between two gauge transformations.

For $n$ transformations and $m$ outcomes, the full intersectional analysis requires computing $\binom{n}{2} \times m$ interaction terms. For the five transformations and five outcomes used above, this is $10 \times 5 = 50$ interaction terms — a substantial but tractable computation.

The most important intersectional terms are typically:

- $V_{(12)1}$ (race $\times$ gender interaction on sentence): Does the racial disparity in sentencing differ by gender? If $V_{(12)1} > 0$, Black men face *more* racial discrimination than Black women (superadditive). If $V_{(12)1} < 0$, Black women face *less* racial discrimination than Black men (subadditive, but note this could mean Black women face a different form of intersectional discrimination that is not captured by the sentencing outcome).

- $V_{(13)2}$ (race $\times$ SES interaction on bail): Does the socioeconomic disparity in bail differ by race? This captures the compounding of racial and class disadvantage in pretrial detention.

### Empirical Predictions

The intersectional tensor makes specific empirical predictions that can be tested against sentencing data:

1. **Prediction:** $V_{(12)1} > 0$ — the race-gender interaction on sentencing is superadditive. Black men face more racial discrimination in sentencing than Black women. This prediction is consistent with the Sentencing Commission's finding that gender and race interact: the 19.1% racial disparity is concentrated among male defendants.

2. **Prediction:** $V_{(13)2} > 0$ — the race-SES interaction on bail is superadditive. Poor Black defendants face more racial discrimination in bail than affluent Black defendants. This prediction follows from the role of "community ties" and "ability to pay" in bail decisions, both of which are simultaneously race- and SES-correlated.

3. **Prediction:** $V_{(25)1} > 0$ — the gender-citizenship interaction on sentencing is superadditive. Non-citizen women face more gender discrimination in sentencing than citizen women. This prediction follows from the compounding of immigration detention and gender norms.

Each prediction is testable using existing sentencing data. The tensor framework converts vague claims about "intersectionality" into precise, quantitative predictions about specific interaction terms.

---

> **RUNNING EXAMPLE — RIVERA'S INTERSECTIONAL ANALYSIS**
>
> *Rivera asks her clerk to compute the key intersectional terms for the district. The results:*
>
> *$V_{(12)1} = +0.047$: the race-gender interaction on sentencing is superadditive. Black men face 4.7 percentage points more racial disparity in sentencing than Black women. This is a modest but measurable intersectional effect.*
>
> *$V_{(13)2} = +0.089$: the race-SES interaction on bail is strongly superadditive. Poor Black defendants receive bail amounts 8.9 percentage points higher than what race and SES disparities separately would predict. The intersection of race and poverty in bail decisions is a concentrated locus of gauge violation.*
>
> *$V_{(12)5} = -0.032$: the race-gender interaction on departure rates is subadditive. The gender advantage in departures (women get more downward departures) partially offsets the racial disadvantage (Black defendants get fewer downward departures) for Black women. Black women receive departure rates closer to the overall average than either Black men or white women.*
>
> *Rivera studies these numbers. The intersectional analysis reveals something the single-axis tensor missed: the most acute gauge violation in the district is not race in sentencing ($V_{11} = 0.191$) but **race-plus-SES in bail** ($V_{12} + V_{32} + V_{(13)2} = 0.224 + 0.312 + 0.089 = 0.625$). Poor Black defendants face a compound gauge violation in bail that is more than three times the racial disparity in sentencing.*
>
> *This finding changes her priorities. She had been focused on sentencing reform — the most visible and most studied dimension of disparity. The tensor tells her that bail is where the most acute injustice is concentrated, and that the injustice is driven by the intersection of race and class rather than by either factor alone.*

---

## From Measurement to Diagnosis

### The Diagnostic Power of the Tensor

The gauge violation tensor is not merely a measurement — it is a *diagnostic tool*. Just as a blood panel gives a physician not just a summary of health but a profile that indicates which systems are stressed and which are functioning normally, the gauge violation tensor gives a profile of the legal system that indicates which transformations are problematic, which outcomes are vulnerable, and — most critically — where the mechanisms of injustice are operating.

Consider the diagnostic implications of different tensor profiles:

**Profile 1: High $V_{i1}$ (sentence), low $V_{i2}$ (bail) across all transformations.** This profile indicates that gauge violations are concentrated in sentencing rather than pretrial decisions. The mechanism is post-conviction: the judge or the guidelines are the source of the variance. Remediation should focus on sentencing: guidelines reform, judicial training, appellate review of sentences that deviate from demographic norms.

**Profile 2: High $V_{i2}$ (bail) across all transformations, moderate $V_{i1}$ (sentence).** This profile indicates that gauge violations are concentrated in pretrial decisions. The mechanism is pre-conviction: bail-setting practices are the primary source of variance. Since bail decisions are often made rapidly, with less information than sentencing decisions, they are more susceptible to heuristic bias and implicit associations. Remediation should focus on bail reform: structured bail schedules, risk-assessment instruments that do not use demographic variables, and monitoring of judicial bail-setting patterns.

**Profile 3: High $V_{1j}$ (race) across all outcomes, low $V_{2j}$ (gender).** This profile indicates that racial gauge violations permeate the system — affecting bail, sentencing, charging, and departures — while gender gauge violations are small. The mechanism is systemic racial bias: a pervasive feature of the legal environment that affects every stage of the process. Remediation requires comprehensive, system-wide reform rather than targeted interventions at any single decision point.

**Profile 4: High $V_{ij}$ for all $(i,j)$.** This profile indicates comprehensive gauge violation: the system is biased along every axis and in every outcome dimension. This is the most alarming profile, and it suggests fundamental structural problems rather than isolated failures.

### Causal Inference

The gauge violation tensor measures *association*, not *causation*. A high $V_{11}$ (race $\times$ sentence) tells us that sentences are correlated with race after controlling for legally relevant variables, but it does not tell us *why*. The causal mechanism could be:

- **Direct judicial bias:** Judges impose harsher sentences on minority defendants because of conscious or unconscious racial prejudice.
- **Prosecutorial charging:** Prosecutors bring more serious charges against minority defendants, leading to higher guidelines ranges and longer sentences.
- **Defense quality:** Minority defendants receive lower-quality legal representation, resulting in worse plea bargains and fewer successful motions.
- **Unmeasured confounders:** Variables that are legally relevant but not captured in the data (e.g., demeanor at sentencing, remorse expressed, family support) may correlate with race and explain part of the disparity.

The tensor identifies which cells are large — which is essential for prioritizing reform — but additional analysis is needed to identify the causal pathways. The causal analysis requires different methods: natural experiments (changes in charging policies), instrumental variables (random assignment of judges), and mediation analysis (decomposing the total racial effect into components flowing through charging, plea bargaining, sentencing, and departures).

The tensor and the causal analysis are complementary. The tensor tells you *where* to look; the causal analysis tells you *what you find when you look there*. Together, they provide a complete diagnostic: the magnitude of the gauge violation, its distribution across transformations and outcomes, and the mechanisms through which it operates.

### The Connection to Chapter 10

The gauge violation tensor provides empirical content for the geometric pathologies of Chapter 10. Each pathology produces a characteristic signature in the tensor:

**Heuristic corruption** produces elevated $V_{ij}$ in outcome dimensions where the corrupted heuristic operates. If media-influenced sentencing corrupts the sentencing heuristic, $V_{i1}$ (sentence column) will be elevated for all transformations $i$, because the corrupted heuristic introduces variance that correlates with any protected characteristic associated with media salience.

**Objective hijacking** produces elevated $V_{ij}$ in the charging and plea dimensions. If the prosecution optimizes for conviction rate rather than justice, $V_{i4}$ (charge severity) and the differential between pre-plea and post-trial outcomes will be large: the system over-charges minority defendants (knowing they are more likely to accept plea bargains) and under-charges majority defendants.

**Local minima** produce stable, non-decreasing $V_{ij}$ over time. If the system is trapped in a bad precedent, the gauge violation associated with that precedent will persist even as other violations are reduced. The temporal trajectory $V_{ij}(t)$ will show a "floor" that cannot be breached without overruling the precedent.

**Gauge breaking** is, of course, the direct measurement target of the tensor. But the tensor also reveals whether the gauge breaking is *diffuse* (spread across many cells, suggesting systemic bias) or *concentrated* (localized in specific cells, suggesting specific mechanisms). Concentrated gauge breaking is easier to remediate; diffuse gauge breaking requires systemic reform.

## Monitoring and Benchmarking

### The Gauge Violation Dashboard

The gauge violation tensor, once computed, provides the foundation for a monitoring system — a "dashboard" that tracks the system's gauge invariance over time and across jurisdictions.

**Temporal monitoring.** Compute $V_{ij}(t)$ quarterly or annually. Plot the trajectories. Identify trends: which cells are improving? Which are worsening? Which are stable?

**Jurisdictional comparison.** Compute $V_{ij}$ for each federal district. Rank districts by total gauge violation ($\sum_{ij} V_{ij}$). Identify outliers: districts with unusually high or low violation. Investigate causes.

**Individual-level monitoring.** Compute $V_{ij}$ for individual judges. This is the most sensitive application of the tensor: it tells each judge where their own decisions deviate from gauge invariance. It is also the most controversial — judges may resist being "scored" on their fairness. But the data is already collected (the Sentencing Commission tracks every federal sentence), and the computation is straightforward.

### Setting Benchmarks

What level of gauge violation is acceptable? The framework does not prescribe a specific threshold — that is a policy decision. But it provides a framework for thinking about benchmarks:

**Zero benchmark.** Perfect gauge invariance: $V_{ij} = 0$ for all $(i,j)$. This is the ideal but is likely unachievable in practice, given the noise in legal decision-making and the impossibility of perfectly controlling for all legally relevant variables.

**Statistical noise benchmark.** The gauge violation due to random variation in case characteristics and judicial decision-making. Even a perfectly gauge-invariant system would show some non-zero $V_{ij}$ due to imperfect matching and sampling error. The noise benchmark is the $V_{ij}$ that would be expected under the null hypothesis of gauge invariance.

**Improvement benchmark.** A percentage reduction from the current level. If $V_{11} = 0.191$ today, a benchmark might be $V_{11} < 0.10$ within five years — a 48% reduction.

**Comparative benchmark.** Match the best-performing jurisdiction. If District $A$ has $V_{11} = 0.08$ and District $B$ has $V_{11} = 0.24$, District $B$'s benchmark might be to match District $A$'s level.

## Worked Example: Computing $V_{ij}$ for a Federal District

### Data

Consider a hypothetical federal district with 2,000 drug sentencing cases over five years. Each case has:

- Defendant demographics: race (Black/White/Hispanic), gender (M/F), SES (low/medium/high), age, citizenship
- Offense characteristics: drug type, quantity, role in offense, prior criminal history
- Outcome: sentence in months

### Step 1: Matching

For each case $s$ with defendant race = Black, find the closest match $s'$ with defendant race = White, matched on:
- Same drug type
- Quantity within 10%
- Same criminal history category
- Same role in offense (leader/manager/courier)
- Same district, same year

This produces $N$ matched pairs $(s_k, s'_k)$.

### Step 2: Computing $V_{11}$ (Race $\times$ Sentence)

$$V_{11} = \frac{1}{N} \sum_{k=1}^{N} \frac{|\text{sentence}(s_k) - \text{sentence}(s'_k)|}{\text{sentence}(s'_k)}$$

For the hypothetical district: $V_{11} = 0.187$ (18.7% average difference in sentence length between matched Black and White defendants).

### Step 3: Computing the Full Tensor

Repeat Step 2 for each combination of transformation and outcome. The full tensor:

| | Sentence | Bail | Conviction Rate | Charge Severity | Departure Rate |
|---|---|---|---|---|---|
| **Race** | 0.187 | 0.213 | 0.038 | 0.082 | 0.104 |
| **Gender** | 0.138 | 0.091 | 0.027 | 0.051 | 0.172 |
| **SES** | 0.159 | 0.298 | 0.058 | 0.039 | 0.083 |
| **Age** | 0.031 | 0.042 | 0.015 | 0.021 | 0.047 |
| **Citizenship** | 0.068 | 0.181 | 0.036 | 0.097 | 0.062 |

### Step 4: Analysis

**Total gauge violation:** $\sum_{ij} V_{ij} = 2.520$

**Dominant violations:** $V_{32}$ (SES $\times$ Bail) = 0.298, $V_{12}$ (Race $\times$ Bail) = 0.213, $V_{11}$ (Race $\times$ Sentence) = 0.187

**Row sums (total violation by transformation):**
- Race: 0.624
- Gender: 0.479
- SES: 0.637
- Age: 0.156
- Citizenship: 0.444

Race and SES produce the largest total violations, followed by gender and citizenship. Age is the smallest violator, consistent with the rational basis review standard (age is a less protected characteristic).

**Column sums (total violation by outcome):**
- Sentence: 0.583
- Bail: 0.825
- Conviction rate: 0.174
- Charge severity: 0.290
- Departure rate: 0.468

Bail is the most gauge-variant outcome, followed by sentence and departure rate. Conviction rate is the least gauge-variant — suggesting that the adjudication process itself is more gauge-invariant than the sentencing and pretrial processes.

### Step 5: Intervention Design

The tensor suggests three priority interventions:

1. **Bail reform** (targeting $V_{\cdot 2} = 0.825$): Reduce the gauge violation in bail by implementing risk-assessment tools that do not use race or SES as inputs, and by reducing reliance on money bail.

2. **Sentencing consistency** (targeting $V_{\cdot 1} = 0.583$): Reduce the gauge violation in sentencing by providing judges with their individual LBI data, training on implicit bias, and strengthening appellate review of within-guidelines sentences that show demographic patterns.

3. **Departure auditing** (targeting $V_{25} = 0.172$): Audit downward departures for gender consistency, and require judges to document the specific factors justifying any departure.

### Step 6: Evaluating Reform

Suppose the district implements bail reform in Year 1 and sentencing consistency training in Year 2. The gauge violation tensor is recomputed annually. The expected trajectory:

**Year 0 (baseline):** $V_{\cdot 2} = 0.825$, $V_{\cdot 1} = 0.583$.

**Year 1 (after bail reform):** $V_{\cdot 2}$ decreases (the new risk-assessment tools reduce demographic dependence in bail). $V_{\cdot 1}$ is unchanged (sentencing reform has not yet been implemented). The total gauge violation decreases, but only in the bail column.

**Year 2 (after sentencing training):** $V_{\cdot 1}$ begins to decrease (judges are aware of their individual LBI data and adjust). $V_{\cdot 2}$ stabilizes at its new, lower level.

**Year 3 and beyond:** Both columns continue to decrease as the reforms take hold and new precedent is decided under the reformed conditions. The tensor provides the evaluation framework: each cell tracks the reform's impact on a specific type of injustice.

If a cell fails to decrease after reform, the reform is not addressing the underlying mechanism. The tensor identifies which reforms are working and which are not — which cells are responding to intervention and which are resistant.

## The Tensor as a Lens on Legal History

### Historical Gauge Violations

The gauge violation tensor is not only a tool for current analysis — it is a lens for understanding legal history. The history of American law can be read as a history of gauge violations and their progressive (if incomplete) reduction.

**The antebellum era.** The gauge violation tensor for the pre-Civil War legal system would show extreme values: $V_{11}$ (race $\times$ legal status) would be maximal, because race determined whether a person was free or enslaved — the most extreme possible gauge violation. The Thirteenth, Fourteenth, and Fifteenth Amendments were, in tensor terms, interventions that aimed to drive $V_{1j}$ toward zero for all outcome dimensions $j$.

**The Jim Crow era.** The post-Reconstruction legal system showed reduced but still enormous gauge violations: $V_{11}$ (race $\times$ sentence) was high (Black defendants received harsher sentences), $V_{12}$ (race $\times$ bail) was high (Black defendants were held on higher bail or denied bail entirely), and $V_{13}$ (race $\times$ conviction rate) was high (all-white juries convicted Black defendants at much higher rates). The Civil Rights era — Brown v. Board, the Civil Rights Act of 1964, the Voting Rights Act of 1965 — was an intervention aimed at reducing the entire first row of the tensor.

**The modern era.** The current tensor shows reduced but persistent gauge violations. The racial disparities are smaller than in the Jim Crow era but remain substantial. Gender disparities have been partially addressed (intermediate scrutiny) but persist in sentencing and departures. Socioeconomic disparities have received less legal attention (rational basis review) and remain large.

The historical trajectory of the tensor tells a story of progressive gauge restoration — incomplete, uneven, and subject to reversals, but real. Each legal reform can be evaluated by its effect on the tensor: which cells did it reduce? By how much? How quickly? Did it create new gauge violations in other cells?

## Chapter Summary

1. The gauge violation tensor $V_{ij}$ is a matrix that indexes gauge violations along two dimensions: the type of transformation ($i$) and the type of outcome ($j$). It decomposes the scalar LBI into its multi-dimensional components.

2. Each entry $V_{ij}$ is computable from sentencing data using matched-pair analysis, regression adjustment, or audit studies.

3. The tensor reveals the structure of legal injustice: which transformations cause the most violation, which outcomes are most susceptible, and how transformations and outcomes interact.

4. The eigendecomposition of the tensor identifies the dominant modes of injustice — the principal axes along which gauge violations are concentrated.

5. Intersectional analysis extends the tensor to capture interaction effects between transformations. Superadditive interactions (e.g., race $\times$ SES in bail) identify compounding disadvantages.

6. The tensor provides a framework for monitoring, benchmarking, and evaluating reform. Temporal tracking of $V_{ij}(t)$ reveals whether interventions are reducing gauge violation.

7. The most actionable finding from the worked example is that bail is more gauge-variant than sentencing — pretrial decisions are where the most acute injustice is concentrated.

---

## Technical Appendix

**Definition (Gauge Violation Tensor — Full).** For a set of cases $S$, a set of gauge transformations $\mathcal{G} = \{\tau_1, \ldots, \tau_m\}$, and a set of outcome functions $\mathcal{O} = \{O_1, \ldots, O_n\}$:

$$V_{ij} = \frac{1}{|S|} \sum_{s \in S} \frac{|O_j(\tau_i(s)) - O_j(s)|}{\max(O_j(s), \epsilon)}$$

where $\epsilon > 0$ is a regularization constant to avoid division by zero.

**Definition (Signed Gauge Violation Tensor).**

$$V_{ij}^{\text{signed}} = \frac{1}{|S|} \sum_{s \in S} \frac{O_j(\tau_i(s)) - O_j(s)}{\max(O_j(s), \epsilon)}$$

The signed tensor has $V_{ij}^{\text{signed}} > 0$ when transformation $\tau_i$ increases outcome $O_j$ and $V_{ij}^{\text{signed}} < 0$ when it decreases it. The unsigned tensor satisfies $V_{ij} = |V_{ij}^{\text{signed}}|$ when all cases have the same direction of violation (all advantages go to the same group).

**Definition (Intersectional Gauge Violation Tensor).** The second-order intersectional tensor:

$$V_{ikj} = V_{ij}^{(\tau_i \circ \tau_k)} - V_{ij}^{(\tau_i)} - V_{kj}^{(\tau_k)}$$

where $V_{ij}^{(\tau_i \circ \tau_k)}$ is the gauge violation when both transformations $\tau_i$ and $\tau_k$ are applied simultaneously.

**Proposition (SVD of the Gauge Violation Tensor).** The gauge violation tensor $V \in \mathbb{R}^{m \times n}$ admits a singular value decomposition $V = U \Sigma W^T$ where:
- $U \in \mathbb{R}^{m \times r}$ is the matrix of left singular vectors (transformation modes)
- $\Sigma = \text{diag}(\sigma_1, \ldots, \sigma_r)$ with $\sigma_1 \geq \cdots \geq \sigma_r > 0$
- $W \in \mathbb{R}^{n \times r}$ is the matrix of right singular vectors (outcome modes)
- $r = \text{rank}(V) \leq \min(m, n)$

The fraction of total violation explained by the first $k$ modes is:

$$f_k = \frac{\sum_{i=1}^k \sigma_i^2}{\sum_{i=1}^r \sigma_i^2}$$

**Proposition (Relationship to LBI).** The Legal Bond Index is related to the gauge violation tensor by:

$$\text{LBI} = \frac{1}{m \cdot n} \|V\|_1 = \frac{1}{m \cdot n} \sum_{i,j} V_{ij}$$

where $\|V\|_1$ is the elementwise $L_1$ norm. Equivalently, $\text{LBI} = \frac{1}{m \cdot n} \text{tr}(V \cdot \mathbf{1}_{n \times 1} \cdot \mathbf{1}_{1 \times m})$.

**Proposition (Statistical Significance).** Under the null hypothesis of gauge invariance ($V_{ij} = 0$), the estimated $\hat{V}_{ij}$ from a sample of $N$ matched pairs is approximately normally distributed:

$$\hat{V}_{ij} \sim \mathcal{N}\left(0, \frac{\sigma_{ij}^2}{N}\right)$$

where $\sigma_{ij}^2$ is the variance of the pairwise differences. The null hypothesis is rejected at level $\alpha$ when $|\hat{V}_{ij}| > z_{\alpha/2} \cdot \sigma_{ij} / \sqrt{N}$.

---

## Notes on Sources

The gauge violation tensor is the legal application of the gauge violation measurement methodology developed in the Geometric Ethics framework (Bond, 2026). The concept directly extends the gauge violation tensor from Geometric Reasoning Chapter 8 (as referenced in the SERIES_OUTLINES). Sentencing disparity data is from the U.S. Sentencing Commission's *Demographic Differences in Sentencing* reports (2012, 2017, 2020). The 19.1% racial disparity figure is from the Commission's 2017 report. Gender disparities in sentencing are documented in Starr (2015), "Estimating Gender Disparities in Federal Criminal Cases." Bail disparities are documented in Arnold, Dobbie, and Yang (2018), "Racial Bias in Bail Decisions." Intersectionality theory was formalized by Crenshaw (1989), "Demarginalizing the Intersection of Race and Sex." The SVD-based decomposition of fairness tensors is methodologically related to principal component analysis of bias in machine learning (Bolukbasi et al., 2016). The matched-pair analysis methodology follows Rosenbaum (2002), *Observational Studies*. The Blinder-Oaxaca decomposition was introduced by Blinder (1973) and Oaxaca (1973) for wage gap analysis and has been applied to sentencing by Rehavi and Starr (2014).

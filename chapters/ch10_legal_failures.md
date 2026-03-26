# Chapter 10: Legal Failures as Geometric Pathologies

> *"The law is a sort of hocus-pocus science, that smiles in yer face while it picks yer pocket."*
> — Charles Macklin, *Love A-la-Mode* (1759)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera has been on the bench for twenty years. In that time, she has sentenced over a thousand defendants, presided over hundreds of civil trials, and ruled on thousands of motions. She has developed what she believes is a sound judicial temperament — careful, principled, attentive to the law and the facts.*
>
> *But a new study crosses her desk that gives her pause. A team of researchers at a Bay Area university has analyzed the sentencing patterns of all federal judges in the Northern District of California over the past decade. The findings are disturbing. They identify four distinct failure modes in judicial decision-making — four ways in which the legal system systematically departs from the geometric ideal of gauge-invariant, optimal pathfinding on the judicial complex.*
>
> *Rivera reads the study and recognizes, with uncomfortable clarity, that her own docket exhibits all four pathologies. Not dramatically. Not in ways that would draw an appellate reversal. But measurably, consistently, and — until now — invisibly.*
>
> *The four failure modes are not new to jurisprudence. Scholars have written about each of them for decades. What is new is the geometric framework that unifies them: each failure mode is a specific **geometric pathology** — a distortion of the judicial complex's structure that causes the legal system to produce systematically wrong outputs. Heuristic corruption, objective hijacking, local minima, and gauge breaking are not merely "problems" with the legal system. They are mathematically characterizable deformations of the legal space, each with a diagnostic signature and — in principle — a geometric remedy.*

---

## The Four Geometric Pathologies

### A Unified Framework for Legal Failure

The preceding chapters developed a positive theory: law as geometry, with legal reasoning as pathfinding on the judicial complex, precedent as weight deformation, equal protection as gauge invariance. This chapter turns to the negative side: what happens when the geometry goes wrong.

The Geometric Ethics programme identified four fundamental failure modes in AI alignment: heuristic corruption, objective hijacking, local minima, and gauge breaking. Each failure mode corresponds to a specific geometric pathology — a distortion of the space, the search, the objective, or the symmetry that causes the system to produce wrong outputs despite "doing everything right" within its distorted frame.

These four failure modes map directly onto well-documented pathologies of the legal system. The mapping is not by analogy; it is by shared mathematical structure. The legal system, like an AI system, searches a structured space using heuristics to find optimal paths subject to constraints. The same geometric distortions that cause AI failures cause legal failures — for the same structural reasons.

| Geometric Pathology | AI Failure Mode | Legal Failure Mode |
|---|---|---|
| Heuristic corruption | Training on biased data | Media-influenced sentencing, racial bias in precedent |
| Objective hijacking | Reward hacking, sycophancy | Plea bargaining as approval-seeking, conviction rate maximization |
| Local minima | Trapped in suboptimal solutions | Bad precedent courts cannot escape, entrenched doctrines |
| Gauge breaking | Representation sensitivity | Sentencing disparities, framing effects on juries |

## Heuristic Corruption: When the Guidance Is Wrong

### The Corrupted Heuristic

Chapter 6 showed that legal doctrines function as heuristic functions — they estimate the remaining cost of reaching a legal goal, guiding the search through the judicial complex toward promising regions and away from dead ends. A good heuristic is admissible (never overestimates the true cost) and informative (provides tight estimates that focus the search).

A *corrupted* heuristic is one that estimates costs incorrectly — not because of poor calibration, but because the heuristic itself has been contaminated by irrelevant information. In AI, heuristic corruption occurs when the training data contains biases that the heuristic absorbs and propagates. In law, heuristic corruption occurs when the precedent field — the accumulated body of case law that guides judicial reasoning — encodes biases that distort the search.

**Definition (Heuristic Corruption).** A doctrinal heuristic $h_D$ is *corrupted* if it systematically misestimates the cost of reaching the goal due to contamination by legally irrelevant factors:

$$h_D^{\text{corrupted}}(c) = h_D^{\text{true}}(c) + \epsilon(c)$$

where $\epsilon(c)$ is a bias term that correlates with legally irrelevant features (the defendant's race, the crime's media profile, the political climate).

### Media-Influenced Sentencing

The most visible form of heuristic corruption in the legal system is the influence of media coverage on sentencing. When a crime receives extensive media attention, the judge's heuristic for "appropriate sentence" is contaminated by the salience of the crime — by how vivid, dramatic, and emotionally charged the media coverage has been.

The mechanism is well-documented in cognitive psychology: the *availability heuristic* causes people to overestimate the frequency and severity of events that are easily recalled. A judge who has been exposed to extensive media coverage of a crime overestimates the severity of similar crimes and underestimates the severity of crimes that receive little coverage. The doctrinal heuristic absorbs this bias:

$$h_{\text{sentencing}}^{\text{corrupted}}(c) = h_{\text{sentencing}}^{\text{true}}(c) + \alpha \cdot \text{media\_salience}(c)$$

where $\alpha > 0$ is the media influence coefficient. The corrupted heuristic assigns higher estimated cost (more severe sentence) to cases with high media salience, regardless of their actual legal severity.

The empirical evidence is substantial. Studies have shown that sentences are measurably harsher for crimes that receive media coverage, after controlling for offense severity and criminal history. The effect is strongest in jurisdictions where judges are elected — where media salience translates directly into political pressure.

### Racial Bias as Heuristic Corruption

A deeper and more pervasive form of heuristic corruption is the encoding of racial bias in the precedent field. The body of case law — the accumulated weight deformation that defines the legal heuristic — was built in a society with a long history of racial injustice. The precedents encode the biases of the judges who decided them, the lawyers who argued them, and the social conditions in which they arose.

This is not a claim about the intentions of individual judges. It is a structural claim about the heuristic field. Just as an AI heuristic trained on biased data will reproduce the bias regardless of the intentions of the engineers who built it, a legal heuristic built on biased precedent will reproduce the bias regardless of the intentions of the judges who follow it.

The geometric diagnosis: the edge weights in the judicial complex have been deformed by precedent that was decided under conditions of racial inequality. These deformed weights make certain paths (paths that lead to harsher treatment of minority defendants) cheaper than they should be and other paths (paths that lead to equal treatment) more expensive. A judge who faithfully follows the heuristic — who applies the precedent as written — reproduces the bias embedded in the precedent field.

---

> **RUNNING EXAMPLE — HEURISTIC CORRUPTION ON RIVERA'S DOCKET**
>
> *Rivera examines her drug sentencing cases and notices a pattern. Cases involving crack cocaine receive substantially harsher sentences than cases involving powder cocaine at equivalent quantities. This is not surprising — the federal sentencing guidelines historically mandated a 100:1 disparity (100 grams of powder cocaine triggered the same sentence as 1 gram of crack). The Fair Sentencing Act of 2010 reduced the disparity to 18:1, and the EQUAL Act would have eliminated it entirely.*
>
> *But Rivera notices something more subtle. Even after controlling for the statutory changes, her sentences in crack cases are approximately 12% harsher than her sentences in comparable powder cases. The guidelines now produce similar ranges for equivalent quantities, yet her heuristic — her intuitive sense of "appropriate sentence" for a drug case — has not fully adjusted. Twenty years of practice under the old guidelines deformed her heuristic, and the deformation persists even after the guidelines changed.*
>
> *This is heuristic corruption. The precedent field — including Rivera's own accumulated experience — encodes a bias that was baked in by the old sentencing structure. The bias was originally rational (it reflected the statutory scheme), but the scheme was racially discriminatory (crack cocaine was disproportionately associated with Black defendants), and the scheme has since been partially corrected. The heuristic, however, has not been fully corrected. It retains the old deformation.*
>
> *Rivera also notices the media effect. Two of her recent drug cases involved defendants who were featured in local news coverage. In both cases, she imposed sentences at the top of the guidelines range. In comparable cases without media coverage, she imposed sentences at or below the midpoint. The difference: 15 months. She had not been conscious of the media influence at the time of sentencing.*
>
> *The geometric framework helps her see what happened: the media coverage corrupted her heuristic by injecting a salience term that made the "distance to adequate punishment" seem longer than it actually was. The corrupted heuristic pushed her toward harsher sentences — not because the cases were more severe, but because they were more vivid.*

---

## Objective Hijacking: When the System Optimizes the Wrong Thing

### The Hijacked Objective

In AI alignment, *objective hijacking* (also called *reward hacking*) occurs when a system finds a way to maximize its objective function without actually achieving the intended goal. A chatbot trained to maximize user approval may learn to agree with everything the user says, regardless of truth — a behavior called sycophancy. The system is optimizing its *stated* objective (approval) at the expense of its *intended* objective (helpfulness).

The legal system has its own version of objective hijacking: situations where the institutional incentives cause legal actors to optimize a measurable proxy rather than the underlying goal of justice.

**Definition (Objective Hijacking).** *Objective hijacking* in the legal system occurs when a legal actor optimizes a measurable proxy $f_{\text{proxy}}(x)$ rather than the intended legal objective $f_{\text{true}}(x)$, because the proxy is easier to measure, easier to maximize, or more directly rewarded:

$$\arg\max_x f_{\text{proxy}}(x) \neq \arg\max_x f_{\text{true}}(x)$$

The actor's behavior is rational with respect to the proxy but irrational with respect to the true objective.

### Plea Bargaining as Sycophancy

The most pervasive form of objective hijacking in the American legal system is plea bargaining. Approximately 97% of federal criminal cases and 94% of state criminal cases are resolved by guilty pleas rather than trials. The plea bargaining system is, in geometric terms, a massive instance of objective hijacking — where the system's stated objective (just adjudication) has been replaced by a proxy objective (efficient case resolution).

The analogy to AI sycophancy is precise. In sycophancy, the AI agrees with the user's stated preference regardless of whether that preference is correct, because agreement maximizes the approval signal. In plea bargaining, the defendant agrees with the prosecution's characterization of the case regardless of whether that characterization is accurate, because agreement minimizes the sentence.

The geometric mechanism:

- **True objective:** Find the optimal path through the judicial complex — the path that correctly weighs the evidence, applies the law, and reaches a just outcome.
- **Proxy objective:** Minimize the defendant's exposure — find the path that minimizes the sentence, regardless of whether that path accurately reflects the facts and the law.
- **The hijack:** The prosecution offers a shorter path to a guaranteed (but suboptimal) outcome: "plead guilty to a lesser charge, and we will recommend 24 months instead of risking 60 months at trial." The defendant takes the shortcut, not because 24 months is the correct outcome, but because the expected cost of the alternative (trial) is too high.

The system is maximizing a proxy (case throughput, plea rate, sentence minimization) rather than the true objective (accurate adjudication). The shortcut bypasses the full search through the judicial complex — the discovery, the weighing of evidence, the adversarial testing of arguments — and arrives at a vertex that may bear little resemblance to the vertex the full search would have reached.

### Conviction Rate Maximization

A related form of objective hijacking occurs when prosecutors optimize for conviction rate rather than justice. The stated objective of a prosecutor is to "do justice" — to bring appropriate charges, present the evidence fairly, and accept the verdict. But the measurable proxy — the conviction rate — creates a perverse incentive to overcharge, withhold exculpatory evidence, and pressure defendants into pleas.

In the geometry of the complex, this manifests as a *distortion of the goal region*. The prosecutor's true goal region $G_{\text{justice}}$ contains vertices where guilty defendants are convicted, innocent defendants are acquitted, and sentences are proportionate. The proxy goal region $G_{\text{conviction}}$ contains only vertices where the defendant is convicted, regardless of guilt. The proxy region is larger and easier to reach — it includes vertices that the true region excludes (wrongful convictions).

The conviction-maximizing prosecutor explores paths that lead to $G_{\text{conviction}}$ rather than $G_{\text{justice}}$. These paths may be shorter (because the proxy region is larger) but they are wrong (because they include unjust outcomes). The system has been hijacked: the measurable output (conviction rate) looks good, but the unmeasured objective (justice) is being sacrificed.

---

> **RUNNING EXAMPLE — OBJECTIVE HIJACKING ON RIVERA'S DOCKET**
>
> *Rivera reviews her criminal docket statistics. Of the 342 criminal cases on her docket in the past three years, 327 — 95.6% — were resolved by guilty pleas. Only 15 went to trial. Of those 15, the government won 12 (80% conviction rate at trial).*
>
> *She finds these numbers troubling. A 95.6% plea rate means that the adversarial system — the constitutionally guaranteed mechanism for testing the government's case — operates in only 4.4% of cases. The legal system is designed around the assumption that cases will be tried; plea bargaining was historically the exception. Now it is the rule, and the system has adapted: courts do not have the resources to try even a fraction of the cases on their dockets.*
>
> *Rivera identifies the objective hijack. The system's true objective is just adjudication — correct outcomes for each defendant. The proxy objective is efficient case disposition — clearing the docket. The proxy has taken over: the system is optimized for throughput, not accuracy.*
>
> *She sees this most clearly in the sentencing differentials. Defendants who plead guilty receive, on average, sentences 30-40% shorter than defendants convicted at trial. This is called the "trial penalty" — the premium defendants pay for exercising their constitutional right to a jury trial. In geometric terms, the trial penalty is a *cost inflation* on the trial path: the system has made the full-search path through the judicial complex so expensive that rational defendants avoid it, even when the full search might produce a better outcome.*
>
> *The result is sycophantic: defendants agree with the prosecution's characterization of the case — "yes, I am guilty of this lesser charge" — not because the characterization is accurate, but because agreement minimizes personal cost. The system rewards agreement and punishes disagreement. This is the structure of sycophancy, transplanted from AI alignment to constitutional law.*

---

## Local Minima: When the System Cannot Escape Bad Precedent

### The Trapped System

In optimization, a *local minimum* is a point where the objective function is lower than at all neighboring points, but not at the global minimum. A system that searches by hill-climbing (moving to neighboring points with lower cost) will become trapped at a local minimum — it cannot escape because every neighboring point is worse, even though a much better point exists far away.

In the legal system, local minima are *bad precedents that courts cannot escape*. The precedent deforms the edge weights in its neighborhood so that all paths from the current case lead through the precedent — and the precedent produces a suboptimal outcome. The system is stuck: following the precedent produces a bad result, but overruling it is too costly (the reliance interest barrier from Chapter 9 is too high).

**Definition (Legal Local Minimum).** A *legal local minimum* is a vertex $c_{\text{min}} \in \mathcal{K}$ (corresponding to an established precedent) such that:

1. The outcome at $c_{\text{min}}$ is suboptimal: $J_{\text{law}}(c_{\text{min}})$ is worse (less just, less efficient, less coherent) than $J_{\text{law}}(c_{\text{global}})$ at the global optimum.
2. All neighboring vertices have higher cost: $\text{BF}_{\text{law}}(\gamma) > \text{BF}_{\text{law}}(c_{\text{min}})$ for all short paths $\gamma$ from $c_{\text{min}}$ to any other vertex in the goal region.
3. The cost barrier to the global optimum is high: the overruling cost (from Chapter 9) exceeds the benefit of reaching the better outcome.

The system is trapped: the local minimum is not the best outcome, but the cost of escaping exceeds the improvement from reaching a better outcome.

### Entrenched Bad Doctrines

The legal system is full of local minima — doctrines that persist not because they are correct but because the cost of overturning them is prohibitive. Some examples:

**Qualified immunity.** The doctrine of qualified immunity, established by the Supreme Court in *Harlow v. Fitzgerald* (1982) and progressively expanded, shields government officials from civil liability unless their conduct violates "clearly established" law. The doctrine has been widely criticized by scholars across the political spectrum as creating a nearly impenetrable barrier to civil rights suits. But the doctrine persists because:

- It has been followed by thousands of cases at every level of the federal judiciary (high reliance interest).
- Overruling it would expose government officials to a flood of retroactive liability (high transition cost).
- The Supreme Court has repeatedly declined to reconsider it, even while acknowledging its problems (the barrier is higher than any individual case's benefit from overruling).

Qualified immunity is a local minimum: the outcome is suboptimal (meritorious civil rights claims are dismissed), but the cost of escaping is higher than the benefit of any individual improvement.

**The third-party doctrine.** In *Smith v. Maryland* (1979), the Supreme Court held that individuals have no reasonable expectation of privacy in information they voluntarily share with third parties (such as phone numbers dialed). This doctrine, established in the era of rotary telephones, now governs the government's access to vast digital records — cell site location data, internet browsing history, social media activity — that people "share" with service providers in the course of daily life.

The doctrine is widely recognized as outdated — the Supreme Court itself limited it in *Carpenter v. United States* (2018) — but it has not been overruled. It persists as a local minimum: the cost of fully overruling it (re-evaluating decades of search-and-seizure cases decided under the doctrine) exceeds the benefit of any individual case.

### The Geometry of Entrapment

The geometric diagnosis of a local minimum is straightforward: the precedent has created a *basin of attraction* in the judicial complex — a region where all paths lead downhill toward the precedent's outcome. A case that enters the basin is pulled toward the local minimum by the weight deformation of the precedent field.

Escaping the basin requires a *long-range jump* — a path that crosses the basin boundary and reaches a different region of the complex. In legal terms, this is overruling: a discontinuous change in edge weights that flattens the basin and allows paths to reach the global optimum. But the cost of the jump (overruling cost) creates a barrier at the basin boundary, and the system remains trapped as long as the barrier exceeds the available energy.

The height of the barrier is not fixed. It depends on:

- **The number of relying cases** (more cases = higher barrier).
- **The strength of the reliance interest** (more significant cases = higher barrier).
- **The availability of alternative paths** (if the local minimum can be distinguished or limited rather than overruled, the effective barrier is lower).
- **The political and institutional costs of overruling** (Supreme Court justices may be reluctant to overrule recent precedents of their predecessors).

---

> **RUNNING EXAMPLE — LOCAL MINIMA ON RIVERA'S DOCKET**
>
> *Rivera encounters a qualified immunity motion in a civil rights case. James Okonkwo — the same plaintiff from Chapter 9 — has sued not only under Bivens but also under 42 U.S.C. Section 1983 (applicable because state police officers were also involved in his detention). The federal defendants move for qualified immunity.*
>
> *The motion forces Rivera into a local minimum. To defeat qualified immunity, Okonkwo must show that the officers violated a "clearly established" right — meaning he must identify a prior case with substantially similar facts where a court held the same conduct unconstitutional. The requirement is so specific that courts routinely grant qualified immunity even in cases of egregious misconduct, simply because no prior case involved precisely the same factual pattern.*
>
> *Rivera finds no case with precisely matching facts. The officers entered a workplace without a warrant, which violates the Fourth Amendment — but the specific combination of workplace entry, immigration enforcement context, and excessive force has not been adjudicated in the Ninth Circuit. Under existing precedent, she is required to grant qualified immunity.*
>
> *She grants the motion, with visible reluctance. In her opinion, she writes: "The court is aware that the doctrine of qualified immunity has been subject to searching criticism from jurists across the ideological spectrum. The requirement that a right be 'clearly established' in the specific factual context at issue creates an asymptotic trap: rights can never become clearly established if the first plaintiff to assert them is always defeated by qualified immunity. This court lacks the authority to overrule Supreme Court precedent, but it observes that the doctrine, as currently applied, functions as a one-way ratchet against civil rights enforcement."*
>
> *Rivera has described a local minimum in precise terms. The "asymptotic trap" she identifies is the geometric entrapment: the doctrine prevents the creation of the very precedents that would be needed to satisfy the doctrine's own requirements. The system cannot escape because the escape condition (clearly established law) is prevented by the entrapment condition (no liability without clearly established law).*

---

## Gauge Breaking: When the System Is Not Invariant

### The Broken Symmetry

Chapter 8 established that equal protection is gauge invariance: legal outcomes must not depend on protected characteristics. This section examines what happens when the gauge symmetry is broken — when the system's outputs do depend on legally irrelevant features.

**Definition (Gauge Breaking).** *Gauge breaking* in the legal system occurs when the legal evaluation function $J_{\text{law}}$ is not invariant under the equal protection gauge group $G_{\text{EP}}$:

$$\exists \; g \in G_{\text{EP}} : J_{\text{law}}(g \cdot x) \neq J_{\text{law}}(x)$$

The degree of gauge breaking is measured by the Legal Bond Index (LBI) defined in Chapter 5.

Gauge breaking has two forms, as discussed in Chapter 8: explicit (the system consciously uses protected characteristics) and spontaneous (the system is facially neutral but produces asymmetric outcomes due to an asymmetric ground state). This chapter focuses on the *mechanisms* of gauge breaking — the specific ways in which the legal system's geometry is deformed to produce asymmetric outcomes.

### Sentencing Disparities

The most extensively documented form of gauge breaking is sentencing disparities: the systematic difference in sentences imposed on defendants who differ in protected characteristics but are otherwise similarly situated.

The U.S. Sentencing Commission's data provides the empirical foundation:

- **Racial disparity:** Black male defendants receive sentences approximately 19.1% longer than similarly situated white male defendants.
- **Gender disparity:** Male defendants receive sentences approximately 63% longer than similarly situated female defendants.
- **Citizenship disparity:** Non-citizen defendants receive sentences approximately 7% longer than similarly situated citizen defendants.

Each of these disparities is a gauge violation: the sentencing function changes when a protected characteristic is transformed. The gauge violation tensor $V_{ij}$ (developed fully in Chapter 11) quantifies these violations across transformation types and outcome dimensions.

### Framing Effects on Juries

A subtler form of gauge breaking occurs in jury decision-making. The way evidence is presented — the "frame" — affects the jury's evaluation, even when the underlying information is identical. This is a gauge violation: the legal evaluation depends on the representation (the frame) rather than the content (the evidence).

Classic examples:

- A defendant described as "having a 90% chance of rehabilitation" is treated differently from one described as "having a 10% chance of recidivism," even though the statistical content is identical.
- An injury described in vivid, emotional terms produces higher damages awards than the same injury described in clinical, medical terms.
- The order in which witnesses testify affects the jury's assessment of credibility, even when the testimonial content is the same.

Each of these is a due process violation under the quotient-space interpretation of Chapter 8: the evaluation is not well-defined on the quotient space of equivalent descriptions. Two descriptions that are in the same equivalence class (same information content) produce different evaluations.

### The Geometric Mechanism of Gauge Breaking

Why does gauge breaking occur? The geometric framework identifies three mechanisms:

**Weight contamination.** The edge weights in the judicial complex have been contaminated by legally irrelevant features. If the precedent field was built under conditions where race affected legal outcomes, the edge weights encode this racial dependence. A judge who faithfully follows the weighted paths reproduces the racial bias embedded in the weights.

**Heuristic-gauge interaction.** The heuristic functions used by judges and juries interact with gauge-variant features of the case. A judge whose heuristic assigns higher severity to crimes associated with minority defendants (due to availability bias from media coverage of minority crime) produces gauge-variant sentences even if the judge is consciously committed to equal treatment.

**Quotient failure.** The evaluation function fails to factor through the quotient space because the representation affects the evaluation at a pre-conscious level. Framing effects operate below the threshold of conscious reasoning: the judge or jury does not consciously use the frame as an input, but the frame shapes the evaluation nonetheless.

---

> **RUNNING EXAMPLE — ALL FOUR PATHOLOGIES ON RIVERA'S DOCKET**
>
> *Rivera now sees her docket through the lens of geometric pathology. She compiles a summary:*
>
> ***Heuristic corruption:*** *Her drug sentencing heuristic retains deformation from the old crack/powder disparity. Her sentences are measurably affected by media coverage of cases. These are corruptions of her sentencing heuristic — her intuitive "distance to appropriate sentence" estimate is systematically biased by legally irrelevant factors.*
>
> ***Objective hijacking:*** *95.6% of her criminal cases are resolved by guilty pleas. The adversarial system — the constitutionally guaranteed mechanism for testing the government's case — operates in fewer than 5% of cases. The system has been hijacked by the efficiency proxy: case throughput has replaced just adjudication as the operative objective.*
>
> ***Local minima:*** *She is trapped by qualified immunity. She can see that the doctrine produces unjust results — meritorious civil rights claims are dismissed on technicalities — but she cannot escape the local minimum because she lacks the authority to overrule Supreme Court precedent and no alternative path exists.*
>
> ***Gauge breaking:*** *Her own sentencing data shows $\text{LBI}_{\text{sex}} = 0.127$ — she gives substantially shorter sentences to female defendants than to comparable male defendants. Her district's data shows $\text{LBI}_{\text{race}} = 0.191$. The system is not gauge-invariant, and she is part of the system.*
>
> *Rivera is not a bad judge. She is, by most measures, an excellent one — thoughtful, hardworking, committed to equal justice. But the geometric pathologies are not about individual virtue. They are structural features of the system in which she operates. A well-intentioned judge working in a system with corrupted heuristics, hijacked objectives, inescapable local minima, and broken gauge symmetry will produce systematically flawed outputs — not because of personal failing, but because the geometry of the space she navigates has been distorted.*
>
> *The question is not whether Rivera is a good judge. The question is whether the judicial complex in which she operates has the right geometry. The answer, on the evidence, is that it does not — and the four pathologies identified in this chapter are the specific diagnoses.*

---

## Interactions Between Pathologies

### Compounding Effects

The four pathologies are not independent. They interact and compound, creating failure modes that are worse than any single pathology alone.

**Heuristic corruption + gauge breaking.** When the heuristic is corrupted by racial bias *and* the gauge symmetry is broken by sentencing disparities, the two pathologies reinforce each other. The corrupted heuristic guides the search toward gauge-variant paths (paths that lead to racially disparate outcomes), and the gauge violation confirms the heuristic's bias (the precedent field, now containing racially disparate outcomes, further corrupts the heuristic for future cases). This is a feedback loop: bias in the heuristic produces bias in the outcomes, which produces more bias in the heuristic.

**Objective hijacking + local minima.** When the system's objective has been hijacked by efficiency *and* the system is trapped in a local minimum of bad doctrine, the two pathologies conspire to prevent escape. The hijacked objective (case throughput) rewards staying in the local minimum (disposing of cases quickly using the existing doctrine) and penalizes escaping (taking cases to trial, writing lengthy opinions distinguishing or criticizing the doctrine). The efficiency proxy *enforces* the local minimum.

**All four together.** In the worst case, all four pathologies operate simultaneously:

1. The heuristic is corrupted by racial bias (heuristic corruption).
2. The efficiency proxy incentivizes plea bargaining over trials (objective hijacking).
3. Bad doctrine like qualified immunity traps the system in suboptimal outcomes (local minima).
4. The system produces racially disparate sentences (gauge breaking).

The result is a system that looks efficient (high plea rate, cleared dockets, consistent application of doctrine) but is systematically unjust (biased heuristics, sycophantic plea bargaining, inescapable bad doctrine, gauge-variant outcomes). The measurable proxies all look good; the unmeasured objectives are being sacrificed.

### Breaking the Feedback Loop

The geometric framework suggests remediation strategies for each pathology:

**For heuristic corruption:** Re-calibrate the edge weights. This requires identifying the corrupting inputs (media salience, outdated guidelines) and adjusting the heuristic to remove them. Concretely: provide judges with data on their own sentencing patterns, identify the specific variables that predict deviation from the guidelines, and offer training on debiasing.

**For objective hijacking:** Realign the objective function. This requires changing the institutional incentives so that the measurable proxy (case throughput) is replaced by or supplemented with the true objective (just outcomes). Concretely: reduce the trial penalty, increase resources for public defenders, and evaluate prosecutors on accuracy rather than conviction rate.

**For local minima:** Reduce the barrier height. This requires making overruling less costly — either by limiting the reliance interest (sunset clauses on doctrines) or by providing mechanisms for gradual evolution (intermediate precedents that erode the basin walls). Concretely: encourage Supreme Court review of entrenched doctrines, create standing to challenge doctrines that function as asymptotic traps.

**For gauge breaking:** Measure and publish the LBI. Transparency is the first step: when gauge violations are visible, they create pressure for correction. Concretely: compute the LBI for every federal court, publish the results, and establish benchmarks for acceptable levels of gauge violation.

## Worked Example: A System Exhibiting All Four Pathologies

### Scenario

A federal criminal case: Marcus Williams, Black male, age 26, is charged with possession with intent to distribute 50 grams of cocaine base. His case proceeds through the federal system.

### Heuristic Corruption

The presentence report includes a description of Williams's neighborhood as "a high-crime area" — a characterization that correlates with race and socioeconomic status but has no legal relevance to the offense of conviction. The "high-crime area" description corrupts the sentencing heuristic by injecting a salience term: cases from "high-crime areas" trigger a danger heuristic that increases the estimated cost of lenient sentencing.

The corruption is measurable. Compare the sentences of defendants with identical offense characteristics and criminal histories, differing only in whether their neighborhoods are described as "high-crime." The difference is the heuristic corruption term $\epsilon(c)$.

### Objective Hijacking

Williams is offered a plea: plead guilty to simple possession (5 years maximum) rather than possession with intent to distribute (20 years maximum). The plea offer is not based on a careful evaluation of the evidence — it is based on the docket pressure facing the U.S. Attorney's office, which has 200 pending cases and the resources to try only a fraction.

Williams's public defender, who has 150 cases of her own, advises him to take the plea. Not because the evidence of intent to distribute is strong — it consists of the quantity alone, without direct evidence of sales — but because the risk of trial (20 years) dwarfs the cost of the plea (5 years). The adversarial system is short-circuited.

### Local Minimum

Williams considers challenging the traffic stop that led to his arrest. The stop was based on a "tip" from an anonymous source and a claim that Williams's car had a broken taillight — a pretext that Williams believes was racially motivated. But the doctrine of *Whren v. United States* (1996) holds that the subjective intent of the officer is irrelevant as long as there was *any* objective basis for the stop. The broken taillight provides that basis.

*Whren* is a local minimum. The doctrine produces outcomes that are widely recognized as enabling pretextual stops — stops motivated by race but justified by minor traffic violations. But overruling *Whren* would require the Supreme Court to adopt a subjective-intent standard for traffic stops, which would be administratively unworkable. The system is trapped.

### Gauge Breaking

Williams is sentenced to 42 months. A similarly situated white defendant in the same district, with the same offense and criminal history, received 34 months. The 24% difference is the gauge violation — the sentencing function changes when the racial coordinate is transformed.

### Compound Effect

All four pathologies interact in Williams's case. The corrupted heuristic (neighborhood description) increased the judge's estimate of danger. The hijacked objective (docket pressure) forced a plea rather than a trial. The local minimum (*Whren*) prevented a challenge to the pretextual stop. The gauge breaking produced a racially disparate sentence. Each pathology made the others worse, and the final outcome — 42 months for a defendant who might have been acquitted at trial if the stop had been suppressed — is the compound product of all four geometric distortions.

## Chapter Summary

1. Legal failures map onto four geometric pathologies: heuristic corruption, objective hijacking, local minima, and gauge breaking. These are not merely "problems" — they are mathematically characterizable distortions of the judicial complex.

2. Heuristic corruption occurs when the precedent field encodes biases from legally irrelevant sources (media salience, racial history). The corrupted heuristic systematically misestimates costs.

3. Objective hijacking occurs when the system optimizes a measurable proxy (case throughput, conviction rate) rather than the true objective (just adjudication). Plea bargaining is the paradigmatic example.

4. Local minima are bad precedents that courts cannot escape because the overruling cost exceeds the benefit. Qualified immunity and the third-party doctrine are examples.

5. Gauge breaking is the failure of gauge invariance — legal outcomes depend on protected characteristics. Sentencing disparities and framing effects are the primary manifestations.

6. The four pathologies interact and compound. Heuristic corruption reinforces gauge breaking; objective hijacking enforces local minima. In the worst case, all four operate simultaneously.

7. The geometric framework suggests specific remediation strategies for each pathology: re-calibration for heuristic corruption, objective realignment for hijacking, barrier reduction for local minima, and transparency (LBI publication) for gauge breaking.

---

## Technical Appendix

**Definition (Corrupted Heuristic — Formal).** A doctrinal heuristic $h_D: V(\mathcal{K}) \to \mathbb{R}_{\geq 0}$ is $\epsilon$-corrupted with respect to a set of irrelevant features $\mathcal{I}$ if:

$$\exists \; f: \mathcal{I} \to \mathbb{R} \text{ such that } h_D(c) = h_D^{\text{true}}(c) + f(\mathcal{I}(c))$$

where $\mathcal{I}(c)$ extracts the irrelevant features of case $c$ and $f$ is a non-zero function. The corruption magnitude is $\|\epsilon\| = \mathbb{E}_c[|f(\mathcal{I}(c))|]$.

**Definition (Objective Hijacking — Formal).** Let $f_{\text{true}}: \mathcal{O} \to \mathbb{R}$ be the true legal objective (quality of outcome) and $f_{\text{proxy}}: \mathcal{O} \to \mathbb{R}$ be a measurable proxy (efficiency, conviction rate). The system is objective-hijacked if the actual optimization solves:

$$\max_{\gamma} f_{\text{proxy}}(J_{\text{law}}(\gamma))$$

rather than:

$$\max_{\gamma} f_{\text{true}}(J_{\text{law}}(\gamma))$$

The hijacking gap is:

$$\Delta_{\text{hijack}} = f_{\text{true}}(\gamma^*_{\text{true}}) - f_{\text{true}}(\gamma^*_{\text{proxy}})$$

where $\gamma^*_{\text{true}}$ and $\gamma^*_{\text{proxy}}$ are the optimal paths under the true and proxy objectives, respectively.

**Definition (Legal Local Minimum — Formal).** A vertex $c_{\text{min}} \in \mathcal{K}$ is a legal local minimum of depth $\delta$ if:

$$f_{\text{true}}(c_{\text{min}}) - f_{\text{true}}(c_{\text{global}}) = \delta > 0$$

and for all paths $\gamma$ from $c_{\text{min}}$ of length $\leq L$:

$$\max_{c \in \gamma} \text{Cost}(c) - \text{Cost}(c_{\text{min}}) > B$$

where $B$ is the barrier height and $L$ is the maximum path length considered. The minimum is inescapable when $B > \delta$ — the cost of climbing out exceeds the benefit of reaching the global optimum.

**Proposition (Feedback Amplification).** Let $h_t$ denote the heuristic at time $t$ and $V_t$ denote the gauge violation at time $t$. If heuristic corruption and gauge breaking interact via the feedback loop:

$$h_{t+1}(c) = h_t(c) + \alpha \cdot V_t(c)$$
$$V_{t+1}(c) = V_t(c) + \beta \cdot \epsilon_t(c)$$

where $\epsilon_t = h_t - h^{\text{true}}$ is the heuristic corruption, then the combined pathology grows exponentially:

$$\|\epsilon_t\| \sim e^{\sqrt{\alpha \beta} \cdot t}$$

when $\alpha \beta > 0$. *Proof.* The coupled system $\epsilon_{t+1} = \epsilon_t + \alpha \beta \epsilon_{t-1}$ has eigenvalues $\lambda_\pm = \frac{1 \pm \sqrt{1 + 4\alpha\beta}}{2}$, and $|\lambda_+| > 1$ when $\alpha\beta > 0$, giving exponential growth. $\square$

---

## Notes on Sources

The four geometric pathologies (heuristic corruption, objective hijacking, local minima, gauge breaking) are mapped from the AI alignment failure modes identified in the Geometric Ethics framework (Bond, 2026). Plea bargaining statistics are from the Bureau of Justice Statistics (2022). The sentencing disparity data is from the U.S. Sentencing Commission's *Demographic Differences in Sentencing* reports (2012, 2017). Qualified immunity was established in *Harlow v. Fitzgerald*, 457 U.S. 800 (1982), and has been criticized by, among others, Judge Don Willett (concurrence in *Zadeh v. Robinson*, 5th Cir. 2019) and Justice Clarence Thomas (dissent from certiorari in *Baxter v. Bracey*, 2020). The third-party doctrine was established in *Smith v. Maryland*, 442 U.S. 735 (1979), and limited in *Carpenter v. United States*, 585 U.S. 296 (2018). *Whren v. United States*, 517 U.S. 806 (1996), held that the subjective intent behind a traffic stop is irrelevant if there is any objective basis. The crack/powder cocaine sentencing disparity was established by the Anti-Drug Abuse Act of 1986 and partially addressed by the Fair Sentencing Act of 2010. Media influence on sentencing is documented in Lim, Snyder, and Strömberg (2015). The feedback amplification model is original to this chapter.

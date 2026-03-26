# Chapter 6: Precedent as Heuristic Field

> *"An algorithm must be seen to be believed."*
> — Donald Knuth, *The Art of Computer Programming* (1968)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera has a new case: Maria Santos, a Latina project manager at a tech company, claims she was denied a promotion in favor of a less-qualified white male colleague. Santos alleges race and sex discrimination under Title VII of the Civil Rights Act of 1964.*
>
> *Rivera knows the framework for analyzing this case before she reads a single brief. It is called **McDonnell Douglas burden-shifting**, after the 1973 Supreme Court case that established it. The framework provides a three-step procedure: (1) the plaintiff establishes a prima facie case of discrimination, (2) the employer articulates a legitimate non-discriminatory reason for the adverse action, (3) the plaintiff shows the stated reason is pretextual.*
>
> *Rivera does not need to search the entire space of legal arguments to find the right analysis. McDonnell Douglas tells her exactly where to look. It narrows the search from the entire judicial complex to a three-step corridor, each step with well-defined elements. Without McDonnell Douglas, Rivera would face an intractable pathfinding problem — thousands of potential arguments, each requiring evaluation. With it, the problem is manageable.*
>
> *In the language of computer science, McDonnell Douglas is a **heuristic** — a function that estimates the remaining cost of reaching a goal, guiding search toward promising regions and away from dead ends. This chapter develops the formal correspondence between legal doctrines and heuristic functions, showing that precedent is not merely a constraint on judicial reasoning but a computational resource that makes legal reasoning tractable.*

---

## The Computational Problem of Legal Reasoning

### Litigation as Pathfinding

Chapter 3 constructed the judicial complex $\mathcal{K}$ and Chapter 4 defined the legal metric — the cost of traversing edges in $\mathcal{K}$. Legal reasoning is the problem of finding paths through this complex.

**Definition (Litigation as Pathfinding).** A *legal dispute* is a pathfinding problem on $\mathcal{K}$:

- **Start node $c_0$:** The vertex corresponding to the plaintiff's current legal position — the alleged wrong, or the most factually similar decided case.
- **Goal region $G$:** A set of vertices corresponding to the desired remedy — cases where similarly situated plaintiffs prevailed.
- **Path $\gamma$:** A sequence of directed edges in $\mathcal{K}$ — a chain of legal arguments, each corresponding to a doctrinal step from one case to the next.
- **Cost function:** The legal friction $\text{BF}_{\text{law}}(\gamma)$ from Chapter 4 — the total edge weight along the path.
- **Constraints:** Regime boundaries, constitutional constraints, statutory requirements that impose edge penalties or block paths entirely.

The optimal legal argument is the minimum-cost path from $c_0$ to $G$:

$$\gamma^* = \arg\min_\gamma \text{BF}_{\text{law}}(\gamma) \quad \text{subject to } \gamma(0) = c_0, \; \gamma(\text{end}) \in G, \; \gamma \text{ respects all constraints}$$

### Why the Problem Is Hard

In a judicial complex of realistic size — millions of decided cases, tens of millions of citation edges — finding the optimal path by exhaustive search is computationally intractable. The number of possible paths grows exponentially with the number of edges. Even in a small complex (a few thousand cases in a single area of law), brute-force search is impractical.

This is not merely a computational observation. It is a *practical* reality of legal reasoning. A lawyer preparing a brief cannot read every case ever decided on the relevant topic. A judge cannot consider every possible doctrinal path from the facts to the remedy. The space is too large.

Legal practice solves this problem the same way computer science solves it: with *heuristics* — functions that estimate the remaining cost of reaching a goal, guiding the search toward promising regions of the complex and away from dead ends.

## $A^*$ Search on the Judicial Complex

### The $A^*$ Algorithm

**Theorem (Optimal Legal Argument as $A^*$).** The optimal legal argument is an instance of $A^*$ search on a weighted graph, with evaluation function $f(n) = g(n) + h(n)$, where:

- $g(n)$ is the accumulated legal friction from $c_0$ to the current node $n$ — the cost of the argument built so far.
- $h(n)$ is the heuristic estimate of remaining friction from $n$ to $G$ — the estimated cost of completing the argument.

At each step, $A^*$ expands the node with the smallest $f(n)$ — the node where the sum of actual cost so far and estimated remaining cost is minimized. This is the legal analogue of working on the most promising argument: the one where the work already done, plus the estimated remaining work, is smallest.

The mapping between $A^*$ and legal reasoning is exact:

| $A^*$ Component | Legal Counterpart |
|-----------------|-------------------|
| Start node $c_0$ | Plaintiff's legal position (complaint) |
| Goal region $G$ | Desired remedy (prayer for relief) |
| Successor function | Legal arguments available at each step |
| Edge cost $c(n, n')$ | Difficulty of establishing the legal move |
| Accumulated cost $g(n)$ | Argument built so far (partial brief) |
| Heuristic $h(n)$ | Legal doctrine estimating remaining burden |
| Open list | Arguments under consideration |
| Closed list | Arguments already evaluated |
| Optimal path $\gamma^*$ | Winning legal argument |
| Path not found | Claim fails (no viable legal theory) |

### Why $A^*$ and Not Dijkstra

Dijkstra's algorithm finds shortest paths without a heuristic — it explores nodes in order of accumulated cost $g(n)$, expanding outward uniformly from the start node. This corresponds to a legal analysis that considers all possible arguments equally, without any doctrinal guidance about which arguments are more promising.

$A^*$ improves on Dijkstra by using the heuristic $h(n)$ to guide the search toward the goal. Instead of expanding uniformly, it expands preferentially toward regions where the estimated remaining cost is low. This corresponds to a legal analysis that uses doctrinal knowledge to focus on the most promising arguments.

The practical difference is enormous. Dijkstra might explore thousands of irrelevant cases before finding the shortest path. $A^*$ with a good heuristic goes almost directly to the answer, expanding only the cases along the most promising paths. This is exactly what experienced lawyers do: they use their knowledge of legal doctrine to skip the irrelevant cases and focus on the ones that matter.

## Legal Doctrines as Heuristic Functions

### The Key Insight

The central claim of this chapter is that *legal doctrines are heuristic functions* — functions that estimate the remaining cost of reaching a legal goal, computed from an established body of legal knowledge.

**Definition (Doctrinal Heuristic).** A *doctrinal heuristic* $h_D$ is a function $h_D: V(\mathcal{K}) \to \mathbb{R}_{\geq 0}$ defined on the vertices of $\mathcal{K}$, derived from an established legal doctrine $D$, that estimates the remaining legal friction to reach a goal region:

$$h_D(c) = \text{estimated remaining burden from } c \text{ to } G \text{ under doctrine } D$$

A doctrinal heuristic takes a legal position and returns a number: the estimated cost of getting from that position to the desired legal outcome. A low value means the position is close to the goal — the remaining legal work is small. A high value means the position is far from the goal — substantial legal work remains.

### Common Doctrinal Heuristics

**Prima facie case doctrine.** For a tort claim, the heuristic $h_{\text{tort}}(p)$ estimates the distance to establishing duty, breach, causation, and damages. At any node $p$, it returns the estimated cost of the remaining unestablished elements. If duty and breach are already established, the heuristic returns only the estimated cost of proving causation and damages. If nothing is established, it returns the sum of all four elements' estimated costs.

**Burden-shifting frameworks.** The McDonnell Douglas framework defines a three-step heuristic:
1. Estimate the cost of establishing a prima facie case of discrimination.
2. If the prima facie case is established, estimate the cost to the defendant of articulating a legitimate non-discriminatory reason.
3. Estimate the cost of proving that the stated reason is pretextual.

The heuristic at each stage approximates the remaining path length. A plaintiff who has already established the prima facie case and shown that the employer's reason is weak has a low heuristic value — she is close to the goal. A plaintiff who has not yet established the prima facie case has a high heuristic value.

**Strict scrutiny.** For constitutional challenges, $h_{\text{strict}}(p)$ estimates the distance to showing that a law is not narrowly tailored to a compelling government interest. This heuristic assigns *high* estimated cost to the government's defense path (the government must overcome the presumption of unconstitutionality) and *low* estimated cost to the challenger's path (the challenger need only show that less restrictive alternatives exist).

**Stare decisis.** Precedent provides a *pattern database* — pre-computed optimal paths from previously solved positions. When the current case is factually close to a precedent ($d(p, p_P) < \epsilon$), the precedent's path provides a near-optimal heuristic. This is why lawyers cite cases: they are importing pre-computed heuristics into the current search.

---

> **RUNNING EXAMPLE — McDONNELL DOUGLAS AS A HEURISTIC IN SANTOS v. TECH COMPANY**
>
> *Judge Rivera applies the McDonnell Douglas heuristic to Santos's case. The three-step procedure structures her analysis:*
>
> ***Step 1: Prima facie case.** Santos must show: (a) she is a member of a protected class (Latina, female — established), (b) she was qualified for the promotion (positive performance reviews — established), (c) she suffered an adverse employment action (denied promotion — established), (d) the promotion was given to someone outside her protected class or the position remained open (given to a white male — established). **Heuristic value at Step 1: low.** Santos has satisfied all elements. The estimated remaining cost is the cost of Steps 2 and 3.*
>
> ***Step 2: Employer's rebuttal.** The company must articulate a legitimate non-discriminatory reason. The company states that the promoted employee had more experience managing cross-functional teams. **Heuristic value at Step 2: moderate.** The employer has articulated a reason, so the burden shifts back to Santos. The estimated remaining cost is the cost of Step 3 — proving pretext.*
>
> ***Step 3: Pretext.** Santos must show that the stated reason is pretextual — that it is not the real reason, or that it is insufficient to explain the decision. Santos presents evidence: her own experience managing cross-functional teams was comparable, the promoted employee had fewer years of total experience, and two other Latina employees were passed over for promotions in the same quarter. **Heuristic value at Step 3: low to moderate.** The evidence of pretext is suggestive but not overwhelming.*
>
> *The McDonnell Douglas heuristic has guided Rivera's analysis from start to finish. Without it, she would have faced the entire space of Title VII doctrine — direct evidence, mixed-motive analysis, pattern-or-practice theories, hostile work environment, retaliation — and would have had to evaluate each path independently. With it, the search is focused on a three-step corridor with well-defined elements at each step.*
>
> *The total legal friction along the McDonnell Douglas path: sum of the three steps' costs. Rivera can compare this to the friction along alternative paths (direct evidence, if available; mixed-motive, if applicable) and select the path with the lowest total friction.*

---

## Admissibility of Doctrinal Heuristics

### The Admissibility Condition

In $A^*$, a heuristic $h$ is *admissible* if it never overestimates the true cost of reaching the goal:

$$h(n) \leq h^*(n) \quad \forall n$$

where $h^*(n)$ is the actual minimum cost from $n$ to $G$. If $h$ is admissible, $A^*$ is guaranteed to find the optimal path — the proof is a standard result in artificial intelligence.

**Theorem (Admissibility of Doctrinal Heuristics).** A doctrinal heuristic $h_D$ is admissible if the doctrine $D$ correctly identifies the elements of a legal claim and assigns non-negative estimated costs that do not exceed actual proving costs. If $h_D$ is admissible, $A^*$ search using $h_D$ is guaranteed to find the optimal legal argument.

**Proof sketch.** Legal doctrines that decompose claims into elements (duty + breach + causation + damages, for example) produce heuristics that sum estimated costs of remaining elements. Each element's estimated cost is a lower bound on the actual proving cost (the element might be easier to prove than estimated, due to shortcuts like res ipsa loquitur or stipulations). Therefore the sum of estimated costs is a lower bound on the total remaining cost, which is the definition of admissibility. By the admissibility theorem for $A^*$, the search is guaranteed to find the optimal path. $\square$

### Inadmissible Heuristics in Legal Practice

Not all legal strategies correspond to admissible heuristics. An *overaggressive* legal theory underestimates cost — it assumes elements will be easier to establish than they actually are, leading the search toward arguments that fail at trial. This is inadmissibility through underestimation: $h(n) > h^*(n)$ because the heuristic is too optimistic about the remaining cost.

Wait — this is backwards. An inadmissible heuristic *overestimates* the true cost, causing $A^*$ to miss optimal paths by avoiding regions that appear (but are not actually) costly. Let us be precise.

An *overconservative* strategy overestimates the remaining cost. It says "this argument will be very expensive to complete," when in fact the argument could be completed cheaply. This causes the search to avoid the argument in favor of apparently cheaper alternatives, potentially missing the optimal path. The result: settlement when litigation would have succeeded, or failure to pursue a winning theory because it "looked" too hard.

An *overaggressive* strategy underestimates the remaining cost. Strictly speaking, this preserves admissibility (underestimation is exactly what admissibility requires). But it degrades the heuristic's *efficiency*: a heuristic that estimates zero remaining cost for every node is admissible but useless — it provides no guidance, and $A^*$ degenerates to Dijkstra. An overaggressive heuristic that estimates very low costs everywhere will explore many irrelevant paths before finding the optimal one.

The sweet spot — the ideal doctrinal heuristic — is both admissible (never overestimates) and *tight* (closely approximates the true remaining cost). Tight heuristics guide the search efficiently to the optimal path with minimal wasted exploration.

### Which Doctrines Are Admissible?

**Admissible doctrines** decompose claims into clearly defined elements whose individual proving costs are well-understood:

- **Negligence:** Duty + Breach + Causation + Damages. Each element has extensive case law establishing the typical proving cost. The heuristic sums the remaining elements' estimated costs. Admissible, because the sum of individual element costs never exceeds the total cost of proving all elements (there are no negative interactions — proving one element does not make another *harder*).

- **McDonnell Douglas:** Prima facie case + Employer's rebuttal + Pretext. Admissible for the same reason: each step's cost is well-characterized, and the costs are additive.

- **Strict scrutiny:** Compelling interest + Narrow tailoring. Admissible from the challenger's perspective: the heuristic estimates the *government's* remaining cost, and the challenger wins by showing the government cannot meet this cost.

**Potentially inadmissible doctrines** involve elements whose costs are poorly characterized or context-dependent:

- **Totality of the circumstances:** This is a *zero heuristic* — it provides no structure for estimating remaining costs. Every case requires de novo evaluation of "all relevant factors," with no decomposition into elements. The heuristic is technically admissible (zero never overestimates) but maximally uninformative.

- **Balancing tests:** When a doctrine requires "balancing" competing interests without specifying the weights, the heuristic is poorly calibrated. The estimated cost of the remaining "balance" depends on how the judge weighs the factors, which is precisely what the search is trying to determine. This is a circular heuristic — it uses the answer to estimate the cost of finding the answer.

- **Novel theories:** When no established doctrine covers the legal question, there is no pre-computed heuristic. The lawyer must search without guidance — the analogue of Dijkstra without a heuristic. Novel legal questions are computationally expensive precisely because they lack doctrinal heuristics.

## The Adversarial Structure

### Two-Player Search

Litigation is not single-agent pathfinding — it is *adversarial*. The plaintiff seeks a path from $c_0$ to $G_\pi$ (the desired remedy); the defendant seeks to block that path or establish a shorter path to $G_\delta$ (judgment for defendant).

**Definition (Adversarial Legal Search).** An *adversarial legal search* is a two-player game on $\mathcal{K}$:

- **Plaintiff (maximizer):** Seeks to minimize $\text{BF}_{\text{law}}(\gamma_\pi)$ to $G_\pi$.
- **Defendant (minimizer):** Seeks to either (a) show no path to $G_\pi$ exists (motion to dismiss), (b) increase $\text{BF}_{\text{law}}(\gamma_\pi)$ above the burden-of-proof threshold, or (c) establish a shorter path to $G_\delta$ (affirmative defense, counterclaim).

The *minimax value* of the dispute is:

$$V(c_0) = \min_{\gamma_\delta} \max_{\gamma_\pi} \left[ \text{BF}_{\text{law}}(\gamma_\delta) - \text{BF}_{\text{law}}(\gamma_\pi) \right]$$

If $V(c_0) > 0$, the plaintiff prevails; if $V(c_0) \leq 0$, the defendant prevails.

### Motions as Search Pruning

Procedural motions correspond to search-pruning operations — moves that eliminate entire branches of the search tree:

**Motion to dismiss (Rule 12(b)(6)).** The defendant claims that even taking all facts as true, no path from $c_0$ to $G_\pi$ exists within the legal constraints. This is a graph-connectivity assertion: the goal region $G_\pi$ is *unreachable* from $c_0$ in $\mathcal{K}$. If the motion is granted, the entire search tree rooted at $c_0$ is pruned.

**Summary judgment.** The defendant claims that on the undisputed facts, the shortest path from $c_0$ leads to $G_\delta$, not $G_\pi$. No adversarial search is needed because the edge weights are determined by stipulated facts. Summary judgment eliminates the need for trial — it computes the optimal path directly from the undisputed graph.

**Motion in limine.** Exclusion of evidence corresponds to removing edges from the judicial complex — eliminating argument paths that rely on the excluded evidence. If a key piece of evidence is excluded, the paths that require it become impassable, potentially transforming a short path to $G_\pi$ into a long path or no path at all.

### Settlement as Shortcut

**Definition (Settlement Region).** A *settlement* is a vertex $c_s \in \mathcal{K}$ that both parties prefer to the expected outcome of continued litigation:

$$c_s \in \{ c \in \mathcal{K} \mid U_\pi(c) > \mathbb{E}[U_\pi(\gamma^*_\pi)] \text{ and } U_\delta(c) > \mathbb{E}[U_\delta(\gamma^*_\delta)] \}$$

where $U_\pi, U_\delta$ are the utility functions of plaintiff and defendant.

**Proposition (Settlement Existence).** A non-empty settlement region exists whenever the sum of both parties' expected litigation costs exceeds the graph distance between their goal regions:

$$\mathbb{E}[\text{BF}_{\text{law}}(\gamma^*_\pi)] + \mathbb{E}[\text{BF}_{\text{law}}(\gamma^*_\delta)] > d_{\mathcal{K}}(G_\pi, G_\delta)$$

This explains the empirical observation that the vast majority of legal disputes settle: litigation costs (path lengths) almost always exceed the distance between the parties' positions. Settlement is a shortcut — a direct edge from the current position to a mutually acceptable vertex, bypassing the long and expensive litigation path.

---

> **RUNNING EXAMPLE — ADVERSARIAL SEARCH IN SANTOS v. TECH COMPANY**
>
> *The tech company responds to Santos's complaint with a two-pronged strategy:*
>
> ***Pruning move (Motion to Dismiss the Sex Discrimination Claim).** The company argues that Santos cannot establish a prima facie case of sex discrimination because several women were promoted in the same quarter. This is a search-pruning move: if granted, it eliminates the sex discrimination path from Santos's search tree, leaving only the race discrimination path.*
>
> *Rivera denies the motion: the fact that some women were promoted does not preclude discrimination against this particular woman. The sex discrimination path remains open.*
>
> ***Adversarial heuristic (Legitimate Non-Discriminatory Reason).** The company articulates its legitimate reason: the promoted employee's cross-functional management experience. This is the adversarial counterpart to Santos's McDonnell Douglas heuristic. The company's heuristic estimates the remaining cost for Santos to reach the goal: "she must now prove pretext, which is expensive."*
>
> *The adversarial structure creates a two-player game. Santos's heuristic says: "the remaining cost is moderate — I have evidence of pretext." The company's counter-heuristic says: "the remaining cost is high — pretext is hard to prove, and our stated reason is facially legitimate."*
>
> *The minimax value of the dispute depends on which heuristic is more accurate — which more closely estimates the actual remaining cost of completing the path. Rivera's role is to evaluate the path, not the heuristics: she assesses whether Santos has actually traversed the McDonnell Douglas steps, not whether the parties' cost estimates are correct.*
>
> ***Settlement analysis.** Both sides compute their expected litigation costs. Santos's expected path cost: moderate (the McDonnell Douglas path is well-defined, but pretext is uncertain). The company's expected path cost: moderate (defending requires producing the promoted employee's records and justifying the decision). The distance between their goal regions: small (the dispute is about one promotion, with damages in the range of lost compensation). Since the combined litigation costs likely exceed the damages gap, a settlement region exists. Both sides have incentive to settle — and in practice, most Title VII cases do settle.*

---

## Precedent as Pattern Database

### Pre-Computed Heuristics

In AI pathfinding, a *pattern database* is a collection of pre-computed optimal solutions to subproblems. When the current problem contains a subproblem that matches a pattern in the database, the pre-computed solution provides an immediate heuristic estimate.

Legal precedent functions as a pattern database. Each decided case is a pre-computed solution to a legal subproblem: the court has already found the optimal path (or at least a path) from a particular starting position to a particular outcome. When a new case is factually similar to a precedent, the precedent's path provides a heuristic for the new case.

This is why lawyers cite cases. They are not merely decorating their arguments with authority. They are importing pre-computed heuristics into the current search. A citation to *McDonnell Douglas* says: "the optimal path from this type of starting position has already been computed. It goes through these three steps. Use this pre-computed path as your heuristic for the current case."

### Binding vs. Persuasive Precedent

The distinction between binding and persuasive precedent maps onto the strength of the heuristic:

**Binding precedent** is a *mandated* heuristic. The court must use it. A district court must apply the Supreme Court's version of the McDonnell Douglas test, even if the district court believes a different test would be better. This is like an $A^*$ implementation where the heuristic function is fixed and cannot be overridden.

**Persuasive precedent** is a *suggested* heuristic. The court may use it or ignore it. A circuit court may consider a sister circuit's interpretation of a statute but is not bound by it. This is like an $A^*$ implementation where multiple heuristics are available and the algorithm selects the most informative one.

**Overruled precedent** is a *deprecated* heuristic. It was once mandated but has been replaced by a better one. Using overruled precedent is like using an outdated pattern database — the pre-computed solutions are no longer valid because the underlying graph has changed (new edges have been added, old weights have been modified).

### The Quality of the Heuristic Field

The *heuristic field* at a given point in the judicial complex is the collection of doctrinal heuristics available at that point. In well-developed areas of law, the heuristic field is strong — there are many precedents providing detailed cost estimates, and the doctrinal tests are well-calibrated. In novel areas, the heuristic field is weak — there are few precedents and no established tests.

**Well-developed law** (strong heuristic field):
- Employment discrimination (McDonnell Douglas provides tight heuristic guidance)
- Negligence (elements test provides clear decomposition)
- Contract formation (offer + acceptance + consideration provides admissible heuristic)

**Novel legal questions** (weak heuristic field):
- AI liability (no established doctrinal test; courts must search without guidance)
- Cryptocurrency regulation (existing securities law heuristics may or may not apply)
- Space law (minimal precedent; the heuristic field is nearly flat)

**Contradictory law** (corrupted heuristic field):
- Circuit splits produce conflicting heuristics at the same point — the guidance "points in different directions," analogous to a heuristic function that returns different values depending on which path you took to reach the current node. A corrupted heuristic field is worse than a flat one: it actively misleads the search.

## Heuristic Corruption and Legal Failure

### When Heuristics Go Wrong

A doctrinal heuristic can be *corrupted* — it provides guidance that systematically leads the search away from the optimal path. Corrupted heuristics are a significant source of legal failure.

**Media-influenced heuristics.** High-profile crimes receive disproportionate media attention, creating a distorted heuristic: the estimated cost of the "acquittal" path is inflated (the public expects conviction), while the estimated cost of the "conviction" path is deflated (the evidence seems overwhelming because the media has pre-judged the case). This is an inadmissible heuristic — it overestimates the cost of certain paths — and it can cause $A^*$ to miss the optimal path (acquittal on the merits).

The formal mechanism: media coverage modifies the edge weights in dimension $d_8$ (public interest), inflating the cost of paths that lead to publicly unpopular outcomes. The heuristic inherits these inflated costs, making "popular" outcomes appear cheaper than they actually are. The corrupted heuristic guides the search toward conviction even when the legal friction along the acquittal path is lower.

**Racial bias in precedential heuristics.** If the body of precedent was developed in a context of racial bias — if cases involving minority defendants consistently received harsher outcomes — then the pattern database (the collection of pre-computed heuristics) encodes the bias. When a new case involving a minority defendant arises, the pattern database returns heuristic estimates calibrated to the biased precedents, systematically underestimating the cost of paths to conviction and overestimating the cost of paths to acquittal.

This is gauge corruption: the heuristic field is not gauge-invariant under the equal-protection transformation (changing the defendant's race should not change the heuristic estimate). The Legal Bond Index (Chapter 5) measures this corruption: a high LBI in the heuristic field means the pre-computed paths depend on legally irrelevant features of the cases.

**Precedent as local minimum.** A body of precedent can create a *local minimum* in the heuristic field — a point where the heuristic says "you are at the goal" when in fact the global minimum is elsewhere. Bad precedent that has been followed for decades creates a deep local minimum: the pre-computed paths all converge on the same (incorrect) outcome, and the heuristic consistently estimates zero remaining cost for paths to that outcome.

Escaping a local minimum requires overruling the precedent — a costly operation that Chapter 9 will model as a discontinuous phase transition in the edge weights. The depth of the local minimum (the number of cases relying on the bad precedent) determines the cost of escape.

### The Heuristic Quality Gradient

Across the judicial complex, the quality of available heuristics varies systematically:

- **High-quality heuristic regions:** Areas of law with extensive case law, clear doctrinal tests, and stable precedent. Employment discrimination (McDonnell Douglas), negligence (elements test), contract formation (offer-acceptance-consideration). In these regions, the heuristic field is strong, the search is efficient, and outcomes are relatively predictable.

- **Low-quality heuristic regions:** Areas of law with sparse precedent, unclear tests, or rapidly evolving doctrine. AI liability, cryptocurrency regulation, genetic privacy. In these regions, the heuristic field is weak or flat, the search is inefficient, and outcomes are unpredictable.

- **Corrupted heuristic regions:** Areas of law where the precedent encodes systematic bias, where media influence distorts the cost estimates, or where outdated doctrine creates false local minima. Sentencing in drug cases, immigration law, qualified immunity. In these regions, the heuristic field actively misleads the search, and the framework identifies the corruption as a gauge violation.

The heuristic quality gradient is itself a measurable property of the judicial complex. It can be estimated by comparing the heuristic estimates $h_D(c)$ to the actual costs $h^*(c)$ in decided cases, computing the average error, and mapping this error across the complex. Regions of high average error have poor heuristics; regions of low average error have good heuristics.

## Appeals as Path Re-Evaluation

An appeal is not a new search — it is a *re-evaluation* of the trial court's path under modified edge weights or modified heuristics:

**De novo review.** The appellate court re-runs $A^*$ from scratch with the same start and goal but potentially different heuristics. The appellate court may use a different doctrinal test, weight the dimensions differently, or interpret the precedent differently. De novo review says: "we disagree about the heuristic."

**Abuse of discretion.** The appellate court checks only whether the trial court's path is *within a neighborhood* of the optimal path — whether the chosen path's cost is within a tolerance $\epsilon$ of the shortest path. Abuse-of-discretion review says: "the trial court's path need not be optimal, only reasonable."

**Clearly erroneous.** The appellate court checks whether the trial court's path crosses a regime boundary that it should not have crossed (factual error) or fails to cross one that it should have (missed element of the claim). Clearly-erroneous review says: "the trial court's path must stay on the right side of the regime boundaries."

Each standard of review corresponds to a different tolerance for sub-optimal paths. De novo review has zero tolerance (the path must be optimal under the appellate court's heuristic). Abuse-of-discretion has moderate tolerance (the path must be within $\epsilon$ of optimal). Clearly-erroneous has high tolerance for path choice but zero tolerance for boundary crossings.

---

## Worked Example: Comparing Doctrinal Heuristics

**Scenario.** A plaintiff alleges employment discrimination. Two doctrinal heuristics are available:

**Heuristic 1: McDonnell Douglas (indirect evidence).** Three steps:
- Step 1 (prima facie case): estimated cost 2.0 friction units
- Step 2 (employer's rebuttal): estimated cost 0.5 (borne by defendant)
- Step 3 (pretext): estimated cost 4.0 friction units
- Total estimated remaining cost from start: $h_{\text{MD}}(c_0) = 2.0 + 0.5 + 4.0 = 6.5$

**Heuristic 2: Direct evidence.** One step:
- Step 1 (produce direct evidence of discriminatory intent): estimated cost 8.0 friction units
- Total estimated remaining cost from start: $h_{\text{direct}}(c_0) = 8.0$

**Analysis.** The McDonnell Douglas heuristic estimates a lower total cost ($6.5 < 8.0$), so $A^*$ will explore the McDonnell Douglas path first. If the plaintiff indeed lacks direct evidence, the McDonnell Douglas path is genuinely cheaper — the heuristic's guidance is correct.

But suppose the plaintiff *does* have a smoking-gun email. Then the actual cost of the direct evidence path is much lower than 8.0 — perhaps 1.0 (produce the email, authenticate it, done). The direct evidence heuristic overestimated the cost, making it inadmissible at this particular node. A better heuristic would condition on whether direct evidence exists: if yes, $h_{\text{direct}} = 1.0$; if no, $h_{\text{direct}} = \infty$ (the path is impassable).

This illustrates a general principle: **good doctrinal heuristics are context-sensitive**. The best heuristic is not a fixed function but a function that conditions on the available evidence. McDonnell Douglas is a good heuristic precisely because it adapts to the evidence: if the plaintiff has direct evidence, she can bypass the burden-shifting framework entirely. The doctrine accommodates both paths, functioning as a *portfolio of heuristics* rather than a single fixed estimate.

## Chapter Summary

1. Legal disputes are pathfinding problems on the judicial complex $\mathcal{K}$. The optimal legal argument is the minimum-cost path from the plaintiff's position to the desired remedy.

2. This pathfinding problem is an instance of $A^*$ search, with legal doctrines serving as the heuristic function $h(n)$ that estimates remaining cost.

3. Admissible doctrinal heuristics — those that never overestimate the true cost — guarantee that $A^*$ finds the optimal legal argument.

4. Specific legal doctrines (McDonnell Douglas, prima facie case, strict scrutiny) are admissible heuristics that decompose claims into elements whose costs can be estimated independently.

5. Litigation is adversarial: the plaintiff seeks the shortest path to the goal, while the defendant seeks to block, lengthen, or redirect the path. Procedural motions are search-pruning operations.

6. Precedent functions as a pattern database — a collection of pre-computed heuristics from previously decided cases. Binding precedent is a mandated heuristic; persuasive precedent is an optional heuristic; overruled precedent is a deprecated heuristic.

7. Settlement exists whenever the combined litigation costs exceed the distance between the parties' goal regions — which is almost always.

---

## Technical Appendix

**Definition (Doctrinal Heuristic).** A *doctrinal heuristic* $h_D: V(\mathcal{K}) \to \mathbb{R}_{\geq 0}$ is a function from vertices of the judicial complex to non-negative reals, derived from a legal doctrine $D$, satisfying:

$$h_D(c) = \sum_{k \in \text{remaining elements}} \hat{w}_k$$

where $\hat{w}_k$ is the estimated cost of establishing element $k$ of the legal claim under doctrine $D$.

**Theorem (Admissibility).** If $\hat{w}_k \leq w_k^*$ for each element $k$ (estimated cost does not exceed actual cost), then $h_D$ is admissible:

$$h_D(c) = \sum_k \hat{w}_k \leq \sum_k w_k^* = h^*(c)$$

and $A^*$ using $h_D$ finds the optimal path. *Proof.* Follows from the additivity of element costs and the standard admissibility theorem for $A^*$. $\square$

**Definition (Adversarial Legal Search).** A two-player search game $(c_0, G_\pi, G_\delta, \text{BF}_{\text{law}})$ where the plaintiff seeks $\min_{\gamma_\pi} \text{BF}_{\text{law}}(\gamma_\pi)$ to $G_\pi$ and the defendant seeks $\min_{\gamma_\delta} \text{BF}_{\text{law}}(\gamma_\delta)$ to $G_\delta$. The minimax value is:

$$V(c_0) = \min_{\gamma_\delta} \max_{\gamma_\pi} [\text{BF}_{\text{law}}(\gamma_\delta) - \text{BF}_{\text{law}}(\gamma_\pi)]$$

**Proposition (Settlement Existence).** A non-empty settlement region exists when:

$$\mathbb{E}[\text{BF}_{\text{law}}(\gamma^*_\pi)] + \mathbb{E}[\text{BF}_{\text{law}}(\gamma^*_\delta)] > d_{\mathcal{K}}(G_\pi, G_\delta)$$

*Proof.* If the combined litigation costs exceed the distance between goal regions, there exist vertices between $G_\pi$ and $G_\delta$ that are cheaper for both parties to reach than their respective litigation endpoints. Any such vertex is a settlement point. $\square$

**Definition (Heuristic Field Strength).** The *heuristic field strength* at a vertex $c \in \mathcal{K}$ is:

$$\mathcal{H}(c) = \frac{h^*(c) - h_{\text{zero}}(c)}{h^*(c)} = 1 - \frac{0}{h^*(c)} = 1$$

when a tight heuristic is available, and $\mathcal{H}(c) = 0$ when only the zero heuristic (no doctrinal guidance) is available. In practice, $\mathcal{H}(c) = 1 - (h^*(c) - h_D(c))/h^*(c) = h_D(c)/h^*(c)$ measures the fraction of the true remaining cost that the heuristic captures.

---

## Notes on Sources

The $A^*$ algorithm was introduced by Hart, Nilsson, and Raphael (1968) and its optimality properties are proved in Pearl (1984). The mapping between legal reasoning and pathfinding was introduced in the Algorithmic Jurisprudence manuscript. The McDonnell Douglas burden-shifting framework was established in *McDonnell Douglas Corp. v. Green*, 411 U.S. 792 (1973), refined in *Texas Department of Community Affairs v. Burdine*, 450 U.S. 248 (1981), and further developed in *St. Mary's Honor Center v. Hicks*, 509 U.S. 502 (1993). Pattern databases in AI pathfinding are developed by Culberson and Schaeffer (1998) and Felner, Korf, and Hanan (2004). The adversarial search framework builds on minimax theory from von Neumann and Morgenstern (1944) and its application to game-playing AI in Russell and Norvig (2021). Settlement theory builds on Priest and Klein (1984). The distinction between binding and persuasive precedent is standard — see Cross and Harris (1991, *Precedent in English Law*).

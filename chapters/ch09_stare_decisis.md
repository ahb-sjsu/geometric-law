# Chapter 9: Stare Decisis as Parallel Transport

> *"It is revolting to have no better reason for a rule of law than that so it was laid down in the time of Henry IV."*
> — Oliver Wendell Holmes Jr., "The Path of the Law" (1897)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera is facing the hardest kind of case: one where the binding precedent is almost certainly wrong.*
>
> *The case involves a Bivens action — a constitutional tort claim against a federal officer. In 1971, the Supreme Court held in Bivens v. Six Unknown Named Agents that individuals could sue federal officers for Fourth Amendment violations even without a statutory cause of action. For decades, lower courts extended Bivens to cover a range of constitutional violations. But starting in the 1980s, the Supreme Court began restricting Bivens, declining to extend it to new contexts. By 2022, in Egbert v. Boule, the Court had made clear that extending Bivens to any new context was "a disfavored judicial activity."*
>
> *The plaintiff in Rivera's case, James Okonkwo, is a permanent resident who was detained by ICE agents at his workplace. The agents entered without a warrant, used excessive force, and held Okonkwo for forty-eight hours before releasing him without charges. Okonkwo sues under Bivens, alleging Fourth Amendment violations.*
>
> *Rivera must follow the precedent. She knows this. But the precedent is in tension with itself. Bivens created a right; subsequent cases eroded it; the most recent cases have left it a hollow shell. The doctrinal chain from Bivens (1971) through Davis v. Passman (1979) through Carlson v. Green (1980) through Ziglar v. Abbasi (2017) through Egbert v. Boule (2022) tells a story of progressive restriction. Following this chain from the 1971 vertex to the 2022 vertex is parallel transport along a curved path — and the rule that arrives at the end is so distorted by the curvature that it barely resembles the rule that began the journey.*
>
> *This chapter develops the formal apparatus for understanding what happens when a legal rule is carried along a chain of precedents. Stare decisis — the doctrine that like cases should be decided alike — is parallel transport on the judicial complex. The rule may arrive "rotated" by the curvature of the precedent field. When the rotation is too great, the transported rule contradicts the original — and the question of overruling becomes a question of whether to perform graph surgery.*

---

## Precedent as Weight Deformation

### How Precedent Shapes the Legal Landscape

Chapter 6 introduced the idea that precedent functions as a heuristic field — a guide for navigating the judicial complex. This chapter examines a deeper structural role: precedent as a *deformation* of the complex itself.

Each judicial decision does not merely provide guidance for future cases. It *changes the structure of the legal space*. A binding precedent modifies the edge weights in the neighborhood of its vertex, making certain paths cheaper (easier to follow) and other paths more expensive (harder to justify).

**Definition (Precedential Weight Deformation).** A binding precedent $P$ at vertex $c_P \in \mathcal{K}$ with holding $H_P$ modifies the edge weights of all edges incident to vertices near $c_P$:

$$w(c_i \to c_j) \to w(c_i \to c_j) + \Delta w(c_i \to c_j; P)$$

where $\Delta w$ is concentrated on edges near $c_P$ (the precedent affects factually similar cases) and encodes the holding $H_P$. The deformation's magnitude decays with graph distance from $c_P$:

$$|\Delta w(c_i \to c_j; P)| \sim \frac{w_P}{d_{\mathcal{K}}(c_i, c_P)^n}$$

where $w_P$ is the precedential weight (Supreme Court > Circuit Court > District Court) and $d_{\mathcal{K}}$ is the shortest-path distance in $\mathcal{K}$.

This definition captures several properties of precedent that legal theory takes as given:

**Locality.** A precedent primarily affects factually similar cases — cases "near" the precedent in the judicial complex. A securities fraud precedent does not change the edge weights in the personal injury region of the complex. The decay with distance $d_{\mathcal{K}}(c_i, c_P)^n$ formalizes this locality.

**Hierarchy.** The weight $w_P$ reflects the court's position in the judicial hierarchy. A Supreme Court decision deforms the complex more than a circuit court decision, which deforms it more than a district court decision. This is because $w_P$ is larger for higher courts — their precedential "gravitational pull" is stronger.

**Accumulation.** Multiple precedents in the same area of law produce cumulative deformation. The edge weights in a well-developed area (say, Fourth Amendment search-and-seizure law) are the baseline weights plus the sum of all precedential deformations. This accumulated deformation is what makes well-settled law feel *settled*: the edge weights are so heavily deformed by decades of precedent that the optimal paths are sharply defined.

### Precedent as a Connection

The weight deformation has a deeper structure: it defines a *connection* on the judicial complex. In differential geometry, a connection specifies how to carry a vector from one point to another — how the vector "rotates" as you move along a path. In the legal context, the connection specifies how a legal rule changes as you carry it from one case to another through intermediate cases.

**Definition (Legal Connection).** The *legal connection* $A$ is defined on the edges of $\mathcal{K}$ by the precedential weight deformation. For an edge $c_i \to c_j$, the connection coefficient $A(c_i, c_j)$ encodes how a legal rule transforms when transported from case $c_i$ to case $c_j$:

$$\text{Rule at } c_j = T(c_i, c_j) \cdot \text{Rule at } c_i$$

where $T(c_i, c_j)$ is the parallel transport matrix from $c_i$ to $c_j$. The transport matrix depends on the edge weight and on the difference in attribute vectors between the two cases.

When the connection is "flat" — when the edge weights are undeformed — parallel transport is trivial: the rule arrives unchanged. When the connection is "curved" — when heavy precedential deformation creates a non-trivial connection — parallel transport may rotate the rule. A rule about "reasonable expectation of privacy" in 1967 (*Katz v. United States*) arrives at a 2018 case (*Carpenter v. United States*) having been progressively rotated by decades of intervening precedent.

## Parallel Transport of Legal Rules

### What It Means to "Follow" Precedent

The doctrine of stare decisis says: decide the current case consistently with how similar cases were decided in the past. But what does "consistently" mean? If the current case is identical to the precedent, the answer is straightforward: decide it the same way. But cases are never identical. The current case is "near" the precedent in the judicial complex — it is connected by edges — but it is not at the same vertex.

Following precedent means *parallel transporting* the legal rule from the precedent's vertex to the current case's vertex. The rule is carried along a path through the complex — a chain of intermediate cases — and the connection determines how the rule changes along the way.

If the connection is flat (the area of law is stable, with no intervening precedents modifying the landscape), the transported rule arrives unchanged. The current case should be decided the same way as the precedent.

If the connection is curved (the area of law has been modified by intervening precedents), the transported rule may arrive rotated. The rule that made sense at the precedent's vertex may not make the same sense at the current vertex, because the legal landscape has changed around it.

### Holonomy: When the Rule Comes Back Changed

The most dramatic consequence of a curved connection is *holonomy*: if you transport a rule around a closed loop — a sequence of cases that returns to a factual configuration equivalent to the starting point — the rule may come back changed. The change is the holonomy of the loop.

In the legal context, holonomy means: start with a legal rule in a case of type $X$. Apply it to a case of type $Y$ (using distinguishing, analogizing, and extending). Apply the modified rule to a case of type $Z$. Apply it again to a case of type $X$. The rule has been transported around a loop $X \to Y \to Z \to X$. If the rule that arrives back at type $X$ is different from the rule that started, the loop has non-trivial holonomy — and the precedent system contains an inconsistency.

This is exactly the Wilson loop test from Chapter 8. Non-trivial holonomy in the precedent connection is a hidden inconsistency in the body of case law. It means that the legal system gives different answers to the same question depending on which chain of precedents you follow.

---

> **RUNNING EXAMPLE — PARALLEL TRANSPORT OF THE BIVENS RULE**
>
> *Rivera traces the parallel transport of the Bivens rule through the chain of Supreme Court cases.*
>
> ***Bivens (1971):*** *The rule at vertex $c_{\text{Bivens}}$: a person whose constitutional rights are violated by a federal officer may sue the officer for damages, even without a statutory cause of action. The rule is broad: it covers Fourth Amendment violations and, by implication, other constitutional violations.*
>
> ***Davis v. Passman (1979):*** *Transport from $c_{\text{Bivens}}$ to $c_{\text{Davis}}$. The rule is extended to Fifth Amendment due process claims. The transport is smooth — the connection between Fourth and Fifth Amendment violations is flat, and the rule arrives essentially unchanged: constitutional violations by federal officers give rise to damages suits.*
>
> ***Carlson v. Green (1980):*** *Transport from $c_{\text{Davis}}$ to $c_{\text{Carlson}}$. The rule is extended to Eighth Amendment claims. Again, the transport is smooth: the rule continues to arrive in recognizable form.*
>
> *But then the connection curves.*
>
> ***Bush v. Lucas (1983):*** *The Court declines to extend Bivens to First Amendment claims by federal employees, citing "special factors counseling hesitation." The connection becomes non-trivial: the transport matrix acquires a restriction term. The rule at $c_{\text{Bush}}$ is the Bivens rule minus a domain restriction.*
>
> ***Schweiker v. Chilicky (1988), Correctional Services Corp. v. Malesko (2001), Wilkie v. Robbins (2007):*** *Each successive refusal to extend Bivens adds more curvature. The connection coefficients grow. The rule is progressively "rotated" by each new restriction.*
>
> ***Ziglar v. Abbasi (2017):*** *The Court announces a two-part test for extending Bivens to any new context: (1) is the case meaningfully different from the three established Bivens contexts? (2) are there special factors counseling hesitation? The connection is now heavily curved — the rule that arrives at $c_{\text{Abbasi}}$ is barely recognizable as the Bivens rule. It has been rotated from "constitutional violations give rise to damages suits" to "damages suits are disfavored and almost never available in new contexts."*
>
> ***Egbert v. Boule (2022):*** *The rotation is nearly 180 degrees. The rule at $c_{\text{Egbert}}$ is effectively the negation of the rule at $c_{\text{Bivens}}$: constitutional violations by federal officers almost never give rise to damages suits.*
>
> *Rivera computes the holonomy. Start with the Bivens rule. Transport it through the chain Bivens → Davis → Carlson → Bush → Abbasi → Egbert. Now transport back to a 1971-type case: a plaintiff suing a federal officer for a Fourth Amendment violation. Has the rule returned unchanged? It has not. The rule that started as "you may sue" has become "you almost certainly may not sue." The holonomy is non-trivial — the precedent system contains a doctrinal inconsistency between the early and late cases.*

---

## Overruling as Graph Surgery

### The Phase Transition

When the holonomy becomes too great — when the transported rule has been so distorted by curvature that it contradicts the original — the legal system faces a choice: continue following the distorted rule, or overrule the precedent. Overruling is a *phase transition* in the judicial complex: a discontinuous change in edge weights that restructures the local topology.

**Definition (Legal Phase Transition).** *Overruling* a precedent $P$ is a discrete graph surgery on $\mathcal{K}$:

$$w(c_i \to c_j) \to w(c_i \to c_j) - \Delta w(c_i \to c_j; P) + \Delta w(c_i \to c_j; P')$$

where $P'$ is the new precedent replacing $P$. This is a *legal phase transition*: the filtration structure changes, vertices that were previously on one side of a regime boundary may now be on the other, and the shortest-path structure of $\mathcal{K}$ is discontinuously altered.

The surgery removes the old precedent's weight deformation and replaces it with the new precedent's deformation. Every edge in the neighborhood of the overruled precedent changes weight simultaneously. The legal landscape is suddenly different, and cases that were easy to win under the old precedent may become difficult or impossible under the new one — and vice versa.

### The Cost of Overruling

Overruling is not free. The cost is proportional to the *reliance interest*: the number and weight of subsequent cases that were decided under the old precedent's weight deformation.

$$\text{Cost}_{\text{overrule}} = \sum_{i=1}^{n} w_{P_i} \cdot |\Delta w(c_i, \cdot \; ; P)|$$

where $P_1, \ldots, P_n$ are the cases decided under the old precedent, $w_{P_i}$ is the weight of each relying case, and $|\Delta w(c_i, \cdot \; ; P)|$ measures how much each case's edge weights change when $P$ is removed.

This formula captures the legal intuition behind stare decisis. The doctrine is not that precedents are infallible — the Supreme Court overrules its own precedents regularly. The doctrine is that overruling has a *cost*, and the benefit of overruling must exceed that cost.

The cost increases with:

- **Number of relying cases.** A precedent that has been followed by thousands of subsequent cases has a higher overruling cost than one that has been cited only a few times.
- **Importance of relying cases.** If the relying cases involve major constitutional rights or property interests, the overruling cost is higher.
- **Depth of reliance.** If parties have structured their affairs in reliance on the precedent (contracts, investments, institutional structures), the overruling cost extends beyond the legal system into the social and economic fabric.

### Brown v. Board of Education as Graph Surgery

The paradigmatic example of graph surgery is *Brown v. Board of Education* (1954), which overruled *Plessy v. Ferguson* (1896).

Under Plessy, edges connecting "separate but equal" vertices to the "constitutional" region of the complex had finite weight: racial segregation was constitutional. Under Brown, those edges acquired infinite weight (or were removed entirely): segregation itself violates equal protection. The graph surgery was dramatic:

- All vertices representing "separate but equal" arrangements were disconnected from the constitutional subcomplex.
- Previously "legal" paths that ran through segregation-compatible vertices became impassable.
- New paths opened from desegregation vertices to the constitutional region.
- The reliance cost was enormous: every institution in the American South had structured itself around Plessy's weight deformation.

But the benefit was also enormous: the overruling eliminated a gauge violation of the first magnitude. The "separate but equal" doctrine was not gauge-invariant under racial transformation — the whole point of the doctrine was to produce different legal environments for different races. Brown restored gauge invariance by removing the gauge-variant vertices from the constitutional subcomplex.

The geometric framework provides a criterion for when overruling is justified: *overrule when the gauge violation removed exceeds the reliance cost incurred*. Brown was justified because the gauge violation (the entire apparatus of legal segregation) was vastly larger than the reliance cost (institutional disruption). Conversely, a precedent whose gauge violation is small and whose reliance interest is large should not be overruled — the cost exceeds the benefit.

## Liability Conservation

### The Conservation Theorem

Restating Theorem from Chapter 5 in the context of stare decisis dynamics:

The deepest consequence of the gauge structure of the legal system is a conservation law. Just as Noether's theorem in physics derives conservation of energy from temporal symmetry and conservation of momentum from spatial symmetry, the gauge symmetry of the legal system generates a conservation law for liability.

**Theorem (Liability-Damages Conservation).** In a closed bilateral tort dispute between plaintiff $A$ and defendant $B$, the total liability-damages balance is conserved:

$$L(A) + L(B) = 0$$

where $L(X)$ is the net liability of party $X$, defined as the signed sum of obligations imposed by adjudication. Equivalently: every dollar of damages awarded to $A$ imposes exactly one dollar of liability on $B$; every Hohfeldian right created for $A$ imposes a correlative duty on $B$.

*Proof.* The proof follows from the correlative structure of Hohfeldian positions. In a closed bilateral system under a fixed legal framework $\mathcal{F}$:

1. Every right of $A$ is a correlative duty of $B$ (Hohfeld's first correlative pair).
2. Every liability of $B$ is a correlative power of $A$ (Hohfeld's second correlative pair).
3. Adjudication does not create Hohfeldian positions *ex nihilo*; it *recognizes* or *assigns* positions that already exist within $\mathcal{F}$.
4. Therefore, the net entitlement change $\Delta E(A) + \Delta E(B) = 0$ at every step of the proceeding.

For damages specifically: compensatory damages transfer wealth from $B$ to $A$, so $\Delta D(A) = -\Delta D(B)$. Punitive damages are an apparent exception, but they are grounded in a duty $B$ owes to the *public interest* (dimension $d_8$), extending the closed system to include the state as a third party; within the extended system $\{A, B, \text{State}\}$, the balance $L(A) + L(B) + L(\text{State}) = 0$ is restored. $\square$

### Scope and Limitations

Liability conservation holds within a fixed legal framework. Three operations break the conservation law:

1. **Legislation.** A new statute can create causes of action *ex nihilo*, generating rights without corresponding prior duties. This is a symmetry-breaking event — it changes the rules $\mathcal{F}$, not the dynamics within $\mathcal{F}$.

2. **Constitutional amendment.** Alters the topological constraint space $\mathcal{C}$ (Chapter 7), potentially creating or destroying entire classes of entitlements.

3. **Third-party intervention.** Adding a new party to the dispute breaks the closure condition. Conservation is restored by extending the subsystem to include all parties.

Each of these operations is analogous to a symmetry-breaking event in physics: legislation is like introducing a new field, constitutional amendment is like changing the topology of spacetime, and third-party intervention is like opening the system to external interactions. In each case, the conservation law fails because the *conditions* for conservation (closed system, fixed framework) are violated, not because the *principle* is wrong.

---

> **RUNNING EXAMPLE — RIVERA CONSIDERS OVERRULING**
>
> *Rivera cannot overrule Bivens or Egbert — she is a district court judge, and those are Supreme Court precedents. But she can distinguish. The question is whether Okonkwo's case presents a "new context" under the Egbert framework, or whether it falls within one of the three established Bivens contexts.*
>
> *She performs the parallel transport analysis. Okonkwo's case involves a Fourth Amendment violation (warrantless entry, excessive force). The Fourth Amendment is the original Bivens context. Transport from $c_{\text{Bivens}}$ to $c_{\text{Okonkwo}}$ passes through the original Bivens vertex — the path is short, the connection is close to flat in this neighborhood, and the rule should arrive unchanged: Fourth Amendment violations by federal officers give rise to damages suits.*
>
> *But Egbert complicates this. Egbert involved a Fourth Amendment claim — the same amendment as Bivens — yet the Court declined to allow it, holding that the immigration enforcement context was "new." The connection from Bivens to Egbert is heavily curved, even though both cases involve the Fourth Amendment.*
>
> *Rivera must decide which path to transport along. If she transports directly from Bivens to Okonkwo (ignoring Egbert), the rule arrives intact: Okonkwo may sue. If she transports through Egbert, the rule arrives heavily rotated: Okonkwo probably may not sue.*
>
> *This is the fundamental problem with stare decisis in a curved legal space: the answer depends on the path. In a flat space, all paths give the same answer — that is what "flatness" means. In a curved space, different paths give different answers, and the judge must choose which path to follow.*
>
> *Rivera writes her opinion. She holds that Okonkwo's case is not a "new context" — it is a straightforward Fourth Amendment excessive force claim, indistinguishable from Bivens itself. She follows the direct path from Bivens, acknowledging Egbert but distinguishing it on its facts (immigration enforcement context versus a standard law enforcement encounter). She notes, in a careful footnote, that the progressive restriction of Bivens has created a doctrinal inconsistency: the rule announced in 1971 and the rule operating in 2022 are incompatible at the same vertex type. She invites the circuit court to address this inconsistency — a non-trivial Wilson loop in the Fourth Amendment region of the complex.*

---

## Legal Phase Transitions

### The Anatomy of Overruling

Not all changes in law are gradual. Some are sudden, discontinuous, and irreversible — phase transitions in the legal system. The overruling of a major precedent is the paradigmatic example, but phase transitions also occur through landmark legislation, constitutional amendments, and sudden shifts in judicial philosophy.

**Definition (Legal Phase Transition).** A *legal phase transition* is a discontinuous change in the edge weights of $\mathcal{K}$ that:

1. Alters the weight deformation in a region of the complex by more than a threshold $\delta$;
2. Changes the shortest-path structure in that region (paths that were optimal before the transition are no longer optimal, and vice versa);
3. May change the regime filtration (vertices that were inside a stratum may now be outside, or vice versa).

Phase transitions come in two types, paralleling the classification in thermodynamics:

**First-order transitions** involve a discontinuous jump in the "order parameter" — the primary legal variable in the affected region. Overruling a precedent is a first-order transition: the holding flips from one state to another (segregation is constitutional / segregation is unconstitutional) without passing through intermediate states.

**Second-order transitions** involve a continuous change in the order parameter but a discontinuous change in its *derivative*. A gradual shift in doctrinal interpretation — where the rule changes smoothly but the rate of change is discontinuous — is a second-order transition. The progressive restriction of Bivens is an example: the rule did not flip; it was gradually eroded, but the erosion accelerated sharply at certain moments (Abbasi, Egbert).

### The Critical Point

Every phase transition has a *critical point* — the moment when the system shifts from one state to another. In the legal system, the critical point is the case that triggers the overruling. What determines when the critical point is reached?

The geometric framework provides a criterion: the critical point is reached when the *holonomy around the doctrinal loop exceeds a threshold*.

$$\|W(\gamma) - I\| > \theta_{\text{critical}}$$

where $W(\gamma)$ is the Wilson loop holonomy around the doctrinal loop, $I$ is the identity matrix, and $\theta_{\text{critical}}$ is the system's tolerance for inconsistency.

When the holonomy is small — the transported rule is close to the original — the system tolerates the inconsistency. Stare decisis holds. When the holonomy grows — the transported rule diverges further from the original — the tension increases. At the critical point, the holonomy exceeds the system's tolerance, and a phase transition occurs: the precedent is overruled.

This explains several empirical observations about overruling:

- **Why overruling is rare.** The threshold $\theta_{\text{critical}}$ is high — the legal system has a strong preference for stability (the reliance interest). Only when the holonomy is large enough to overcome this preference does overruling occur.

- **Why overruling clusters.** When one precedent is overruled, the resulting change in edge weights may push the holonomy of *other* doctrinal loops above the threshold, triggering a cascade of overrulings. This explains why legal revolutions tend to come in waves: Brown triggered a cascade in equal protection; the New Deal triggered a cascade in Commerce Clause jurisprudence.

- **Why there are "warning signs."** Before a phase transition, the holonomy is growing but has not yet reached the threshold. This growth is visible in the case law as increasing numbers of concurrences, dissents, and "distinguish rather than follow" opinions — signs that the transported rule is straining under the curvature.

## Distinguishing as Path Selection

### The Judge's Choice

When a judge "distinguishes" a precedent — declaring that it does not apply to the current case because of factual differences — the judge is choosing which path to transport along. The precedent's rule is available, but the judge selects a different path through the complex, one that avoids the precedent's vertex and therefore avoids the weight deformation it would impose.

Distinguishing is not the same as overruling. Overruling removes the precedent's weight deformation from the complex entirely. Distinguishing leaves the deformation in place but routes around it — the judge finds a path through the complex that does not pass through the neighborhood where the precedent's deformation is concentrated.

**Definition (Distinguishing).** *Distinguishing* a precedent $P$ at vertex $c_P$ means constructing a path $\gamma$ from the current case $c$ to the goal region $G$ that avoids the neighborhood $N_\epsilon(c_P)$ of the precedent:

$$\gamma \cap N_\epsilon(c_P) = \emptyset$$

where $N_\epsilon(c_P) = \{c_i \in \mathcal{K} : d_{\mathcal{K}}(c_i, c_P) < \epsilon\}$ is the $\epsilon$-neighborhood of the precedent vertex.

The cost of distinguishing is the *excess path length*: the difference between the shortest path through $N_\epsilon(c_P)$ (following the precedent) and the shortest path avoiding $N_\epsilon(c_P)$ (distinguishing). If the excess is small — if there is a nearly-as-short path that avoids the precedent — distinguishing is easy. If the excess is large — if the precedent is unavoidable — distinguishing is difficult or impossible, and the judge must either follow or overrule.

### When Distinguishing Fails

Distinguishing fails when the precedent's weight deformation covers the entire relevant region of the complex. If every path from the current case to the goal passes through the precedent's neighborhood, there is no route around it. The judge must either follow the precedent (accepting its weight deformation) or overrule it (performing graph surgery).

This is the geometric explanation for "controlling precedent" — precedent that *must* be followed because there is no alternative path. A Supreme Court case on point is controlling because its weight deformation covers the entire relevant region at the top of the hierarchy. A district court case may be easily distinguished because its weight deformation is local and there are many alternative paths.

---

> **RUNNING EXAMPLE — RIVERA'S DISTINGUISHING STRATEGY**
>
> *Rivera's opinion in Okonkwo's case is, at its core, a distinguishing argument. She is not overruling Egbert — she cannot. She is finding a path from Okonkwo's case to the Bivens remedy that avoids the Egbert neighborhood.*
>
> *Her argument: Egbert involved a border patrol agent acting in an immigration enforcement capacity. The "special factors" that counseled hesitation included national security concerns, congressional oversight of immigration enforcement, and the availability of an alternative remedial scheme (administrative complaints to CBP). None of these factors apply to Okonkwo's case, which involves standard law enforcement agents acting in a non-immigration context without any alternative remedial scheme.*
>
> *In the geometry of the complex, Rivera is saying: $c_{\text{Okonkwo}}$ is not in $N_\epsilon(c_{\text{Egbert}})$. The factual distance between the two cases — along the dimensions of enforcement context, available alternative remedies, and national security implications — is large enough that the Egbert deformation does not reach Okonkwo's vertex.*
>
> *But Rivera is honest in her opinion about the difficulty of the argument. The Egbert majority opinion used broad language suggesting that its restriction applies to all new Bivens contexts, not just immigration enforcement. If taken at face value, Egbert's deformation covers the entire Bivens neighborhood — there is no path around it. Rivera addresses this by interpreting the holding narrowly: the breadth of the language is dictum, and the actual holding is limited to the specific context before the Court.*
>
> *This is the judge's art: finding the gap in the precedential deformation, the narrow path between vertices where the rule has been distorted and vertices where it retains its original shape. The geometric framework does not eliminate the need for this art — but it makes visible the structure within which the art operates.*

---

## The Doctrine of Stare Decisis as a Geometric Principle

### Formal Statement

Stare decisis is often stated as a normative principle: like cases should be decided alike. The geometric framework reveals that this normative principle has a mathematical content: stare decisis is the requirement that *parallel transport on the judicial complex be approximately path-independent*.

In a flat space (a consistent body of case law), parallel transport is path-independent: no matter which chain of precedents you follow from case $A$ to case $B$, the legal rule arrives at $B$ in the same form. In a curved space (an inconsistent body of case law), parallel transport is path-dependent: different chains of precedent give different rules at the same destination.

Stare decisis is the commitment to make the space as flat as possible — to decide new cases in a way that minimizes curvature, so that future parallel transport is approximately path-independent. Each time a judge decides a case consistently with precedent, she adds a vertex to the complex that *does not* create new curvature. The edge weights from the new vertex to the precedent vertex are consistent with the existing deformation. The space remains flat.

Each time a judge departs from precedent — either by distinguishing or by overruling — she adds curvature. The edge weights from the new vertex are inconsistent with the existing deformation. The space becomes curved, and future parallel transport becomes path-dependent.

### Why Stare Decisis Matters

The geometric perspective explains why stare decisis is important in a way that transcends the usual justifications (predictability, reliance, judicial economy). The fundamental reason is:

**Path-dependent law is gauge-variant law.**

If different chains of precedent give different rules for the same type of case, then the legal outcome depends on which chain the judge follows — which is an arbitrary choice of "path" through the complex. This is a gauge variance: the outcome depends on a feature of the analysis (the path through the complex) that should not affect the result.

Stare decisis is therefore a *gauge-fixing condition*: it selects a preferred path through the complex (follow the most analogous precedent) and requires judges to use that path. This is exactly what gauge fixing does in physics: it selects a preferred description from among equivalent descriptions, eliminating the gauge freedom.

## Worked Example: Precedent Overruling

### Scenario

The Supreme Court considers overruling a 40-year-old precedent $P$ that established a particular interpretation of the Commerce Clause, holding that a certain category of economic regulation is within Congress's power.

### Analysis on the Judicial Complex

**Step 1: Current structure.** Precedent $P$ at vertex $c_P$ has modified edge weights throughout the Commerce Clause neighborhood. Hundreds of subsequent cases ($c_1, \ldots, c_n$) have been decided with these modified weights, creating a web of reliance interests.

**Step 2: Holonomy computation.** Compute the Wilson loop around the Commerce Clause doctrinal loop. The loop runs: Commerce Clause → economic regulation → interstate effects → substantial effects test → Commerce Clause. The holonomy $W(\gamma)$ measures the consistency of the doctrine around this loop.

If $W(\gamma)$ is close to the identity, the doctrine is consistent — stare decisis is satisfied. If $W(\gamma)$ is far from the identity, the doctrine contains internal inconsistencies that have accumulated over 40 years of case-by-case modification.

**Step 3: Phase transition cost.** The cost of overruling is:

$$\text{Cost}_{\text{overrule}} = \sum_{i=1}^n w_{P_i} \cdot |\Delta w(c_i, \cdot \; ; P)|$$

This is a sum over all $n$ relying cases, weighted by the importance of each case and the magnitude of the weight change. For a 40-year-old precedent with hundreds of relying cases, the cost is substantial.

**Step 4: Decision criterion.** The Court overrules $P$ when the topological benefit (removing a constitutional inconsistency, reducing Wilson loop complexity) exceeds the transition cost. This is a graph optimization problem: find the weight perturbation that minimizes total re-evaluation cost while restoring topological consistency.

Formally, the Court seeks the minimum-cost perturbation $\Delta w'$ such that:

$$\|W(\gamma)\| \text{ is reduced below } \theta_{\text{critical}}$$

subject to:

$$\text{Cost}(\Delta w') = \sum_{i} w_{P_i} \cdot |\Delta w'(c_i, \cdot)| < \text{Benefit}(\Delta w')$$

where the benefit is measured by the reduction in holonomy and the restoration of gauge invariance.

**Step 5: Stare decisis as inertia.** The doctrine of stare decisis corresponds to a *cost barrier* around established precedents — the legal system's inertia against weight changes. The height of the barrier is the accumulated reliance interest. The Court overrules only when the "energy" of the inconsistency exceeds the barrier height.

## Chapter Summary

1. Precedent modifies the structure of the judicial complex through weight deformation: each binding decision changes the edge weights in its neighborhood, making certain paths cheaper and others more expensive.

2. Following precedent is parallel transport: carrying a legal rule from the precedent's vertex to the current case's vertex along a path through intermediate cases. The legal connection determines how the rule changes along the way.

3. Non-trivial holonomy (a transported rule returning changed after a closed loop) indicates doctrinal inconsistency — a hidden contradiction in the precedent system detectable by the Wilson loop test.

4. Overruling is graph surgery: a discontinuous change in edge weights that restructures the local topology. The cost of overruling is the accumulated reliance interest.

5. Liability conservation holds within a closed bilateral dispute: the net change in Hohfeldian entitlements is zero. This is a consequence of gauge invariance enforced by the correlative structure of Hohfeldian positions.

6. Legal phase transitions occur when the holonomy around a doctrinal loop exceeds the system's tolerance for inconsistency. Phase transitions may cascade, explaining why legal revolutions come in waves.

7. Distinguishing a precedent is path selection: routing around the precedent's weight deformation rather than removing it. Distinguishing fails when the deformation covers the entire relevant region and there is no alternative path.

8. Stare decisis is a gauge-fixing condition: it selects preferred paths through the complex, reducing path dependence and thereby reducing gauge variance.

---

## Technical Appendix

**Definition (Precedential Weight Deformation — Full).** For precedent $P$ at vertex $c_P$ with hierarchical weight $w_P$, decay exponent $n$, and holding operator $H_P$:

$$\Delta w(c_i \to c_j; P) = w_P \cdot \langle H_P, \Delta \mathbf{v}(c_i, c_j) \rangle \cdot d_{\mathcal{K}}(c_i, c_P)^{-n}$$

where $\langle H_P, \Delta \mathbf{v} \rangle$ is the inner product of the holding with the attribute-vector difference (how much the precedent's holding bears on the doctrinal step from $c_i$ to $c_j$).

**Definition (Legal Connection — Formal).** The legal connection on $\mathcal{K}$ is a $G_{\mathfrak{H}}$-valued 1-form $A$ on the edges, where $G_{\mathfrak{H}} = D_4 \rtimes D_4$ is the Hohfeldian gauge group. For edge $c_i \to c_j$:

$$A(c_i \to c_j) = \sum_P \Delta w(c_i \to c_j; P) \cdot g_P$$

where the sum is over all precedents $P$ whose deformation reaches the edge, and $g_P \in G_{\mathfrak{H}}$ is the gauge element corresponding to $P$'s holding (the Hohfeldian transformation that $P$ effects).

**Definition (Holonomy).** For a closed directed path $\gamma = (c_0, c_1, \ldots, c_m, c_0)$ in $\mathcal{K}$, the holonomy is:

$$\text{Hol}(\gamma) = \prod_{k=0}^{m} A(c_k \to c_{k+1 \bmod (m+1)})$$

The holonomy is trivial ($\text{Hol}(\gamma) = e \in G_{\mathfrak{H}}$) iff the connection is flat along $\gamma$.

**Theorem (Liability-Damages Conservation — Full Statement).** In a closed bilateral dispute $(A, B)$ under fixed framework $\mathcal{F}$, with Hohfeldian correlative structure:

$$\sum_{h \in \mathfrak{H}_+} w_h(A) - \sum_{h \in \mathfrak{H}_-} w_h(A) + \sum_{h \in \mathfrak{H}_+} w_h(B) - \sum_{h \in \mathfrak{H}_-} w_h(B) = 0$$

where $\mathfrak{H}_+ = \{\text{right, liberty, power, immunity}\}$ and $\mathfrak{H}_- = \{\text{duty, no-right, liability, disability}\}$. *Proof.* Each position in $\mathfrak{H}_+$ for party $A$ is a correlative position in $\mathfrak{H}_-$ for party $B$, and vice versa. Therefore the positive terms for $A$ equal the negative terms for $B$, and the positive terms for $B$ equal the negative terms for $A$, giving a net sum of zero. $\square$

**Proposition (Overruling Cost).** Let $P$ be a precedent with $n$ relying cases $\{c_1, \ldots, c_n\}$. The minimum-cost overruling perturbation $\Delta w^*$ that restores flatness in the neighborhood of $c_P$ satisfies:

$$\text{Cost}(\Delta w^*) \geq \sum_{i=1}^{n} w_{P_i} \cdot \min_{\Delta w'} |\Delta w'(c_i, \cdot)|$$

subject to $\text{Hol}(\gamma) = e$ for all loops $\gamma$ in $N_\epsilon(c_P)$. *Proof.* Each relying case must have its edge weights adjusted to be consistent with the new precedent. The minimum adjustment is the minimum perturbation that restores flatness, which is bounded below by the product of the case weight and the minimum weight change. $\square$

---

## Notes on Sources

Holmes's "The Path of the Law" was published in the *Harvard Law Review* (1897) and remains one of the most cited articles in legal scholarship. *Bivens v. Six Unknown Named Agents*, 403 U.S. 388 (1971), established implied damages actions for constitutional violations. The progressive restriction of Bivens runs through *Bush v. Lucas*, 462 U.S. 367 (1983), *Schweiker v. Chilicky*, 487 U.S. 412 (1988), *Correctional Services Corp. v. Malesko*, 534 U.S. 61 (2001), *Wilkie v. Robbins*, 551 U.S. 537 (2007), *Ziglar v. Abbasi*, 582 U.S. 120 (2017), and *Egbert v. Boule*, 596 U.S. 482 (2022). *Brown v. Board of Education*, 347 U.S. 483 (1954), overruled *Plessy v. Ferguson*, 163 U.S. 537 (1896). The parallel transport interpretation of stare decisis is original to the Algorithmic Jurisprudence framework. Liability conservation (Theorem 7.1 in the AJ manuscript) extends the harm conservation principle from Geometric Ethics. The concept of legal phase transitions builds on Kuhn's theory of scientific revolutions (1962) applied to law; see Ackerman, *We the People* (1991) for a historical account of constitutional "moments" as phase transitions. The connection formalism follows standard differential geometry (Kobayashi and Nomizu, *Foundations of Differential Geometry*, 1963) adapted to discrete complexes.

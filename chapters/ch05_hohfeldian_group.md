# Chapter 5: The $D_4$ Hohfeldian Group

> *"The universe is an enormous direct product of representations of symmetry groups."*
> — Hermann Weyl, *Symmetry* (1952)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera is reviewing a set of four cases from her circuit that deal with the same legal question: whether a city's ban on sleeping in public parks violates the Eighth Amendment's prohibition on cruel and unusual punishment when applied to homeless individuals who have no alternative shelter.*
>
> *The first case (2019) held that the ban is constitutional because it regulates conduct, not status. The second case (2020) held that a nearly identical ban is unconstitutional because criminalizing involuntary conduct is cruel and unusual. The third case (2021) synthesized the first two by holding that the ban is constitutional only if shelter is available — creating a conditional rule. The fourth case (2022) applied the third case's rule but reached a result inconsistent with the second case.*
>
> *Rivera suspects there is a contradiction hidden in this chain of precedent. But reading the four opinions, each seems internally coherent. The problem is not that any single case is wrong — it is that the system of cases is inconsistent. Following the chain from Case 1 through Case 2 through Case 3 through Case 4 and back to Case 1 produces a different Hohfeldian configuration than you started with.*
>
> *This chapter provides the tool for detecting such contradictions: the Wilson loop, which measures the holonomy of the legal connection around a closed cycle of precedent. A non-trivial Wilson loop is a hidden inconsistency — proof that the body of case law contradicts itself, even though each case is individually coherent.*

---

## From Tetrad to Octad

Chapter 2 showed that Hohfeld's first square of legal relations — right, duty, liberty, no-right — has the symmetry structure of the dihedral group $D_4$. The correlative operation and the jural opposite operation generate an 8-element group acting on the four positions.

But law requires more than the first square. The full Hohfeldian system has *eight* positions, arranged in two squares:

| First Square (First-Order) | Second Square (Second-Order) |
|---|---|
| Right | Power |
| Duty | Liability |
| Liberty | Immunity |
| No-right | Disability |

The first square captures *first-order* legal relations — relations about acts ("A has a right that B do $\varphi$"). The second square captures *second-order* legal relations — relations about legal relations themselves ("A has the power to alter B's legal position").

Each square individually has $D_4$ symmetry, as Chapter 2 established. The question is: what is the symmetry of the *combined* octad?

### The Naive Answer: $D_4 \times D_4$

The simplest possibility is that the two squares are independent — that the symmetry of the octad is the direct product $D_4 \times D_4$. This would mean that transformations of first-order positions are independent of transformations of second-order positions. You could swap Right and Duty (a first-order correlative transformation) without affecting Power and Liability, and vice versa.

In the ethical domain, this is approximately correct. Ethical analysis typically involves only first-order positions (rights, duties, liberties, no-rights), and the second-order positions (powers, immunities) play a limited role. The Geometric Ethics programme used $D_4$ (for the first square) and noted that the full moral gauge group is $D_4 \times D_4$ when the second square is included.

But in law, the two squares are *not* independent.

### The Legal Coupling

Second-order positions *act on* first-order positions. This coupling is the defining feature of legal reasoning:

- Exercising a **power** creates, modifies, or destroys first-order positions. When a legislature enacts a statute, it exercises its power to create new rights and duties. When a judge issues a ruling, they exercise judicial power to determine which first-order positions obtain.

- Holding an **immunity** prevents another party's power from altering one's first-order positions. The First Amendment grants speakers an immunity against legislative power to restrict speech — the legislature's power to create a duty-not-to-speak is disabled by the speaker's immunity.

- A **liability** to a power means one's first-order positions are subject to alteration. A citizen's liability to legislative power means that the legislature can impose new duties (pay this tax, follow this regulation) that change the citizen's first-order Hohfeldian structure.

- A **disability** means the inability to alter first-order positions. The Supremacy Clause creates a disability for states: they lack the power to create state-law duties that conflict with federal rights.

This coupling means that a second-order gauge transformation (relabeling power $\leftrightarrow$ liability, say) *induces* a corresponding transformation on the first-order square. Relabeling the party who has the power changes which party's first-order positions are subject to alteration. The two squares are linked.

## The Full Gauge Group

### Semi-Direct Product

**Theorem (Octahedral Gauge Group).** The symmetry group of the full Hohfeldian octad is the *semi-direct product*:

$$G_{\mathfrak{H}} = D_4 \rtimes_\varphi D_4$$

where the first factor $D_4$ acts on first-order relations (right--duty--liberty--no-right), the second factor $D_4$ acts on second-order relations (power--liability--immunity--disability), and the homomorphism $\varphi: D_4 \to \text{Aut}(D_4)$ encodes how second-order operations act on first-order positions.

**Proof sketch.** Each Hohfeldian square admits $D_4$ symmetry by the argument of Chapter 2: four positions form two correlative pairs connected by jural opposition and correlative swap, generating $D_4$.

However, the two squares are not independent. A second-order gauge transformation $g_2 \in D_4$ (e.g., relabeling power $\leftrightarrow$ liability) induces a corresponding transformation on the first-order square. Specifically: the right that a power would create is relabeled as the duty that the correlative liability would impose. This is precisely the structure of a semi-direct product: the second factor acts on the first via the homomorphism $\varphi$.

The group $G_{\mathfrak{H}} = D_4 \rtimes_\varphi D_4$ has its multiplication rule given by:

$$(g_1, g_2) \cdot (h_1, h_2) = (g_1 \cdot \varphi(g_2)(h_1), \; g_2 \cdot h_2)$$

The first-order transformation $h_1$ is "twisted" by the second-order transformation $g_2$ before being composed. This captures the legal reality that the meaning of a first-order operation (creating a right) depends on the second-order context (whether the creating party has the power to do so). $\square$

### Why Semi-Direct, Not Direct

The distinction between the semi-direct product $D_4 \rtimes D_4$ and the direct product $D_4 \times D_4$ is not merely technical. It captures a fundamental asymmetry of legal reasoning.

In the direct product $D_4 \times D_4$, the multiplication rule is $(g_1, g_2) \cdot (h_1, h_2) = (g_1 h_1, g_2 h_2)$. The two factors are independent — transformations of first-order positions and transformations of second-order positions commute. This would mean that the act of creating a right (a first-order operation) is independent of whether the creating party has the power to create it (a second-order question). But this is legally false: a legislature without the constitutional power to regulate in a given area *cannot* create rights in that area, no matter what statute it enacts.

In the semi-direct product $D_4 \rtimes_\varphi D_4$, the second factor *twists* the first. The twist captures exactly the dependence described above: first-order operations are conditioned on the second-order context.

When the coupling homomorphism $\varphi$ is trivial — when every $\varphi(g_2)$ is the identity — the semi-direct product reduces to the direct product, recovering the Geometric Ethics result as a special case. This explains why the direct product is adequate for ethics (where second-order operations are rare) but inadequate for law (where they are pervasive).

### The Order of the Group

The group $G_{\mathfrak{H}} = D_4 \rtimes_\varphi D_4$ has order at most $|D_4| \times |D_4| = 8 \times 8 = 64$. The actual order depends on the specific homomorphism $\varphi$. In the trivial case ($\varphi = \text{id}$), all 64 elements are distinct. In a non-trivial case, some elements may coincide, giving a quotient. For the legal application, we work with the full 64-element group.

Each of the 64 elements corresponds to a distinct legal re-description — a way of permuting the Hohfeldian labels across both squares while preserving the bond structure. The legal evaluation must be invariant under all 64 transformations:

$$J_{\text{law}}(g \cdot p) = J_{\text{law}}(p) \quad \forall \; g \in G_{\mathfrak{H}}$$

This is the Judicial Bond Invariance Principle (JBIP) in its full form.

## Legal Gauge Transformations

### What a Gauge Transformation Does

A *legal gauge transformation* $g \in G_{\mathfrak{H}}$ acts on a vertex $c \in \mathcal{K}$ by:

1. **Permuting the Hohfeldian labels of the parties.** For instance, swapping the right-holder and the duty-bearer while preserving the bond. The legal situation is the same — the same obligation exists between the same parties — but the description has changed.

2. **Rotating through the correlative-opposite structure.** Viewing a right from the correlative duty perspective, or viewing a liberty from the opposite duty perspective. Each rotation produces a different description of the same underlying legal relation.

3. **Composing first- and second-order transformations.** Asking whether the power to create a right is itself subject to an immunity, or whether a liability to a power is correlative with the power itself. These compound transformations require the full semi-direct product structure.

### Gauge Invariance as a Legal Requirement

A legal evaluation $J_{\text{law}}$ is *gauge-invariant* if:

$$J_{\text{law}}(g \cdot p) = J_{\text{law}}(p) \quad \forall \; g \in G_{\mathfrak{H}}$$

This requirement has immediate practical content. A legal system that reaches different conclusions when the same dispute is viewed from the correlative perspective — the right-holder's view versus the duty-bearer's view — is *gauge-variant*. It is sensitive to a choice of description that should not affect the outcome.

Consider a landlord-tenant dispute. If the court analyzes the case as "the tenant has a right to quiet enjoyment" and finds for the tenant, but would analyze the same case as "the landlord has a duty of non-interference" and find for the landlord, the court is making a gauge error. The right-holder's right and the duty-bearer's duty are the same bond viewed from different perspectives — the $D_4$ correlative transformation. A gauge-invariant evaluation must reach the same conclusion regardless of which perspective is adopted.

This is not an exotic requirement. It is what the law already demands: that outcomes depend on substance, not on framing. Gauge invariance is the mathematical formalization of this demand.

---

> **RUNNING EXAMPLE — GAUGE-VARIANT REASONING IN RIVERA'S CIRCUIT**
>
> *Rivera examines the four Eighth Amendment cases more carefully. She notices that Cases 1 and 2 describe the same legal relationship from different perspectives:*
>
> *Case 1 frames the issue as: "Does the city have a **liberty** to ban sleeping in parks?" (No duty not to ban $\Rightarrow$ liberty exists $\Rightarrow$ ban is permissible.)*
>
> *Case 2 frames the issue as: "Does the individual have a **right** not to be punished for involuntary conduct?" (Right exists $\Rightarrow$ correlative duty on the city $\Rightarrow$ ban violates the duty $\Rightarrow$ ban is impermissible.)*
>
> *These two framings are related by a $D_4$ gauge transformation: the correlative rotation takes the city's liberty (first-square, city's perspective) to the individual's no-right (correlative of liberty), and then the opposite operation takes the individual's no-right to the individual's right (opposite of no-right). The net transformation is $r \cdot s$ — a composition of correlative and opposite operations.*
>
> *If the legal evaluation were gauge-invariant, Cases 1 and 2 would reach the same conclusion. They do not. This means the circuit's jurisprudence is **gauge-variant** — the outcome depends on which $D_4$ representative the court chose to frame the analysis.*
>
> *Rivera can now diagnose the inconsistency precisely: it is a gauge violation, located at the correlative-opposite transformation $rs \in D_4$, applied to the Eighth Amendment bond between the individual and the state. The inconsistency is not a vague "the cases disagree" — it is a specific mathematical defect with a specific group-theoretic signature.*

---

## Wilson Loops: Detecting Hidden Inconsistency

### The Legal Connection

In gauge theory, a *connection* specifies how to parallel-transport a field value from one point to another. In the legal setting, the *legal connection* specifies how Hohfeldian labels transform as you move through the judicial complex — from one case to the next, following citation edges.

When a court applies a precedent, it *transports* the precedent's Hohfeldian structure to the current case. The transportation is not trivial: the precedent may involve different parties, different acts, and different legal contexts. The court must map the precedent's right-duty structure onto the current case's right-duty structure, adjusting for factual differences while preserving the legal essence. This mapping is the legal connection.

Formally: the legal connection $A_\mu$ encodes how Hohfeldian positions change under parallel transport through the case law. Moving along an edge $c_i \to c_j$ in the judicial complex, the connection specifies the transformation $g_{ij} \in G_{\mathfrak{H}}$ that maps the Hohfeldian structure of $c_i$ to the Hohfeldian structure of $c_j$.

### The Wilson Loop

**Definition (Legal Wilson Loop).** A *legal Wilson loop* $W(\gamma)$ is the holonomy of the legal connection around a closed path $\gamma$ in $\mathcal{K}$:

$$W(\gamma) = \mathcal{P} \exp\left( \oint_\gamma A_\mu \, dx^\mu \right)$$

where $A_\mu$ is the legal connection and $\mathcal{P}$ denotes path ordering.

In the discrete setting, this simplifies to the ordered product of gauge transformations along the edges of the cycle:

$$W(\gamma) = g_{01} \cdot g_{12} \cdot g_{23} \cdots g_{(m-1)0}$$

where $g_{ij}$ is the Hohfeldian transformation induced by traversing the edge from $c_i$ to $c_j$.

### What a Non-Trivial Wilson Loop Means

A non-trivial Wilson loop ($W(\gamma) \neq \mathbf{1}$) means that traversing a cycle of legal reasoning — applying a sequence of legal principles that returns to the same factual configuration — changes the Hohfeldian structure. You start with one configuration of rights and duties, follow a chain of precedents through the case law, and return to the same starting point with a *different* configuration.

This is a *legal inconsistency*: the system of precedents contains a hidden contradiction. The contradiction is hidden because each individual step in the chain is locally valid — each case correctly applies the precedent it cites. But the *global* effect of following the entire chain is contradictory: the Hohfeldian labels have been rotated or reflected by the non-trivial holonomy.

**Proposition (Wilson Loop Test for Consistency).** A body of case law is internally consistent if and only if all Wilson loops in the precedent-defined connection are trivial. Non-trivial Wilson loops identify specific circuits of legal reasoning that produce contradictions.

### Detecting Circuit Splits

Circuit splits — cases where different federal circuits reach opposite conclusions on the same legal question — are a common and important source of legal inconsistency. The Wilson loop formalism provides a precise tool for detecting and analyzing them.

A circuit split creates a non-trivial Wilson loop whenever there exists a path from Circuit A's case through a common precedent to Circuit B's case and back to Circuit A's case (through another path of shared precedent). If the Hohfeldian labels change around this loop, the split is a genuine inconsistency, not merely a difference in emphasis or dicta.

The Wilson loop also provides a *measure* of the inconsistency. The holonomy $W(\gamma)$ is an element of $G_{\mathfrak{H}}$. Its distance from the identity (in the group metric) quantifies how severe the inconsistency is. A holonomy of $r$ (a single correlative rotation) is a mild inconsistency — the cases disagree about which party's perspective controls. A holonomy of $s$ (a jural negation) is a severe inconsistency — the cases disagree about whether a legal relation exists at all.

---

> **RUNNING EXAMPLE — THE WILSON LOOP IN RIVERA'S CIRCUIT**
>
> *Rivera now computes the Wilson loop for the four Eighth Amendment cases. The cycle is:*
>
> *$\gamma = (c_1, c_2, c_3, c_4, c_1)$*
>
> *where $c_1$ is the 2019 case (ban constitutional), $c_2$ is the 2020 case (ban unconstitutional), $c_3$ is the 2021 case (ban constitutional if shelter available), and $c_4$ is the 2022 case (applied $c_3$'s rule but reached a result inconsistent with $c_2$).*
>
> ***Edge $c_1 \to c_2$:** Case 2 distinguishes Case 1 by reframing the issue from the city's liberty to the individual's right. Gauge transformation: $g_{12} = rs$ (correlative rotation composed with opposite, as analyzed above).*
>
> ***Edge $c_2 \to c_3$:** Case 3 synthesizes Cases 1 and 2 by adding a condition (shelter availability). It preserves the Hohfeldian structure of Case 2 but adds a conditional modifier. Gauge transformation: $g_{23} = e$ (identity — the Hohfeldian positions are preserved; only the boundary condition changes).*
>
> ***Edge $c_3 \to c_4$:** Case 4 applies Case 3's rule. Gauge transformation: $g_{34} = e$ (identity — direct application of the precedent).*
>
> ***Edge $c_4 \to c_1$:** Returning from Case 4's result to Case 1's starting point. Case 4's outcome (ban constitutional when shelter is available) is consistent with Case 1 (ban constitutional, period) only if the conditional is satisfied. But Case 4 actually applied the condition in a context where shelter was arguably not available, reaching a result that Case 2 would have prohibited. Gauge transformation: $g_{41} = s$ (jural negation — the loop reverses whether the individual has a right).*
>
> ***Wilson loop:** $W(\gamma) = g_{12} \cdot g_{23} \cdot g_{34} \cdot g_{41} = rs \cdot e \cdot e \cdot s = rs^2 = r$.*
>
> *The Wilson loop is **non-trivial**: $W(\gamma) = r \neq e$. The holonomy is a single correlative rotation — a moderate inconsistency. Traversing the full cycle of precedent changes which party (city or individual) the law regards as the primary position-holder.*
>
> *Rivera has now identified the specific inconsistency: the circuit's case law rotates the Hohfeldian perspective by one correlative step every time the full cycle of precedent is traversed. This is not a vague disagreement. It is a precise group-theoretic defect with a specific signature ($r \in D_4$) and a specific location (the cycle $c_1 \to c_2 \to c_3 \to c_4 \to c_1$).*
>
> *Armed with this diagnosis, Rivera can write an opinion that resolves the inconsistency. She does not need to "overrule" any case. She needs to identify which gauge choice is correct — which $D_4$ representative accurately describes the Eighth Amendment relation between the individual and the state — and hold that the circuit's law is the holding reached under that gauge choice. The other holdings, reached under different gauge choices, are reconciled by recognizing them as descriptions of the same underlying bond.*

---

## Gauge Theory on the Judicial Complex

### The Fiber Bundle Structure

The judicial complex $\mathcal{K}$ is the *base space*. At each vertex $c \in \mathcal{K}$, the Hohfeldian octad defines a *fiber* — the set of possible Hohfeldian configurations at that vertex. The gauge group $G_{\mathfrak{H}} = D_4 \rtimes D_4$ acts on each fiber, permuting the Hohfeldian labels.

A *section* of this fiber bundle is a choice of Hohfeldian labels at each vertex — a global assignment of rights, duties, liberties, and so on to all the parties in all the decided cases. A *connection* is a rule for how the Hohfeldian labels transform as you move from one vertex to another along an edge.

A connection is *flat* if all Wilson loops are trivial — if parallel-transporting the Hohfeldian labels around any cycle returns them to their starting values. A flat connection corresponds to a *consistent* body of case law: the Hohfeldian structure at any vertex can be determined unambiguously from the structure at any other vertex by following the connection along any path between them.

A connection with *curvature* (non-trivial Wilson loops) corresponds to an *inconsistent* body of case law: the Hohfeldian structure you compute at a vertex depends on *which path* you take from the reference vertex. This path-dependence is the formal definition of legal inconsistency.

### The Curvature Tensor

The curvature of the legal connection at a vertex $c \in \mathcal{K}$ is measured by the *curvature 2-form*:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu]$$

In the discrete setting, this becomes the Wilson loop around the smallest cycle containing the vertex. High curvature at a vertex means that the precedent in its neighborhood is inconsistent — small cycles around that vertex have non-trivial holonomy.

The non-abelian commutator $[A_\mu, A_\nu]$ is essential. It is present because the gauge group $G_{\mathfrak{H}}$ is non-abelian (the semi-direct product of two non-abelian groups). If the gauge group were abelian (like $U(1)$ in electromagnetism), the curvature would be linear in the connection. The non-abelian structure means that curvature can arise not just from the connection values but from their *non-commutation* — the fact that applying two gauge transformations in different orders produces different results.

Legally, this non-commutativity captures a real phenomenon: the order in which you apply legal tests matters. Standing before merits, jurisdiction before substance, prima facie case before burden-shifting — the legal system is full of ordered sequences where reversing the order changes the analysis. This ordering dependence is a direct manifestation of the non-abelian gauge structure.

### Gauge-Fixing and Legal Conventions

A *gauge choice* is a selection of one representative from each $G_{\mathfrak{H}}$ orbit — a decision to describe every legal relation from a specific perspective. Common gauge choices in legal practice include:

- **Plaintiff's perspective:** Describe every legal relation in terms of the plaintiff's positions (rights, liberties, powers, immunities). This is the default in complaint drafting.
- **Defendant's perspective:** Describe every relation in terms of the defendant's positions (duties, no-rights, liabilities, disabilities). This is the default in responsive pleading.
- **Neutral perspective:** Describe relations bilaterally, explicitly specifying both parties' positions. This is the default in judicial opinions.

These gauge choices are legally equivalent — the JBIP requires that the outcome be independent of which gauge is chosen. But in practice, gauge choice can influence analysis. A court that habitually adopts the plaintiff's gauge may be subtly biased toward finding rights; a court that habitually adopts the defendant's gauge may be subtly biased toward finding liberties (and corresponding no-rights for the plaintiff).

The framework makes this bias visible. By computing the Wilson loop under different gauge choices and verifying that it is gauge-invariant (as it must be, since the Wilson loop is gauge-invariant by construction), we can check whether a court's analysis depends on its perspective or whether it is genuinely perspective-independent.

## Conservation Laws from Gauge Symmetry

### The Symmetry-Conservation Correspondence

Each symmetry of the legal evaluation implies a conserved quantity. This is the discrete analogue of Noether's theorem:

| Symmetry | Legal Source | Conserved Quantity |
|----------|-------------|-------------------|
| Party-identity invariance | Equal Protection (14th Amdt.) | Liability-damages balance |
| Temporal translation | Prospectivity (Ex Post Facto Clause) | Reliance interest |
| Re-description invariance | Rule of Law | Outcome consistency |
| Hohfeldian correlative structure | Common-law structure | Entitlement balance |

### Liability-Damages Conservation

**Theorem (Liability-Damages Conservation).** In a closed bilateral tort dispute between plaintiff $A$ and defendant $B$, the total *liability-damages balance* is conserved:

$$L(A) + L(B) = 0$$

where $L(X)$ is the net liability of party $X$, defined as the signed sum of obligations imposed by adjudication. Every dollar of damages awarded to $A$ imposes exactly one dollar of liability on $B$; every Hohfeldian right created for $A$ imposes a correlative duty on $B$.

**Proof.** The proof follows from the correlative structure of Hohfeldian positions. In a closed bilateral system under a fixed legal framework $\mathcal{F}$:

1. Every right of $A$ is a correlative duty of $B$ (Hohfeld's first correlative pair).
2. Every liability of $B$ is a correlative power of $A$ (Hohfeld's second correlative pair).
3. Adjudication does not create Hohfeldian positions *ex nihilo*; it recognizes or assigns positions that already exist within $\mathcal{F}$.
4. Therefore, the net entitlement change $\Delta E(A) + \Delta E(B) = 0$ at every step of the proceeding.

For damages specifically: compensatory damages transfer wealth from $B$ to $A$, so $\Delta D(A) = -\Delta D(B)$. Punitive damages are an apparent exception, but they are grounded in a duty $B$ owes to the public interest (dimension $d_8$), extending the closed system to include the state as a third party; within the extended system $\{A, B, \text{State}\}$, the balance $L(A) + L(B) + L(\text{State}) = 0$ is restored. $\square$

### Scope and Limitations

Liability conservation holds within a fixed legal framework. Three operations break the conservation law:

1. **Legislation.** A new statute can create causes of action *ex nihilo*, generating rights without corresponding prior duties. This is a symmetry-breaking event — it changes the rules $\mathcal{F}$, not the dynamics within $\mathcal{F}$.

2. **Constitutional amendment.** Alters the topological constraint space $\mathcal{C}$ (Chapter 7), potentially creating or destroying entire classes of entitlements.

3. **Third-party intervention.** Adding a new party to the dispute breaks the closure condition. Conservation is restored by extending the subsystem to include all parties.

### Equal Protection as Gauge Invariance

**Theorem (Equal Protection as Invariance Constraint).** The Equal Protection Clause requires that the legal evaluation be invariant under transformations of protected-class attributes. In any closed bilateral dispute, this invariance implies the *entitlement balance*: the signed sum of Hohfeldian positions, weighted by the edge weights of $\mathcal{K}$, is invariant under adjudication.

**Proof sketch.** Let $\tau_g$ be a transformation that changes a party's race, gender, religion, or national origin while preserving all legally relevant facts. Equal protection requires $J_{\text{law}}(\tau_g(x)) = J_{\text{law}}(x)$.

In the judicial complex, this means: for any two vertices $c_i, c_j$ that differ only in the protected-class attributes of the parties, $J_{\text{law}}(c_i) = J_{\text{law}}(c_j)$. Combined with the Hohfeldian correlative structure, this forces the entitlement balance: whatever the court awards to one party, it must impose correlationally on the other. $\square$

### Due Process as Well-Definedness

**Theorem (Due Process as Quotient Regularity).** Due process is the requirement that the legal evaluation map $J_{\text{law}}$ be *well-defined on the quotient space* $\mathcal{J} / \mathcal{T}_{\text{irrelevant}}$:

$$\begin{array}{ccc}
\mathcal{J} & \xrightarrow{J_{\text{law}}} & \mathcal{O} \\
\downarrow \pi & & \nearrow \bar{J}_{\text{law}} \\
\mathcal{J} / \mathcal{T}_{\text{irrelevant}} & &
\end{array}$$

where $\pi$ is the quotient projection and $\mathcal{O}$ is the space of legal outcomes. Due process fails when $J_{\text{law}}$ does not factor through $\pi$ — when the outcome depends on which representative of the equivalence class was presented.

**Proof sketch.** If $J_{\text{law}}$ depends on the representative, then two descriptions of the same legal dispute can yield different outcomes. This is precisely what procedural due process prohibits: outcomes must depend on the merits (the equivalence class) rather than on irrelevant features of presentation (the specific representative). $\square$

## The Legal Bond Index

### Quantifying Gauge Violation

**Definition (Legal Bond Index).** The *Legal Bond Index* $\text{LBI} \in [0, 1]$ quantifies the degree to which a legal judgment system violates the JBIP:

$$\text{LBI} = \frac{1}{|S|} \sum_{s \in S} \| J_{\text{law}}(\tau(s)) - J_{\text{law}}(s) \|$$

where $S$ is a set of test cases and $\tau$ ranges over bond-preserving transformations (renaming parties, rephrasing without changing Hohfeldian structure, translating, etc.).

The LBI provides a *quantitative test for judicial consistency*: a court system with high LBI is treating equivalent cases differently. This is not a theoretical abstraction — it is an empirically measurable quantity that could be computed from existing case databases.

An LBI of 0 means perfect gauge invariance: the system produces identical outcomes for all gauge-equivalent descriptions. An LBI of 1 means maximal gauge violation: the outcomes are completely unrelated under gauge transformations. The empirically calibrated baseline from the moral domain is approximately 0.155; the legal baseline remains to be measured.

### Measuring the LBI in Practice

To compute the LBI for a given court or jurisdiction:

1. Collect a set $S$ of decided cases with known outcomes.
2. For each case $s \in S$, generate gauge-transformed versions: rename the parties, rephrase the legal arguments without changing their Hohfeldian content, translate (for multilingual jurisdictions).
3. Submit the transformed cases to the same court (or to an AI system modeling the court's behavior).
4. Measure the outcome differences.
5. Average the differences to compute the LBI.

Steps 1-2 can be automated. Step 3 is the bottleneck: submitting transformed cases to a real court requires actual litigation, which is impractical for large-scale measurement. For AI legal systems, however, the LBI is directly computable: generate transformed case descriptions, run them through the AI, and measure the output variance.

## The Non-Commutativity of Legal Operations

### Why Order Matters

The gauge group $G_{\mathfrak{H}} = D_4 \rtimes D_4$ is *non-abelian*: the order in which gauge transformations are applied matters. Concretely: applying the correlative swap and then the jural negation produces a different result than applying them in the reverse order. $rs \neq sr$ in $D_4$.

This non-commutativity has a direct legal interpretation: the order in which legal tests are applied changes the analysis. This is not a theoretical curiosity — it is one of the most important structural features of legal reasoning.

**Standing before merits.** A court must determine whether the plaintiff has standing (procedural question) before reaching the merits (substantive question). Reversing the order — deciding the merits first and then checking standing — is procedurally improper and can produce different outcomes. A plaintiff who would win on the merits might lack standing; a plaintiff who has standing might lose on the merits. The composition of these two evaluations is non-commutative.

**Jurisdiction before substance.** A court must establish subject-matter jurisdiction before exercising judicial power. A court without jurisdiction cannot render a valid judgment, no matter how correct its substantive analysis. The order is mandatory: jurisdiction first, substance second.

**Prima facie case before burden-shifting.** Under McDonnell Douglas, the plaintiff must establish a prima facie case before the burden shifts to the employer. If the burden shifted first (requiring the employer to justify the action before the plaintiff established a prima facie case), the analysis would be radically different — the employer's justification would be evaluated in a vacuum, without the contextual framework that the prima facie case provides.

Each of these ordering requirements corresponds to a non-commutative composition in the gauge group. The empirical evidence from the Geometric Ethics programme confirms this: 16,798 commutator measurements on normative frameworks demonstrate that the order of applying normative frameworks changes the outcome. The commutator $[U, D] = UDU^{-1}D^{-1} \neq e$ — the frameworks do not commute.

### The Physical Analogy

In physics, non-abelian gauge theories (like the SU(3) gauge theory of quantum chromodynamics) produce qualitatively different phenomena than abelian theories (like the U(1) gauge theory of electromagnetism). In particular, non-abelian theories exhibit *confinement* — the gauge bosons interact with each other, creating self-referential loops that confine the fundamental charges.

The legal analogue of confinement is *precedential lock-in*: a body of non-abelian precedent can create a self-reinforcing cage of case law from which it is extremely difficult to escape. Each case reinforces the others, and the non-commutativity of the legal operations means that the order in which you apply the precedents matters — you cannot simply "reverse" the chain of reasoning. Overruling one case does not unwind the effects of the cases that built on it, because the non-abelian multiplication means the composition of transformations is not simply reversible.

This is precisely the phenomenon that stare decisis produces in practice. A body of case law can become so internally reinforced that overruling any single case is insufficient to change the legal landscape — you must overrule a *connected set* of cases simultaneously, which is politically and institutionally costly. The non-abelian gauge structure provides the mathematical explanation for why precedential systems exhibit this lock-in phenomenon.

### The Commutator as a Measure of Order-Dependence

For any two gauge transformations $g, h \in G_{\mathfrak{H}}$, the *commutator* $[g, h] = ghg^{-1}h^{-1}$ measures the degree to which the order matters. If $[g, h] = e$ (the identity), the transformations commute and order does not matter. If $[g, h] \neq e$, the order matters, and the commutator tells you how much.

In the legal setting, the commutator of two legal operations — say, the standing test and the merits analysis — measures how much the outcome depends on which operation is performed first. A large commutator (far from the identity in the group metric) means the order is highly consequential. A small commutator (close to the identity) means the order has mild effects.

The non-commutativity of $G_{\mathfrak{H}}$ is not a deficiency of the framework. It is a *feature* — it captures a genuine structural property of legal reasoning that the logical formalization (deontic logic) misses entirely. Deontic logic does not naturally encode ordering requirements; the gauge-theoretic formalization does.

---

> **RUNNING EXAMPLE — RIVERA RESOLVES THE INCONSISTENCY**
>
> *Armed with the Wilson loop analysis, Rivera writes an opinion addressing the circuit inconsistency in the Eighth Amendment cases.*
>
> *Her opinion begins by identifying the gauge transformation that generated the inconsistency: Cases 1 and 2 adopted different $D_4$ representatives for the same underlying legal bond. Case 1 described the bond from the city's perspective (liberty to regulate), while Case 2 described it from the individual's perspective (right not to be punished). The different framings led to different outcomes — a gauge violation.*
>
> *Rivera's holding: the correct gauge choice for Eighth Amendment analysis is the individual's perspective. The Eighth Amendment is a constraint on governmental power — it protects individuals from cruel and unusual punishment. The natural gauge is therefore the individual's Hohfeldian position (right, or its absence), not the government's position (liberty, or its absence).*
>
> *Under this gauge choice, the analysis is:*
> *- **The individual has a right not to be punished for involuntary conduct** (Eighth Amendment).*
> *- **The city has a correlative duty not to impose such punishment** (correlative of the right).*
> *- **Whether the conduct is involuntary depends on the availability of alternatives** (the conditional from Case 3).*
> *- **If no shelter is available, sleeping in a park is involuntary, and the ban is unconstitutional** (application of the rule).*
>
> *This holding is gauge-invariant: you can re-describe it from the city's perspective (the city has a duty, whose correlative is the individual's right) and reach the same conclusion. The Wilson loop is now trivial: traversing the cycle of precedent returns to the same Hohfeldian configuration you started with.*
>
> *Rivera has not "overruled" any case. She has identified the gauge transformation that caused the inconsistency and fixed the gauge. Cases 1 and 4, which reached different conclusions under a different gauge choice, are reconciled — they are re-read as holdings about the city's duty rather than about the city's liberty, and under this re-reading, they are consistent with Cases 2 and 3.*

---

## Worked Example: Wilson Loop in a Contract Dispute

**Facts.** Three appellate cases in a circuit deal with the enforceability of arbitration clauses in consumer contracts:

- **Case A (2018):** An arbitration clause is enforceable because the consumer agreed to it. (Consumer has a no-right — no claim against the company regarding arbitration.)
- **Case B (2020):** An arbitration clause is unenforceable because the consumer lacked meaningful choice. (Consumer has a right to judicial access, which the clause impermissibly extinguishes.)
- **Case C (2022):** An arbitration clause is enforceable if the consumer was given a reasonable opportunity to reject it. (Conditional: consumer's Hohfeldian position depends on the adequacy of notice.)

**The Wilson Loop.** Consider the cycle $\gamma = (A, B, C, A)$:

**Edge $A \to B$:** Case B distinguishes Case A by finding that the consumer had no meaningful choice. This is a Hohfeldian relabeling: the consumer's position changes from no-right (Case A) to right (Case B). Gauge transformation: $g_{AB} = s$ (jural opposite — no-right $\to$ right).

**Edge $B \to C$:** Case C synthesizes by adding a condition. The consumer's position changes from unconditional right (Case B) to conditional right (Case C). Gauge transformation: $g_{BC} = e$ (identity — the Hohfeldian label is preserved; only a boundary condition is added).

**Edge $C \to A$:** Returning to Case A. If the consumer was given adequate notice (the condition is satisfied), Case C says the clause is enforceable — matching Case A. Gauge transformation: $g_{CA} = s$ (jural opposite — right $\to$ no-right, contingent on the condition).

**Holonomy:** $W(\gamma) = g_{AB} \cdot g_{BC} \cdot g_{CA} = s \cdot e \cdot s = s^2 = e$.

The Wilson loop is *trivial*: $W(\gamma) = e$. The body of case law is consistent. Cases A and B are not contradictory — they are different applications of the same conditional rule that Case C made explicit. The no-right (Case A) and the right (Case B) obtain in different factual circumstances (adequate notice vs. no meaningful choice), and these circumstances are precisely the condition that Case C articulated.

This example illustrates the power of the Wilson loop: it distinguishes *genuine* inconsistencies (non-trivial holonomy) from *apparent* inconsistencies that dissolve when the conditioning is made explicit (trivial holonomy).

## Chapter Summary

1. The full Hohfeldian octad (eight positions in two coupled squares) has the symmetry group $G_{\mathfrak{H}} = D_4 \rtimes_\varphi D_4$ — a semi-direct product of two dihedral groups.

2. The semi-direct product (not direct product) captures the essential legal coupling: second-order positions (power, immunity, liability, disability) *transform* first-order positions (right, duty, liberty, no-right).

3. Legal gauge transformations are re-descriptions that preserve Hohfeldian bond structure. The JBIP requires that legal evaluation be invariant under all such transformations.

4. Wilson loops detect hidden inconsistencies in case law. A non-trivial Wilson loop ($W(\gamma) \neq e$) identifies a specific cycle of legal reasoning that produces a contradictory Hohfeldian configuration.

5. The gauge structure implies conservation laws: liability-damages conservation in closed bilateral disputes, entitlement balance from equal protection, and outcome consistency from the rule of law.

6. The Legal Bond Index (LBI) quantifies gauge violation — how much a legal system's outcomes depend on legally irrelevant features of description.

---

## Technical Appendix

**Definition (Semi-Direct Product).** Given groups $N$ and $H$ and a homomorphism $\varphi: H \to \text{Aut}(N)$, the *semi-direct product* $N \rtimes_\varphi H$ is the set $N \times H$ with multiplication:

$$(n_1, h_1) \cdot (n_2, h_2) = (n_1 \cdot \varphi(h_1)(n_2), \; h_1 \cdot h_2)$$

When $\varphi$ is trivial, this reduces to the direct product $N \times H$.

**Theorem (Octahedral Gauge Group — Full Statement).** Let $D_4^{(1)} = \langle r_1, s_1 \mid r_1^4 = s_1^2 = e, \; s_1 r_1 s_1 = r_1^{-1} \rangle$ act on first-order positions and $D_4^{(2)} = \langle r_2, s_2 \mid r_2^4 = s_2^2 = e, \; s_2 r_2 s_2 = r_2^{-1} \rangle$ act on second-order positions. The coupling homomorphism $\varphi: D_4^{(2)} \to \text{Aut}(D_4^{(1)})$ maps $r_2 \mapsto \alpha$ where $\alpha(r_1) = r_1$, $\alpha(s_1) = s_1 r_1$ (the second-order correlative rotation twists the first-order reflection). Then $G_{\mathfrak{H}} = D_4^{(1)} \rtimes_\varphi D_4^{(2)}$ is a group of order 64.

**Definition (Legal Wilson Loop — Discrete).** For a directed cycle $\gamma = (c_0, c_1, \ldots, c_m, c_0)$ in $\mathcal{K}$, the Wilson loop is:

$$W(\gamma) = \prod_{i=0}^{m} g_{i, (i+1 \bmod m+1)}$$

where $g_{ij} \in G_{\mathfrak{H}}$ is the gauge transformation induced by the edge $c_i \to c_j$, determined by how the citing case relabels the Hohfeldian positions of the cited case. $W(\gamma) \in G_{\mathfrak{H}}$; it equals $e$ if and only if the cycle is consistent.

**Proposition (Gauge Invariance of the Wilson Loop).** The Wilson loop $W(\gamma)$ is invariant under gauge transformations at the vertices. That is, if we change the Hohfeldian labeling at each vertex by $h_i \in G_{\mathfrak{H}}$, the Wilson loop transforms by conjugation: $W(\gamma) \to h_0^{-1} W(\gamma) h_0$. Its conjugacy class (and in particular, whether it is trivial) is gauge-invariant.

**Proposition (Closed Subsystem Conservation).** In a closed legal subsystem $\mathcal{K}_S$ (fixed parties, fixed legal framework), the total signed Hohfeldian charge is conserved: $\sum_{X \in \text{parties}} Q(X) = 0$, where $Q(X) = \#\{\text{rights and liberties of } X\} - \#\{\text{duties and no-rights of } X\}$.

---

## Notes on Sources

The semi-direct product construction follows Lang (2002, *Algebra*, Ch. I) and Dummit and Foote (2004, *Abstract Algebra*, Ch. 5). Wilson loops in gauge theory are developed in Wilson (1974) and are standard material in Peskin and Schroeder (1995). The application of gauge theory to legal reasoning is original to the Algorithmic Jurisprudence framework. The Legal Bond Index extends the Bond Index of Bond (2026a, *Geometric Ethics*, Ch. 14). The connection between equal protection and gauge invariance extends Sunstein (1994) and Siegel (2004). The due process characterization as quotient regularity extends Fallon (2007). The non-commutativity of legal operations is empirically confirmed by Bond (2026a), with 16,798 commutator measurements demonstrating that the order of applying normative frameworks changes the outcome.

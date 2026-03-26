# Chapter 2: Hohfeld's Original Insight

> *"The greatest single achievement of analytical jurisprudence in the twentieth century was the demonstration that what lawyers loosely call 'a right' is in fact a complex bundle of distinct jural relations."*
> — Arthur Corbin, "Jural Relations and Their Classification" (1921)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera is reviewing a landlord-tenant dispute. Marcus Thompson, a tenant, claims his landlord, Victoria Chen, has violated his lease by entering his apartment without notice, changing the locks to the storage unit included in his lease, and raising his rent mid-term. Chen responds that she has the right to inspect her own property, that the storage unit was never part of the lease, and that the rent increase was authorized by a city ordinance.*
>
> *Rivera notices something: every time the parties say "right," they mean something different. Thompson's "right" to quiet enjoyment is a claim against Chen — it imposes a duty on her not to enter without notice. Chen's "right" to inspect her property is a liberty — the absence of a duty not to inspect. Thompson's "right" to the storage unit is a power to enforce the lease term. And the rent increase depends on whether Chen has a legal power to modify the lease terms, or whether Thompson holds an immunity against mid-term changes.*
>
> *Four different legal relations, all called "right." Rivera has spent twenty years disambiguating this word. She does not yet know that an analytical jurist named Wesley Newcomb Hohfeld solved this problem in 1913 — and that his solution, properly understood, is a piece of abstract algebra.*

---

## The Word That Means Four Things

Every first-year law student learns, painfully, that the word "right" is doing too much work.

When we say "you have a right to free speech," we mean something different from "you have a right to be paid for your labor," which means something different from "you have a right to make a will," which means something different from "you have a right not to be forced to testify against yourself." These are not four instances of the same relation. They are four fundamentally different jural relations that English happens to denote with the same word.

This ambiguity is not merely an academic nuisance. It is the source of some of the deepest confusions in legal reasoning. When a court says that a corporation has a "right" to free speech, is it saying that the corporation has a *claim* against the government (imposing a *duty* on the government not to restrict its speech)? Or is it saying that the corporation has a *liberty* to speak (the absence of a duty not to speak)? These are different assertions with different legal consequences, and the difference matters enormously for the scope of constitutional protection.

Wesley Newcomb Hohfeld, a professor at Yale Law School, published a pair of articles in 1913 and 1917 that cut through this confusion with a precision that still feels almost surgical. He identified not one but eight fundamental jural relations — four in the "first square" of primary relations, four in the "second square" of secondary relations — and he mapped the exact logical relationships among them.

What Hohfeld did not know, and what this chapter will demonstrate, is that his taxonomy is not merely a classification scheme. It is a *group-theoretic structure*. The four relations of the first square — right, duty, liberty, no-right — are related by exactly two operations (correlative swap and jural opposite) that satisfy exactly the relations of the dihedral group $D_4$. Hohfeld was doing group theory in 1913 without the vocabulary.

## Hohfeld's First Square: The Tetrad

### The Four Relations

Hohfeld's first insight was that every legal relation between two persons with respect to a single act can be described as exactly one of four positions. Let $A$ and $B$ be two persons, and let $\varphi$ be an act (say, entering an apartment). Then:

1. **Right (Claim).** $A$ has a *right* that $B$ do $\varphi$ (or refrain from $\varphi$). This means that $B$ is legally obligated — $B$ has a *duty* — with respect to $A$'s interest in $\varphi$. If Thompson has a right to quiet enjoyment, Chen has a correlative duty not to enter without notice.

2. **Duty.** $B$ has a *duty* to $A$ regarding $\varphi$. This is the correlative of $A$'s right. You cannot have a right without someone else having a duty, and you cannot have a duty without someone else having a right. They are two perspectives on a single legal bond.

3. **Liberty (Privilege).** $A$ has a *liberty* (Hohfeld called it a "privilege") to do $\varphi$ if and only if $A$ has *no duty* to refrain from $\varphi$. Chen's claimed "right" to inspect her property is, in Hohfeldian terms, a *liberty* — the absence of a duty not to inspect. A liberty is the opposite of a duty: if you have a duty not to do something, you do not have a liberty to do it, and vice versa.

4. **No-right.** $B$ has a *no-right* with respect to $A$'s doing $\varphi$ if $B$ has no claim against $A$ regarding $\varphi$. If Chen has a liberty to inspect, then Thompson has a no-right — he cannot demand that she refrain. No-right is the correlative of liberty, just as duty is the correlative of right.

These four positions exhaust the logical space. For any two persons $A$ and $B$ and any act $\varphi$, the legal relation is one of these four — or a combination of them across different acts.

### Correlatives and Opposites

Hohfeld identified two fundamental relationships among these four positions:

**Correlative pairs** link positions that are two perspectives on the same legal bond:
- Right (of $A$) $\longleftrightarrow$ Duty (of $B$)
- Liberty (of $A$) $\longleftrightarrow$ No-right (of $B$)

The correlative operation swaps the perspective from one party to the other. If you know $A$'s position, the correlative tells you $B$'s position, and vice versa. The bond is the fundamental unit; right and duty are two views of the same bond.

**Opposite (jural negation) pairs** link positions that negate each other within a single party's perspective:
- Right $\longleftrightarrow$ No-right
- Duty $\longleftrightarrow$ Liberty

If $A$ has a right regarding $\varphi$, then $A$ does not have a no-right regarding $\varphi$, and vice versa. If $B$ has a duty regarding $\varphi$, then $B$ does not have a liberty regarding $\varphi$, and vice versa. The opposite operation negates the normative valence.

These two relationships — correlative and opposite — completely determine the structure. Given any one of the four positions, you can derive the other three by applying correlative and opposite operations in sequence.

### The Table

Hohfeld presented these relationships in a table that has been reproduced in every jurisprudence textbook for over a century:

| Position | Correlative | Opposite |
|----------|-------------|----------|
| Right | Duty | No-right |
| Duty | Right | Liberty |
| Liberty | No-right | Duty |
| No-right | Liberty | Right |

Read the table this way: if $A$ has a *Right*, then $B$ has a correlative *Duty*, and the opposite of $A$'s Right (what $A$ would have instead, in the absence of the right) is a *No-right*. If $A$ has a *Liberty*, then $B$ has a correlative *No-right*, and the opposite of $A$'s Liberty is a *Duty* (if you don't have the liberty, you have the duty to refrain).

---

> **RUNNING EXAMPLE — HOHFELDIAN ANALYSIS OF THOMPSON v. CHEN**
>
> *Judge Rivera now has the vocabulary to disambiguate the dispute:*
>
> ***Quiet enjoyment.** Thompson has a **right** to quiet enjoyment. This means Chen has a correlative **duty** not to enter without notice. When Chen entered without notice, she breached this duty. The issue is not whether Chen has a "right" to inspect — it is whether Thompson's right to quiet enjoyment, created by the lease, trumps any liberty Chen might otherwise have.*
>
> ***Inspection.** Outside the lease, a property owner has a **liberty** to inspect — no duty prevents it. But the lease modifies the Hohfeldian structure: by granting Thompson a right to quiet enjoyment, the lease imposes a duty on Chen, converting her liberty into a duty-not-to-enter-without-notice. Chen's supposed "right" to inspect is extinguished by the lease — or more precisely, it was a liberty that has been overridden by a contractual duty.*
>
> ***Storage unit.** If the lease includes the storage unit, Thompson has a **right** to access it, and Chen has a correlative **duty** not to impede access. If the lease does not include it, Thompson has a **no-right** — no claim against Chen regarding the storage unit — and Chen has a correlative **liberty** to do as she pleases with it. The factual question (what does the lease say?) determines which Hohfeldian position obtains.*
>
> ***Rent increase.** The question is whether Chen has a **power** to modify the rent (a second-square relation — we will get to this shortly) or whether Thompson has an **immunity** against mid-term changes. If the lease fixes rent for the term, Thompson has an immunity, and Chen has a correlative disability — she lacks the power to change the rent regardless of what any ordinance says, unless the ordinance itself modifies the Hohfeldian structure.*
>
> *Rivera notices that the entire dispute reduces to identifying which Hohfeldian positions obtain and whether contractual or statutory sources have modified the default positions. Every "right" the parties invoke is resolvable into a specific tetrad position.*

---

## Why This Is Group Theory

Here is the claim that takes Hohfeld from legal taxonomy to mathematics: the two operations — correlative and opposite — together with the four positions they relate, form a group. Specifically, they form the dihedral group $D_4$, the symmetry group of the square.

### The Operations as Generators

Let us label the four positions of the first square and arrange them as the vertices of a square:

```
    Right ——— Duty
      |         |
      |         |
   No-right — Liberty
```

Now define two operations:

**Operation $r$ (correlative rotation):** This cycles the positions in a specific order. Starting from Right, the correlative gives Duty. Starting from Duty, the opposite gives Liberty. Starting from Liberty, the correlative gives No-right. Starting from No-right, the opposite gives Right. The cycle is:

$$r: \text{Right} \to \text{Duty} \to \text{Liberty} \to \text{No-right} \to \text{Right}$$

This is a 90-degree rotation of the square. It has order 4: applying $r$ four times returns every position to itself. $r^4 = e$, where $e$ is the identity operation (do nothing).

**Operation $s$ (jural negation/reflection):** This swaps each position with its opposite:

$$s: \text{Right} \leftrightarrow \text{No-right}, \quad \text{Duty} \leftrightarrow \text{Liberty}$$

This is a reflection of the square across a diagonal. It has order 2: applying $s$ twice returns every position to itself. $s^2 = e$.

### The Dihedral Relations

The key algebraic fact is that $r$ and $s$ satisfy the *dihedral relation*:

$$srs = r^{-1}$$

This says: if you first negate ($s$), then rotate ($r$), then negate again ($s$), the result is the *reverse* rotation ($r^{-1}$). Let us verify this concretely.

Start with Right. Apply $s$: Right $\to$ No-right. Apply $r$: No-right $\to$ Right. Apply $s$: Right $\to$ No-right. So $srs(\text{Right}) = \text{No-right}$.

Now compute $r^{-1}(\text{Right})$: the reverse rotation takes Right $\to$ No-right.

The results agree. The reader can verify the relation on all four positions.

The three relations — $r^4 = e$, $s^2 = e$, $srs = r^{-1}$ — are the *defining presentation* of the dihedral group $D_4$:

$$D_4 = \langle r, s \mid r^4 = s^2 = e, \; srs = r^{-1} \rangle$$

This group has exactly 8 elements: $\{e, r, r^2, r^3, s, sr, sr^2, sr^3\}$. Each element corresponds to a distinct way of permuting the four Hohfeldian positions while preserving their relational structure.

### What the Group Elements Mean Legally

Each of the 8 elements of $D_4$ corresponds to a legal operation — a way of re-describing a legal situation that preserves the underlying bond structure:

| Group Element | Operation | Legal Meaning |
|---------------|-----------|---------------|
| $e$ | Identity | Describe the situation as-is |
| $r$ | Correlative rotation | Shift perspective by one position (right-holder $\to$ duty-bearer) |
| $r^2$ | Double rotation | Shift by two positions (right $\to$ liberty, duty $\to$ no-right) |
| $r^3$ | Triple rotation | Shift by three positions (inverse of single correlative) |
| $s$ | Jural negation | Swap each position with its opposite |
| $sr$ | Negation then rotation | Combine perspective shift with normative inversion |
| $sr^2$ | Negation then double rotation | Swap correlative pairs |
| $sr^3$ | Negation then triple rotation | Combined operation |

The crucial point: *all eight operations preserve the legal bond structure*. If two parties are in a right-duty relationship, applying any element of $D_4$ produces a valid re-description of the same underlying legal relationship. The bond is invariant; only the labeling changes.

This is precisely what physicists call a *gauge symmetry*: a transformation that changes the description without changing the physics. In the legal case, $D_4$ transformations change the Hohfeldian labeling without changing the legal substance.

### Why $D_4$ and Not Some Other Group

One might ask: why the dihedral group? Why not the cyclic group $C_4$ (rotations only, no reflections)? Why not the symmetric group $S_4$ (all permutations of four elements)?

The answer is that the *structure* of Hohfeld's relations constrains the symmetry group. Not every permutation of the four positions preserves the correlative-opposite structure. A permutation that sends Right to Liberty, for instance, would map a correlative pair (Right-Duty) to a non-correlative pair (Liberty-?), breaking the relational structure unless it simultaneously performs a consistent remapping of all positions.

The dihedral group $D_4$ is *exactly* the group of permutations that preserves the incidence structure of the square — the group of symmetries of a square with labeled vertices. Since Hohfeld's correlative and opposite relations define a square (correlatives are adjacent, opposites are diagonal), $D_4$ is the unique maximal symmetry group that preserves this structure.

This is not an analogy. Hohfeld's four relations, connected by correlative and opposite relationships, *are* the vertices of a square. The symmetry group of that square *is* $D_4$. The identification is exact.

## Hohfeld's Second Square: The Power Tetrad

### The Four Second-Order Relations

Hohfeld's first square captures *first-order* legal relations — relations about acts. "A has a right that B perform $\varphi$" is about an act $\varphi$. But law also involves *second-order* relations — relations about legal relations themselves. The power to *create* a right, the immunity from having one's rights *altered*, the liability to having one's position *changed* — these are relations whose objects are not acts but legal positions.

Hohfeld identified a second square of four positions:

5. **Power.** $A$ has a *power* to change $B$'s legal position. A legislature has the power to create new duties (by enacting statutes). A contracting party has the power to create mutual rights and duties (by entering a contract). A judge has the power to determine which rights and duties exist (by adjudicating).

6. **Liability.** $B$ has a *liability* to having their legal position changed by $A$. Liability here is not the tort concept — it is the Hohfeldian concept of being subject to another's power. If a legislature has the power to impose a new tax, every citizen has a correlative liability to the tax.

7. **Immunity.** $A$ has an *immunity* if no other party has the power to change $A$'s legal position in a particular respect. Constitutional rights are often immunities: the First Amendment gives speakers an immunity against legislative power to restrict speech (within established limits). An immunity is to a power what a liberty is to a duty — the absence of the correlative constraint.

8. **Disability.** $B$ has a *disability* if $B$ lacks the power to change $A$'s legal position. If $A$ has a constitutional immunity, the legislature has a correlative disability — it simply cannot enact a law that alters $A$'s protected position, regardless of political will.

### The Second Square's Internal Structure

The second square has the same correlative-opposite structure as the first:

| Position | Correlative | Opposite |
|----------|-------------|----------|
| Power | Liability | Disability |
| Liability | Power | Immunity |
| Immunity | Disability | Liability |
| Disability | Immunity | Power |

The parallels are exact:
- Power $\leftrightarrow$ Liability (correlatives): $A$'s power to change $B$'s position means $B$ is liable to having it changed.
- Immunity $\leftrightarrow$ Disability (correlatives): $A$'s immunity from change means the other party is disabled from making that change.
- Power $\leftrightarrow$ Disability (opposites): if you have the power, you do not have a disability (and vice versa).
- Liability $\leftrightarrow$ Immunity (opposites): if you are liable, you are not immune (and vice versa).

The second square is therefore also a $D_4$ structure. The same two operations — correlative rotation and jural negation — generate the same 8-element group acting on the four second-order positions.

### The Coupling Between Squares

The two squares are not independent. Second-order positions *act on* first-order positions:

- Exercising a **power** creates, modifies, or destroys first-order positions. When a legislature exercises its power to enact a statute, it creates new rights and duties.
- Holding an **immunity** prevents another party's power from altering one's first-order positions. The First Amendment immunity means that Congress's legislative power *cannot* create a duty to refrain from speech.
- A **liability** means one's first-order positions are subject to alteration. A citizen's liability to taxation means the legislature can impose new duties (to pay taxes) that alter the citizen's financial rights.
- A **disability** means the inability to alter another's first-order positions. A state legislature's disability under the Supremacy Clause means it cannot create state-law duties that conflict with federal rights.

This coupling is the crucial structural feature that distinguishes the legal domain from the moral domain treated in *Geometric Ethics*. In ethical analysis, we typically work with first-order positions only — rights, duties, liberties, no-rights — because the ethical evaluator does not usually exercise second-order legal powers. In law, second-order positions are essential: they govern how the legal system *changes itself*.

---

> **RUNNING EXAMPLE — SECOND-SQUARE ANALYSIS OF THOMPSON v. CHEN**
>
> *Judge Rivera now turns to the rent increase. The question is not about first-order relations (who has what right or duty) but about second-order relations (who has the power to change the first-order structure).*
>
> *The lease fixes rent at $2,400 per month for 24 months. Chen claims that a new city ordinance authorizes landlords to increase rent annually by up to 5%. The question is: does the ordinance give Chen a **power** to increase the rent, overriding the lease's grant of **immunity** to Thompson?*
>
> *The analysis proceeds through second-order Hohfeldian positions:*
>
> *1. **The lease creates an immunity.** By fixing the rent for the term, the lease grants Thompson an immunity against rent changes — and imposes a correlative disability on Chen. Chen lacks the power to increase the rent unilaterally, regardless of her wishes.*
>
> *2. **The ordinance creates a power.** The city ordinance purports to grant landlords a power to increase rent by up to 5% annually. This would convert Chen's disability into a power, and Thompson's immunity into a liability.*
>
> *3. **The conflict is second-order.** The dispute is not about whether Thompson owes $2,400 or $2,520. It is about whether the ordinance has the **power** to modify the Hohfeldian structure created by the lease. This is a second-order question — a question about the power to create powers.*
>
> *4. **Resolution requires third-order analysis.** Does the city have the power (via its police power) to enact an ordinance that modifies private lease immunities? Does the Contracts Clause of the federal Constitution grant Thompson a constitutional immunity against retroactive impairment of contract rights? These are questions about the boundaries of governmental power — the highest level of Hohfeldian analysis.*
>
> *Rivera sees the architecture: the dispute is not flat. It has layers. First-order relations (rights and duties under the lease), second-order relations (powers and immunities regarding lease modification), and third-order relations (constitutional constraints on governmental power to modify private legal structures). Each layer has the same four-position structure. Each layer is governed by the same correlative-opposite symmetry.*

---

## The Symmetry That Hohfeld Discovered

### Why "Discovered" Rather Than "Invented"

There is a persistent debate in the philosophy of mathematics about whether mathematical structures are discovered or invented. Do we find the integers in nature, or do we construct them for our purposes?

In the case of Hohfeld's tetrad, the answer is unambiguous: Hohfeld *discovered* an algebraic structure that was already present in legal reasoning. He did not propose a new way to organize legal concepts. He identified a structure that working lawyers and judges already relied upon, implicitly, every time they reasoned about legal relations — and he made it explicit.

The evidence for this is that Hohfeld's taxonomy *works*. A century after its publication, it remains the standard analytical framework for decomposing legal relations. No one has found a legal relation that does not fit one of the eight positions. No one has found a correlative or opposite relationship that Hohfeld got wrong. The structure has survived every challenge because it captures something real — the symmetry structure of legal relations.

What Hohfeld did not do — what he could not have done in 1913, when abstract algebra was still in its infancy — was identify this structure as a *group*. The concept of the dihedral group $D_4$ existed in the mathematical literature (it was well-known from studies of regular polygons), but the idea that a legal taxonomy could be an instance of an algebraic group would have seemed bizarre. Mathematics was about numbers and shapes. Law was about rights and obligations. The two domains had no visible connection.

A century later, we can see what Hohfeld could not: his four positions, his correlative operation, and his opposite operation are not merely a useful taxonomy. They are the generators and relations of a specific finite group, and that group has properties — closure, associativity, identity, inverses — that constrain legal reasoning in ways that Hohfeld intuited but could not formalize.

### The Geometric Interpretation

Consider the first square arranged as a square in the plane, with the four Hohfeldian positions at the vertices:

```
         Right ———[correlative]——— Duty
           |                         |
       [opposite]               [opposite]
           |                         |
        No-right —[correlative]— Liberty
```

The correlative operation maps opposite edges (Right $\to$ Duty, No-right $\to$ Liberty). The opposite operation maps diagonals (Right $\to$ No-right, Duty $\to$ Liberty). Together, they generate all eight symmetries of this square: four rotations (by 0, 90, 180, and 270 degrees) and four reflections (across the two diagonals and the two midline axes).

Each symmetry of the square is a legal transformation:
- **0-degree rotation (identity):** No change of perspective.
- **90-degree rotation (correlative):** View from the other party's perspective.
- **180-degree rotation:** View from the diametrically opposite position.
- **270-degree rotation (inverse correlative):** The inverse of the correlative shift.
- **Horizontal reflection (opposite):** Negate the normative valence.
- **Vertical reflection:** Negate and swap.
- **Diagonal reflections:** Combined operations.

This is the dihedral group $D_4$ acting on the vertices of a square. The legal content of the group action is this: *every symmetry of the Hohfeldian square is a legally meaningful operation*, and *every legally meaningful operation on the four positions is a symmetry of the square*. The correspondence is bijective.

### The Invariance Principle

The deepest consequence of the group structure is an *invariance principle*: legal analysis should not depend on which element of the $D_4$ orbit you start from. If two cases have the same Hohfeldian bond structure but are described from different positions within the $D_4$ orbit (one from the right-holder's perspective, the other from the duty-bearer's perspective), the legal analysis should reach the same conclusion.

This is what we will call the *Judicial Bond Invariance Principle* (JBIP): legal evaluation must be invariant under transformations that preserve Hohfeldian bond structure.

$$J_{\text{law}}(g \cdot x) = J_{\text{law}}(x) \quad \forall \; g \in D_4$$

A court that reaches different conclusions depending on whether a dispute is framed as "the plaintiff has a right" versus "the defendant has a duty" is making a *gauge error* — its analysis depends on the choice of description rather than on the underlying legal reality. The $D_4$ symmetry makes this error detectable and, in principle, correctable.

## A Century of Implicit Group Theory

### Corbin and the Yale School

Arthur Corbin, Hohfeld's colleague at Yale, immediately recognized the power of the taxonomy and spent decades extending it. Corbin's treatise on contracts — still the standard reference — systematically applies Hohfeldian analysis to classify contractual relations. When Corbin writes that a contractual promise creates a "right in the promisee and a correlative duty in the promisor," he is applying the correlative operation of $D_4$.

But neither Corbin nor any subsequent jurisprudential scholar identified the algebraic structure. The legal literature treats Hohfeld's correlatives and opposites as *logical relations* — as implications or biconditionals in a deontic logic. They are discussed in the language of "if A has a right, then B has a duty" — the language of propositions and entailments.

This is correct but incomplete. Logical relations tell you what *follows from what*. Group-theoretic relations tell you what *transformations preserve what*. The $D_4$ structure tells us not merely that right and duty are correlative (a logical fact) but that the entire legal evaluation must be invariant under the correlative swap (a symmetry constraint). The logical formalization captures the relations; the algebraic formalization captures the invariance.

### Deontic Logic and Its Limitations

Formal deontic logic — the logic of obligation, permission, and prohibition — has been the standard framework for formalizing normative reasoning since von Wright's pioneering work in 1951. Deontic logicians have formalized Hohfeldian relations as modal operators: "A has a right that B do $\varphi$" becomes $O_B\varphi$ (B is obligated to do $\varphi$), and "A has a liberty to do $\varphi$" becomes $\neg O_A \neg \varphi$ (A is not obligated to refrain from $\varphi$).

This formalization is technically adequate — it captures the truth conditions. But it misses the *geometric* structure. In deontic logic, the correlative relationship between right and duty is an axiom: $R_A\varphi \leftrightarrow O_B\varphi$. In the group-theoretic formalization, it is a *generator*: the correlative swap $r$ is one of the two generators of $D_4$, and its properties (order 4, conjugation by $s$ yields $r^{-1}$) determine the entire structure.

The practical difference emerges when we ask about *consistency*. In deontic logic, consistency means the absence of logical contradiction: $O\varphi \wedge O\neg\varphi$ is inconsistent. In the geometric formalization, consistency means the triviality of Wilson loops: traversing a cycle of legal reasoning and returning to the starting position must not change the Hohfeldian labels. This is a *stronger* requirement. A body of law can be deontic-logically consistent (no outright contradictions) while still having non-trivial Wilson loops (subtle inconsistencies detectable only by following a chain of precedents around a full cycle). The group structure detects what the logic misses.

### International Convergence

Perhaps the most striking evidence that Hohfeld discovered a real structure rather than inventing a convenient taxonomy is the fact that every legal tradition that has independently analyzed the structure of legal relations has converged on essentially the same set of positions.

Civil law systems, which derive from Roman law rather than English common law, distinguish between *Anspruch* (claim/right), *Pflicht* (duty), *Erlaubnis* (permission/liberty), and the absence of claim (*kein Anspruch* / no-right). The correlative and opposite relationships are the same, even though the terminology differs and the intellectual history is independent.

Islamic jurisprudence (*fiqh*) classifies legal relations into *wajib* (obligatory/duty), *haram* (forbidden/no-liberty), *mubah* (permissible/liberty), *mandub* (recommended), and *makruh* (discouraged). The core tetrad — obligation, prohibition, permission, and the absence of obligation — maps directly onto Hohfeld's first square, even though the Islamic system adds gradations (recommended and discouraged) that Hohfeld's binary framework does not capture.

This cross-traditional convergence is what we would expect if the Hohfeldian positions capture the *symmetry group* of legal relations — a mathematical structure that is invariant under changes of legal tradition, language, and culture. The empirical evidence from the Geometric Ethics programme confirms this: the dimensional structure of normative evaluation is topologically stable across 11 languages and 3,000 years of texts. The Hohfeldian positions are not an artifact of the common-law tradition. They are a structural feature of normative reasoning itself.

## The Full Octad

### Combining the Two Squares

Hohfeld's complete system has eight positions — four in the first square and four in the second:

| First Square | Second Square |
|--------------|---------------|
| Right | Power |
| Duty | Liability |
| Liberty | Immunity |
| No-right | Disability |

The two squares are not parallel structures that happen to share the same pattern. They are *coupled*: second-order positions act on first-order positions. Exercising a power creates, modifies, or destroys rights and duties. Holding an immunity prevents another's power from altering one's rights and duties.

This coupling has a precise algebraic description, which Chapter 5 will develop in full. Each square has its own $D_4$ symmetry, but the two symmetries are not independent. The second $D_4$ acts on the first through a homomorphism $\varphi: D_4 \to \text{Aut}(D_4)$, making the full symmetry group a *semi-direct product*:

$$G_{\mathfrak{H}} = D_4 \rtimes_\varphi D_4$$

The semi-direct product captures the asymmetric coupling: the second-order positions (power, immunity, liability, disability) *transform* the first-order positions (right, duty, liberty, no-right), but not vice versa. This is exactly the legal reality: a legislature's exercise of power changes citizens' rights and duties, but a citizen's rights and duties do not change the legislature's power (except through constitutional constraints, which are *third-order* Hohfeldian positions — immunities against the exercise of power).

We defer the full development to Chapter 5. For now, the essential point is that the octad is not merely "two tetrads" but a single algebraic structure with internal coupling.

### Why the Octad Matters for Law

In ethics — the domain of *Geometric Ethics* — the first square usually suffices. Ethical analysis asks: who has what rights and duties? Ethical evaluation does not typically involve the exercise of powers to *change* the rights-and-duties structure.

In law, the second square is essential. Every legal proceeding involves the exercise of second-order positions:

- **Legislation** is the exercise of *power* to create new first-order positions.
- **Adjudication** is the exercise of judicial *power* to determine which first-order positions obtain.
- **Contract formation** is the exercise of *power* (capacity to contract) to create mutual rights and duties.
- **Constitutional review** is the judicial determination of whether a legislature's *power* is limited by constitutional *immunities*.
- **Delegation** is the transfer of *power* from one entity to another (e.g., Congress delegating regulatory authority to an agency).
- **Waiver** is the voluntary relinquishment of an *immunity* or *right*, converting it to a *liability* or *no-right*.

Without the second square, legal analysis cannot account for how the legal system *changes itself*. And since the central questions of law — what can the legislature do? what can the court do? what rights cannot be taken away? — are all second-order questions, the full octad is indispensable.

## What Hohfeld Got Right

### The Minimality of the Taxonomy

Hohfeld's taxonomy is *minimal*: every position is necessary, and none is redundant. You cannot derive Right from the other three positions, or eliminate Duty as a mere restatement of Right. Each position captures a distinct legal relation, and the four positions (in each square) exhaust the logical space.

This minimality is a direct consequence of the group structure. The four positions are the vertices of the square, and the square is the minimal regular polygon that supports the $D_4$ group. Three positions would give a triangle, with symmetry group $D_3$ (six elements) — which does not have the right structure (there is no operation that has order 4 on three elements). Five positions would give a pentagon with symmetry group $D_5$ (ten elements) — which has no subgroup isomorphic to $D_4$. Four positions is the unique choice that yields the $D_4$ structure.

In other words: Hohfeld found exactly the right number of positions because legal relations have exactly the symmetry structure of a square. The number four is not arbitrary — it is forced by the mathematics.

### The Bilateral Structure

Hohfeld insisted that every jural relation is *bilateral*: it holds between two determinate persons with respect to a determinate act. There is no such thing as a "right" in the abstract — only a right of $A$ against $B$ regarding $\varphi$.

This insistence on bilateral specification is, in group-theoretic terms, the insistence that the gauge group acts on *bonds*, not on isolated positions. A bond is a pair $(A, B, \varphi)$ together with a Hohfeldian label. The $D_4$ gauge group acts on the label, permuting the positions while preserving the bond. But the bond must be specified — you must know who $A$ is, who $B$ is, and what $\varphi$ is — before the group action is defined.

This is precisely the structure of a *gauge theory*: the gauge group acts on the fibers (the Hohfeldian labels) at each point of the base space (the bilateral bonds). The base space is the space of $(A, B, \varphi)$ triples; the fiber at each point is the set of Hohfeldian positions; and the gauge group $D_4$ acts on the fibers. Chapter 5 will develop this gauge-theoretic interpretation in full.

### The Priority of Structure Over Label

Perhaps Hohfeld's deepest insight was that the *structure* of legal relations — the pattern of correlatives and opposites — is more fundamental than the *labels*. It does not matter whether we call the positions "right, duty, liberty, no-right" or "claim, obligation, privilege, absence-of-claim" or use any other set of names. What matters is that there are four positions, that they are connected by two operations (correlative swap and jural negation), and that these operations satisfy the dihedral relations.

This is the insight that the $D_4$ group structure is *invariant under relabeling*. The abstract group $D_4$ does not care what we call its elements. It is defined by its multiplication table — the pattern of how elements combine — not by the names attached to the elements. Hohfeld's taxonomy succeeds because it captures this abstract structure, not because the English words "right," "duty," "liberty," and "no-right" have any magical properties.

This structural invariance is what makes Hohfeldian analysis portable across legal traditions and languages. The German, Arabic, and Chinese terms for the four positions are different words with different etymologies, but the correlative-opposite structure they satisfy is the same $D_4$ group. The structure travels; the labels do not.

---

> **RUNNING EXAMPLE — RESOLUTION OF THOMPSON v. CHEN**
>
> *Judge Rivera issues her ruling. She does not use the words "dihedral group" or "gauge symmetry." But her analysis, stripped to its logical skeleton, is group-theoretic:*
>
> *1. **Quiet enjoyment: Thompson prevails.** The lease created a right in Thompson and a correlative duty in Chen. Chen breached the duty. This is a straightforward application of the correlative operation: if the right exists, the duty exists; if the duty is breached, the right is violated. Rivera awards damages for the unlawful entries.*
>
> *2. **Storage unit: Thompson prevails.** The lease includes the storage unit (factual finding based on the lease text). Therefore Thompson has a right to access, and Chen has a correlative duty not to impede. By changing the locks, Chen breached this duty. Rivera orders Chen to provide Thompson with a key.*
>
> *3. **Rent increase: Thompson prevails.** The lease grants Thompson an immunity against mid-term rent changes. The city ordinance purports to create a power in Chen, but the Contracts Clause limits the city's power to impair existing contractual obligations. The ordinance cannot retroactively convert Thompson's contractual immunity into a liability. (If Thompson's lease were up for renewal, the analysis would differ — the immunity exists only for the lease term.)*
>
> *Rivera's analysis has traversed the Hohfeldian structure systematically: identifying the positions, applying the correlative operation to determine the other party's position, checking whether second-order positions (powers, immunities) modify the first-order structure, and resolving conflicts between statutory and contractual sources. At no point did she confuse "right" with "liberty" or "power" with "right." The taxonomy kept her reasoning clean.*
>
> *And the taxonomy's internal consistency — the fact that every correlative operation is reversible, that opposites are genuinely exhaustive, that the operations compose consistently — is not an accident. It is the algebraic closure of $D_4$.*

---

## Worked Example: The Neighbor's Fence

To consolidate the Hohfeldian framework, consider a simple property dispute analyzed through all four first-square positions.

**Facts.** Alice and Bob are neighbors. Alice wants to build a fence on the property line. Bob objects, claiming the fence would block his view.

**Hohfeldian Analysis.**

**Step 1: Identify the relevant act.** $\varphi$ = "Alice builds a fence on the property line."

**Step 2: Determine Alice's position.**
Under standard property law, Alice has a *liberty* to build on her own property. She has no duty to refrain from building. A liberty is the *opposite* of a duty: $\text{Liberty} = \text{opposite}(\text{Duty})$.

**Step 3: Apply the correlative.** Alice's liberty correlates with Bob's *no-right*. Bob has no claim against Alice regarding the fence. He cannot demand that she refrain. $\text{No-right} = \text{correlative}(\text{Liberty})$.

**Step 4: Check for modifications.**
- Does a zoning ordinance create a *duty* for Alice (e.g., fence height limits)? If so, Alice's liberty is converted to a duty, and Bob's no-right is converted to a right. The ordinance exercises a governmental *power* to modify the Hohfeldian structure.
- Does an easement exist? If Bob has a view easement, then Bob has a *right* to the view, and Alice has a correlative *duty* not to obstruct it. The easement modifies the default position.
- Does a homeowners' association covenant apply? If so, the covenant may grant the HOA a *power* to regulate fences, and both Alice and Bob have *liabilities* to the HOA's decisions.

**Step 5: Compose the analysis.**
If no modifications apply: Alice has a liberty, Bob has a no-right, and the fence may be built. If a height ordinance applies: Alice has a conditional liberty (she may build, but only within the height limit), and Bob has a partial right (he can demand compliance with the ordinance but cannot prevent the fence entirely). If a view easement exists: Bob has a right, Alice has a duty, and the fence cannot be built.

The analysis is purely structural. The $D_4$ group ensures that it is internally consistent: every position determination is reversible (applying the correlative twice returns to the original position), every opposite is genuinely exclusive (you cannot simultaneously have a right and a no-right regarding the same act), and the operations compose correctly.

## What Hohfeld Could Not See

### The Absence of the Mathematical Vocabulary

Hohfeld published in 1913 and died in 1918, at the age of 38. Abstract algebra, in anything like its modern form, did not exist. The first edition of van der Waerden's *Moderne Algebra* — the book that established abstract algebra as a discipline — appeared in 1930, twelve years after Hohfeld's death. The concept of a "group" was known (it dates to Galois in the 1830s), but the dihedral groups were studied primarily by geometers interested in the symmetries of regular polygons, not by legal scholars.

Hohfeld could not have known that his taxonomy was an instance of $D_4$, because the conceptual apparatus for recognizing it did not yet exist. He had the four positions, the two operations, and the table of relationships — everything needed to *define* the group — but not the mathematical language to identify what he had defined.

This is not unusual in the history of ideas. Mendel's genetic experiments (1866) established the laws of inheritance decades before the molecular mechanism (DNA) was discovered. Darwin's theory of natural selection (1859) preceded any understanding of the genetic basis for variation. In each case, the *structure* was discovered before the *formalism* that explained it. Hohfeld's case is analogous: he discovered the algebraic structure of legal relations before algebra had the vocabulary to describe it.

### The Missing Conservation Laws

A group symmetry implies conservation laws. This is the content of Noether's theorem (1918 — the same year Hohfeld died). If the $D_4$ symmetry of legal relations is genuine, it should imply conserved quantities in legal reasoning.

Hohfeld glimpsed this. His insistence that right and duty are "correlative" — that you cannot have one without the other — is a conservation principle in embryonic form: in a bilateral legal relation, the total "entitlement" is conserved. Creating a right for $A$ necessarily creates a duty for $B$; the net change in the legal system is zero.

But Hohfeld did not generalize this to a formal conservation law, and the legal literature has not done so either. The Liability-Damages Conservation theorem — that in a closed bilateral dispute, the signed sum of obligations is conserved — is a direct consequence of the $D_4$ correlative structure, but it took the geometric formalization to derive it. Chapter 5 develops the conservation laws in full, and Chapter 9 extends them to the dynamics of precedent.

### The Missing Inconsistency Detection

The most practically important consequence of the $D_4$ structure is Wilson loop detection: the ability to identify *hidden inconsistencies* in a body of law by computing the holonomy of the legal connection around closed cycles in the citation graph.

Hohfeld's framework, as traditionally applied, is *local*: it analyzes a single bilateral relation at a time. It answers the question "what is $A$'s position relative to $B$ regarding $\varphi$?" but does not answer the question "is the system of legal relations among many parties and many acts internally consistent?" The global question requires not just the group $D_4$ but the *gauge theory* built on $D_4$ — a connection, a notion of parallel transport, and a test for holonomy. This is the subject of Chapter 5.

## Chapter Summary

1. Hohfeld (1913, 1917) identified eight fundamental jural relations: four first-order (right, duty, liberty, no-right) and four second-order (power, liability, immunity, disability).

2. The four first-order positions are connected by two operations — correlative swap and jural negation (opposite) — that satisfy the defining relations of the dihedral group $D_4$: $r^4 = e$, $s^2 = e$, $srs = r^{-1}$.

3. This is not an analogy. The four Hohfeldian positions *are* the vertices of a square, and $D_4$ *is* the symmetry group of that square. The identification is exact.

4. The second square (power, liability, immunity, disability) has the same $D_4$ structure, coupled to the first square through a semi-direct product $D_4 \rtimes D_4$.

5. The group structure implies an invariance principle: legal evaluation must not depend on which $D_4$-orbit representative is used to describe the dispute. This is the Judicial Bond Invariance Principle (JBIP).

6. Hohfeld was doing group theory in 1913 without the vocabulary. The mathematical formalization explains *why* his taxonomy has been so durable (it captures the symmetry group of legal relations), extends it with new tools (Wilson loops, conservation laws, gauge invariance), and connects it to the broader programme of Geometric Law.

---

## Technical Appendix

**Definition (Dihedral Group $D_4$).** The dihedral group of order 8, denoted $D_4$, is the group of symmetries of a square. It has the presentation:

$$D_4 = \langle r, s \mid r^4 = e, \; s^2 = e, \; srs = r^{-1} \rangle$$

Its 8 elements are $\{e, r, r^2, r^3, s, sr, sr^2, sr^3\}$. The element $r$ is a rotation by 90 degrees; $s$ is a reflection. The group is non-abelian: $rs \neq sr$ in general.

**Theorem (Hohfeldian $D_4$).** The four first-order Hohfeldian positions $\{\text{Right}, \text{Duty}, \text{Liberty}, \text{No-right}\}$, together with the correlative operation $r$ (cycling Right $\to$ Duty $\to$ Liberty $\to$ No-right $\to$ Right) and the opposite operation $s$ (swapping Right $\leftrightarrow$ No-right and Duty $\leftrightarrow$ Liberty), form a $D_4$-set. The group action is faithful: distinct group elements produce distinct permutations of the positions.

*Proof.* Direct verification. The correlative cycle has order 4 ($r^4 = e$). The opposite swap has order 2 ($s^2 = e$). The conjugation $srs$ maps Right $\to$ No-right $\to$ Right $\to$ No-right (by applying $s$, then $r$, then $s$), which equals $r^{-1}$ = $r^3$ (the reverse cycle). All three defining relations are satisfied. Faithfulness: each of the 8 group elements produces a distinct permutation of the four positions (the reader can construct the full multiplication table). $\square$

**Definition (Hohfeldian Bond).** A *Hohfeldian bond* is a tuple $(A, B, \varphi, h)$ where $A$ and $B$ are legal persons, $\varphi$ is an act, and $h \in \{\text{Right}, \text{Duty}, \text{Liberty}, \text{No-right}\}$ (for first-order bonds) or $h \in \{\text{Power}, \text{Liability}, \text{Immunity}, \text{Disability}\}$ (for second-order bonds) is the Hohfeldian position of $A$ relative to $B$ with respect to $\varphi$.

**Proposition (Correlative Involution).** The correlative operation, restricted to the labels, is an involution of order 2 that swaps the two correlative pairs: Right $\leftrightarrow$ Duty, Liberty $\leftrightarrow$ No-right. Applied to a bond, it swaps $A$ and $B$ and replaces $h$ with its correlative: $(A, B, \varphi, \text{Right}) \mapsto (B, A, \varphi, \text{Duty})$.

**Proposition (Conservation of Bond Charge).** In a bilateral legal relation $(A, B, \varphi)$, the sum of Hohfeldian "charges" is zero. Assign charge $+1$ to Right and Liberty (entitlements of the holder), and charge $-1$ to Duty and No-right (constraints on the holder). Then for any bond, $\text{charge}(A) + \text{charge}(B) = 0$. This follows directly from the correlative structure: Right ($+1$ for $A$) correlates with Duty ($-1$ for $B$); Liberty ($+1$ for $A$) correlates with No-right ($-1$ for $B$).

---

## Notes on Sources

Hohfeld's original papers are "Some Fundamental Legal Conceptions as Applied in Judicial Reasoning" (1913, 1917), published in the *Yale Law Journal*. Corbin's extensions appear in "Jural Relations and Their Classification" (1921). The $D_4$ identification is original to Bond (*Geometric Ethics*, 2026, Chapter 12), where it was derived independently in the context of moral relations and then recognized as Hohfeld's structure. Cook (1919) and Kocourek (1920) provided early formalizations that anticipated some structural features without the algebraic framework. The cross-traditional convergence of jural categories is documented in Raz (1970) and Kramer, Simmonds, and Steiner (1998). The deontic logic tradition begins with von Wright (1951) and is surveyed comprehensively in McNamara (2014).

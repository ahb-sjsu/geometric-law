# Chapter 1: The Binary Verdict and the Scalar Sentence

> *"The life of the law has not been logic: it has been experience."*
> — Oliver Wendell Holmes Jr., *The Common Law* (1881)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Elena Rivera sits in her chambers at the federal courthouse in San Francisco. On her desk are three cases. The first is a civil rights challenge to a state voting restriction — a case where the same facts have produced opposite outcomes in different circuits. The second is a contract dispute where two statutes flatly contradict each other — federal law requires disclosure while state law prohibits it. The third is a criminal sentencing where the defendant's profile is statistically identical to defendants who received sentences ranging from 2 to 12 years in her district.*
>
> *Every case requires her to compress a multi-dimensional legal reality into a binary output: liable or not, constitutional or not, guilty or not. And then into a scalar: how many years, how many dollars, how much injunctive relief. She knows, with the precision of twenty years on the bench, that these compressions destroy information — that the structure of legal reasoning, which rights conflict and why, is exactly what the verdict discards.*
>
> *This book argues that the destruction is not inevitable. It provides the mathematical vocabulary for the structure that Judge Rivera intuits but the legal system cannot express.*

---

## The Shape of the Problem

Something has gone wrong with how we deliver justice — not the substance, but the *form*.

For its entire history, the legal system has operated with a tacit assumption: that legal evaluation, at the moment of decision, reduces to a binary verdict and a scalar sentence. Guilty or not guilty. Liable or not liable. Constitutional or unconstitutional. And then: how many years, how many dollars, how much remedy.

These outputs are always low-dimensional. A binary. A number. A ranking.

This book argues that the assumption is wrong. Not because legal decisions are *vague* or *subjective* or *too political to formalize*, but because they have *geometric structure* that a binary verdict and a scalar sentence cannot represent. Legal evaluation is not a point on a line. It is a location in a space — a space with eight dimensions, distances, curvatures, symmetries, and boundaries. When we flatten this structure into a verdict, we lose information. And the information we lose is precisely the information that matters most: which rights are at stake, where the constitutional boundaries lie, how precedent interacts with novel facts, and why the same case can produce different outcomes in different courts.

The mathematical name for this structure is *geometry*. And **Geometric Law** argues that legal reality has exactly this character.

Consider what a judge actually does when she decides a case. She does not simply compute a number. She navigates a landscape. She identifies the applicable legal doctrines. She determines which constitutional provisions constrain the outcome. She weighs the factual record against the requirements of the law. She assesses how binding precedent bears on the present facts. She evaluates the remedies available, the procedural posture of the case, the public interest implications, and the entitlement structure — which party has a right, which party bears a duty, whether those positions are modified by statute or contract or constitutional provision.

Each of these considerations is a *dimension* of the legal analysis. The judge must locate the case in all of these dimensions simultaneously, understand the relationships among them, and then produce an output — the verdict and the sentence — that the legal system can execute. The output is always low-dimensional: a binary (guilty/not guilty, liable/not liable, constitutional/unconstitutional) followed by a scalar (how many years, how many dollars, how much injunctive relief). The input is high-dimensional: the full structure of the legal analysis across all the relevant dimensions.

The compression from input to output is the central pathology of legal form. It is not a necessary feature of law. It is an artifact of a legal system designed before anyone had the mathematical vocabulary to describe the alternative.

## The Binary as Projection

To make the problem precise, consider the simplest case: a binary verdict. The legal system asks: guilty or not guilty? Liable or not liable?

In mathematical terms, a binary verdict is a function $\phi: \mathbb{R}^8 \to \{0, 1\}$. The domain is the eight-dimensional legal space (the eight dimensions developed formally in Chapter 3). The range is one bit: yes or no.

The Scalar Irrecoverability Theorem, developed in *Geometric Reasoning* (Bond, 2026c, Ch. 10) and restated in the Technical Appendix below, proves that no such function can be injective — that is, no binary classification can assign different outputs to every distinct input. This is not a contingent failure of any particular legal system. It is a mathematical necessity. Any function from $\mathbb{R}^8$ to $\{0, 1\}$ must map uncountably many distinct legal situations to the same verdict.

**[Conditional Theorem.]** The binary verdict partitions the eight-dimensional legal space into exactly two regions: the "guilty" region and the "not guilty" region. The boundary between them — the decision surface — is a seven-dimensional hypersurface. Every case that falls on one side of this surface receives the same verdict, regardless of where in that half-space it lies. A case that barely qualifies as guilty receives the same verdict as a case that is overwhelmingly guilty. A case that barely qualifies as not guilty receives the same verdict as a case where guilt was never plausible. The binary verdict discards all information about *where* within its half-space the case falls.

This is not an abstract concern. It manifests in practice as the disconnect between the verdict and the reasoning that produced it. When a jury returns "not guilty," the legal system does not know whether the jury believed the defendant was innocent, or believed the defendant was probably guilty but the prosecution failed to prove it beyond a reasonable doubt, or acquitted on emotional grounds, or compromised among jurors who disagreed about different elements of the offense. All of these distinct situations — which occupy different locations in the eight-dimensional legal space — are compressed into the same one-bit output.

The scalar sentence is marginally better: it replaces a binary with a real number. But a real number is still one-dimensional, and the legal space is eight-dimensional. The function $\psi: \mathbb{R}^8 \to \mathbb{R}$ (mapping legal situations to sentences) is still a compression from eight dimensions to one, and the Scalar Irrecoverability Theorem applies with equal force. The sentence tells you how many years. It does not tell you *which dimensions of the legal analysis drove the number*. Was the sentence high because the offense was severe (dimension $d_2$, factual nexus), or because the defendant had a long criminal history (dimension $d_6$, precedential constraint), or because the judge perceived the defendant as a public danger (dimension $d_8$, public interest), or because the judge's implicit racial bias inflated the assessment (a gauge violation, developed in Chapter 8)? The scalar sentence cannot distinguish among these causes. The structural information is destroyed in the compression.

## Three Failures of the Binary

The limitations of binary/scalar legal evaluation manifest in three domains where the stakes are highest.

### Failure 1: Sentencing Disparities

**[Legal Doctrine.]** The promise of equal justice under law is that equivalent defendants who commit equivalent crimes receive equivalent sentences. The reality is that sentencing varies dramatically by race, gender, geography, and the identity of the sentencing judge. The U.S. Sentencing Commission has documented these disparities exhaustively.

The numbers are stark. Black male defendants in the federal system receive sentences approximately 19.1% longer than white male defendants convicted of comparable offenses, after controlling for criminal history category, offense severity, and other legally relevant factors. Female defendants receive sentences approximately 63% shorter than male defendants for similar crimes. Sentences for identical offenses vary by as much as a factor of three across federal districts. The same defendant, facing the same charges, can expect a meaningfully different sentence depending on which judge draws the case.

These disparities are not new, and the legal system is aware of them. The U.S. Sentencing Guidelines were enacted in 1984 precisely to reduce sentencing variation by constraining judicial discretion within computed ranges. The effort was partially successful — disparities decreased — but the remaining variation is still large enough to constitute a systemic failure of equal treatment.

The geometric diagnosis: sentencing disparities are *gauge violations*. The legal system should be invariant under transformations that change the defendant's race, gender, or socioeconomic status while preserving the legally relevant facts. When it is not — when swapping the defendant's race changes the sentence — the system has violated a symmetry it claims to possess.

Chapter 8 develops this formally. The Legal Invariance Principle (LIP) requires that legal outcomes be unchanged under legally irrelevant transformations. The Legal Bond Index quantifies the violation magnitude. Sentencing disparities are not political controversies to be debated; they are measurable gauge anomalies on the judicial manifold.

The power of the geometric formulation is that it transforms a normative claim ("sentences should be equal") into a measurable quantity ("the gauge violation tensor $V_{ij}$ has magnitude 0.191 on the race-sentence component"). The normative claim can be debated indefinitely. The measurement can be verified or falsified.

### Failure 2: Circuit Splits

**[Legal Doctrine.]** The same legal question, applied to the same facts, can produce opposite outcomes depending on which federal circuit hears the case. Circuit splits are not rare — the Supreme Court's docket is dominated by resolving them. But the binary verdict provides no diagnostic: both circuits say "yes" or "no" without making explicit which dimensions of the legal analysis they weight differently.

Consider a concrete example. The question of whether the Fourth Amendment prohibits warrantless searches of cell phone location data was answered differently by different circuits before the Supreme Court resolved the split in *Carpenter v. United States* (2018). Some circuits held that cell site location information is not protected by the Fourth Amendment because the user has voluntarily conveyed it to a third party (the cell phone company). Other circuits held that the pervasive, detailed, and retrospective nature of cell location data makes it qualitatively different from the business records at issue in the third-party doctrine.

In the eight-dimensional legal framework, these circuits are not disagreeing about a binary question. They are weighting different dimensions differently. The circuits that applied the third-party doctrine weighted $d_4$ (statutory authority — the existing doctrine) heavily and weighted $d_5$ (constitutional conformity — the Fourth Amendment's protection of privacy) less. The circuits that distinguished cell location data weighted $d_5$ heavily — the constitutional dimension — and treated the existing third-party doctrine ($d_4$) as inapplicable to the new technological context.

A binary output cannot express this difference. Both sides said "yes" or "no." The *reason* for the disagreement — the dimensional weighting — was accessible only by reading the full opinions. The geometric framework makes the disagreement structurally visible: the circuits are located at different points on the eight-dimensional manifold, and the split is the distance between those points projected away by the binary verdict.

The geometric diagnosis: a circuit split is a *Wilson loop* — a closed cycle in the citation network that produces contradictory Hohfeldian labels when you traverse it completely. It is the legal analogue of a gauge anomaly in physics: local consistency at each step, but global inconsistency around the full loop. Chapter 5 develops the Wilson loop formalism and shows how to detect circuit splits algorithmically.

### Failure 3: Constitutional Ambiguity

**[Legal Doctrine.]** Is a law constitutional? The answer depends on which test the court applies (strict scrutiny, intermediate scrutiny, rational basis), which itself depends on how the court characterizes the right at stake, which depends on how the court reads the constitutional text, which is written in natural language with irreducible ambiguity.

The Second Amendment provides a vivid illustration. "A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed." Does this protect an individual right to own firearms, or a collective right connected to militia service? The Supreme Court answered this question in *District of Columbia v. Heller* (2008), but the answer came 217 years after ratification, and the five-four decision demonstrated that the textual analysis, even after two centuries of reflection, does not compel a unique answer.

The problem is not that the justices disagreed. The problem is that the legal system's method for resolving the disagreement — a binary vote among nine people — discards the structure of the disagreement. The majority opinion in *Heller* advanced a textual, historical, and structural argument for the individual-right reading. The dissent advanced a textual, historical, and structural argument for the militia-connected reading. Both arguments navigate the same constitutional space; they diverge on how to weight the textual, historical, and structural dimensions. The five-four vote collapses this rich structural disagreement into a single bit: individual right or militia right. The information about *where* the justices disagreed and *why* — the geometric structure of the constitutional analysis — is available only in the opinions, not in the holding.

The geometric diagnosis: constitutional review is a *topological* computation, not a textual one. A statute is constitutional if and only if its addition to the judicial complex preserves the path homology of the constitutional subcomplex — that is, if it does not create contradictions or destroy rights-paths that the Constitution guarantees. This is a machine-checkable criterion, not a matter of judicial temperament. Chapter 7 develops the formalism.

## The Deep Structure: Why Law Has Geometry

The claim that law has geometric structure requires justification beyond the three failures. Why should legal reasoning inhabit a structured space at all?

The answer comes from the nature of legal relations. A legal dispute does not exist in isolation. It exists in a web of relationships: between parties, between the dispute and applicable statutes, between the statutes and the constitution, between the current case and prior cases, between the legal outcome and the public interest. These relationships have *structure*. They constrain which outcomes are consistent with which inputs. They define which transformations preserve legal substance and which do not.

Structure of this kind — a space of states, with distances, symmetries, and constraints — is precisely what geometry studies. The legal manifold is not a metaphor imported from physics. It is the natural mathematical description of the structure that legal reasoning already possesses.

### The Eight Dimensions

**[Modeling Axiom.]** The legal space has eight dimensions. They are not chosen arbitrarily; they are derived from the structure of legal analysis itself, inheriting the scope-mode decomposition from the parent moral manifold developed in *Geometric Ethics* (Bond, 2026b, Ch. 5). The eight dimensions are:

1. **Entitlement structure** ($d_1$): Which party holds which Hohfeldian position — right, duty, liberty, no-right, power, liability, immunity, disability — with respect to which acts? This is the fundamental dimension of legal analysis, developed in Chapter 2.

2. **Factual nexus** ($d_2$): What happened? The factual record, as established by evidence, mapped to its legal significance. Two cases with identical facts can differ on every other dimension; two cases with different facts can be identical on every other dimension.

3. **Procedural posture** ($d_3$): What stage is the case at? A motion to dismiss evaluates different questions than a summary judgment motion, which evaluates different questions than a trial on the merits. The procedural posture determines which legal standards apply and what evidence is considered.

4. **Statutory authority** ($d_4$): Which statutes, regulations, and rules of law govern the dispute? This dimension encodes the positive law — the enacted rules — that constrain the outcome.

5. **Constitutional conformity** ($d_5$): Does the proposed outcome — or the statute that authorizes it — conform to constitutional requirements? This is the topological dimension developed in Chapter 7.

6. **Precedential constraint** ($d_6$): What do prior cases require? Stare decisis — the obligation to follow precedent — is the legal analogue of parallel transport, developed in Chapter 9.

7. **Remedial scope** ($d_7$): What remedies are available? Damages, injunctive relief, declaratory judgment, specific performance — the range of possible outputs, each with different legal implications.

8. **Public interest** ($d_8$): How does the outcome affect persons and interests beyond the immediate parties? This dimension is especially important in constitutional litigation, administrative law, and cases with precedential impact.

A legal judgment is a point $\mathbf{v} = (d_1, d_2, \ldots, d_8)$ in this eight-dimensional space. The binary verdict is a projection $\pi: \mathbb{R}^8 \to \{0, 1\}$ — a map that discards seven and a half dimensions of information. The scalar sentence is a projection $\psi: \mathbb{R}^8 \to \mathbb{R}$ — a map that discards seven dimensions. Neither projection is invertible. The information destroyed by the projection is, by the Scalar Irrecoverability Theorem, mathematically irrecoverable.

### The Metric

Not all dimensions interact equally. The relationship between entitlement structure ($d_1$) and constitutional conformity ($d_5$) is different from the relationship between procedural posture ($d_3$) and public interest ($d_8$). Some dimension pairs covary strongly: a change in entitlement structure almost always implies a change in remedial scope. Others are nearly independent: procedural posture rarely correlates with public interest.

These interactions are encoded in the *legal metric* — an $8 \times 8$ covariance matrix $\Sigma$ whose entries $\sigma_{ij}$ measure how strongly dimensions $d_i$ and $d_j$ co-vary across the body of decided cases. The metric determines which legal situations are "close" (similar on the manifold) and which are "far" (dissimilar). Two cases are close when the Mahalanobis distance $d(x, y) = \sqrt{(x - y)^T \Sigma^{-1} (x - y)}$ is small.

**[Modeling Axiom.]** The legal metric is not given *a priori*. It is calibrated from data — from the corpus of decided cases, which provides empirical evidence about how the eight dimensions interact in practice. Different legal traditions (common law, civil law, religious law) correspond to different metrics — different notions of which cases are "close." The metric is the bridge between the formal structure and the empirical reality. Chapter 4 develops this construction.

### The Symmetry Group

The deepest structure in the legal space is its symmetry. Not every transformation of the legal description changes the legal substance. Swapping the defendant's race changes the description but should not change the outcome. Relabeling the parties ("Smith v. Jones" becomes "Doe v. Roe") changes the description but preserves the substance. Translating the legal arguments from English to Spanish changes the description but not the meaning.

Transformations that change the description without changing the substance are *gauge transformations*. The set of all such transformations forms the *gauge group* of the legal system. The requirement that legal outcomes be invariant under gauge transformations is the *Legal Invariance Principle* (LIP), the foundational axiom of the geometric framework.

The most important subgroup of the legal gauge group is the *Hohfeldian gauge group*, which describes the symmetries of jural relations. As Chapter 2 will demonstrate, the four first-square Hohfeldian relations (right, duty, liberty, no-right) and the two operations connecting them (correlative swap and jural negation) form the dihedral group $D_4$ — the eight-element symmetry group of the square. Together with the second square (power, liability, immunity, disability), the full Hohfeldian octad forms the gauge group $D_4 \rtimes D_4$, developed in Chapter 5.

This gauge structure is not optional. It is the mathematical expression of a principle that every legal system claims to satisfy: that the law treats like cases alike. The gauge group tells us *which transformations should leave the outcome unchanged*. The gauge violation tensor tells us *whether the system actually satisfies this requirement*. The Legal Bond Index gives a *number* — a single, interpretable, falsifiable number — that measures how far the system deviates from the invariance it claims.

## What Geometry Provides

**Dimensions, not just verdicts.** A legal judgment is not merely "guilty" or "not guilty." It is a position in an eight-dimensional space — entitlement structure, factual nexus, procedural posture, statutory authority, constitutional conformity, precedential constraint, remedial scope, and public interest. The binary verdict is a projection from eight dimensions to one bit.

**Symmetry and invariance.** Equal protection is not a vague aspiration. It is a precise mathematical requirement: legal outcomes must be invariant under a specific group of transformations (the gauge group). The Legal Bond Index measures whether this requirement is satisfied, and by how much it is violated.

**Topology for constitutionality.** The Constitution is not a list of rules. It is a topological constraint on the judicial manifold — a requirement that certain paths through the legal space remain connected. A statute that breaks this connectivity is unconstitutional, and the breaking is detectable by computing path homology.

**Conservation laws.** In a closed bilateral dispute, liability is conserved: the plaintiff's gain is the defendant's loss on transferable legal dimensions. This is the legal analogue of conservation of charge in physics, derived from the same mathematical principle (Noether's theorem applied to the legal invariance principle).

**Computability.** The judicial complex can be constructed from case databases using natural language processing. Legal dimensions can be scored by linear probes on language-agnostic embeddings. Edge weights can be calibrated from outcomes. The framework is not merely theoretical — it admits implementation.

**Diagnostics for failure.** The geometric framework does not merely describe the legal system. It diagnoses its failures. Sentencing disparities are gauge violations (Chapter 11). Circuit splits are Wilson loops (Chapter 5). Constitutional ambiguity is topological obstruction (Chapter 7). Bad precedent is a local minimum (Chapter 10). Plea bargaining pathologies are objective hijacking (Chapter 12). Each failure mode has a geometric signature, and each signature is computationally detectable.

## What This Book Is Not

**This is not a claim that law can be reduced to mathematics.** The framework does not determine verdicts. It provides a structural vocabulary for analyzing legal reasoning — making implicit assumptions explicit, measuring consistency, and detecting contradictions. Judgment remains human. The geometry makes judgment *auditable*.

The distinction between *determining* verdicts and *auditing* verdicts is crucial. A GPS system does not decide where you should go. It shows you where you are, how far you have traveled, and whether you are on course. The geometric framework is a GPS for legal reasoning: it shows the judge where the case sits on the eight-dimensional manifold, how it relates to nearby cases, whether the proposed outcome satisfies the invariance requirements, and whether the reasoning path is geodesic or circuitous. The judge still decides. The geometry illuminates the decision space.

**This is not a claim that current legal AI is adequate.** The framework sets a higher standard than current legal AI achieves. It requires gauge invariance (most legal AI exhibits disparate impact), topological consistency (most legal AI produces ad hoc predictions), and conservation compliance (most legal AI ignores structural constraints). The geometric framework is not a validation of existing legal technology. It is a specification for what legal technology should become.

**This is not legal formalism in disguise.** Legal formalists claim that legal reasoning is deductive — that correct outcomes follow mechanically from rules. Legal realists counter that legal reasoning is irreducibly political and experiential. The geometric framework transcends both: it provides formal structure (the manifold, the metric, the gauge group) while acknowledging that the metric is not given but must be calibrated from data — which is irreducibly empirical.

Holmes wrote that "the life of the law has not been logic: it has been experience." The geometric framework agrees. The *structure* of the legal space — its dimensions, its symmetries — is given by logic and by the nature of legal relations. But the *metric* — the distances between legal states, the weights assigned to different dimensions, the boundary penalties that encode sacred constraints — is given by experience. By the accumulated corpus of decided cases, by the empirical reality of how legal systems function, by the cultural and institutional context in which law operates. The framework is formal. Its content is empirical. This is not formalism. It is geometry.

**This is not a claim that the framework is complete.** Chapter 16 catalogs what the framework cannot yet explain, what it needs but does not yet have, and where the mathematics is speculative rather than proven. The eight dimensions are a modeling choice, not a derivation from first principles. The metric requires empirical calibration that has not been fully performed. The conservation laws are conditional on assumptions that may not hold in all legal contexts. The framework is a beginning, not an end.

## The Arc of the Book

**Part I: The Problem** (Chapters 1--2) motivates geometric law. This chapter has argued that binary verdicts and scalar sentences destroy legal structure. Chapter 2 traces Hohfeld's 1913 discovery that jural relations have algebraic structure — the $D_4$ dihedral group, identified independently in our framework a century later.

**Part II: The Framework** (Chapters 3--6) builds the apparatus. Chapter 3 constructs the judicial complex — the weighted simplicial complex on which legal reasoning takes place. Chapter 4 defines the legal metric — the Mahalanobis distance that measures closeness between legal states. Chapter 5 develops the Hohfeldian gauge group — the $D_4 \rtimes D_4$ symmetry of jural relations. Chapter 6 models precedent as the heuristic field guiding search through the complex — the legal analogue of the price signal in *Geometric Economics*.

**Part III: Dynamics and Symmetry** (Chapters 7--9) adds constitutional structure and conservation. Chapter 7 derives constitutionality as path homology preservation — a topological criterion for whether a statute is compatible with the Constitution. Chapter 8 proves that equal protection is a gauge invariance requirement — the Equal Protection Clause is the legal system's demand for invariance under the gauge group of protected characteristics. Chapter 9 models stare decisis as parallel transport of legal rules along precedent paths — and shows that holonomy (the rotation that accumulates along a curved path) explains why precedent can evolve without being overruled.

**Part IV: Failure Modes** (Chapters 10--12) catalogs what goes wrong. Chapter 10 maps the four geometric pathologies from *Geometric Reasoning* — heuristic corruption, objective hijacking, local minima, gauge breaking — onto their legal manifestations. Chapter 11 measures sentencing disparities as gauge violation tensors — converting the normative demand for equal treatment into a quantitative, falsifiable measurement. Chapter 12 models the adversarial system as manifold exploration by opposing searchers — prosecution and defense trace different paths through the legal complex, and the judge evaluates which path is more geometrically consistent.

**Part V: Applications** (Chapters 13--15) develops three domains. Chapter 13 treats contract law as boundary construction on the legal manifold. Chapter 14 models international law as multi-manifold diplomacy — each nation's legal system is a separate manifold, and international law attempts to construct a shared product space. Chapter 15 addresses AI legal reasoning — what it would mean for an AI system to reason legally in a geometrically principled way.

**Part VI: Horizons** (Chapter 16) surveys open questions — what the framework cannot yet explain, what empirical work remains, and where the mathematics points toward future development.

---

## Worked Example: Judge Rivera's Three Cases

Let us formalize the opening scenario.

**Case 1: The voting rights challenge.** The state restricts early voting in a way that disproportionately affects minority voters. On the eight-dimensional judicial manifold:
- $d_1$ (entitlement): right to vote vs. state's power to regulate elections
- $d_5$ (constitutionality): Equal Protection Clause at stake
- $d_8$ (public interest): democratic participation

The Legal Invariance Principle test: change the racial composition of affected voters while preserving all other facts. If the court's analysis changes, the LIP is violated — the outcome depends on a legally irrelevant characteristic. This is measurable (Chapter 8).

The binary verdict — "constitutional" or "unconstitutional" — will not capture the dimensional structure of the analysis. The court might find the restriction unconstitutional because it violates equal protection ($d_5$), or because it burdens the fundamental right to vote ($d_1$) without sufficient justification ($d_8$). These are different reasons with different precedential implications ($d_6$), but the verdict is the same single bit. The geometric framework preserves the distinction.

**Case 2: The statutory conflict.** Federal law requires data disclosure; state law prohibits it. On the manifold, this is a topological obstruction — no path exists from the company's current state to a compliant state, because every path that satisfies federal law crosses the state-law boundary and vice versa. The company is trapped in a graph with no exit. The resolution is the Supremacy Clause, which the framework models as a topological constraint that removes the state-law boundary when it conflicts with federal law (Chapter 7).

The geometric perspective reveals why the company's situation is not merely "difficult" but *topologically impossible*: the intersection of the two statutory constraints creates an empty feasible region. No amount of good-faith effort can produce compliance with both requirements. This is a structural defect, not a failure of will. The Supremacy Clause resolves it by modifying the topology — removing the state-law constraint and restoring a connected feasible region.

**Case 3: The sentencing disparity.** Two defendants with identical criminal histories and identical offenses receive sentences of 3 and 9 years. The gauge violation tensor $V_{ij}$ measures the difference: the index $i$ identifies the transformation (race swap) and $j$ identifies the outcome dimension (sentence length). A non-zero $V_{ij}$ is a measurable injustice — not a political claim but a geometric fact (Chapter 11).

The scalar sentence (3 years vs. 9 years) tells Rivera that something is different. But it does not tell her *what* is different. The gauge violation tensor decomposes the difference into its components: how much is attributable to race ($V_{\text{race}, \text{sentence}}$), how much to geography ($V_{\text{district}, \text{sentence}}$), how much to judge identity ($V_{\text{judge}, \text{sentence}}$), and how much to legitimate legal factors (zero, by construction, since legitimate factors are held constant). The tensor is a diagnostic tool. The scalar is a symptom.

---

## The Moral Contraction Parallel

This book is the fifth volume in the Geometric Series, and the legal scalar failure has a direct precedent in the ethical scalar failure analyzed in *Geometric Ethics* (Bond, 2026b). In that volume, the central argument is that moral evaluation — collapsing a nine-dimensional moral judgment into a scalar "goodness score" or a binary "right/wrong" — destroys the structure that matters most in hard moral cases. The trolley problem is not a question with a scalar answer. It is a location on the moral manifold where two dimensions (harm minimization and rights) point in different directions, and the structural fact that they diverge is exactly what makes the problem hard. Collapsing the divergence to a single number declares the problem solved when it has merely been suppressed.

The legal parallel is precise. A sentencing decision is not a question with a scalar answer. It is a location on the legal manifold where multiple dimensions — offense severity, criminal history, deterrence, rehabilitation, retribution, public safety — may point in different directions. The Federal Sentencing Guidelines attempt to reduce this multi-dimensional reality to a sentencing range by crossing offense level (one axis) with criminal history category (a second axis) in a two-dimensional grid. This is an improvement over fully discretionary sentencing — it captures two dimensions instead of zero — but it still discards six dimensions of the eight-dimensional legal space. The remaining discretion that judges exercise within and beyond the guidelines range is the space where the undiscarded dimensions find expression — and where gauge violations enter.

The Scalar Irrecoverability Theorem applies identically in both domains. In ethics: no continuous function from the nine-dimensional moral manifold to a scalar preserves the moral distance structure. In law: no continuous function from the eight-dimensional legal manifold to a scalar preserves the legal distance structure. The theorem is domain-independent. The consequences are domain-specific but structurally identical.

The conservation law parallel is equally exact. In ethics, the conservation of harm (derived from Noether's theorem applied to the moral gauge group) states that harm is neither created nor destroyed by re-description — it is only transferred between parties. In law, the conservation of liability (derived from the same mathematical principle applied to the legal gauge group) states that in a closed bilateral dispute, the plaintiff's gain is the defendant's loss on transferable dimensions. This is not a normative principle. It is a mathematical consequence of the symmetry structure of legal relations. Chapter 9 develops the formal derivation.

## The Historical Precedent: From Binary to Geometric in Physics

The transition from binary/scalar evaluation to geometric evaluation has happened before — not in law, but in physics. The precedent is instructive.

Before Einstein, the physics of gravity was scalar. Newtonian mechanics describes gravity as a force proportional to mass and inversely proportional to the square of distance. The gravitational field at each point in space is a single number: the field strength. The theory is spectacularly successful within its domain.

Einstein's general relativity replaces the scalar field with a *geometric* object: the metric tensor $g_{\mu\nu}$, a $4 \times 4$ symmetric matrix at each point of spacetime. The metric tensor encodes not just the strength of gravity but its *structure*: how spacetime curves, which paths are geodesics, how clocks run at different locations, how light bends around massive objects. The scalar gravitational potential of Newton is a specific contraction of the metric tensor — a projection from 10 independent components to one number.

The projection is lossy. The Newtonian scalar tells you how fast an apple falls. The metric tensor tells you how fast an apple falls *and* how much clocks slow down near the earth's surface *and* how much starlight bends around the sun *and* whether the orbit of Mercury precesses. The scalar is the shadow of a richer geometric reality, and the shadow cannot predict what the full geometry predicts.

The parallel to law is exact. The binary verdict is the Newtonian scalar. The eight-dimensional legal manifold is the metric tensor. The projection from the manifold to the verdict is the contraction from geometry to scalar — and the Scalar Irrecoverability Theorem says the contraction is lossy in a way that no amount of post-hoc analysis can repair.

This parallel is not merely decorative. The mathematical framework is the same. Gauge invariance in general relativity (coordinate invariance) corresponds to gauge invariance in the legal framework (invariance under legally irrelevant transformations). Geodesics in general relativity (paths of least action) correspond to geodesics on the legal manifold (optimal litigation strategies). Curvature in general relativity (the Riemann tensor) corresponds to curvature on the legal manifold (the sensitivity of legal outcomes to small perturbations in the facts). The mathematics is borrowed, but it is not borrowed loosely. The correspondences are formal and precise.

---

## Technical Appendix

**The Scalar Irrecoverability Theorem (Legal Version).** **[Conditional Theorem.]** Let $\mathcal{K}$ be a judicial complex with attribute vectors $\mathbf{v} \in \mathbb{R}^8$. No continuous function $\phi: \mathbb{R}^8 \to \{0, 1\}$ (binary verdict) preserves the distance structure of $\mathcal{K}$. Cases that are close on the manifold (similar legal issues, similar facts) may receive different verdicts, and cases that are far apart may receive the same verdict. The binary projection is informationally lossy and the loss is irrecoverable.

*Proof sketch.* The function $\phi$ partitions $\mathbb{R}^8$ into two regions: $\phi^{-1}(0)$ and $\phi^{-1}(1)$. Each region contains uncountably many points with pairwise distances ranging from zero to the diameter of the manifold. But $\phi$ assigns the same value to all points within each region. Therefore $\phi$ identifies points that are arbitrarily far apart on the manifold (they get the same verdict) and separates points that are arbitrarily close (they get different verdicts, if they lie on opposite sides of the decision boundary). The distance structure is not preserved. Moreover, no function $\psi: \{0, 1\} \to \mathbb{R}^8$ can invert $\phi$: since $\phi$ is not injective, no left inverse exists. The information loss is irrecoverable. $\square$

**Corollary (Scalar Sentence Irrecoverability).** No continuous function $\psi: \mathbb{R}^8 \to \mathbb{R}$ is injective. Therefore no scalar sentence preserves the eight-dimensional structure of the legal analysis that produced it. The sentence destroys at least seven dimensions of information, and no post-hoc procedure can recover the destroyed information.

**The Eight Legal Dimensions (Preview).** The eight dimensions — entitlement structure ($d_1$), factual nexus ($d_2$), procedural posture ($d_3$), statutory authority ($d_4$), constitutional conformity ($d_5$), precedential constraint ($d_6$), remedial scope ($d_7$), public interest ($d_8$) — are developed formally in Chapter 3. They inherit the scope $\times$ mode decomposition from the parent moral manifold (*Geometric Ethics*, Chapter 5), adapted for legal contexts.

**The Legal Manifold (Preview).** The judicial complex $\mathcal{K}$ is a weighted directed simplicial complex. Its 0-simplices (vertices) are decided cases, each tagged with an attribute vector $\mathbf{v} \in \mathbb{R}^8$. Its 1-simplices (edges) are doctrinal relationships — citations, overrulings, distinguishings — weighted by the Mahalanobis distance between the connected cases plus boundary penalties for crossing regime boundaries (e.g., the boundary between criminal and civil law, between federal and state jurisdiction). Higher-dimensional simplices encode multi-case doctrinal structures. The formal construction occupies Chapter 3; the metric occupies Chapter 4.

---

## Notes on Sources

The sentencing disparity literature includes the U.S. Sentencing Commission's reports on demographic sentencing patterns, Mustard (2001) on racial disparity, and Starr (2015) on gender disparity. The 19.1% racial sentencing disparity figure is from the U.S. Sentencing Commission's 2017 report on demographic differences in sentencing. The 63% gender disparity figure is from Starr (2015). Circuit splits are catalogued annually in the Supreme Court's certiorari petitions. The *Carpenter v. United States* (2018) decision resolved a circuit split on Fourth Amendment protection for cell site location information. The *District of Columbia v. Heller* (2008) decision interpreted the Second Amendment's scope. The constitutional ambiguity problem is developed in Fallon (2007) and Balkin (2011). Holmes's observation about experience over logic opens *The Common Law* (1881), the foundational text of legal realism.

The Hohfeldian framework begins with Hohfeld (1913, 1917) and is developed in Corbin (1919, 1921), Cook (1919), and the Yale School. The gauge-theoretic reinterpretation of Hohfeld is original to Bond (2026b, *Geometric Ethics*, Chapter 12). The Scalar Irrecoverability Theorem is proved in Bond (2026c, *Geometric Reasoning*, Chapter 10) and is a corollary of the rank-nullity theorem applied to the derivative of any continuous function from $\mathbb{R}^n$ to $\mathbb{R}$ (or to $\{0, 1\}$).

The analogy between legal and physical geometry is not original to this book. Langdell (1871) compared legal reasoning to scientific reasoning. Cardozo (1921) described the "directive force" of precedent in terms that map naturally onto the heuristic field formalism. Dworkin (1986) argued that legal interpretation has a structural character — that judges seek the interpretation that best "fits" the existing body of law — which is precisely the geodesic minimization this framework formalizes. The contribution of the present work is to provide the *mathematical* framework that makes these intuitions precise, measurable, and computationally implementable.

The Scalar Irrecoverability Theorem, in its general form, is proved in *Geometric Reasoning* (Bond, 2026c, Ch. 10). The legal version above is a direct application to the eight-dimensional judicial complex. The economic version (GDP Irrecoverability) appears in *Geometric Economics* (Bond, 2026d, Ch. 6). The ethical version (Moral Irrecoverability) appears in *Geometric Ethics* (Bond, 2026b, Ch. 15). In every domain, the theorem says the same thing: when you project a multi-dimensional reality onto a scalar, you destroy structure that no subsequent analysis can recover. The destruction is not a matter of measurement precision or computational power. It is a mathematical impossibility, as absolute as the impossibility of inverting a non-injective function. The binary verdict and the scalar sentence are such projections. Their inadequacy is not a failure of the legal system's effort. It is a failure of the legal system's output format.

What this book offers is not a replacement for the verdict. The legal system will always produce outputs — decisions that resolve disputes, sentences that determine consequences. What the book offers is the *intermediate representation*: the eight-dimensional description of the case, the metric that measures proximity to other cases, the gauge invariance test that checks for illegitimate influences, the topological constraint that verifies constitutionality, the conservation law that audits the transfer of rights. The verdict is the compression of this intermediate representation. The framework makes the representation visible, auditable, and computable — so that when the compression destroys information, we know exactly what was lost and why.

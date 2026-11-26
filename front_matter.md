# Front Matter

---

## Title Page

**Geometric Law: Symmetry, Invariance, and the Structure of Legal Reasoning**

Andrew H. Bond
Senior Member, IEEE
Department of Computer Engineering
San Jose State University

Book 5 of the Geometric Series

*San Jose, 2026*

---

## Series Foreword

This is the fifth volume in the Geometric Series.

The series began with a simple observation: across domains --- ethics, law, economics, cognition, communication, medicine --- the standard methodology compresses multi-dimensional structure into scalar numbers and then wonders why the numbers behave badly. Utility functions do not capture decision-making. GDP does not capture economic wellbeing. Binary verdicts do not capture legal reasoning. The pattern is universal and the diagnosis is the same: scalar reduction destroys geometric structure, and the destruction is irreversible.

*Geometric Methods in Computational Modeling* (Book 1) assembled the mathematical toolkit: Riemannian geometry, hyperbolic embeddings, persistent homology, SPD manifolds, gauge theory. *Geometric Reasoning: From Search to Manifolds* (Book 2) developed the parent framework --- the heuristic field formalism, geodesic deviation, the four failure modes, gauge invariance, and the Scalar Irrecoverability Theorem that unifies them. *Geometric Ethics* (Book 3) was the first domain instantiation, demonstrating the framework on the 9-dimensional stratified moral manifold with its $V_4 \times U(1)_H$ symmetry group. *Geometric Economics* (Book 4) was the second instantiation, proving that Nash equilibrium is the scalar projection of the Bond Geodesic Equilibrium on the economic decision manifold.

This book is the third domain instantiation, and in many ways the most urgent. Law is the institutional machinery through which society enforces the principles that ethics articulates and economics measures. If the legal system's output format destroys the structure of legal reasoning --- and the Scalar Irrecoverability Theorem proves that it does --- then the consequences are not merely academic. They are measured in years of unjust incarceration, in constitutional rights that go unprotected because the binary verdict cannot express *why* they were violated, and in circuit splits where courts reach opposite conclusions without a shared vocabulary for identifying where their analyses diverge.

The central constructions of this volume are the **judicial complex** $\mathcal{K}$ --- a weighted directed simplicial complex of decided cases and doctrinal relationships --- and the **Hohfeldian gauge group** --- the group of relabelings of Wesley Newcomb Hohfeld's eight jural relations, which on each of the two squares is the Klein four-group $V_4$ (the dihedral group $D_4$ and the product $D_4 \rtimes D_4$ of earlier versions are withdrawn; see the dated notes of 2026-11-26 in Chapters 2 and 5). On this complex, we define the Legal Invariance Principle (equal protection as gauge invariance), constitutional review as path homology preservation, stare decisis as parallel transport, and the Legal Bond Index as a quantitative measure of how far the system deviates from the invariance it claims.

The empirical foundation draws from the companion paper *Algorithmic Jurisprudence* (Bond, 2026), the legal-retrieval Kaggle competition (109K passages across 11 languages), and the cross-lingual invariance experiments from *Geometric Ethics*. The results quoted from those sources: the Hohfeldian positions carry the Klein four-group $V_4$ (the D$_4$ structure stated in earlier versions is withdrawn), the Bond Index baseline from the moral domain is 0.155 (the legal baseline remains to be measured), and *Geometric Ethics* reports cross-lingual deontic transfer at 100% (confidence interval [99.96%, 100%]), measured through a multilingual embedding model and not on human subjects.

One result on legal data has been added since. The paper "The Legal Bond Index: A Matched-Neighbourhood Diagnostic of Algorithmic Disparity, Applied to COMPAS" (Bond, in press, *Journal of Science and Law*) defines a form of the index that can be computed from recorded data and computes it for the COMPAS risk score on 5,278 defendants. The index is a ratio in which 1 means no excess disparity. It lies between 1.041 and 1.069 across neighborhood scales and falls to between 1.00 and 1.02 when the matches across race are forced to be as close as the matches within race. The result is conditional on the predictors in the public dataset, which are a subset of those the algorithm uses. It is a screening diagnostic, not proof of legal unfairness and not a causal effect of race. It is on a different scale from the 0.155 above and from the illustrative index values in the chapters. Chapter 8 reports it in full, with its limits.

The relationship between this volume and its predecessor is worth noting. *Geometric Economics* proved that Nash equilibrium is the scalar projection of a richer geometric object (the BGE). This volume proves an analogous result for law: the binary verdict is the scalar projection of a richer geometric object (the eight-dimensional legal evaluation). In both cases, the projection is lossy, the loss is irrecoverable, and the richer object resolves puzzles that the scalar projection cannot address. The mathematical structure is inherited from the parent framework. The domain-specific content --- Hohfeld's taxonomy, constitutional topology, the adversarial system --- is original to the legal instantiation.

Subsequent volumes extend the framework further: *Geometric Cognition* (Book 6) turns the manifold inward on the mind, *Geometric Communication* (Book 7) applies it across species and millennia, and *Geometric Medicine* (Book 8) brings it to the bedside where the stakes are highest. Each domain instantiation reveals new structure. Each confirms the same theorem: scalar reduction is irrecoverable, and the geometry matters.

---

## Preface

### The Structure Behind the Verdict

Every law student learns, in the first week of the first semester, that legal analysis is *structured*. Cases have elements. Statutes have requirements. Constitutional provisions have tests --- strict scrutiny, intermediate scrutiny, rational basis. The entire apparatus of legal education is an apprenticeship in navigating this structure: identifying which elements are at issue, which requirements are met, which tests apply, and how prior cases constrain the present analysis.

And then, at the end of all that structured reasoning, the legal system demands a binary output. Guilty or not guilty. Liable or not liable. Constitutional or unconstitutional. The structure that the judge, the jury, or the justice navigated so carefully is compressed into a single bit.

This book asks: what is that structure, mathematically? And what does the compression destroy?

The answer to the first question is geometric. Legal reasoning takes place on a judicial manifold --- an eight-dimensional space whose dimensions are entitlement structure, factual nexus, procedural posture, statutory authority, constitutional conformity, precedential constraint, remedial scope, and public interest. The manifold has a metric (which measures the distance between legal states), a symmetry group (which identifies the transformations that should leave legal outcomes unchanged), a topological structure (which determines whether proposed statutes are compatible with the Constitution), and conservation laws (which constrain the transfer of rights between parties).

The answer to the second question is given by the Scalar Irrecoverability Theorem: the compression destroys at least seven dimensions of information, and the destruction is mathematically irrecoverable. No post-hoc analysis, no appellate review, no supplementary opinion can reconstruct the eight-dimensional structure from the one-bit verdict.

The thesis is not that judges should stop producing verdicts. It is that the legal system should make visible the *intermediate representation* --- the eight-dimensional description of the case --- before compressing it. The verdict is necessary. The invisibility of the structure it compresses is not.

I did not set out to write a book about law. The project began as Chapter 22 of *Geometric Ethics*, on the application of the moral manifold to legal reasoning, and grew into an independent work when the mathematical structures proved richer than the chapter format could contain. The Hohfeldian gauge group was discovered in the ethics manuscript, but its implications for constitutional topology, sentencing disparities, and the adversarial system required a full-length treatment. The companion paper *Algorithmic Jurisprudence* developed the formal framework; this book develops the intuition, the applications, and the empirical validation.

This book is written for three audiences, and it asks something different of each.

For **legal scholars and practitioners**, the book provides a mathematical vocabulary for structures that legal reasoning already possesses. The Hohfeldian taxonomy is already taught in every jurisprudence course; this book shows that it is group theory. Equal protection is already the law of the land; this book shows that it is gauge invariance. Stare decisis is already the organizing principle of common law; this book shows that it is parallel transport. The mathematics does not replace legal reasoning. It illuminates it.

For **mathematicians, physicists, and computer scientists** curious about applications of differential geometry, gauge theory, and simplicial topology to the social sciences, the book provides a worked example of what it means to apply these tools with rigor. The Hohfeldian gauge group is a genuine algebraic structure, not a metaphor. The path homology criterion for constitutionality is a genuine topological computation. The Legal Bond Index is a genuine quantitative measure. The framework is formal and falsifiable.

For **citizens and policymakers** who believe that "equal justice under law" should be more than an inscription on a building, the book provides a tool. The Legal Bond Index measures whether the legal system satisfies the invariance it claims. A gauge violation tensor of 0.191 on the race-sentence component means that Black defendants receive sentences 19.1% longer than white defendants for equivalent crimes. This is not a political argument. It is a measurement. The framework converts normative demands into empirical tests. The figure of 19.1% is the U.S. Sentencing Commission's. The one form of the Legal Bond Index that has been computed on legal data is a different quantity on a different scale, a matched-neighborhood ratio for the scores of one risk-assessment algorithm, and Chapter 8 reports it with what it does and does not show.

### A Note on Scope

This book does not claim that law is "merely" geometry. Human judgment, institutional context, political power, historical contingency --- these shape the law in ways that no mathematical framework fully captures. The claim is narrower and more precise: legal reasoning has geometric structure that its output format destroys, and making that structure visible would improve the auditability, consistency, and fairness of legal decisions.

Chapter 16 is honest about what the framework cannot yet explain. The eight dimensions are a modeling choice whose adequacy has not been fully validated across all legal domains. The legal metric has not been calibrated from large-scale case data. The conservation laws are conditional on assumptions that may not hold universally. The AI implementation described in Chapter 15 is a research programme, not a deployed system. These limitations are not hedges. They are the frontier.

Each chapter opens with a running example --- Judge Elena Rivera, a federal district court judge in San Francisco --- that grounds the abstract framework in judicial decision-making. Rivera's docket includes civil rights challenges, contract disputes, criminal sentencings, constitutional questions, and international law issues. Her cases instantiate every construct in the book. Judge Rivera, her docket, the studies and systems she meets, and every figure computed in the running examples and worked examples are illustrative or hypothetical. None is a measurement. The reader who follows Rivera's story through sixteen chapters will have seen the full framework applied to a single, coherent judicial career.

### How to Read This Book

- **The theoretical path**: Chapters 1--9. From the scalar failure of binary verdicts through the full geometric framework.
- **The applied path**: Chapters 10--15. Failure modes, sentencing, adversarial system, contracts, international law, AI.
- **The constitutional path**: Chapters 7, 8, and the worked examples. How to test constitutionality topologically and equal protection as gauge invariance.
- **The fast path**: Chapters 1, 5, 7, 8. Binary verdicts fail; Hohfeld is $V_4$; constitutionality is topology; equal protection is gauge invariance.

---

## Core Objects at a Glance

| Object | What It Is | Where Developed |
|--------|-----------|-----------------|
| **Judicial complex** $\mathcal{K}$ | Weighted directed simplicial complex of decided cases and doctrinal relationships | Ch. 3 |
| **8 legal dimensions** | Entitlement, factual nexus, procedure, statutory authority, constitutionality, precedent, remedies, public interest | Ch. 3 |
| **Legal Invariance Principle** (LIP) | Legal judgments must be invariant under legally irrelevant transformations | Ch. 8 |
| **Hohfeldian gauge group** | $V_4$ on each square of jural relations; the group of the full octad, formerly $D_4 \rtimes_\varphi D_4$, is withdrawn pending restatement (2026-11-26) | Ch. 2, 5 |
| **Legal Bond Index** | Quantitative measure of judicial inconsistency under gauge transformations. Its measured form is a matched-neighborhood ratio centered on 1 | Ch. 8 |
| **Path homology** | Topological invariant of directed graphs; constitutionality = homology preservation | Ch. 7 |
| **Doctrinal heuristic** $h_D(n)$ | Legal doctrine as A* heuristic function guiding search through $\mathcal{K}$ | Ch. 6 |
| **Precedential weight deformation** | Stare decisis as local modification of edge weights via parallel transport | Ch. 9 |
| **Legal friction** BF$_{\text{law}}$ | Total cost of a litigation path through the judicial complex | Ch. 4 |

## Key Results at a Glance

| Finding | Source |
|---------|--------|
| Equal protection is a gauge symmetry | Ch. 8 |
| Constitutionality iff path homology preserved, within the model; completeness is a conjecture | Ch. 7 |
| Liability conserved in closed bilateral disputes | Ch. 9 |
| Hohfeldian relations on each square form $V_4$ ($D_4 \rtimes D_4$ withdrawn pending restatement, 2026-11-26) | Ch. 2, 5 |
| Due process = well-definedness on quotient space | Ch. 8 |
| Cross-lingual invariance of normative structure (109K passages, 11 languages; exploratory and model-mediated in that volume's claim ledger) | *Geometric Ethics* |
| Bond Index baseline from the moral domain: 0.155 (no legal value on that scale has been measured) | *Geometric Ethics* |
| Legal Bond Index, matched-neighborhood form, for COMPAS risk scores ($n = 5{,}278$): 1.041 to 1.069 across neighborhood scales, 1.049 at $k = 20$ (95% interval 1.027 to 1.072). Under matching parity: 1.00 to 1.02. Conditional on the measured predictors. A research-stage screening diagnostic for one algorithm, not a finding of legal unfairness | Ch. 8; Bond (in press), *Journal of Science and Law* |

The last row is the one measurement on legal data in this volume. It is a ratio centered on 1, on a different scale from the 0.155 of the row above, and it measures the scores of an algorithm. It is taken from a paper that makes no use of the framework of this book and is not a test of it.

## Epistemic Status Classification

| Tag | Meaning | Approx. Count |
|-----|---------|---------------|
| **[Established Mathematics.]** | Standard results from topology, group theory, graph theory | ~15 |
| **[Legal Doctrine.]** | Established principles of law (equal protection, due process, stare decisis) | ~8 |
| **[Modeling Axiom.]** | Structural choices (8 dimensions, Mahalanobis metric, path homology for constitutionality) | ~10 |
| **[Conditional Theorem.]** | Results following from axioms (LIP $\to$ gauge invariance, conservation, optimality) | ~12 |
| **[Speculation/Extension.]** | Forward-looking claims (AI implementation, cross-jurisdictional metrics) | ~8 |

---

## Acknowledgments

A book that reaches from Hohfeld's 1913 taxonomy of jural relations to the gauge-theoretic measurement of sentencing disparities is indebted to more intellectual traditions than any acknowledgment section can encompass.

The geometric framework that underpins this book was developed as part of the Geometric Ethics programme at San Jose State University. The legal instantiation grew directly from the Hohfeldian gauge group first identified in *Geometric Ethics* (Bond, 2026b, Ch. 12), and the observation that Hohfeld's correlative-opposite structure is a group, stated first as the dihedral group $D_4$ and since *Geometric Ethics* v1.25 as the Klein four-group $V_4$, was the generative insight for the entire volume. The transition from ethical to legal geometry proved remarkably natural --- more natural, in some ways, than the economic instantiation --- because law already possesses the structural vocabulary (rights, duties, precedent, constitutional constraint) that the geometric framework formalizes.

The legal foundations of this work rest on Hohfeld's extraordinary achievement. Wesley Newcomb Hohfeld published two articles in 1913 and 1917 that identified the eight fundamental jural relations and their logical interconnections. He did not live to complete his projected treatise --- he died in 1918 at the age of 38 --- but his taxonomy has structured analytical jurisprudence for over a century. The observation that his taxonomy is group-theoretic, that the two operations generate a group, is new to this series. But the raw material is entirely Hohfeld's.

The jurisprudential tradition from which this book draws is deep: Hart's *The Concept of Law* (1961), Dworkin's *Law's Empire* (1986), Raz's *The Authority of Law* (1979), and Posner's *Economic Analysis of Law* (1973) each contributed to the understanding of legal structure that this book formalizes. The legal realist tradition --- Holmes, Llewellyn, Frank --- contributed the insistence that law is empirical, not merely logical. The geometric framework inherits both: formal structure from the analytical tradition, empirical calibration from the realist tradition.

The empirical work underlying the Legal Bond Index and the cross-lingual invariance experiments was conducted using the legal-retrieval Kaggle competition dataset (109,000 passages across 11 languages) and the Geometric Ethics experimental infrastructure. The computational experiments were performed on the Atlas workstation and the San Jose State University High-Performance Computing cluster.

Institutional support came from the Department of Computer Engineering at San Jose State University, the College of Engineering, and the SJSU Research Foundation. I thank my colleagues in the department for providing an environment where a computer scientist can apply gauge theory to constitutional law without having to justify the enterprise at every faculty meeting.

The series editors and early readers of the manuscript improved it through criticism that ranged from constructive to humbling. Colleagues at the IEEE Computational Intelligence Society, workshop participants at NeurIPS 2025, and anonymous reviewers of the *Algorithmic Jurisprudence* companion paper identified weaknesses, suggested improvements, and insisted on precision. The errors that remain are evidence of finite bandwidth on an eight-dimensional problem.

Finally, and as always: to my family, who have endured a year of dinner-table discussions about Hohfeldian octads, Wilson loops in the citation network, and whether the Supremacy Clause is really a topological constraint. Their patience, humor, and well-calibrated heuristic for when to change the subject have been indispensable.

Andrew H. Bond
San Jose, California
March 2026

# Index Framework

*Chapter-level index for Geometric Law. Page-level entries to be generated at typesetting.*

---

## Concepts

**A* search**, 6, B --- evaluation function $f(n) = g(n) + h_D(n)$; System 2 deliberation + System 1 doctrinal heuristic; legal pathfinding on the judicial complex
**admissible heuristic**, 6, 10 --- $h_D(n) \leq h^*(n)$; admissible = well-developed precedent; inadmissible = contradictory or corrupt precedent
**adversarial system**, 12 --- prosecution and defense as opposing searchers on the judicial complex; debate-based manifold exploration
**attribute vector** ($\mathbf{v} \in \mathbb{R}^8$), 3, 4, 8 --- point on the judicial manifold; eight legal dimensions

**binary verdict**, 1 --- projection $\phi: \mathbb{R}^8 \to \{0, 1\}$; destroys at least 7 dimensions of legal structure
**Bond Invariance Principle** (BIP), 8, 9 --- *see also* Legal Invariance Principle
**boundary penalty** ($\beta_k$), 3, 4, 13 --- discrete cost of crossing a regime boundary (criminal/civil, federal/state)
**breach of contract**, 13 --- crossing a contractually constructed boundary on the legal manifold

**circuit split**, 1, 5 --- opposite outcomes in different circuits on the same legal question; Wilson loop with non-trivial holonomy
**conservation of liability**, 9 --- Noether's theorem applied to Hohfeldian gauge group; plaintiff's gain = defendant's loss on transferable dimensions
**constitutional conformity** ($d_5$), 3, 7, 8 --- fifth legal dimension; topological compatibility with constitutional subcomplex
**constitutional review**, 7 --- statute is constitutional iff its addition to $\mathcal{K}$ preserves path homology of $\mathcal{C}$
**constitutional subcomplex** ($\mathcal{C}$), 7 --- subcomplex of $\mathcal{K}$ containing constitutionally relevant cases
**contract law**, 13 --- boundary construction on the legal manifold; breach = boundary crossing
**correlative**, 2, 5 --- Hohfeldian operation swapping perspective between parties; right $\leftrightarrow$ duty, liberty $\leftrightarrow$ no-right
**covariance matrix** ($\Sigma$), 4, 11 --- $8 \times 8$ matrix encoding interactions among legal dimensions

**$D_4$** (dihedral group), 2, 5 --- symmetry group of Hohfeld's first square; 8 elements; generators $r$ (correlative rotation), $s$ (jural negation)
**dihedral group**, *see* $D_4$
**disability**, 2, 5 --- Hohfeldian second-square position; lack of power to change another's legal position; correlative of immunity
**doctrinal heuristic** ($h_D$), 6 --- precedent as A* heuristic guiding judicial search; quality varies with precedent density
**due process**, 8 --- invariance under transformations (3)--(5) of the LIP; well-definedness on the quotient space
**duty**, 2, 5 --- Hohfeldian first-square position; obligation correlative to right; opposite of liberty

**eight legal dimensions**, 1, 3 --- entitlement ($d_1$), factual nexus ($d_2$), procedure ($d_3$), statutory authority ($d_4$), constitutionality ($d_5$), precedent ($d_6$), remedies ($d_7$), public interest ($d_8$)
**entitlement structure** ($d_1$), 1, 2, 3 --- first legal dimension; Hohfeldian position of parties
**equal protection**, 8 --- gauge invariance under protected-characteristic transformations; the Fourteenth Amendment geometrized

**factual nexus** ($d_2$), 3 --- second legal dimension; what happened, mapped to legal significance
**failure modes**, 10 --- heuristic corruption, objective hijacking, local minima, gauge breaking; the four geometric pathologies instantiated for law

**gauge breaking**, 8, 10, 11 --- sentencing disparities, discriminatory outcomes; failure of invariance under legally irrelevant transformations
**gauge group**, *see* Hohfeldian gauge group
**gauge invariance**, 8, 9 --- legal outcomes unchanged under gauge transformations; mathematical statement of equal protection
**gauge transformation**, 8 --- change in case description (e.g., defendant's race) that should not affect legal outcome
**gauge violation tensor** ($V_{ij}$), 8, 11 --- $V_{ij} = J_j(\tau_i(x)) - J_j(x)$; measures invariance failure by transformation and outcome dimension

**heuristic corruption**, 6, 10 --- price signal (precedent) overestimates or underestimates cost; media influence, racial bias in the heuristic field
**Hohfeld, Wesley Newcomb**, 2, 5 --- identified eight jural relations (1913, 1917); taxonomy is $D_4$ group theory
**Hohfeldian gauge group** ($G_{\mathcal{Ho}} = D_4 \rtimes D_4$), 5 --- full symmetry group of jural relations; 64 elements; semidirect product of first and second squares
**Hohfeldian octad**, 2, 5 --- the eight jural relations: right, duty, liberty, no-right, power, liability, immunity, disability
**holonomy**, 9 --- rotation accumulated during parallel transport around a closed loop; explains doctrinal evolution without explicit overruling

**immunity**, 2, 5 --- Hohfeldian second-square position; protection against another's power; correlative of disability; opposite of liability
**intermediate scrutiny**, 7, 8 --- constitutional review standard for sex-based classifications
**international law**, 14 --- multi-manifold diplomacy; each nation has a separate legal manifold

**judicial complex** ($\mathcal{K}$), 3, 4, 5, 6, 7 --- weighted directed simplicial complex; vertices = cases, edges = doctrinal relationships
**Judicial Bond Invariance Principle** (JBIP), 8 --- structural invariance: legal outcomes invariant under Hohfeldian gauge transformations applied to party labels and positions
**jural negation**, 2, 5 --- Hohfeldian operation swapping opposites; right $\leftrightarrow$ no-right, duty $\leftrightarrow$ liberty; reflection $s$ of $D_4$

**Legal Bond Index** (LBI), 8, 11 --- aggregate quantitative measure of gauge violation; baseline 0.155
**legal friction** ($\text{BF}_{\text{law}}$), 4, 6 --- total path cost on the judicial complex; sum of edge weights along litigation path
**Legal Invariance Principle** (LIP), 8 --- $J_{\text{law}}(\tau(x)) = J_{\text{law}}(x)$ for all $\tau \in \mathcal{T}_{\text{irrelevant}}$; foundational axiom
**legal metric**, 4 --- Mahalanobis distance + boundary penalties; $d(x,y) = d_M(x,y) + \sum_k \beta_k$
**liberty**, 2, 5 --- Hohfeldian first-square position; absence of duty; correlative of no-right; opposite of duty
**liability**, 2, 5 --- Hohfeldian second-square position; susceptibility to another's power; correlative of power
**local minimum**, 10 --- bad precedent that courts cannot escape; locally stable but globally suboptimal doctrine

**Mahalanobis distance**, 4, A --- $\sqrt{(x-y)^T \Sigma^{-1} (x-y)}$; natural metric on the judicial manifold
**manifold**, *see* judicial complex

**no-right**, 2, 5 --- Hohfeldian first-square position; absence of claim; correlative of liberty; opposite of right
**Noether's theorem**, 9, A --- continuous symmetry $\to$ conservation law; applied to Hohfeldian gauge group to derive liability conservation

**objective hijacking**, 10, 12 --- plea bargaining as sycophancy; conviction-rate optimization as proxy worship

**parallel transport**, 9 --- carrying a legal rule along a citation path; stare decisis formalized
**path homology** ($\widetilde{H}_n^{\text{path}}$), 7 --- topological invariant of directed graphs; basis for constitutional review
**plea bargaining**, 10, 12 --- defendant agrees with prosecutor regardless of guilt; objective hijacking on the legal manifold
**power**, 2, 5 --- Hohfeldian second-square position; ability to change another's legal position; correlative of liability
**precedent**, 6, 9 --- prior decided cases; functions as heuristic field (Ch. 6) and parallel transport source (Ch. 9)
**precedential constraint** ($d_6$), 3, 6, 9 --- sixth legal dimension; weight of prior cases
**procedural posture** ($d_3$), 3 --- third legal dimension; stage of case (motion to dismiss, summary judgment, trial)
**public interest** ($d_8$), 3, 7 --- eighth legal dimension; impact on interests beyond the immediate parties

**rational basis review**, 7, 8 --- lowest constitutional review standard; most deferential to government
**remedial scope** ($d_7$), 3, 13 --- seventh legal dimension; damages, injunction, specific performance
**right** (claim), 2, 5 --- Hohfeldian first-square position; claim against another; correlative of duty; opposite of no-right

**Scalar Irrecoverability Theorem**, 1, A --- no continuous $\phi: \mathbb{R}^n \to \mathbb{R}$ ($n > 1$) is injective; binary verdicts and scalar sentences destroy legal structure irrecoverably
**scalar sentence**, 1 --- projection $\psi: \mathbb{R}^8 \to \mathbb{R}$; discards 7 dimensions
**sentencing disparities**, 1, 8, 11 --- gauge violations: outcomes depend on protected characteristics; 19.1% racial gap measured as $V_{\text{race}, \text{sentence}}$
**stare decisis**, 9 --- following precedent; formalized as parallel transport on the judicial complex
**statutory authority** ($d_4$), 3 --- fourth legal dimension; positive law governing the dispute
**strict scrutiny**, 7, 8 --- highest constitutional review standard; narrowly tailored to compelling interest
**Supremacy Clause**, 7 --- topological constraint removing state-law boundaries when they conflict with federal law

**treaty**, 14 --- international agreement; parallel transport between national legal manifolds

**Wilson loop** ($W(\ell)$), 5 --- closed cycle in citation network; non-trivial holonomy detects circuit splits

---

## People

**Austin, John**, 2 --- analytical jurisprudence; command theory of law
**Balkin, Jack**, 1, 7 --- living originalism; constitutional interpretation
**Cardozo, Benjamin**, 1, 6 --- *The Nature of the Judicial Process*; directive force of precedent
**Cook, Walter Wheeler**, 2 --- developed Hohfeldian analysis; Yale School
**Corbin, Arthur**, 2 --- developed Hohfeldian analysis; jural relations classification
**Dworkin, Ronald**, 1, 6 --- *Law's Empire*; law as integrity; fit and justification
**Fallon, Richard**, 1, 7 --- uneasy case for judicial review; constitutional theory
**Fuller, Lon**, 6 --- *The Morality of Law*; inner morality of law
**Hart, H. L. A.**, 2, 6 --- *The Concept of Law*; rule of recognition; legal positivism
**Hohfeld, Wesley Newcomb**, 2, 5 --- fundamental legal conceptions (1913, 1917); the $D_4$ taxonomy
**Holmes, Oliver Wendell, Jr.**, 1, 2 --- legal realism; *The Common Law*; "the life of the law has not been logic"
**Kelsen, Hans**, 7 --- pure theory of law; basic norm
**Langdell, Christopher Columbus**, 1 --- case method; law as science
**Llewellyn, Karl**, 2 --- legal realism; the common law tradition
**Posner, Richard**, 13 --- economic analysis of law; law and economics
**Rawls, John**, 8, 14 --- *A Theory of Justice*; veil of ignorance; law of peoples
**Raz, Joseph**, 2, 8 --- *The Authority of Law*; service conception of authority

---

## Institutions and Data Sources

**CourtListener**, 3, B --- open-access repository of court opinions; primary data source for judicial complex construction
**Federal Sentencing Guidelines**, 1, 11 --- U.S. Sentencing Commission guidelines; constrain judicial discretion within computed ranges
**International Court of Justice**, 14 --- principal judicial organ of the United Nations; global path-homology verifier
**Supreme Court of the United States**, 1, 5, 7, 8 --- final arbiter of circuit splits; constitutional review
**U.S. Sentencing Commission**, 1, 11 --- produces demographic sentencing reports; documents gauge violations

---

## Mathematical Objects and Notation

**$\mathbf{v} \in \mathbb{R}^8$** (attribute vector), 3, 4 --- point on the judicial manifold
**$\beta_k$** (boundary penalty), 4, 13 --- discrete cost of crossing regime boundary $k$
**$\text{BF}_{\text{law}}$** (legal friction), 4, 6 --- total path cost; $\sum w(v_i, v_{i+1})$
**$\mathcal{C}$** (constitutional subcomplex), 7 --- subcomplex of constitutionally relevant cases
**$d_1, \ldots, d_8$** (legal dimensions), 3 --- coordinates on the judicial manifold
**$D_4$** (dihedral group), 2, 5 --- $\langle r, s \mid r^4 = s^2 = e, \; srs = r^{-1} \rangle$
**$d(x,y)$** (legal distance), 4 --- $d_M(x,y) + \sum_k \beta_k \cdot \mathbb{1}[\text{boundary}_k]$
**$d_M(x,y)$** (Mahalanobis distance), 4 --- $\sqrt{(x-y)^T \Sigma^{-1} (x-y)}$
**$f(n) = g(n) + h_D(n)$** (A* evaluation), 6 --- accumulated cost + doctrinal heuristic
**$G_{\mathcal{Ho}} = D_4 \rtimes D_4$** (Hohfeldian gauge group), 5 --- 64-element gauge group
**$h_D(n)$** (doctrinal heuristic), 6 --- precedent-based estimate of cost-to-goal
**$\widetilde{H}_n^{\text{path}}$** (path homology), 7 --- topological invariant of the citation network
**$J_{\text{law}}$** (legal judgment function), 8 --- maps legal situations to legal outcomes
**$\mathcal{K}$** (judicial complex), 3 --- weighted directed simplicial complex of decided cases
**$\Sigma$** (covariance matrix), 4, 11 --- $8 \times 8$ SPD matrix encoding dimension interactions
**$\tau$** (gauge transformation), 8 --- legally irrelevant re-description
**$V_{ij}$** (gauge violation tensor), 8, 11 --- measures invariance failure: $J_j(\tau_i(x)) - J_j(x)$
**$W(\ell)$** (Wilson loop), 5 --- trace of holonomy around closed citation cycle
**$w(v_i, v_j)$** (edge weight), 4 --- $d(v_i, v_j)$; cost of doctrinal transition

---

*Note: This index framework provides chapter-level references. Final page numbers, sub-entries, and cross-reference refinements will be generated during typesetting from the compiled manuscript. Entries marked with "see" or "see also" indicate planned cross-references to be verified against the final chapter text.*

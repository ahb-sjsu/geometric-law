# Appendix C: Notation and Conventions

This appendix collects the notation used throughout the book. Conventions are consistent with the Geometric Series (*Geometric Methods*, *Geometric Reasoning*, *Geometric Ethics*, *Geometric Economics*). Where legal-specific notation diverges from or extends the series conventions, the divergence is noted.

---

## C.1 The Judicial Complex

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $\mathcal{K}$ | Judicial complex (weighted directed simplicial complex) | Ch. 3 |
| $V(\mathcal{K})$ | Vertex set of $\mathcal{K}$ (decided cases) | Ch. 3 |
| $E(\mathcal{K})$ | Edge set of $\mathcal{K}$ (doctrinal relationships) | Ch. 3 |
| $\mathbf{v} \in \mathbb{R}^8$ | Attribute vector of a case | Ch. 3 |
| $d_1, \ldots, d_8$ | Eight legal dimensions | Ch. 3 |
| $d_1$ | Entitlement structure | Ch. 3 |
| $d_2$ | Factual nexus | Ch. 3 |
| $d_3$ | Procedural posture | Ch. 3 |
| $d_4$ | Statutory authority | Ch. 3 |
| $d_5$ | Constitutional conformity | Ch. 3 |
| $d_6$ | Precedential constraint | Ch. 3 |
| $d_7$ | Remedial scope | Ch. 3 |
| $d_8$ | Public interest | Ch. 3 |
| $\mathcal{C} \subseteq \mathcal{K}$ | Constitutional subcomplex | Ch. 7 |

---

## C.2 The Legal Metric

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $\Sigma \in \mathbb{R}^{8 \times 8}$ | Covariance matrix of legal dimensions | Ch. 4 |
| $\sigma_{ij}$ | Entry $(i,j)$ of $\Sigma$ | Ch. 4 |
| $d_M(x, y)$ | Mahalanobis distance: $\sqrt{(x-y)^T \Sigma^{-1} (x-y)}$ | Ch. 4 |
| $\beta_k$ | Boundary penalty for regime transition $k$ | Ch. 4 |
| $d(x, y)$ | Full legal distance: $d_M(x, y) + \sum_k \beta_k \cdot \mathbb{1}[\text{boundary}_k]$ | Ch. 4 |
| $\text{BF}_{\text{law}}$ | Legal friction (total path cost on $\mathcal{K}$) | Ch. 4 |
| $w(v_i, v_j)$ | Edge weight: $d(v_i, v_j)$ | Ch. 4 |

---

## C.3 The Hohfeldian Gauge Group

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $D_4$ | Dihedral group of order 8 (symmetry group of the square) | Ch. 2 |
| $r$ | Correlative rotation generator ($r^4 = e$) | Ch. 2 |
| $s$ | Jural negation generator ($s^2 = e$, $srs = r^{-1}$) | Ch. 2 |
| $G_{\mathcal{Ho}} = D_4 \rtimes D_4$ | Full Hohfeldian gauge group (64 elements) | Ch. 5 |
| First square | Right, Duty, Liberty, No-right | Ch. 2 |
| Second square | Power, Liability, Immunity, Disability | Ch. 2 |

---

## C.4 Invariance and Gauge Theory

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| LIP | Legal Invariance Principle | Ch. 8 |
| JBIP | Judicial Bond Invariance Principle | Ch. 8 |
| $\mathcal{T}_{\text{irrelevant}}$ | Set of legally irrelevant transformations | Ch. 8 |
| $\tau \in \mathcal{T}$ | A specific gauge transformation | Ch. 8 |
| $J_{\text{law}}(x)$ | Legal judgment function | Ch. 8 |
| $V_{ij}$ | Gauge violation tensor: $J_j(\tau_i(x)) - J_j(x)$ | Ch. 8 |
| LBI | Legal Bond Index: aggregate gauge violation measure | Ch. 8 |

---

## C.5 Topology and Constitutional Review

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $\Omega_n(G)$ | Path chain group of degree $n$ | Ch. 7 |
| $\partial_n$ | Boundary operator: $\Omega_n \to \Omega_{n-1}$ | Ch. 7 |
| $\widetilde{H}_n^{\text{path}}(G)$ | Path homology group of degree $n$ | Ch. 7 |
| $\beta_n = \text{rank}(\widetilde{H}_n^{\text{path}})$ | Betti number of degree $n$ | Ch. 7 |
| $W(\ell)$ | Wilson loop around closed cycle $\ell$ | Ch. 5 |

---

## C.6 Precedent and Parallel Transport

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $h_D(n)$ | Doctrinal heuristic at vertex $n$ | Ch. 6 |
| $f(n) = g(n) + h_D(n)$ | A* evaluation function | Ch. 6 |
| $g(n)$ | Accumulated path cost to vertex $n$ | Ch. 6 |
| $\nabla$ | Legal connection (parallel transport rule) | Ch. 9 |
| $P_\gamma$ | Parallel transport along path $\gamma$ | Ch. 9 |
| $\text{Hol}(\ell)$ | Holonomy around loop $\ell$ | Ch. 9 |

---

## C.7 Failure Modes

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| HC | Heuristic corruption | Ch. 10 |
| OH | Objective hijacking | Ch. 10 |
| LM | Local minimum | Ch. 10 |
| GB | Gauge breaking | Ch. 10 |

---

## C.8 Conventions

**Indices.** Latin indices $i, j, k$ range over the eight legal dimensions $\{1, \ldots, 8\}$. Greek indices $\mu, \nu$ are used for general tensor components when the context is inherited from the physics literature (gauge theory, parallel transport).

**Summation.** The Einstein summation convention (repeated indices are summed) is used sparingly and only when explicitly noted. Most sums are written explicitly.

**Epistemic tags.** Each substantive claim in the book is tagged with one of five epistemic status labels:
- **[Established Mathematics.]** — standard results
- **[Legal Doctrine.]** — established legal principles
- **[Modeling Axiom.]** — structural choices
- **[Conditional Theorem.]** — results following from axioms
- **[Speculation/Extension.]** — forward-looking claims

**Series references.** Books in the Geometric Series are cited as Bond (2026a) through Bond (2026h), corresponding to *Geometric Methods* (a), *Geometric Reasoning* (b), *Geometric Ethics* (c), *Geometric Economics* (d), *Geometric Law* (e, this volume), *Geometric Cognition* (f), *Geometric Communication* (g), and *Geometric Medicine* (h).

**Running example.** All chapter-opening scenarios feature Judge Elena Rivera, a fictional federal district court judge in San Francisco. Rivera's cases are constructed to illustrate every geometric structure in the book; they are not based on actual cases or persons.

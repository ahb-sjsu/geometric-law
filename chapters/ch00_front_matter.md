# Geometric Law: Symmetry, Invariance, and the Structure of Legal Reasoning

**Andrew H. Bond**
Senior Member, IEEE
Department of Computer Engineering
San Jose State University
andrew.bond@sjsu.edu

Spring 2026

---

## Preface

This book argues that the law has a hidden mathematical structure — and that making it visible could transform how we think about constitutional review, judicial consistency, and legal AI.

The argument begins with a simple observation: the entire legal system — every statute, every constitutional provision, every court opinion — is written in natural language. And natural language is inherently ambiguous. What does "equal protection" *mean*? Does "arms" in the Second Amendment include assault rifles? Does "commerce among the several states" cover wheat grown for personal consumption? Every landmark case in American constitutional law turns on the interpretation of a phrase.

Behind all that language, legal reasoning has *geometric structure* — a shape — that the words obscure. This book constructs that shape formally, using the same mathematics that describes gauge symmetry in physics, topological invariance in mathematics, and optimal pathfinding in computer science. The result is a framework in which constitutional review becomes a topological computation, equal protection becomes a gauge symmetry, sentencing consistency becomes a measurable index, and legal reasoning itself becomes A* search on a judicial manifold.

The central construction is the **judicial complex** $\mathcal{K}$ — a weighted directed simplicial complex whose vertices are decided cases, whose edges are doctrinal relationships, and whose attribute vectors encode eight dimensions of legal significance. On this complex, we define invariance principles (legal judgments must not depend on legally irrelevant features), gauge structure (the Hohfeldian octad forms a $D_4 \rtimes D_4$ gauge group), conservation laws (liability is conserved in closed disputes), and constitutional constraints (a statute is constitutional if and only if it preserves the path homology of the constitutional subcomplex).

This is the fifth book in the Geometric Series. *Geometric Methods* (2026a) provides the mathematical toolkit. *Geometric Ethics* (2026b) develops the moral manifold. *Geometric Reasoning* (2026c) establishes the general framework of search on geometric spaces. *Geometric Economics* (2026d) instantiates it on the economic decision manifold. The present book instantiates it on the judicial manifold, inheriting the D₄ Hohfeldian structure first discovered in the ethics framework.

Andrew H. Bond
San Jose, California
March 2026

---

## Core Objects at a Glance

| Object | What It Is | Where Developed |
|--------|-----------|-----------------|
| **Judicial complex** $\mathcal{K}$ | Weighted directed simplicial complex of decided cases and doctrinal relationships | Ch. 3 |
| **8 legal dimensions** | Entitlement, factual nexus, procedure, statutory authority, constitutionality, precedent, remedies, public interest | Ch. 3 |
| **Legal Invariance Principle** (LIP) | Legal judgments must be invariant under legally irrelevant transformations | Ch. 8 |
| **Hohfeldian octad gauge group** | $D_4 \rtimes_\varphi D_4$ — the symmetry group of jural relations | Ch. 5 |
| **Legal Bond Index** | Quantitative measure of judicial inconsistency under gauge transformations | Ch. 8 |
| **Path homology** | Topological invariant of directed graphs; constitutionality = homology preservation | Ch. 7 |
| **Doctrinal heuristic** $h_D(n)$ | Legal doctrine as A* heuristic function guiding search through $\mathcal{K}$ | Ch. 6 |
| **Precedential weight deformation** | Stare decisis as local modification of edge weights | Ch. 9 |
| **Legal friction** BF$_{\text{law}}$ | Total cost of a litigation path through the judicial complex | Ch. 4 |

## Key Results at a Glance

| Finding | Source |
|---------|--------|
| Equal protection is a gauge symmetry (Theorem 7.2) | AJ manuscript |
| Constitutionality iff path homology preserved (Theorem 6.1) | AJ manuscript |
| Liability conserved in closed bilateral disputes (Theorem 7.1) | AJ manuscript |
| Hohfeldian relations form $D_4 \rtimes D_4$ (Theorem 5.1) | AJ manuscript |
| Due process = well-definedness on quotient space (Theorem 7.3) | AJ manuscript |
| Cross-lingual legal invariance (109K passages, 11 languages) | Geometric Ethics |
| Legal Bond Index baseline: 0.155 | Geometric Ethics |

Note: Theorem numbers refer to the companion paper *Algorithmic Jurisprudence* (Bond, 2026), not to chapter numbers in this book.

## How to Read This Book

- **The theoretical path**: Chapters 1–9. From the scalar failure of binary verdicts through the full geometric framework.
- **The applied path**: Chapters 10–15. Failure modes, sentencing, adversarial system, contracts, international law, AI.
- **The constitutional path**: Chapters 7, 8, and the worked examples. How to test constitutionality topologically.
- **The fast path**: Chapters 1, 5, 7, 8. Binary verdicts fail; Hohfeld is D₄; constitutionality is topology; equal protection is gauge invariance.

Each chapter opens with a running example — Judge Elena Rivera, a federal district court judge — that grounds the abstract framework in judicial decision-making.

---

## Epistemic Status Classification

| Tag | Meaning | Approx. Count |
|-----|---------|---------------|
| **[Established Mathematics.]** | Standard results from topology, group theory, graph theory | ~15 |
| **[Legal Doctrine.]** | Established principles of law (equal protection, due process, stare decisis) | ~8 |
| **[Modeling Axiom.]** | Structural choices (8 dimensions, Mahalanobis metric, path homology for constitutionality) | ~10 |
| **[Conditional Theorem.]** | Results following from axioms (LIP → gauge invariance, conservation, optimality) | ~12 |
| **[Speculation/Extension.]** | Forward-looking claims (AI implementation, cross-jurisdictional metrics) | ~8 |

---

## Table of Contents

### Part I: The Problem
1. The Binary Verdict and the Scalar Sentence
2. Hohfeld's Original Insight — Geometry Before Geometry

### Part II: The Framework
3. The Judicial Reasoning Space
4. The Legal Metric
5. The D₄ Hohfeldian Group
6. Precedent as Heuristic Field

### Part III: Dynamics and Symmetry
7. Constitutional Review as Path Homology
8. Equal Protection as Gauge Invariance
9. Stare Decisis as Parallel Transport

### Part IV: Failure Modes
10. Legal Failures as Geometric Pathologies
11. Sentencing Disparities as Gauge Violation Tensors
12. The Adversarial System as Manifold Exploration

### Part V: Applications
13. Contract Law as Boundary Construction
14. International Law as Multi-Manifold Diplomacy
15. AI Legal Reasoning

### Part VI: Horizons
16. Open Questions

### Appendices
A. Mathematical Prerequisites (Topology, Group Theory)
B. The NLP Pipeline for Judicial Complex Construction
C. The Algorithmic Jurisprudence Paper (Full Reference)

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $\mathcal{K}$ | Judicial complex |
| $d_1, \ldots, d_8$ | Eight legal dimensions |
| $\Sigma$ | 8×8 covariance matrix of legal dimensions |
| $\beta_k$ | Regime boundary penalty |
| $h_D(n)$ | Doctrinal heuristic function |
| $\text{BF}_{\text{law}}$ | Legal friction (total litigation path cost) |
| $G_{\mathcal{Ho}}$ | Hohfeldian gauge group ($D_4 \rtimes D_4$) |
| LIP | Legal Invariance Principle |
| JBIP | Judicial Bond Invariance Principle |
| $\widetilde{H}_n^{\text{path}}$ | Path homology groups |
| $\mathcal{C}$ | Constitutional subcomplex |
| $W(\ell)$ | Wilson loop around legal cycle $\ell$ |

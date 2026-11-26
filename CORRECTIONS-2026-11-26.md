# Geometric Law: corrections of 2026-11-26

These corrections were made on 2026-11-26 at the author's direction after a review of the series.

Each item says where the text is, what it said, what it says now, and how the right value or statement was established. No figure file and no figure caption was changed.

## Reconciled

1. **Chapter 11, worked example, Step 4 (total gauge violation).** The text said the 25 cells sum to 2.520. It now says 2.340. The 25 printed cells, the five printed row sums (0.624, 0.479, 0.637, 0.156, 0.444) and the five printed column sums (0.583, 0.825, 0.174, 0.290, 0.468) all add to 2.340.

2. **Chapter 11, running example "Rivera decomposes the tensor".** The text gave singular values 0.42 and 0.19, accounting for 58% and 22% of the violation, with printed singular vectors, and said two interventions would eliminate 80%. A singular value decomposition of the five by five table printed in the same running example gives singular values 0.591, 0.144, 0.072, 0.041 and 0.004. By the chapter's own formula in its Technical Appendix (share of the sum of squared singular values) the first two modes carry 92.7% and 5.5%. The text now gives 0.59 and 93%, 0.14 and 6%, the recomputed vectors u1 = (0.55, 0.38, 0.62, 0.13, 0.39), w1 = (0.50, 0.73, 0.15, 0.23, 0.37), u2 = (0.09, 0.83, -0.48, 0.15, -0.23), w2 = (0.30, -0.59, -0.05, 0.10, 0.74), and "about 98%" for the two modes together. The first mode is now described as dominated by socioeconomic status (0.62) and race (0.55), where the text had race first. The story of the example (a race and class mode in bail and sentencing, and a gender mode in departures) is unchanged. The second mode is much smaller than the text had said.

3. **Chapter 11, "Decomposability".** The text called the Legal Bond Index "the trace (or norm) of the tensor" and said it is recovered "by summing". The formula printed beside it is the mean of all entries. The text now says "the mean of the entries" and "by averaging".

4. **Chapter 15, Technical Appendix, minimum sample size.** The text said that for d = 768, epsilon = 0.05 and delta = 0.05 the bound gives about 500 examples. The expression printed inside the bound, (d + log(8/delta)) / epsilon squared, is about 309,000 for those values. The text now gives that value and says the figure of 500 is the recommendation of the Algorithmic Jurisprudence manuscript (as Step 2 of the chapter states) and does not follow from the bound.

5. **Chapter 15, Step 3, "Regularization".** The text said the number of scored cases is always small relative to the number of dimensions, "given that the minimum recommended sample is 500 cases". Five hundred cases is not small relative to eight dimensions. The text now says that 500 comfortably exceeds eight dimensions and that a domain-specific subset may be far smaller.

6. **Chapter 15, running example, the Martinez scores.** The text said the maximum discrepancy is on the second dimension. The printed scores differ by 0.05 on each of the first four dimensions and by less on the others. The text now says the maximum discrepancy is 0.05, on dimensions one through four.

7. **Chapter 6, "Inadmissible Heuristics in Legal Practice".** A paragraph said an overaggressive theory is inadmissible through underestimation, with h greater than the true cost, and the next paragraph began "Wait — this is backwards." The wrong paragraph and the draft remark were removed. The corrected account that followed them is kept as it was.

8. **Chapter 6, proof sketch of the admissibility theorem.** A parenthesis said an element "might be easier to prove than estimated", which contradicts the claim it supported, that each estimate is a lower bound. The parenthesis was removed and the sentence now says the lower bound holds under the theorem's hypothesis.

9. **Chapter 6, Technical Appendix, heuristic field strength.** The displayed formula reduced to the constant 1. It now displays the formula the same paragraph gave "in practice", the heuristic estimate divided by the true remaining cost, which is 1 for a tight heuristic and 0 for the zero heuristic.

10. **Chapter 7, the theorem and the conjecture.** The Topological Constitutionality Theorem and the Completeness Conjecture stated the same equivalence. One sentence after the theorem now relates them: the equivalence holds within the model, where a violation is a change in path homology, and that no violation escapes that description is the conjecture. The Technical Appendix already stated the theorem in three one-directional parts.

11. **Chapter 7, "The Finite Computation".** The text gave O(n^3) for p = 1 while naming a matrix of n^2 rows and n^3 columns. The Technical Appendix gives O(n^(3(p+1))), which is O(n^6) for p = 1. The body now cites the appendix bound.

12. **Chapters 5 and 7, directed cycles in an acyclic citation graph.** Chapter 3 states that the temporal citation subgraph is acyclic, while Wilson loops and path homology use directed cycles. One sentence in each chapter now says that a closed path must include an edge that is not a forward citation, as the chapters' own examples do (the return comparison in Chapter 5, the edges a statute adds in Chapter 7).

13. **Chapter 8, the forms of the Legal Bond Index.** The index is stated as a mean absolute change in Chapters 5 and 8, as a mean relative change in the Technical Appendix of Chapter 8 and in Chapter 11, and with Mahalanobis distances between system outputs in Chapter 15. A short paragraph after the definition in Chapter 8 now names the forms and says their values are not directly comparable. Chapter 15's Technical Appendix now says its normalizer differs from the one in the body definition. Which form is the definition is listed under Unresolved.

14. **Chapters 10, 11 and 15, where the index is defined.** Chapter 10 said "defined in Chapter 5", Chapter 11 said "Chapter 8 introduced", Chapter 15 said "introduced in Chapter 5". The index is defined briefly in Chapter 5 and in full in Chapter 8. All three now say Chapters 5 and 8.

15. **Chapter 8, running example "Rivera quantifies the violation".** The chapter predicts the index should be smallest for race. The running example then said its numbers, largest for race, "match the tiers of scrutiny in a troubling way". The text now says they invert the ordering the tiers predict.

16. **Chapter 4, the edge weight.** The underbrace labelled the quadratic form "Mahalanobis distance", though the chapter defines that distance with a square root and the worked example adds the squared value. The label now reads "squared Mahalanobis distance".

17. **Chapter 4, legal friction.** The body formula adds boundary penalties as a separate term, although the edge weights already contain them, and the Technical Appendix gives the form without the separate term. The first item under the formula now says the penalties are written out separately and counted once, and points to the appendix form.

18. **Chapter 12, worked example.** The running example settles the case, and the worked example then began "EJAC v. City of San Francisco goes to trial" and ended with the judge entering a "consent decree" after trial. The scenario now begins "Suppose the settlement conference had failed", and the decision reads "enters judgment".

19. **Chapter 12, Technical Appendix, settlement existence.** The proposition defined both probabilities as estimates of plaintiff success, while its inequality and the body of the chapter use the defendant's estimate of the defendant winning. The definition now matches the body.

20. **Chapter 14, Technical Appendix, impossibility region.** The proposition named two dimensions and used one. It now names one.

21. **Chapter 1, Technical Appendix.** The theorem spoke of a continuous function from the eight-dimensional space to {0, 1}. Such a function is constant, and the proof sketch uses two regions. The word "continuous" was removed there. The corollary on the scalar sentence keeps it, where it is needed.

22. **Chapter 0, "Key Results at a Glance".** The table gave only the theorem numbers of the companion paper as the source. It now gives the chapter of this book where each result is stated, keeps the companion paper's number, and labels the results as conditional theorems.

23. **Front matter, appendix B and the index: the 0.155 baseline.** The front matter, Appendix B and the index called 0.155 the baseline of the Legal Bond Index, and Appendix B said it "indicates moderate gauge violation in the legal systems studied". Chapters 5 and 8 say it is the moral-domain Bond Index of *Geometric Ethics* and that the legal baseline remains to be measured. The front matter, Appendix B and the index now say the same.

Checked and found consistent, so not changed: Chapter 14 says the set of compliant positions is empty and the impossibility region is non-empty. These are the same statement.

## Marked as illustrative or simulated

1. **Chapter 0 and the front matter, "How to Read This Book".** One sentence now says that Judge Rivera, her docket, the studies and systems she meets, and every figure computed in the running examples and worked examples are illustrative or hypothetical, and none is a measurement.

2. **Chapter 8, running example "Rivera quantifies the violation".** The table of indices was introduced as computed from "the Sentencing Commission's data for her district". It is now introduced as illustrative figures for the running example, not Sentencing Commission statistics.

3. **Chapter 11, running examples.** The district tensor, its decomposition and its intersectional terms are now introduced as illustrative.

4. **Chapter 10, opening running example.** The study that "crosses her desk" is now marked hypothetical.

5. **Chapter 15, running example "Rivera's LIP test".** The results are now headed hypothetical, and "confirming that the embedding is capturing legal content" now reads "which in the example indicates".

6. **Chapter 16, Open Problem 1, "What We Know".** The text said the Algorithmic Jurisprudence manuscript "demonstrated" a Spearman correlation of 0.72 on 10,000 federal opinions. No record of that run is in this repository, Chapter 4 says the calibration programme "has not yet been executed on legal data", the front matter says the metric "has not been calibrated from large-scale case data", and the README of 2026-07-14 calls the framework posited. The sentence now says the manuscript "reports" the result and that it is not reproduced in this book.

7. **Chapter 2, "International Convergence", and the key-results tables.** "The empirical evidence from the Geometric Ethics programme confirms this" now reads that the programme reports evidence consistent with it, classed as exploratory and model-mediated in that volume's claim ledger (row GE-CROSSLINGUAL). The key-results rows on cross-lingual invariance carry the same label.

8. **Front matter, "The results".** The sentence listing results now says they are quoted from other sources, and gives the confidence interval that *Geometric Ethics* prints for deontic transfer, [99.96%, 100%], measured through a multilingual embedding model. It had said "99.7% CI".

## Withdrawn or updated

*Geometric Ethics* withdrew the dihedral group D4 as the symmetry group of the four Hohfeldian positions in its version 1.25 (2026-11-08). The correlative and the opposite are commuting involutions and generate the Klein four-group V4, of order 4. There is no quarter-turn. The same version restated the group of the full octad as a conjecture, V4 semi-direct V4, not proved.

In this volume the rotation r was defined by applying the correlative at two positions and the opposite at the other two. The chapter's own Technical Appendix states that the correlative is an involution that swaps the two correlative pairs. The quarter-turn is therefore not one of Hohfeld's operations and is not generated by them.

1. **Chapter 2.** A dated note stands at the head of "Why This Is Group Theory". It says what was withdrawn, what stands (the tables of correlatives and opposites, the bilateral bond, invariance under the correlative swap and under V4, the correlative involution, the conservation of bond charge) and what is withdrawn pending restatement (the quarter-turn, order 4, the dihedral relation, the eight elements, non-commutativity, D4 semi-direct D4). Short dated notes stand at the head of four further sections. Marked withdrawn at their statements: the rotation r, "The Dihedral Relations", the table of eight elements, "Why D4 and Not Some Other Group", the eight symmetries of "The Geometric Interpretation", the minimality argument, and the Theorem (Hohfeldian D4) of the Technical Appendix. Restated for V4 where the statement is true as written: the opening paragraph, the sentence on the second square, the remark on deontic logic, the two worked-example sentences, and the chapter summary.

2. **Chapter 5.** The chapter title is now "The Hohfeldian Gauge Group". A dated note stands at the head of the chapter. Marked withdrawn pending restatement: the Octahedral Gauge Group theorem and its full statement in the Technical Appendix, "Why Semi-Direct, Not Direct", "The Order of the Group", the two paragraphs on the non-abelian commutator in the curvature, and the section "The Non-Commutativity of Legal Operations". The chapter summary is restated.

   The worked example (opposite, identity, opposite) uses only that the opposite applied twice is the identity. It stands as written.

   The running example uses the symbol r only for the correlative swap, from the city's liberty to the individual's no-right. The dated note says that with r read as the correlative involution c the loop is cs, e, e, s, with product c, a non-trivial element of V4, so the example stands with holonomy the correlative swap. The text of the running example itself was not rewritten.

3. **Chapter 8.** A dated note stands at the head of "The Judicial Bond Invariance Principle". The section had identified the bond-preserving transformations with D4 semi-direct D4 and called the equal protection group a subgroup of that group. A group that only relabels Hohfeldian positions contains no change of a protected characteristic. The text now names the group of bond-preserving transformations, as the chapter's Technical Appendix already does, and says the Hohfeldian relabelings and the equal protection group are both subgroups of it.

4. **Chapters 1, 3, 9 and 16.** Sentences that named D4 or D4 semi-direct D4 now name V4 or point to the dated notes. Chapter 16 no longer says that non-commutativity is captured by the semi-direct product.

5. **Order effects cited from *Geometric Ethics*.** Chapters 5 and 16 said that 16,798 commutator measurements "demonstrate" or "empirically confirm" non-commutativity. *Geometric Ethics* (Chapter 17, and its change note for v1.25) records that result as observed in one language model and not yet tested in people. The three sentences now say that.

6. **Front matter, Chapter 0, Appendix A, Appendix C, the index and the table of contents.** Every place that advertised D4, D4 semi-direct D4 or 64 elements now states V4 and the withdrawal. Appendix A keeps the definitions of the dihedral group and the semi-direct product, which are standard mathematics, and marks their legal interpretations withdrawn.

7. **Chapter 1, "The Moral Contraction Parallel": Conservation of Harm.** The text cited "the conservation of harm (derived from Noether's theorem applied to the moral gauge group)" as a result of *Geometric Ethics*. That volume withdrew the conservation law for harm on 2026-06-19 (its ledger row GE-HARM-CONSERVATION) and kept the weaker claim, representation-invariance of harm accounting. The sentence now states the weaker claim and gives the date of the withdrawal. The sentence on the conservation of liability in law, which rests on the correlative pairs, is unchanged.

Restatements that need new mathematics, and were therefore marked and not attempted: the symmetry group of the full octad and its coupling homomorphism, a V4 form of the eight-element table, the minimality argument, and any account of why the order of legal tests matters.

The SU(2) gauge prediction and hysteresis, which *Geometric Ethics* records as refuted, are not cited in this volume.

## Unresolved

1. **The 63% gender figure (Chapters 1 and 10).** Chapter 1 says female defendants receive sentences "approximately 63% shorter" than male defendants. Chapter 10 says male defendants receive sentences "approximately 63% longer" than female defendants. Both cite Starr (2015). The two cannot both hold: 63% longer for men is about 39% shorter for women. The paper is not in the repository, so neither was changed. The author needs to check the paper and make the two chapters agree. If Chapter 1 changes, the caption of Figure 1.1 and the figure itself may need the same change.

2. **The hierarchical cost between courts of the same level (Chapters 3 and 4).** Chapter 3's definition says binding precedent has the level of the cited court greater than or equal to that of the citing court, and its worked example gives cost 0 from one Supreme Court case to another. Chapter 4's formula gives the persuasive cost eta at the same level and infinity from a lower court to a higher one, and its next paragraph says a district court opinion is persuasive to a circuit court at cost eta. These are three rules. The choice is a modeling decision. The author needs to fix one rule and make the definition, the formula, the paragraph and the Chapter 3 example agree.

3. **How many theories survive the motion to dismiss (Chapter 12, running example).** Phase 1 says two of five theories are removed and three survive, and names two dismissed and two sustained. Phase 5 says the search space has been pruned to two viable theories. Either the count in Phase 1 or the count in Phase 5 is wrong, or a fifth theory is missing from the text. The author needs to say which.

4. **The Spearman correlation of 0.72 on 10,000 federal opinions (Chapter 16).** The sentence now says "reports". No record of the run is in this repository. The author needs to supply the record, or remove the figure.

5. **The baseline 0.155 from 20,030 normative evaluations (Chapters 5 and 8, front matter, Appendix B, index).** The figure is attributed to *Geometric Ethics*. It does not appear in the current edition of that volume (v1.28), which since v1.26 defines the Bond Index as a mean deviation over a tolerance. The author needs to give the source of 0.155 or remove it.

6. **The 109,000 passages in 11 languages (front matter and Chapter 0).** The front matter says they come from the legal-retrieval Kaggle competition. *Geometric Ethics* describes a cross-lingual corpus of 109,294 passages of normative text spanning 3,000 years. The author needs to say which corpus is meant and whether any of it is legal text.

7. **Which form of the Legal Bond Index is the definition.** The forms are now named and related (Reconciled, item 13). Chapter 15 gives two different normalizers of its own, the distance to the mean output in the body and the expected distance between two outputs in the appendix. The thresholds and example values in the book (0.05, 0.08, 0.19) are stated without saying which form they belong to.

8. **The legal connection (Chapters 5, 8 and 9).** Chapter 9's formal definition writes the connection as a sum of real weights times group elements, which is not an element of the group, and its critical-point criterion takes a matrix norm of the Wilson loop minus the identity, while Chapter 5 takes the Wilson loop to be an element of a finite group. Appendix A defines the Wilson loop as a trace. A restatement needs mathematics and was not attempted.

9. **Feasibility of path homology at scale (Chapter 7).** The chapter says the computation is feasible for a subcomplex with millions of vertices and that implementations "have been validated on graphs of comparable size". No source is given, and the bound in the same chapter is O(n^6) for the first homology group. The author needs a source or a weaker sentence.

10. **Sentencing figures stated as data (Chapter 8).** "The U.S. Sentencing Commission data suggests that the racial index for federal sentencing is approximately 0.19. State-level data suggests even higher values." The first restates the 19.1% figure as an index. No source is given for the second.

11. **Statistical significance of a tensor entry (Chapter 11, Technical Appendix).** The proposition gives a normal distribution with mean zero for an entry that is a mean of absolute values. Under the null hypothesis such a mean is positive. A restatement needs the signed tensor and was not attempted.

12. **The running example of Chapter 12.** The hypothetical appeal speaks of a jury verdict, and the worked example speaks of a bench trial. Each is a separate hypothetical, so nothing was changed, but the author may wish them to agree.

## Integration of the Legal Bond Index paper (2026-11-26)

The paper is "The Legal Bond Index: A Matched-Neighbourhood Diagnostic of Algorithmic Disparity, Applied to COMPAS" (Bond), accepted by the *Journal of Science and Law* and in press. The book cites it as in press, with no volume or page. Every number was taken from the accepted text (`lbi_manuscript.tex`) and checked against `outputs/revision2_results.json`. The two agree to the printed precision. No figure file and no figure caption was changed. No running example was changed, and no real figure was attached to Judge Rivera's docket.

### What was added, and where

1. **Chapter 8, new section "The Measured Form of the Index"**, placed after "The Wilson Loop Test" and before "The Tiers of Scrutiny as Gauge-Breaking Terms". Nine subsections. "One Measurement on Legal Data" says what the measurement is and that the paper makes no use of this book's framework. "The Matched-Neighborhood Definition" gives the paper's definition. "How This Form Relates to the Others" calls the earlier forms transformation forms (theoretical, equal to 0 under invariance, not computed on legal data) and the paper's form a comparison form (a ratio centered on 1, the operational form), and says the scales must not be mixed. "The COMPAS Result" gives the data, the curve over six scales for race and sex, the threshold result and the focal-group asymmetry. "What Reduces the Figure" gives the distance ratio 1.28 and the table of matching-parity specifications (1.00 to 1.02). "The Test" gives the conditional randomization result. "The Two-Sided Reading" restates the paper's summary. "What the Measurement Does Not Show" lists eight limits and quotes "a research-stage screening signal that may contribute one input to an audit, not a validated regulatory audit standard". "Relation to the Impossibility Results" covers Chouldechova and Kleinberg et al. and says what the Lean file states and what it does not.

2. **Chapter 8, smaller changes.** One paragraph after the definition names the measured form as a further form. "Empirical Baseline" now says that 0.19 restates the Commission's 19.1% and is not a computed index, that one computation exists on a different scale, and that the baseline for the forms defined in the chapter remains unmeasured. Summary item 4 no longer says the index "is empirically measurable from existing data" without qualification. Summary item 9 is new. The Notes on Sources cite the paper, ProPublica, the vendor's reply and the two impossibility papers.

3. **Chapter 15, new section "Testing Invariance from Recorded Data"**, placed after "The Legal Bond Index in Practice" and before Worked Example 1. Five subsections: when the swap test is not available, the paper's four-step screening procedure, why the permutation test fails (with the table of three null constructions), the validation on scores with known structure (with the seven-row table), and what the chapter takes from the paper, including its limits. Criterion 2 now points to this section. The paragraph on comparability says the measured form is on another scale and the 0.05 threshold does not apply to it. Summary item 7 is new. The Notes on Sources cite the paper.

4. **Chapter 16, new section "What Has Been Measured"**, placed before Open Problem 1. It lists what is known from the one measurement and what is not, and says the measurement leaves the five open problems open and does not calibrate the legal metric. One sentence under "Sensitivity analysis" in Open Problem 1 reports the paper's sensitivity result and says it concerns a different metric. Summary item 8 is new. The Notes on Sources cite the paper.

5. **Chapter 5.** After the sentence that the legal baseline remains to be measured, one paragraph says a measurement exists in a different form on a different scale and that the baseline for the form defined there is still unmeasured. "Measuring the LBI in Practice" gains a paragraph on the third route, comparison of recorded cases.

6. **Chapter 10, "Breaking the Feedback Loop".** One paragraph after the remedy "Measure and publish the LBI" says what the one measured index shows a publication would need (matching diagnostics, intervals, a calibrated test) and that the paper proposes no benchmark.

7. **Chapter 11.** "The Matching Problem" gains the matched-neighborhood comparison as a method and a caution on match quality. "Setting Benchmarks" gains the measured null level (1.009 in simulation, 1.015 as the centre of the calibrated null). The Technical Appendix gains a remark on randomization tests after the proposition on statistical significance. Summary item 2 and the Notes on Sources are extended.

8. **Front matter and Chapter 0.** The key-results tables gain a row for the measurement with its attenuation and its status, and the row for 0.155 now reads "no legal value on that scale has been measured". The core-objects row for the index names the measured form. The Series Foreword gains a paragraph on the paper. The Preface sentence on 19.1% is followed by a sentence that attributes the figure to the Sentencing Commission and points to Chapter 8.

9. **Back matter and appendices.** The bibliography has a new section, "Algorithmic Fairness and Risk Assessment", with the paper (in press) and four sources. The table of contents entries for Chapters 8, 15 and 16 mention the new sections. The index has new entries (caliper, conditional randomization test, matched-neighborhood ratio, matching parity, permutation test, COMPAS, and the symbol for the ratio) and a revised entry for the Legal Bond Index. Appendix B says its code is the transformation form and points to the paper's archive for the measured form. Appendix C has two new notation rows.

### Effect on the earlier Unresolved items

- **Item 5 (the source of 0.155).** Left open. The paper does not contain the figure. The book now says in each place that the measured ratio is on a different scale and cannot be set beside 0.155. The source of 0.155 is still needed.

- **Item 7 (which form of the index is the definition).** Partly settled. The book now says plainly that the paper's matched-neighborhood ratio is the measured, operational form, and that the forms of Chapters 5, 8, 11 and 15 are theoretical forms that have not been computed on legal data. Which of the theoretical forms is the definition is still open, as are the two normalizers of Chapter 15. The values 0.05, 0.08 and 0.19 are now said not to be on the scale of the measured form. Which theoretical form each belongs to is still not stated.

- **Item 10 (sentencing figures stated as data, Chapter 8).** Partly settled. The text now says that 0.19 restates the Commission's 19.1% as a relative change and is not a computed index. "State-level data suggests even higher values" still has no source and was not changed.

- **Item 11 (statistical significance of a tensor entry, Chapter 11).** Left open. The new remark gives the calibrated alternative for matched estimates and says it has been established for one index on one dataset only. The proposition itself was not restated.

- **Statements that the legal baseline is unmeasured** (Chapters 5 and 8, front matter, Chapter 0, Appendix B, index; Reconciled item 23). Qualified, not removed. No value of the transformation forms has been measured for any court or dataset. One value of a different form has been measured for one algorithm.

### New points for the author

1. **The tiers of scrutiny prediction (Chapter 8).** The chapter predicts that the index should be smallest for race and larger for sex. For COMPAS the paper finds the index for race distinguishable from 1 and the index for sex not. The new section records this in one paragraph and draws no conclusion, since COMPAS is one algorithm and the measured form is not the form of the prediction.

2. **Thresholds.** Chapter 15 uses a threshold of 0.05 from the Algorithmic Jurisprudence manuscript, and Chapter 10 calls for benchmarks. The paper proposes no threshold and withdrew the descriptive ranges of an earlier draft. The book now says the 0.05 belongs to the swap form only.

3. **The Acknowledgments (front matter).** They say the empirical work underlying the Legal Bond Index was conducted using the legal-retrieval Kaggle dataset. The measured index of the paper was computed on the ProPublica COMPAS file. The sentence was not changed (see also Unresolved item 6).

4. **The paper's author note.** It cites the companion theoretical work on the judicial complex with two references whose titles are an economics monograph and a working paper on bounded rationality. Neither is this volume or the Algorithmic Jurisprudence manuscript. The paper's proofing is closed, so this is recorded only.

5. **The README epistemic status** still reads "posited framework with one instrumented corner" (the legal text embedding). It was not changed. The COMPAS measurement does not instrument the framework, since the paper does not use it.

6. **The Lean file** (`LbiImpossibility.lean`) is not mentioned in the paper's text. The book describes what its header states and says it was not rebuilt for this volume.

## Repaired in the survey of 2026-11-26: mechanical defects

Found by the series checker (`tools/series-build/series_check.py` in erisml-lib), with its paragraph checks also run on the text as the build reads it (LF line ends). Hard defects: 8 before, 6 after; the six are listed under "Left as they are".

- **Literal dollar signs.** Amounts written with a bare `$` now use `\$`: the two rent sentences of the Thompson v. Chen running example (Chapter 2, Hohfeld's Second Square), and the reporting threshold in the scenario, the dimension table and Step 4 of Worked Example 2 (Chapter 15). The checker counted an odd number of dollar signs in these paragraphs.

### Left as they are

- **Front matter, Key Results at a Glance, and Chapter 9, Notes on Sources.** "AJ Theorem 7.2", 6.1, 7.1, 5.1, 7.3, and "Theorem 7.1 in the AJ manuscript", are theorem numbers of the companion paper *Algorithmic Jurisprudence*, as the note under the table says. They are correct; the checker counts every "Theorem N.M" against this book's own numbering.

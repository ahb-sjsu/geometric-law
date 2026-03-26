# Chapter 14: International Law as Multi-Manifold Diplomacy

> *"International law is the vanishing point of law."*
> — Thomas Holland, *The Elements of Jurisprudence* (1880)

---

> **RUNNING EXAMPLE — JUDGE RIVERA'S DOCKET**
>
> *Judge Rivera faces a case that refuses to stay within one legal system. Vertex Dynamics, a Delaware-incorporated technology company with headquarters in San Francisco, develops machine learning models for supply chain optimization. Its primary client is a consortium of European manufacturers. Its training data is processed at a facility in Shenzhen, China, operated by a subsidiary of Vertex's Chinese partner, Jianlong Technologies.*
>
> *The European Commission has determined that Vertex's data processing practices violate the General Data Protection Regulation (GDPR), specifically Article 44's restrictions on transferring personal data to third countries that lack "adequate" data protection. The Commission has ordered Vertex to cease all data transfers to the Shenzhen facility and to delete all personal data of European citizens held there. Simultaneously, Chinese law — specifically, the Data Security Law of 2021 and the Personal Information Protection Law — requires Jianlong to store certain data categories within China and prohibits transferring "important data" to foreign entities without government approval.*
>
> *Vertex is trapped. European law says: do not send personal data to China. Chinese law says: do not send important data out of China. American law provides no resolution — there is no bilateral treaty between the United States and either the EU or China that harmonizes data protection standards.*
>
> *The European plaintiffs — individuals whose data was processed in Shenzhen — have sued Vertex in Rivera's court under the Alien Tort Statute and supplemental GDPR enforcement theories. China's Ministry of State Security has sent Jianlong a compliance notice demanding that no data leave the Shenzhen facility. Vertex's general counsel has described the situation as "legally impossible."*
>
> *Rivera must determine: Does she have jurisdiction? Which law applies? Can the conflicting obligations be reconciled? These are the fundamental questions of international law, and they require a framework that can handle multiple legal systems simultaneously. This chapter argues that each nation's legal system is a separate manifold, that treaties are edges connecting these manifolds, and that conflicts of law are fundamentally questions about which manifold governs a given transaction. The tools of multi-manifold geometry — product spaces, fiber bundles, and connection maps — provide the vocabulary.*

---

## The Multi-Manifold Problem

### One World, Many Legal Systems

The framework developed in Chapters 3 through 13 has operated, implicitly, within a single legal system. The judicial complex $\mathcal{K}$, the legal metric, the Hohfeldian gauge group, the constitutional subcomplex — all are defined with reference to a single sovereign's law. When Judge Rivera applies the Equal Protection Clause or traces a precedent chain through federal case law, she is working within the American legal manifold.

But the world contains approximately 200 sovereign legal systems, each with its own judicial complex, its own metric, its own constitutional constraints, and its own Hohfeldian structure. When a transaction crosses borders — as most consequential modern transactions do — the question "which law applies?" becomes the question "which manifold governs?"

This is not merely a choice-of-law question in the traditional sense. Traditional conflict-of-laws doctrine asks which sovereign's rules apply to a given dispute, as if the rules were interchangeable labels that could be swapped without structural consequence. The geometric framework reveals that the question is deeper: different legal manifolds have different topologies, different metrics, and different gauge groups. Choosing which manifold governs is choosing which *geometry* shapes the analysis — which dimensions matter, how distance is measured, and which symmetries are preserved.

### Each Nation as a Separate Manifold

**Definition (National Legal Manifold).** The *legal manifold* of nation $N$ is the judicial complex $\mathcal{K}_N$, equipped with:

- **Dimensions $d_1^N, \ldots, d_8^N$:** The eight legal dimensions, calibrated to nation $N$'s legal system. The dimensions are the same in category (entitlement, factual nexus, procedural posture, statutory authority, constitutional conformity, precedential constraint, remedial scope, public interest) but differ in calibration. What counts as a "right" in American law ($d_1^{\text{US}}$) may differ from what counts as a "right" in Chinese law ($d_1^{\text{CN}}$), because the two systems define rights differently.

- **Metric $d_M^N$:** The Mahalanobis distance calibrated to nation $N$'s covariance structure. The correlation between dimensions differs across legal systems — in a common-law system, precedential constraint ($d_6$) is heavily correlated with entitlement structure ($d_1$), because precedent defines rights. In a civil-law system, statutory authority ($d_4$) plays this role, and $d_6$ is less correlated with $d_1$.

- **Gauge group $G_{\mathfrak{H}}^N$:** The Hohfeldian gauge group, potentially differing across systems. While the abstract Hohfeldian structure (right-duty-liberty-no-right, power-liability-immunity-disability) is universal, the *coupling* between first-order and second-order positions may differ. In systems with strong judicial review, the coupling between constitutional immunity and legislative power is tight; in systems without judicial review, this coupling is looser.

- **Constitutional subcomplex $\mathcal{C}_N$:** The topological constraints specific to nation $N$'s constitutional order. The American $\mathcal{C}_{\text{US}}$ includes the Bill of Rights, the Fourteenth Amendment, and separation of powers. The German $\mathcal{C}_{\text{DE}}$ includes the Basic Law's human dignity provision and the Bundesverfassungsgericht's jurisprudence. The Chinese $\mathcal{C}_{\text{CN}}$ includes the constitutional provisions as interpreted by the National People's Congress Standing Committee.

The key insight is that these manifolds are *not isometric*. There is no distance-preserving map from $\mathcal{K}_{\text{US}}$ to $\mathcal{K}_{\text{EU}}$ or from $\mathcal{K}_{\text{EU}}$ to $\mathcal{K}_{\text{CN}}$. The legal systems measure distance differently, weight dimensions differently, and enforce different topological constraints. A transaction that is short-distance (legally straightforward) on one manifold may be long-distance (legally complex) on another.

## Treaties as Inter-Manifold Edges

### The Structure of Treaty Connections

If each national legal system is a separate manifold, how do they interact? Through *treaties* — agreements between sovereigns that create connections between their respective manifolds.

**Definition (Treaty Edge).** A *treaty* $\tau$ between nations $N_1$ and $N_2$ is an edge connecting the manifolds $\mathcal{K}_{N_1}$ and $\mathcal{K}_{N_2}$. Formally, $\tau$ specifies:

1. **A subregion of each manifold:** The treaty applies to specific legal domains — trade, human rights, intellectual property, data protection — not to the entire legal system. The subregions $\mathcal{K}_{N_1}^\tau \subset \mathcal{K}_{N_1}$ and $\mathcal{K}_{N_2}^\tau \subset \mathcal{K}_{N_2}$ identify the portions of each manifold that the treaty connects.

2. **A connection map:** The treaty specifies how legal positions on one manifold correspond to legal positions on the other. A mutual legal assistance treaty, for example, maps a subpoena issued in $\mathcal{K}_{N_1}$ to an enforceable order in $\mathcal{K}_{N_2}$. An extradition treaty maps criminal charges in $\mathcal{K}_{N_1}$ to arrest authority in $\mathcal{K}_{N_2}$.

3. **A compatibility condition:** The treaty requires that certain legal positions on $\mathcal{K}_{N_1}$ and $\mathcal{K}_{N_2}$ be *consistent* — that traversing the treaty edge and returning should not produce a Hohfeldian contradiction. This is the treaty analogue of the Wilson loop: a non-trivial holonomy around a treaty-connected cycle indicates a conflict between the treaty obligations and domestic law.

The connection map is the critical structure. It is a partial function $\phi_\tau: \mathcal{K}_{N_1}^\tau \to \mathcal{K}_{N_2}^\tau$ that maps legal positions in one system to corresponding positions in the other. The map is partial because the treaty does not cover all legal positions, and it is generally not invertible because the two systems may have different structures in the treaty domain.

### The Treaty Network

The global legal system is not a collection of isolated manifolds — it is a *network* of manifolds connected by treaty edges. The structure of this network determines the possibilities for cross-border legal cooperation and the locations of cross-border legal conflict.

**Definition (Treaty Network).** The *treaty network* $\mathcal{T}$ is a graph whose nodes are national legal manifolds $\{\mathcal{K}_N\}$ and whose edges are treaties $\{\tau_{ij}\}$, with each edge carrying a connection map $\phi_{\tau_{ij}}$.

The treaty network has several important structural properties:

**Connectivity.** Not all manifolds are directly connected by treaty. The path from $\mathcal{K}_{\text{US}}$ to $\mathcal{K}_{\text{CN}}$ on data protection issues may not exist as a direct edge (there is no bilateral data protection treaty between the US and China), requiring instead an indirect path through intermediate manifolds — if one exists.

**Asymmetry.** Treaty edges are often directed or asymmetric. A trade agreement may give nation $N_1$'s goods preferential access to $N_2$'s market without reciprocal access. An extradition treaty may be invocable by $N_1$ but not by $N_2$ for certain categories of offenses.

**Domain specificity.** A treaty edge connects only specific subregions of the manifolds. The US-EU Privacy Shield (now invalidated) connected the data protection subregions of $\mathcal{K}_{\text{US}}$ and $\mathcal{K}_{\text{EU}}$; it said nothing about trade, immigration, or criminal law. The treaty network is not a single graph but a *multiplex* — a layered graph where each layer corresponds to a legal domain (trade, human rights, criminal cooperation, data protection).

---

> **RUNNING EXAMPLE — THE MISSING TREATY EDGES**
>
> *Rivera maps the treaty network relevant to the Vertex Dynamics dispute.*
>
> *US-EU connection: The EU-US Data Privacy Framework (successor to the invalidated Privacy Shield) creates an edge between $\mathcal{K}_{\text{US}}$ and $\mathcal{K}_{\text{EU}}$ on data protection. Vertex could invoke this framework — but only if it has self-certified compliance with the Framework's principles. The record shows that Vertex did self-certify, but the certification covers only data transfers between the US and EU, not transfers from the EU to China via the US.*
>
> *US-China connection: There is no bilateral data protection treaty between the United States and China. On the data protection layer of the treaty network, no edge connects $\mathcal{K}_{\text{US}}$ and $\mathcal{K}_{\text{CN}}$.*
>
> *EU-China connection: There is no adequacy decision by the European Commission recognizing China's data protection framework as adequate under GDPR Article 45. No edge connects $\mathcal{K}_{\text{EU}}$ and $\mathcal{K}_{\text{CN}}$ on data protection.*
>
> *The treaty network is disconnected on the data protection layer. There is no path — direct or indirect — from the European data subjects' legal positions on $\mathcal{K}_{\text{EU}}$ to a compliant legal position on $\mathcal{K}_{\text{CN}}$. The data transfer from the EU to the Shenzhen facility traverses a gap in the treaty network — it crosses between manifolds without a treaty edge to authorize the crossing.*
>
> *This disconnection is the geometric diagnosis of the dispute. The legal impossibility that Vertex's counsel described is a topological fact: the treaty network lacks the connectivity required to make the data flow lawful.*

---

## Conflict of Laws as Manifold Selection

### The Traditional Problem

Conflict of laws (also called private international law) is the body of doctrine that determines which nation's law applies to a dispute with cross-border elements. The three classic questions are:

1. **Jurisdiction:** Does this court have authority to hear the case?
2. **Choice of law:** Which nation's substantive law governs the merits?
3. **Recognition and enforcement:** Will a judgment issued by this court be recognized and enforced in other nations?

Each question has a geometric interpretation.

### Jurisdiction as Manifold Access

Jurisdiction is the question of whether a court sitting on manifold $\mathcal{K}_N$ has authority to adjudicate a dispute that involves elements on manifolds $\mathcal{K}_{N'}$ and $\mathcal{K}_{N''}$.

**Definition (Jurisdictional Reach).** The *jurisdictional reach* of a court on $\mathcal{K}_N$ is the subregion $\mathcal{J}_N \subseteq \bigcup_M \mathcal{K}_M$ that the court can access — the set of legal positions across all manifolds that the court has authority to adjudicate.

In American law, jurisdictional reach is determined by constitutional due process (the defendant must have "minimum contacts" with the forum) and statutory authorization (a long-arm statute must authorize the court's exercise of jurisdiction). In the geometric framework:

**Minimum contacts** require that the defendant's legal position have a non-zero projection onto the forum manifold — that some legally relevant aspect of the defendant's conduct occurred on $\mathcal{K}_N$ or had effects there. The projection is measured by the Mahalanobis distance from the defendant's position to the forum manifold:

$$\pi_N(\mathbf{v}_{\text{defendant}}) = \arg\min_{\mathbf{v} \in \mathcal{K}_N} d_M(\mathbf{v}_{\text{defendant}}, \mathbf{v})$$

If $d_M(\mathbf{v}_{\text{defendant}}, \pi_N(\mathbf{v}_{\text{defendant}}))$ is below a threshold (sufficient contacts), the court has personal jurisdiction.

For Rivera's case: Vertex is incorporated in Delaware and headquartered in San Francisco. It has extensive contacts with the forum ($\mathcal{K}_{\text{US}}$). The European plaintiffs' claims arise from Vertex's data processing practices, which were directed from San Francisco. The jurisdictional reach of Rivera's court extends to the dispute.

But what about Jianlong Technologies, the Chinese partner? Jianlong operates in Shenzhen, has no offices in the United States, and has no direct contact with American consumers. Its connection to the dispute runs through Vertex — it processes data on Vertex's behalf. Rivera must determine whether Jianlong's contacts with the forum are sufficient for personal jurisdiction, or whether Jianlong is beyond her jurisdictional reach.

### Choice of Law as Metric Selection

Once jurisdiction is established, the court must determine which nation's substantive law governs the merits. This is the choice-of-law question, and in the geometric framework, it is the question of which manifold's *metric* to use.

**Definition (Choice of Law as Metric Selection).** A *choice-of-law determination* selects, for each legal dimension $d_k$, the national manifold whose calibration governs:

$$d_k^{\text{governing}} = d_k^{N(k)}$$

where $N(k)$ is the nation whose law governs dimension $k$ of the dispute.

The choice of law need not be uniform across dimensions. A court may apply the contract law of nation $N_1$ (governing $d_1$ and $d_7$), the data protection law of nation $N_2$ (governing $d_2$ and $d_5$), and the procedural law of the forum nation $N_3$ (governing $d_3$). This is the practice of *dépeçage* — slicing the dispute into issues and applying different nations' laws to different issues.

In the geometric framework, dépeçage is a *hybrid metric* — a Mahalanobis distance computed using the covariance matrix of one manifold for some dimensions and another manifold for others:

$$d_M^{\text{hybrid}}(c_i, c_j) = \sqrt{\Delta \mathbf{v}^T \, \Sigma_{\text{hybrid}}^{-1} \, \Delta \mathbf{v}}$$

where $\Sigma_{\text{hybrid}}$ combines the covariance entries from different national manifolds according to the choice-of-law determination.

### The Traditional Choice-of-Law Methods

American choice-of-law doctrine offers several competing methodologies, each with a geometric interpretation:

**The Restatement (First) approach** (1934) uses territorial rules: the law of the place of the wrong governs torts, the law of the place of making governs contracts. In geometric terms, this selects the manifold where the relevant event's vertex is located — a purely geometric criterion (which manifold contains the vertex?).

**The Restatement (Second) approach** (1971) uses the "most significant relationship" test: the law of the jurisdiction with the most significant relationship to the issue governs. In geometric terms, this selects the manifold whose metric best fits the dispute — the manifold where the dispute's attribute vector has the smallest Mahalanobis distance to the most relevant cluster of decided cases.

**Governmental interest analysis** (Brainerd Currie) asks which sovereign has a genuine interest in applying its law to the dispute. In geometric terms, this asks which manifold's constitutional subcomplex constrains the dispute — which sovereign's topological constraints are activated by the facts.

**Comparative impairment** (William Baxter) asks which sovereign's interests would be more impaired by non-application of its law. In geometric terms, this measures the deformation cost of applying a foreign metric: which manifold's metric, when applied to the dispute, produces less distortion?

Each methodology selects a different metric — a different way of measuring distance on the legal space. The geometric framework does not choose among them; it provides a common vocabulary for stating what each methodology does.

---

> **RUNNING EXAMPLE — WHICH MANIFOLD GOVERNS?**
>
> *Rivera confronts the choice-of-law question. The dispute involves three national legal manifolds and multiple legal dimensions.*
>
> *Data protection (dimensions $d_1$, $d_2$, $d_5$): The GDPR governs the processing of European citizens' personal data. Under the GDPR's extraterritorial reach (Article 3), the regulation applies to the processing of personal data of EU data subjects by a controller or processor not established in the EU, when the processing relates to offering goods or services to EU data subjects. Vertex processes EU personal data as part of its service to European manufacturers. GDPR applies. Governing manifold: $\mathcal{K}_{\text{EU}}$.*
>
> *Data storage and localization (dimensions $d_2$, $d_4$): China's Data Security Law requires that "important data" processed in China be stored domestically and undergo a security assessment before cross-border transfer. The Shenzhen facility processes data that may qualify as "important data" under Chinese law. Governing manifold: $\mathcal{K}_{\text{CN}}$.*
>
> *Corporate liability and remedies (dimensions $d_1$, $d_7$): The plaintiffs sue Vertex, a US corporation, in US court. US law governs corporate liability and the available remedies. Governing manifold: $\mathcal{K}_{\text{US}}$.*
>
> *Procedural posture ($d_3$): The forum is a US federal court. US procedural law (Federal Rules of Civil Procedure) governs. Governing manifold: $\mathcal{K}_{\text{US}}$.*
>
> *Rivera must apply a hybrid metric — the GDPR for data protection, Chinese law for data localization, and US law for corporate liability and procedure. The hybrid metric combines covariance structures from three different national manifolds. This is dépeçage in action — and it produces the very legal impossibility that Vertex claims.*

---

## The Impossibility Region

### When Manifolds Conflict

The Vertex dispute illustrates a phenomenon that has no analogue in single-manifold analysis: the *impossibility region* — a set of legal positions that violate the constraints of two or more manifolds simultaneously, such that no compliant position exists on any manifold.

**Definition (Impossibility Region).** An *impossibility region* $\mathcal{I}$ arises when the constraints of two or more national manifolds are jointly unsatisfiable:

$$\mathcal{I} = \{ \mathbf{v} \in \bigcup_N \mathcal{K}_N \mid \nexists \mathbf{v}' \text{ such that } \mathbf{v}' \in \mathcal{C}_{N_1} \cap \mathcal{C}_{N_2} \cap \cdots \cap \mathcal{C}_{N_m} \}$$

An impossibility region is the multi-manifold analogue of a graph trap from Chapter 7: a position from which no compliant path exists, because every path that satisfies one manifold's constraints violates another's.

For Vertex: the GDPR requires deletion of EU personal data from the Shenzhen facility and cessation of data transfers to China. Chinese law requires that the data remain in China and prohibits transfer to foreign entities without government approval. The intersection of compliant positions — positions that satisfy both the GDPR and Chinese law — is empty for data that is simultaneously "personal data of EU citizens" under the GDPR and "important data" under Chinese law. The impossibility region is the set of legal positions involving such dual-characterized data.

### Resolution Mechanisms

How do legal systems resolve impossibility regions? The geometric framework identifies four mechanisms:

**Treaty resolution.** A treaty between the conflicting jurisdictions may provide a connection map that harmonizes the constraints, creating a compliant intersection where none existed before. The EU-US Privacy Shield (while it lasted) resolved an impossibility region between EU data protection law and US commercial law by creating a treaty edge with specific compliance conditions. No analogous treaty exists between the EU and China, or between the US and China, on data protection.

**Comity and sovereign deference.** A court on one manifold may defer to another manifold's constraints, effectively applying the foreign metric in the impossibility region. Comity is a soft resolution — the court voluntarily cedes metric authority — and it does not create a treaty edge. It is a one-time manifold selection, not a structural connection.

**Blocking statutes and clawback provisions.** A sovereign may enact legislation that prohibits its nationals from complying with foreign legal requirements that conflict with domestic law. France's blocking statute (Loi n° 68-678 of 1968) prohibits French entities from disclosing certain economic information to foreign authorities. China's data localization requirements serve a similar function. In geometric terms, a blocking statute creates a *hard boundary* on the domestic manifold that prevents entities from reaching the positions required by the foreign manifold. The blocking statute does not resolve the impossibility region — it deepens it, by explicitly prohibiting the very compliance that the foreign manifold demands.

**Diplomatic negotiation.** When the legal impossibility region is large enough and the commercial stakes are high enough, the resolution may require creating new treaty edges — negotiating new agreements that harmonize the conflicting constraints. This is manifold surgery at the international level: modifying the topology of the treaty network to create connections where none existed.

## Extraterritorial Jurisdiction as Manifold Extension

### The Problem of Long-Arm Reach

Extraterritorial jurisdiction — a nation's assertion of legal authority over conduct occurring on another nation's manifold — is one of the most contested issues in international law. The geometric framework clarifies the structure of the controversy.

**Definition (Extraterritorial Extension).** A nation $N$ asserts *extraterritorial jurisdiction* when its jurisdictional reach extends beyond its own manifold:

$$\mathcal{J}_N \not\subset \mathcal{K}_N$$

That is, the court claims authority to adjudicate legal positions that reside on foreign manifolds.

The GDPR's extraterritorial reach is a paradigmatic example. Article 3(2) extends the GDPR's application to controllers and processors not established in the EU, when their processing activities relate to offering goods or services to EU data subjects. In geometric terms, the GDPR extends the boundary of $\mathcal{K}_{\text{EU}}$ to encompass certain legal positions that would otherwise reside entirely on $\mathcal{K}_{\text{US}}$ or $\mathcal{K}_{\text{CN}}$.

This extension creates the possibility of *manifold overlap* — regions of legal space that are claimed by two or more manifolds simultaneously. The overlap region is where conflicts are most likely, because entities operating in the overlap are subject to the constraints of all claiming manifolds.

**Definition (Manifold Overlap).** The *overlap region* between manifolds $\mathcal{K}_{N_1}$ and $\mathcal{K}_{N_2}$ is:

$$\mathcal{O}_{N_1, N_2} = \mathcal{J}_{N_1} \cap \mathcal{J}_{N_2}$$

the set of legal positions over which both nations claim jurisdictional authority.

For the Vertex dispute, the overlap region includes all data processing activities involving EU personal data conducted by US companies at facilities in China. This is a three-way overlap: $\mathcal{O}_{\text{US, EU, CN}} = \mathcal{J}_{\text{US}} \cap \mathcal{J}_{\text{EU}} \cap \mathcal{J}_{\text{CN}}$. Each nation claims authority over the activity, but their respective constraints are incompatible.

### The Prescriptive Jurisdiction Hierarchy

International law attempts to manage manifold overlap through a hierarchy of prescriptive jurisdiction bases, ranked by legitimacy:

1. **Territorial jurisdiction.** A nation has primary authority over conduct on its territory. This is the default rule: each manifold governs its own domain.

2. **Nationality jurisdiction.** A nation has authority over the conduct of its nationals, even abroad. The US taxes worldwide income of US citizens; this is a manifold extension based on nationality.

3. **Effects jurisdiction.** A nation has authority over foreign conduct that produces effects within its territory. The GDPR's Article 3(2) is an effects-based extension: foreign data processing is within EU jurisdiction because it affects EU data subjects.

4. **Protective jurisdiction.** A nation has authority over foreign conduct that threatens its security interests. China's data localization requirements may be understood as protective jurisdiction — protecting national data security from foreign access.

5. **Universal jurisdiction.** A nation has authority over certain offenses (piracy, genocide, crimes against humanity) regardless of where they occur or who is involved. This is the most aggressive manifold extension — it claims that certain positions on any manifold fall within every nation's jurisdictional reach.

In the geometric framework, each jurisdiction basis defines a different extension rule for $\mathcal{J}_N$:

$$\mathcal{J}_N^{\text{territorial}} \subset \mathcal{J}_N^{\text{nationality}} \subset \mathcal{J}_N^{\text{effects}} \subset \mathcal{J}_N^{\text{protective}} \subset \mathcal{J}_N^{\text{universal}}$$

The hierarchy is a nesting of manifold extensions, from the narrowest (territorial: only the domestic manifold) to the broadest (universal: all manifolds).

---

> **RUNNING EXAMPLE — RIVERA RULES ON JURISDICTION**
>
> *Rivera addresses the jurisdictional question first.*
>
> *Over Vertex: Jurisdiction is clear. Vertex is a Delaware corporation headquartered in San Francisco. Rivera's court has both personal and subject-matter jurisdiction. Vertex's legal position is primarily on $\mathcal{K}_{\text{US}}$, well within the court's jurisdictional reach.*
>
> *Over the European plaintiffs' claims: The plaintiffs invoke the Alien Tort Statute (28 U.S.C. § 1350) and argue that GDPR violations constitute a violation of the "law of nations." Rivera is skeptical — the Alien Tort Statute has been narrowed significantly by Kiobel v. Royal Dutch Petroleum (2013) and Nestlé USA v. Doe (2021). The claims must "touch and concern" the territory of the United States with "sufficient force" to displace the presumption against extraterritorial application. Vertex's data processing decisions were made in San Francisco and directed from San Francisco. The "touch and concern" requirement is arguably met for Vertex's own conduct, though not for Jianlong's.*
>
> *Over Jianlong Technologies: Rivera lacks personal jurisdiction over Jianlong. The Chinese company has no offices, employees, or assets in the United States. Its contacts with the forum are entirely indirect — it processed data on Vertex's behalf, pursuant to a contract governed by Hong Kong law. Under the minimum contacts analysis, Jianlong's position on the treaty network has no projection onto $\mathcal{K}_{\text{US}}$ — the Mahalanobis distance from Jianlong's legal position to the US manifold exceeds the jurisdictional threshold.*
>
> *Rivera dismisses the claims against Jianlong for lack of personal jurisdiction. The dispute will proceed against Vertex alone. But the Chinese legal constraints remain relevant — Vertex cannot comply with any order requiring action at the Shenzhen facility without Jianlong's cooperation, and Jianlong is subject to Chinese law that may prohibit such cooperation.*

---

## The Fiber Bundle Model of International Law

### Why Fiber Bundles?

The multi-manifold structure of international law has a natural mathematical model: the *fiber bundle*. A fiber bundle is a space that looks locally like a product of two spaces (the base space and the fiber) but may have a different global structure — the fibers may be "twisted" relative to each other.

In the international law context:

- **The base space** $B$ is the space of *transactions* — commercial exchanges, data flows, migrations, communications. Each point in $B$ represents a cross-border activity.

- **The fiber** over each point is the *legal space* — the set of legal positions available for that transaction. Each fiber is a copy of the eight-dimensional judicial space, but calibrated to the national manifold that governs the transaction.

- **The total space** $E$ is the fiber bundle: the collection of all fibers over all transactions. A point in $E$ is a transaction together with a legal position for that transaction.

**Definition (International Legal Bundle).** The *international legal bundle* is a fiber bundle $\pi: E \to B$ where:

- $B$ is the transaction space (the set of cross-border activities)
- The fiber $F_b = \pi^{-1}(b)$ over transaction $b$ is the legal space of the governing manifold
- The structure group is the set of transition maps between national legal calibrations

The fiber bundle model captures a crucial feature of international law: *the legal space changes as you move across borders*. A data transfer from San Francisco to Shenzhen traverses the base space $B$, and as it crosses the border, the fiber changes — the legal space transitions from $\mathcal{K}_{\text{US}}$ calibration to $\mathcal{K}_{\text{CN}}$ calibration. The transition map between the fibers is the treaty connection map (if a treaty exists) or undefined (if no treaty connects the manifolds on this issue).

### The Connection and Its Curvature

A *connection* on the fiber bundle specifies how to parallel-transport legal positions from one fiber to another — how to carry a legal analysis across a border crossing.

**Definition (International Legal Connection).** An *international legal connection* $\nabla^{\text{int}}$ specifies, for each path $\gamma$ in the transaction space $B$ and each legal position $\mathbf{v}$ in the fiber $F_{\gamma(0)}$, a transported position $P_\gamma \mathbf{v}$ in the fiber $F_{\gamma(1)}$:

$$P_\gamma: F_{\gamma(0)} \to F_{\gamma(1)}$$

The transport map $P_\gamma$ is the aggregate effect of all treaty connection maps, choice-of-law rules, and comity doctrines along the path $\gamma$.

The *curvature* of the connection measures the extent to which parallel transport around a closed loop in the transaction space produces a non-trivial transformation — a change in legal position when you return to the starting point. This is the international-law analogue of the Wilson loop from Chapter 5.

**Definition (International Curvature).** The *international curvature* $\Omega^{\text{int}}$ at a point $b \in B$ is the holonomy of the connection around an infinitesimal loop at $b$:

$$\Omega^{\text{int}}(b) = \lim_{\text{loop} \to b} W(\gamma_{\text{loop}})$$

Non-zero curvature indicates that the international legal system is *locally inconsistent* at that point in the transaction space — that a round trip through the legal systems returns to a different legal position than the starting one.

For the Vertex dispute, the curvature is non-zero. Start at Vertex's San Francisco headquarters (on $\mathcal{K}_{\text{US}}$). Transfer data to the EU (crossing to $\mathcal{K}_{\text{EU}}$ via the EU-US Data Privacy Framework). Transfer data from the EU to China (crossing to $\mathcal{K}_{\text{CN}}$ — but there is no treaty edge, so the crossing is unauthorized). Process data in China (on $\mathcal{K}_{\text{CN}}$). Return results to San Francisco (crossing back to $\mathcal{K}_{\text{US}}$). The round trip produces a non-trivial holonomy: the data started as "lawfully held personal data" and returned as "data processed in violation of the GDPR." The Hohfeldian labels have changed — the EU data subjects started with a right to data protection and ended with a no-right (their data has been processed in a jurisdiction with no GDPR-equivalent protection).

## Worked Example: The Vertex Dynamics Dispute

**Scenario.** Vertex Dynamics, a US company, processes EU personal data at a Chinese facility. The GDPR prohibits the transfer; Chinese law requires the data to remain in China. Vertex is caught in an impossibility region.

**Step 1: Map the manifolds.**

Three manifolds are relevant:
- $\mathcal{K}_{\text{US}}$: US law governs Vertex's corporate obligations and the court's procedural rules.
- $\mathcal{K}_{\text{EU}}$: EU law (GDPR) governs the data protection rights of EU data subjects.
- $\mathcal{K}_{\text{CN}}$: Chinese law governs data processing at the Shenzhen facility.

**Step 2: Identify the treaty edges.**

| Edge | Status | Implication |
|------|--------|-------------|
| US-EU (data protection) | EU-US Data Privacy Framework (active) | Vertex can transfer data between US and EU if self-certified |
| US-CN (data protection) | No treaty | No authorized pathway for data transfers |
| EU-CN (data protection) | No adequacy decision | No GDPR-compliant pathway for data transfers |

The treaty network is disconnected on the US-CN and EU-CN edges. The data flow EU $\to$ US $\to$ CN traverses a gap.

**Step 3: Compute the impossibility region.**

GDPR constraint: $\Psi_{\text{EU}}$: Personal data of EU citizens may not be transferred to a country without adequate data protection unless specific safeguards are in place (Standard Contractual Clauses, Binding Corporate Rules, or an adequacy decision). China lacks an adequacy decision. No SCCs or BCRs are in place between Vertex and Jianlong.

Chinese constraint: $\Psi_{\text{CN}}$: "Important data" must be stored in China and may not be transferred abroad without a security assessment by the Cyberspace Administration of China.

Intersection: $\Psi_{\text{EU}} \cap \Psi_{\text{CN}} = \emptyset$ for data that is both "personal data of EU citizens" and "important data" under Chinese law. The impossibility region is non-empty.

**Step 4: Evaluate resolution mechanisms.**

Treaty resolution: Not available. No treaty harmonizes EU and Chinese data protection requirements.

Comity: Limited utility. If Rivera defers to Chinese law, she permits GDPR violations. If she defers to EU law, she orders actions that Chinese law prohibits.

Practical resolution: Rivera can order Vertex to cease the data transfers and to implement a compliant data processing architecture — one that does not route EU personal data through China. This resolves the impossibility region by restructuring the transaction to avoid the gap in the treaty network. Vertex's data flow will run EU $\to$ US (via the Data Privacy Framework) without the Chinese leg.

**Step 5: Remedies.**

Rivera orders:
- Vertex shall cease all transfers of EU personal data to the Shenzhen facility within 90 days.
- Vertex shall implement Standard Contractual Clauses for any EU-US data transfers.
- Vertex shall conduct a Data Protection Impact Assessment (DPIA) for its revised data processing architecture.
- Damages for the European plaintiffs are assessed under the GDPR's remedial provisions (Article 82: compensation for material and non-material damage resulting from a GDPR violation).

The order does not require Jianlong to do anything — Rivera has no jurisdiction over Jianlong. The order focuses on what Vertex, a US company subject to Rivera's jurisdiction, can do: restructure its own data processing to avoid the impossibility region.

## Sovereignty as Manifold Integrity

### The Geometric Meaning of Sovereignty

Sovereignty, in the geometric framework, is *manifold integrity* — the principle that each national legal manifold governs its own domain without unauthorized intrusion from other manifolds.

**Definition (Sovereignty as Manifold Integrity).** A nation $N$'s sovereignty is the principle that:

$$\mathcal{K}_N \text{ is self-governing: no foreign court or authority may modify } \mathcal{K}_N \text{ without } N\text{'s consent.}$$

Treaty consent is the mechanism by which a nation voluntarily permits another manifold to influence its own — a controlled weakening of manifold integrity in exchange for reciprocal benefits.

The tension in international law is between manifold integrity (sovereignty) and manifold connectivity (cooperation). A fully sovereign manifold is isolated — no treaty edges, no connection maps, no possibility of cross-border legal cooperation. A fully connected manifold network sacrifices sovereignty — every manifold is subject to the constraints of every other, and no manifold is self-governing.

The current international legal order occupies an intermediate position: nations are sovereign (each manifold is self-governing in principle) but connected by a dense network of treaties, customs, and institutional arrangements (manifolds are linked by edges that permit coordinated legal action). The balance between integrity and connectivity is the central structural question of international law.

### Jus Cogens as Universal Topological Constraints

*Jus cogens* norms — peremptory norms of international law from which no derogation is permitted — are the international analogue of constitutional constraints. They are topological constraints that apply to *every* national manifold, regardless of treaty consent.

**Definition (Jus Cogens as Universal Constraint).** A *jus cogens* norm $\Phi_{\text{JC}}$ is a constraint that every national constitutional subcomplex must satisfy:

$$\Phi_{\text{JC}}(\sigma) = \text{true} \quad \forall \sigma \in \mathcal{C}_N, \; \forall N$$

Examples include the prohibition on genocide, the prohibition on slavery, the prohibition on torture, and the principle of sovereign equality. No treaty may authorize a violation of these norms — a treaty that purports to do so is void (Vienna Convention on the Law of Treaties, Article 53).

In the geometric framework, jus cogens norms are *universal path-homology constraints*. They require that every national manifold's constitutional subcomplex preserve certain path-homology classes — that certain directed cycles (those corresponding to genocide, slavery, torture) remain non-existent in every $\mathcal{C}_N$. A national law that creates such a cycle violates jus cogens regardless of domestic constitutional authorization.

## Chapter Summary

1. Each national legal system is a separate **manifold** $\mathcal{K}_N$ with its own metric, gauge group, and constitutional subcomplex. The manifolds are not isometric — different legal systems measure distance differently and enforce different topological constraints.

2. **Treaties** are edges in a multi-manifold network, connecting subregions of different national manifolds via connection maps that specify how legal positions in one system correspond to positions in another.

3. **Conflict of laws** is manifold selection: which manifold's metric governs each dimension of the dispute. Dépeçage — applying different nations' laws to different issues — is a hybrid metric that combines covariance structures from multiple manifolds.

4. **Impossibility regions** arise when the constraints of multiple manifolds are jointly unsatisfiable. These regions are the geometric diagnosis of "legal impossibility" in cross-border disputes.

5. **Extraterritorial jurisdiction** is manifold extension — a nation's claim of authority over legal positions on foreign manifolds. The prescriptive jurisdiction hierarchy ranks these extensions by legitimacy.

6. The **fiber bundle model** captures the structure of international law: the legal space (fiber) changes as transactions cross borders (traverse the base space), and the connection's curvature measures the inconsistency of the international legal system.

7. **Sovereignty** is manifold integrity — the principle that each manifold is self-governing. *Jus cogens* norms are universal topological constraints that apply to all manifolds regardless of consent.

---

## Technical Appendix

**Definition (National Legal Manifold).** A national legal manifold is a tuple $(\mathcal{K}_N, d_M^N, G_{\mathfrak{H}}^N, \mathcal{C}_N)$ where $\mathcal{K}_N$ is the judicial complex of nation $N$, $d_M^N$ is the Mahalanobis metric calibrated to $N$'s covariance structure, $G_{\mathfrak{H}}^N$ is the Hohfeldian gauge group (with potentially different coupling $\varphi^N$), and $\mathcal{C}_N$ is the constitutional subcomplex.

**Definition (Treaty Connection Map).** A treaty $\tau$ between nations $N_1$ and $N_2$ defines a partial map $\phi_\tau: \mathcal{K}_{N_1}^\tau \to \mathcal{K}_{N_2}^\tau$ satisfying:

(i) **Domain restriction:** $\phi_\tau$ is defined only on the treaty's subject-matter domain $\mathcal{K}_{N_1}^\tau \subset \mathcal{K}_{N_1}$.

(ii) **Hohfeldian compatibility:** $\phi_\tau$ maps Hohfeldian positions in $\mathcal{K}_{N_1}$ to the corresponding positions in $\mathcal{K}_{N_2}$, up to the gauge transformation induced by the treaty: $\phi_\tau(\mathbf{v}) = g_\tau \cdot \mathbf{v}'$ for some $g_\tau \in G_{\mathfrak{H}}^{N_2}$.

(iii) **Metric compatibility:** The distance between treaty-connected positions is bounded: $d_M^{N_2}(\phi_\tau(\mathbf{v}_1), \phi_\tau(\mathbf{v}_2)) \leq L_\tau \cdot d_M^{N_1}(\mathbf{v}_1, \mathbf{v}_2)$ for some Lipschitz constant $L_\tau$ measuring the treaty's "friction."

**Definition (Impossibility Region).** The impossibility region for a set of nations $\{N_1, \ldots, N_m\}$ with constraints $\{\mathcal{C}_{N_k}\}$ is:

$$\mathcal{I} = \left\{ \mathbf{v} \in \mathcal{O}_{N_1, \ldots, N_m} \mid \bigcap_{k=1}^{m} \mathcal{C}_{N_k}|_{\mathbf{v}} = \emptyset \right\}$$

where $\mathcal{O}_{N_1, \ldots, N_m}$ is the jurisdictional overlap region and $\mathcal{C}_{N_k}|_{\mathbf{v}}$ is the set of $N_k$-compliant positions accessible from $\mathbf{v}$.

**Proposition (Impossibility Region Non-Emptiness).** The impossibility region $\mathcal{I}$ is non-empty if and only if there exist dimensions $d_k, d_l$ and nations $N_i, N_j$ such that $\mathcal{C}_{N_i}$ requires $d_k$ to lie in an interval $[a, b]$ and $\mathcal{C}_{N_j}$ requires $d_k$ to lie in an interval $[c, d]$ with $[a, b] \cap [c, d] = \emptyset$.

**Definition (International Legal Fiber Bundle).** The international legal bundle $\pi: E \to B$ is a fiber bundle with:

- Base space $B$: the space of cross-border transactions, parameterized by geographic location, parties, and subject matter.
- Fiber $F_b = \mathbb{R}^8$ with Mahalanobis metric $d_M^{N(b)}$ determined by the governing nation $N(b)$.
- Structure group $G = \{\phi_{\tau}: \tau \in \mathcal{T}\}$: the group generated by all treaty connection maps.
- Connection $\nabla^{\text{int}}$: specified by the choice-of-law rules and treaty connection maps along each path in $B$.

**Proposition (Curvature as Conflict Measure).** The curvature $\Omega^{\text{int}}$ of the international legal connection is non-zero at $b \in B$ if and only if there exists a closed loop $\gamma$ in $B$ based at $b$ such that the parallel transport $P_\gamma: F_b \to F_b$ is not the identity. Non-zero curvature indicates that the international legal order is locally inconsistent at $b$ — different paths through the treaty network produce different legal outcomes for the same transaction.

---

## Notes on Sources

The multi-manifold model of international law extends the single-manifold framework of the Algorithmic Jurisprudence manuscript to the international setting. Choice-of-law methodology is surveyed in Symeonides (2016, *Choice of Law*) and the Restatement (Second) of Conflict of Laws (1971). The "most significant relationship" test originates with Willis Reese and the American Law Institute. Governmental interest analysis is developed by Brainerd Currie (1963, *Selected Essays on the Conflict of Laws*). Comparative impairment is developed by William Baxter (1963) and applied in *Bernhard v. Harrah's Club*, 16 Cal. 3d 313 (1976). The GDPR's extraterritorial reach is discussed in Kuner (2020, *The Internet and the Global Reach of EU Law*). China's Data Security Law (2021) and Personal Information Protection Law (2021) are analyzed in Creemers (2022). The EU-US Data Privacy Framework was adopted by the European Commission in July 2023 as the successor to the invalidated Privacy Shield. The Alien Tort Statute's modern scope is defined by *Kiobel v. Royal Dutch Petroleum Co.*, 569 U.S. 108 (2013), and *Nestlé USA, Inc. v. Doe*, 593 U.S. 628 (2021). Fiber bundles in mathematics are developed in Steenrod (1951, *The Topology of Fibre Bundles*) and Husemoller (1994). The application to international law is original to the Geometric Law framework. Jus cogens norms are codified in the Vienna Convention on the Law of Treaties, Article 53 (1969), and discussed in Orakhelashvili (2006, *Peremptory Norms in International Law*). The concept of sovereignty as manifold integrity extends Krasner (1999, *Sovereignty: Organized Hypocrisy*) into geometric language.

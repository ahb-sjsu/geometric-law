"""Figures for Chapters 1 to 16 of Geometric Law.

Each figure is drawn from a formula, a definition or numbers printed in its chapter. The
volume is a posited framework (see the README), and Chapter 4 says the scoring and
calibration programme has not been run on legal data: the scores, tensors and costs drawn
here are the chapters' illustrative or hypothetical values, and each caption says so.
Schematics are labelled as schematics.

The earlier hand-drawn files figures/fig_NN_1_*.svg are left untouched. Where one of them
planned a figure, the function here redraws it from the chapter text, and keeps only what
the chapter prints. No figure draws the Hohfeldian positions under a dihedral or octad
group (Chapters 2 and 5 get a plain diagram of the pairs and a Wilson loop instead).
"""

import math

from figkit import BORDER, BOX, CRITICAL, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend, reg

DIMS = ["entitlement structure", "factual nexus", "procedural posture", "statutory authority",
        "constitutional conformity", "precedential constraint", "remedial scope", "public interest"]
SHORT = ["entitlement", "facts", "procedure", "statute", "constitution", "precedent", "remedy", "public interest"]


# ------------------------------------------------------------------ helpers
def _rect(c, x, y, w, h, fill="none", opacity=1.0, rx=6, stroke=None, sw=1, dash=None):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" '
          f'fill-opacity="{opacity}"{st}{da}/>')


def _circle(c, x, y, r, fill, stroke=None, sw=1.5, opacity=1.0):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    c.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" fill-opacity="{opacity}"{st}/>')


def _lines(c, x, y, lines, size=11, anchor="start", color=INK2, lh=15, weight="normal", italic=False):
    for i, s in enumerate(lines):
        c.text(x, y + i * lh, s, size, anchor, color, weight, italic)


def _node(c, x, y, w, h, lines, fill=BOX, stroke=BORDER, size=11.5, dash=None, opacity=1.0):
    """Box with centred lines; the first line is the name, the rest are smaller."""
    _rect(c, x, y, w, h, fill, opacity, 6, stroke, 1, dash)
    n = len(lines)
    top = y + h / 2 - (n - 1) * 7 + 4
    for i, s in enumerate(lines):
        if i == 0:
            c.text(x + w / 2, top, s, size, "middle", INK, "600")
        else:
            c.text(x + w / 2, top + i * 14, s, 10.5, "middle", INK2)


def _poly(c, pts, col, width=2, dash=None, opacity=1.0):
    d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="{width}" stroke-opacity="{opacity}" '
          f'stroke-linejoin="round" stroke-linecap="round"{da}/>')


def _head(c, p_from, p_to, col, width=1.5, size=8):
    ang = math.atan2(p_to[1] - p_from[1], p_to[0] - p_from[0])
    for s in (+1, -1):
        a = ang + s * 2.6
        c.line(p_to[0], p_to[1], p_to[0] + size * math.cos(a), p_to[1] + size * math.sin(a), col, width)


def _arrow(c, x1, y1, x2, y2, col=INK2, width=1.5, dash=None, opacity=1.0):
    c.line(x1, y1, x2, y2, col, width, dash, opacity)
    _head(c, (x1, y1), (x2, y2), col, width)


def _bez(p0, p1, p2, n=40):
    out = []
    for i in range(n + 1):
        t = i / n
        out.append(((1 - t) ** 2 * p0[0] + 2 * t * (1 - t) * p1[0] + t * t * p2[0],
                    (1 - t) ** 2 * p0[1] + 2 * t * (1 - t) * p1[1] + t * t * p2[1]))
    return out


def _carrow(c, p0, p1, p2, col=INK2, width=1.5, dash=None):
    pts = _bez(p0, p1, p2)
    _poly(c, pts, col, width, dash)
    _head(c, pts[-3], pts[-1], col, width)


def _cross(c, x, y, col=CRITICAL, s=6, width=2.5):
    c.line(x - s, y - s, x + s, y + s, col, width)
    c.line(x - s, y + s, x + s, y - s, col, width)


def _shorten(x1, y1, x2, y2, a, b):
    """The segment from (x1, y1) to (x2, y2), cut back by a at the start and b at the end."""
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    return x1 + a * ux, y1 + a * uy, x2 - b * ux, y2 - b * uy


# ------------------------------------------------------------------ chapter 1
def fig_1_1():
    assert 2008 - 1791 == 217  # Heller, 217 years after ratification
    p = reg("chapters/ch01_binary_verdict.md", "1.1",
            "The three failures of the binary verdict that the chapter names, each with the facts the chapter cites, "
            "what the one-bit or one-number output leaves out, and the geometric diagnosis the book proposes. The "
            "disparity figures are the ones the chapter quotes from the U.S. Sentencing Commission. The diagnoses "
            "are the framework's posited reading, developed in the chapters named.",
            "## The Deep Structure: Why Law Has Geometry")
    c = Canvas(720, 400, "Three failures of the binary verdict and the diagnosis proposed")
    cols = [
        ("Sentencing disparities", "same offence, different sentence",
         ["Black men: about 19.1% longer", "sentences than comparable", "white men (federal system)",
          "identical offences: up to a factor", "of three across districts"],
         ["which factor drove the number"],
         "gauge violation", "Chapters 8 and 11", SERIES[0]),
        ("Circuit splits", "same question, opposite holdings",
         ["same legal question and facts,", "opposite outcomes by circuit", "cell-site location data: split",
          "until Carpenter (2018)"],
         ["which dimensions each circuit", "weighted more heavily"],
         "non-trivial Wilson loop", "Chapter 5", SERIES[1]),
        ("Constitutional ambiguity", "one text, more than one reading",
         ["Second Amendment: Heller", "(2008), decided five to four,", "217 years after ratification"],
         ["where the justices disagreed,", "and why"],
         "topological obstruction", "Chapter 7", SERIES[2]),
    ]
    for i, (name, sub, cited, lost, diag, chap, col) in enumerate(cols):
        x = 20 + i * 230
        _rect(c, x, 46, 220, 334, BOX, 0.45, 8, BORDER)
        c.text(x + 14, 72, name, 13.5, "start", INK, "600")
        c.text(x + 14, 90, sub, 11, "start", INK3, italic=True)
        c.text(x + 14, 120, "cited in the chapter", 10.5, "start", INK3)
        _lines(c, x + 14, 138, cited, 11.5, color=INK, lh=16)
        c.text(x + 14, 236, "left out of the verdict", 10.5, "start", INK3)
        _lines(c, x + 14, 254, lost, 11.5, color=INK, lh=16)
        c.line(x + 14, 298, x + 206, 298, BORDER, 1)
        c.text(x + 14, 320, "diagnosis proposed", 10.5, "start", INK3)
        _rect(c, x + 14, 331, 12, 12, col, 1.0, 3)
        c.text(x + 32, 342, diag, 12.5, "start", INK, "600")
        c.text(x + 32, 360, chap, 11, "start", INK2)
    c.save(p)


def fig_1_2():
    p = reg("chapters/ch01_binary_verdict.md", "1.2",
            "The two outputs of a legal decision as maps on the eight-dimensional legal space of the chapter. The "
            "binary verdict sends a point with eight coordinates to one bit, and the scalar sentence sends it to one "
            "number. Neither map is injective, so cases that differ on any of the eight dimensions can receive the "
            "same output. This is a schematic of the maps, not data.",
            "### The Metric")
    c = Canvas(720, 400, "Eight coordinates in, one bit or one number out")
    c.text(40, 62, "a legal judgment: a point v = (d1, ..., d8)", 11.5, "start", INK2)
    for k, name in enumerate(DIMS):
        y = 78 + k * 36
        _rect(c, 40, y, 250, 28, BOX, 1.0, 6, BORDER)
        c.text(54, y + 18, f"d{k + 1}", 11.5, "start", INK, "600")
        c.text(82, y + 18, name, 11.5, "start", INK)
        c.line(290, y + 14, 398, 220, SERIES[0], 1.2, opacity=0.75)
    _circle(c, 400, 220, 7, SERIES[0])
    c.text(420, 224, "projection", 11, "start", INK2, italic=True)
    _arrow(c, 410, 214, 476, 150, INK2, 1.5)
    _arrow(c, 410, 226, 476, 290, INK2, 1.5)
    _node(c, 480, 112, 210, 62, ["binary verdict", "one bit: guilty or not guilty,", "liable or not liable"])
    _node(c, 480, 262, 210, 62, ["scalar sentence", "one number: years, dollars,", "amount of relief"])
    c.text(585, 98, "φ: ℝ⁸ → {0, 1}", 11.5, "middle", INK2)
    c.text(585, 342, "ψ: ℝ⁸ → ℝ", 11.5, "middle", INK2)
    _lines(c, 585, 200, ["neither map can be inverted:", "many distinct cases, one output"], 11, "middle", INK3, 15,
           italic=True)
    c.text(16, 390, "schematic", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_2_1():
    first = {"Right": "Duty", "Liberty": "No-right"}          # correlatives, A's position: B's position
    first_opp = {"Right": "No-right", "Duty": "Liberty"}
    second = {"Power": "Liability", "Immunity": "Disability"}
    second_opp = {"Power": "Disability", "Liability": "Immunity"}
    p = reg("chapters/ch02_hohfeld.md", "2.1",
            "Hohfeld's eight positions as the chapter's two tables give them. In each square the left column is the "
            "position of one party and the right column is the position of the other. A horizontal line joins "
            "correlatives, two views of one legal bond. A diagonal line joins opposites, positions that negate each "
            "other. The second square holds the positions about changing legal positions, and exercising them creates, "
            "modifies or destroys positions of the first square. The figure shows the pairs only and makes no claim "
            "about the group the two operations generate.",
            "## The Symmetry That Hohfeld Discovered")
    c = Canvas(720, 400, "Hohfeld's two squares: correlative pairs and opposite pairs")
    w, h = 104, 40

    def square(x0, corr, opp, title, sub):
        (a1, b1), (a2, b2) = corr.items()
        pos = {a1: (x0, 122), b1: (x0 + 176, 122), a2: (x0, 262), b2: (x0 + 176, 262)}
        c.text(x0 + 140, 72, title, 12.5, "middle", INK, "600")
        c.text(x0 + 140, 89, sub, 11, "middle", INK3, italic=True)
        c.text(x0 + w / 2, 112, "one party", 10.5, "middle", INK3)
        c.text(x0 + 176 + w / 2, 112, "the other party", 10.5, "middle", INK3)
        for a, b in opp.items():
            (xa, ya), (xb, yb) = pos[a], pos[b]
            c.line(xa + w / 2, ya + h / 2, xb + w / 2, yb + h / 2, SERIES[1], 2)
        for a, b in corr.items():
            (xa, ya), (xb, yb) = pos[a], pos[b]
            c.line(xa + w, ya + h / 2, xb, yb + h / 2, SERIES[0], 2.5)
        for name, (x, y) in pos.items():
            _rect(c, x, y, w, h, SURFACE, 1.0, 6)
            _node(c, x, y, w, h, [name], BOX, BORDER, 12.5)

    square(30, first, first_opp, "first square", "relations about an act")
    square(410, second, second_opp, "second square", "relations about legal positions")
    _arrow(c, 404, 212, 318, 212, INK2, 1.5)
    c.text(361, 200, "acts on", 11.5, "middle", INK)
    _lines(c, 361, 232, ["a power creates,", "modifies or destroys", "first-square", "positions"], 10.5, "middle",
           INK3, 14, italic=True)
    legend(c, 30, 352, [("correlative: the same bond seen from the other party", SERIES[0])])
    legend(c, 30, 376, [("opposite: the position that negates it", SERIES[1])])
    c.save(p)


# ------------------------------------------------------------------ chapter 3
RIVERA = [0.9, 0.7, 0.8, 0.6, 0.8, 0.5, 0.7, 0.9]


def fig_3_1():
    p = reg("chapters/ch03_judicial_complex.md", "3.1",
            "The attribute vector of the voting rights case in the running example, one score from 0 to 1 on each of "
            "the eight legal dimensions: v = (0.9, 0.7, 0.8, 0.6, 0.8, 0.5, 0.7, 0.9). The scores are the ones Judge "
            "Rivera assigns in the example. They are illustrative, not the output of a scoring run.",
            "## The Judicial Complex: Construction")
    c = Canvas(720, 400, "One case as a point in eight dimensions: the voting rights example")
    ax = Axes(c, 230, 52, 420, 288, (0, 1), (0, 8), [0, 0.25, 0.5, 0.75, 1], [], "score on the dimension (0 to 1)", "")
    for v in (0.25, 0.5, 0.75, 1.0):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    for k, (name, v) in enumerate(zip(DIMS, RIVERA)):
        y = ax.y0 + 36 * k + 8
        c.text(40, y + 14, f"d{k + 1}", 11.5, "start", INK, "600")
        c.text(66, y + 14, name, 11.5, "start", INK2)
        c.hrect(ax.x0, y, ax.X(v) - ax.x0, 20, SERIES[0], title=f"d{k + 1} {name}: {v}")
        c.text(ax.X(v) + 8, y + 14, f"{v:.1f}", 11, "start", INK)
    c.text(16, 390, "illustrative scores from the running example", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_3_2():
    cases = {
        "c1": ("Harper v. Virginia", 1966, [0.9, 0.6, 0.9, 0.3, 0.9, 0.7, 0.8, 0.9]),
        "c2": ("Crawford v. Marion County", 2008, [0.7, 0.5, 0.9, 0.5, 0.7, 0.8, 0.6, 0.7]),
        "c3": ("Shelby County v. Holder", 2013, [0.8, 0.4, 0.9, 0.8, 0.9, 0.9, 0.7, 0.9]),
        "c4": ("Brnovich v. DNC", 2021, [0.8, 0.6, 0.9, 0.7, 0.6, 0.9, 0.6, 0.8]),
        "c5": ("Rivera's case", 2026, RIVERA),
    }
    edges = [("c1", "c2"), ("c1", "c3"), ("c2", "c4"), ("c3", "c4"), ("c2", "c5"), ("c4", "c5")]
    for a, b in edges:
        assert cases[a][1] < cases[b][1]  # an edge runs from the earlier case to the later one that cites it

    def delta(a, b):
        return [round(y - x, 10) for x, y in zip(cases[a][2], cases[b][2])]

    assert delta("c2", "c5") == [0.2, 0.2, -0.1, 0.1, 0.1, -0.3, 0.1, 0.2]
    assert delta("c4", "c5") == [0.1, 0.1, -0.1, -0.1, 0.2, -0.4, 0.1, 0.1]
    p = reg("chapters/ch03_judicial_complex.md", "3.2",
            "The mini-complex of the worked example: five voter identification cases as vertices and six citations "
            "as directed edges, each running from the earlier case to the later case that cites it. The four Supreme "
            "Court cases bind the district court case at the lower right. On the two edges into Rivera's case the "
            "largest change in the attribute vector is on d6, precedential constraint, which falls by 0.3 from "
            "Crawford and by 0.4 from Brnovich. The cases are placed in order of date, not to scale, and the "
            "attribute vectors are the example's illustrative scores.",
            "## Technical Appendix")
    c = Canvas(720, 400, "A judicial complex in miniature: five cases, six citations")
    pos = {"c1": (90, 170), "c2": (265, 96), "c3": (350, 240), "c4": (500, 170), "c5": (630, 332)}
    c.text(20, 62, "Supreme Court", 11.5, "start", INK2)
    c.line(20, 304, 560, 304, GRID, 1, dash="4 4")
    c.text(20, 322, "district court", 11.5, "start", INK2)
    for a, b in edges:
        x1, y1, x2, y2 = _shorten(*pos[a], *pos[b], 13, 15)
        into_rivera = b == "c5"
        _arrow(c, x1, y1, x2, y2, SERIES[1] if into_rivera else SERIES[0], 2)
    lab = {"c1": (90, 204, "middle"), "c2": (265, 62, "middle"), "c3": (350, 274, "middle"),
           "c4": (520, 152, "start"), "c5": (630, 364, "middle")}
    for k, (name, year, _) in cases.items():
        x, y = pos[k]
        _circle(c, x, y, 11, BOX, SERIES[0] if k != "c5" else SERIES[1], 2)
        c.text(x, y + 4, k, 10.5, "middle", INK, "600")
        lx, ly, anchor = lab[k]
        c.text(lx, ly, name, 11.5, anchor, INK, italic=(k != "c5"))
        c.text(lx, ly + 15, str(year), 10.5, anchor, INK2)
    c.text(362, 202, "Δd6 = −0.3", 11, "middle", INK)
    c.text(580, 246, "Δd6 = −0.4", 11, "start", INK)
    legend(c, 20, 384, [("citation between Supreme Court cases", SERIES[0]), ("binding edge into Rivera's case", SERIES[1])])
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def fig_4_1():
    va = [0.8, 0.7, 0.9, 0.9, 0.3, 1.0, 0.7, 0.6]
    vb = [0.85, 0.5, 0.8, 0.8, 0.2, 0.7, 0.6, 0.4]
    var = 0.04
    dv = [round(b - a, 10) for a, b in zip(va, vb)]
    assert dv == [0.05, -0.2, -0.1, -0.1, -0.1, -0.3, -0.1, -0.2]
    parts = [d * d / var for d in dv]
    for got, want in zip(parts, [0.0625, 1.0, 0.25, 0.25, 0.25, 2.25, 0.25, 1.0]):
        assert abs(got - want) < 1e-9
    total = sum(parts)
    assert abs(total - 5.3125) < 1e-9
    p = reg("chapters/ch04_legal_metric.md", "4.1",
            "The squared Mahalanobis distance of the worked example, split by dimension. Each bar is the squared "
            "difference between the two attribute vectors on one dimension, divided by the variance 0.04 that the "
            "example assumes for every dimension. The bars sum to 5.3125. Precedential constraint (d6) and factual "
            "nexus (d2) supply most of it. The boundary penalty and the hierarchical cost are both 0 on this edge, "
            "so 5.3125 is also the edge weight. The vectors and the diagonal covariance are the chapter's "
            "illustrative values, not calibrated ones.",
            "## Cross-Dimensional Correlations: What the Data Should Show")
    c = Canvas(720, 400, "Where the doctrinal distance of the worked example comes from")
    ax = Axes(c, 70, 56, 620, 250, (0, 8), (0, 2.5), [], [0, 0.5, 1, 1.5, 2, 2.5], "", "contribution to the squared distance")
    for k, v in enumerate(parts):
        x = ax.X(k + 0.5) - 12
        c.rect(x, ax.Y(v), 24, ax.Y(0) - ax.Y(v), SERIES[0], title=f"d{k + 1} {DIMS[k]}: {v:g}")
        c.text(x + 12, ax.Y(v) - 7, f"{v:g}", 11, "middle", INK)
        c.text(x + 12, ax.Y(0) + 17, f"d{k + 1}", 11.5, "middle", INK, "600")
        c.text(x + 12, ax.Y(0) + 32, SHORT[k], 10.5, "middle", INK2)
        c.text(x + 12, ax.Y(0) + 48, f"Δ = {dv[k]:+g}".replace("-", "−"), 10.5, "middle", INK3)
    c.text(ax.x0 + 8, ax.y0 + 14, f"sum of the eight bars: {total:g}", 11.5, "start", INK)
    c.text(16, 390, "illustrative: McDonnell Douglas (1973) to a 2025 district court case, variance 0.04 on every dimension",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_5_1():
    # Jural opposite as an involution on the consumer's position; the identity leaves it alone.
    opp = {"no-right": "right", "right": "no-right"}
    pos = "no-right"                       # Case A
    pos = opp[pos]                         # edge A to B: opposite
    assert pos == "right"
    pos = pos                              # edge B to C: identity
    pos = opp[pos]                         # edge C to A: opposite
    assert pos == "no-right"               # the loop returns the starting position: trivial holonomy
    p = reg("chapters/ch05_hohfeldian_group.md", "5.1",
            "The Wilson loop of the worked example, three appellate cases on arbitration clauses in consumer "
            "contracts. From Case A to Case B the consumer's position changes from a no-right to a right, the jural "
            "opposite. From B to C the position is kept and a condition is added. From C back to A the opposite is "
            "applied again. Two opposites cancel, so the loop returns the position it started with: the holonomy is "
            "the identity and the three cases are consistent. The computation uses only that the opposite applied "
            "twice restores the original position.",
            "## Chapter Summary")
    c = Canvas(720, 400, "A Wilson loop that closes: three arbitration cases")
    a, b, d = (60, 286), (275, 62), (490, 286)
    w, h = 170, 58
    _node(c, *a, w, h, ["Case A (2018)", "clause enforceable", "consumer: no-right"])
    _node(c, *b, w, h, ["Case B (2020)", "clause unenforceable", "consumer: right"])
    _node(c, *d, w, h, ["Case C (2022)", "enforceable after fair notice", "consumer: right, on a condition"])
    _arrow(c, 175, 282, 318, 126, SERIES[1], 2)
    _arrow(c, 402, 126, 545, 282, SERIES[0], 2)
    _arrow(c, 486, 322, 236, 322, SERIES[1], 2)
    _lines(c, 232, 190, ["opposite", "no-right to right"], 11.5, "end", INK, 16)
    _lines(c, 510, 178, ["identity", "position kept,", "condition added"], 11.5, "start", INK, 16)
    _lines(c, 360, 342, ["opposite: right to no-right,", "where the condition is met"], 11.5, "middle", INK, 16)
    c.text(360, 224, "opposite · identity · opposite", 12, "middle", INK2)
    c.text(360, 246, "= identity", 13.5, "middle", INK, "600")
    c.text(360, 268, "trivial loop: consistent", 11, "middle", INK3, italic=True)
    legend(c, 20, 384, [("opposite (jural negation)", SERIES[1]), ("identity", SERIES[0])])
    c.save(p)


# ------------------------------------------------------------------ chapter 6
def fig_6_1():
    md = [("prima facie case", 2.0), ("employer's rebuttal", 0.5), ("pretext", 4.0)]
    h_md = sum(v for _, v in md)
    h_direct, actual_direct = 8.0, 1.0
    assert abs(h_md - 6.5) < 1e-12 and h_md < h_direct
    assert h_direct > actual_direct  # with the email the estimate exceeds the true cost: inadmissible at that node
    p = reg("chapters/ch06_precedent_heuristic.md", "6.1",
            "The two doctrinal heuristics of the worked example as estimates of the remaining cost of an employment "
            "discrimination claim, in the chapter's illustrative friction units. McDonnell Douglas adds three steps "
            "to 6.5, below the direct-evidence estimate of 8.0, so the search explores the McDonnell Douglas path "
            "first. If the plaintiff holds a smoking-gun email, the direct-evidence path actually costs about 1.0. "
            "The estimate of 8.0 then exceeds the true cost, and a heuristic that overestimates is not admissible.",
            "## Chapter Summary")
    c = Canvas(720, 400, "Two heuristics for one claim, and an estimate that overshoots")
    ax = Axes(c, 240, 70, 430, 240, (0, 9), (0, 3), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [],
              "remaining cost, friction units (illustrative)", "")
    for v in range(1, 10):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    rows = [106, 186, 266]
    _lines(c, 226, rows[0] - 2, ["McDonnell Douglas", "estimate h = 6.5"], 11.5, "end", INK, 15)
    _lines(c, 226, rows[1] - 2, ["direct evidence", "estimate h = 8.0"], 11.5, "end", INK, 15)
    _lines(c, 226, rows[2] - 9, ["direct evidence,", "actual cost with a", "smoking-gun email"], 11.5, "end", INK, 15)
    acc = 0.0
    cols = [SERIES[0], SERIES[2], SERIES[4]]
    for j, (name, v) in enumerate(md):
        x0, x1 = ax.X(acc) + (1 if j else 0), ax.X(acc + v) - 1
        if j == len(md) - 1:
            c.hrect(x0, rows[0] - 12, x1 - x0, 24, cols[j], title=f"{name}: {v}")
        else:
            c.add(f'<rect x="{x0:.2f}" y="{rows[0] - 12:.2f}" width="{x1 - x0:.2f}" height="24" fill="{cols[j]}">'
                  f'<title>{name}: {v}</title></rect>')
        c.text((x0 + x1) / 2, rows[0] - 20, f"{v:g}", 11, "middle", INK)
        acc += v
    c.text(ax.X(h_md) + 8, rows[0] + 4, "6.5", 11.5, "start", INK, "600")
    c.hrect(ax.X(0), rows[1] - 12, ax.X(h_direct) - ax.X(0), 24, SERIES[1], title="direct evidence, estimate 8.0")
    c.text(ax.X(h_direct) + 8, rows[1] + 4, "8.0", 11.5, "start", INK, "600")
    c.hrect(ax.X(0), rows[2] - 12, ax.X(actual_direct) - ax.X(0), 24, SERIES[1], title="direct evidence, actual about 1.0",
            opacity=0.55)
    c.text(ax.X(actual_direct) + 8, rows[2] + 4, "about 1.0", 11.5, "start", INK, "600")
    c.line(ax.X(actual_direct), rows[1] + 16, ax.X(actual_direct), rows[2] - 16, INK3, 1.5, dash="3 3")
    c.text(ax.X(actual_direct) + 60, rows[1] + 44, "estimate above the true cost: not admissible here", 11, "start",
           INK2, italic=True)
    legend(c, 240, 46, [("prima facie case", cols[0]), ("rebuttal (defendant)", cols[1]), ("pretext", cols[2])])
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_7_1():
    def reachable(edges, start, goal):
        seen, todo = {start}, [start]
        while todo:
            n = todo.pop()
            for a, b in edges:
                if a == n and b not in seen:
                    seen.add(b)
                    todo.append(b)
        return goal in seen

    # Before preemption: the edge to "disclose" has infinite weight under B, and "withhold" is forbidden by A.
    before = [("disclose", "goal")]
    after = [("company", "disclose"), ("disclose", "goal")]
    assert not reachable(before, "company", "goal") and reachable(after, "company", "goal")
    p = reg("chapters/ch07_constitutional_topology.md", "7.1",
            "The statutory conflict of the worked example as a reachability problem. Federal statute A requires the "
            "company to disclose certain data and state statute B prohibits it. Above: the step to disclosure is "
            "blocked by B and the position of withholding is forbidden by A, so no directed path leads from the "
            "company's position to compliance with all applicable law. The chapter calls this a graph trap. Below: "
            "the Supremacy Clause preempts the state statute, the block is removed, and a directed path to "
            "compliance exists. This is a schematic of the example's five steps.",
            "## Chapter Summary")
    c = Canvas(720, 430, "A statutory conflict as a trap in the graph, and its release")

    def panel(y, title, freed):
        c.text(20, y + 4, title, 12, "start", INK, "600")
        _node(c, 20, y + 62, 160, 56, ["company", "holds the data;", "federal and state law apply"])
        _node(c, 285, y + 22, 170, 46, ["disclose", "required by federal A"])
        _node(c, 540, y + 62, 160, 56, ["compliance", "with all applicable law"])
        if freed:
            _arrow(c, 182, y + 80, 282, y + 50, SERIES[0], 2.5)
            _arrow(c, 457, y + 50, 537, y + 80, SERIES[0], 2.5)
            _node(c, 285, y + 112, 170, 46, ["withhold", "state B preempted"], SURFACE, INK3, 11.5, "4 4")
            c.text(232, y + 48, "open", 11, "middle", INK)
            c.text(620, y + 48, "a directed path exists", 11, "middle", INK2, italic=True)
        else:
            _arrow(c, 182, y + 80, 282, y + 50, INK3, 1.5, "5 4")
            _cross(c, 232, y + 65)
            c.text(232, y + 44, "blocked by B", 11, "middle", INK)
            _arrow(c, 457, y + 50, 537, y + 80, INK3, 1.5, "5 4")
            _node(c, 285, y + 112, 170, 46, ["withhold", "required by state B"], SURFACE, CRITICAL, 11.5, "4 4")
            _arrow(c, 182, y + 104, 282, y + 132, INK3, 1.5, "5 4")
            _cross(c, 472, y + 135)
            c.text(486, y + 152, "forbidden by A", 11, "start", INK)
            c.text(620, y + 48, "no directed path: a trap", 11, "middle", INK2, italic=True)

    panel(56, "Both statutes in force", False)
    c.line(20, 234, 700, 234, GRID, 1)
    panel(252, "After preemption under the Supremacy Clause", True)
    c.text(16, 420, "schematic of the worked example", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_8_1():
    p = reg("chapters/ch08_equal_protection.md", "8.1",
            "The test that the Legal Invariance Principle states. A case and a copy of it changed by a legally "
            "irrelevant transformation are put through the same judgment procedure, and the two outcomes are "
            "compared. If they agree for every such transformation the procedure is invariant. A difference is what "
            "the chapter calls a gauge violation. The five kinds of transformation are the ones the axiom lists, and "
            "equal protection is the second of them. This is a schematic of the definition.",
            "## The Judicial Bond Invariance Principle")
    c = Canvas(720, 400, "The invariance test: change what is irrelevant, compare the outcomes")
    _node(c, 30, 70, 150, 52, ["case x", "facts, law, parties"])
    _node(c, 30, 196, 150, 52, ["transformed case τ(x)", "same facts and law"])
    _node(c, 270, 70, 130, 52, ["judgment J", "the same procedure"])
    _node(c, 270, 196, 130, 52, ["judgment J", "the same procedure"])
    _node(c, 480, 70, 110, 52, ["outcome J(x)"])
    _node(c, 480, 196, 110, 52, ["outcome J(τ(x))"])
    _arrow(c, 182, 96, 266, 96)
    _arrow(c, 182, 222, 266, 222)
    _arrow(c, 402, 96, 476, 96)
    _arrow(c, 402, 222, 476, 222)
    _arrow(c, 105, 124, 105, 192, SERIES[1], 2)
    _lines(c, 116, 152, ["τ: a legally", "irrelevant change"], 11, "start", INK, 14)
    c.line(535, 124, 535, 194, SERIES[0], 2, dash="5 4")
    c.text(546, 164, "compare", 11.5, "start", INK, "600")
    _lines(c, 602, 92, ["equal for every τ:", "invariant"], 11, "start", INK2, 14)
    _lines(c, 602, 218, ["different for some τ:", "gauge violation"], 11, "start", INK2, 14)
    c.line(30, 282, 690, 282, GRID, 1)
    c.text(30, 304, "legally irrelevant transformations listed by the axiom", 11.5, "start", INK, "600")
    items = ["1  renaming the parties", "2  changing race, gender, religion or national origin",
             "3  rephrasing an argument without changing its logical content",
             "4  changing the order of presentation", "5  translating between natural languages"]
    _lines(c, 30, 324, items[:3], 11, "start", INK2, 17)
    _lines(c, 420, 324, items[3:], 11, "start", INK2, 17)
    c.text(704, 390, "schematic", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 9
def fig_9_1():
    n = 2
    courts = [("Supreme Court", 3.0), ("circuit court", 2.0), ("district court", 1.0)]
    ds = list(range(1, 9))
    p = reg("chapters/ch09_stare_decisis.md", "9.1",
            "The size of a precedent's weight deformation against graph distance from the precedent, from the "
            "chapter's rule that it falls off as the precedential weight divided by the distance to the power n. "
            "The horizontal axis is the shortest-path distance in the judicial complex and the vertical axis is the "
            "size of the change in edge weight, in arbitrary units. The curves are drawn for n = 2 and weights 3, 2 "
            "and 1, values chosen for illustration. The chapter fixes only the form of the decay and the order "
            "Supreme Court, circuit court, district court.",
            "### Precedent as a Connection")
    c = Canvas(720, 400, "A precedent bends the edge weights near it, and less with distance")
    ax = Axes(c, 70, 66, 520, 266, (0.5, 8.5), (0, 3.2), ds, [0, 1, 2, 3],
              "graph distance from the precedent", "size of the weight change")
    for j, (name, wp) in enumerate(courts):
        fine = [1 + 7 * i / 140 for i in range(141)]
        c.polyline([(ax.X(d), ax.Y(wp / d ** n)) for d in fine], SERIES[j], 2, title=name)
        for d in ds:
            c.dot(ax.X(d), ax.Y(wp / d ** n), SERIES[j], 4, title=f"{name}, distance {d}: {wp / d ** n:.3f}")
    legend(c, 70, 50, [(f"{name}, weight {wp:g}", SERIES[j]) for j, (name, wp) in enumerate(courts)])
    c.text(ax.x0 + ax.w, ax.y0 + 34, "size = weight / distance²", 11.5, "end", INK2, italic=True)
    c.text(16, 390, "illustrative values of the weight and of n", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_9_2():
    chain = [("Bivens", 1971, 0), ("Davis", 1979, 0), ("Carlson", 1980, 0), ("Bush", 1983, 25), ("Chilicky", 1988, 50),
             ("Malesko", 2001, 75), ("Wilkie", 2007, 100), ("Abbasi", 2017, 140), ("Egbert", 2022, 170)]
    assert [y for _, y, _ in chain] == sorted(y for _, y, _ in chain)
    p = reg("chapters/ch09_stare_decisis.md", "9.2",
            "Parallel transport of the Bivens rule through the Supreme Court cases of the running example. Each "
            "arrow stands for the rule as it arrives at a case. Through Davis and Carlson the rule is extended and "
            "arrives unchanged. From Bush v. Lucas on, each refusal to extend it turns the rule further, and at "
            "Egbert v. Boule the chapter describes the rotation as nearly 180 degrees: a rule that damages suits "
            "lie has become a rule that they almost never do. The cases are in order of date, not to scale. The "
            "angles between the first three cases and the last are a schematic, since the chapter gives no values "
            "for them.",
            "## Overruling as Graph Surgery")
    c = Canvas(720, 400, "The Bivens rule, carried forward and turned")
    y0, length = 196, 46
    c.line(40, y0 + 62, 680, y0 + 62, GRID, 1)
    for i, (name, year, ang) in enumerate(chain):
        x = 64 + i * 74
        col = SERIES[0] if ang == 0 else (CRITICAL if name == "Egbert" else SERIES[1])
        c.line(x, y0, x, y0 - length, GRID, 1.5, dash="3 3")
        a = math.radians(ang)
        _arrow(c, x, y0, x + length * math.sin(a), y0 - length * math.cos(a), col, 2.5)
        _circle(c, x, y0, 3.5, INK)
        c.text(x, y0 + 84, name, 11.5, "middle", INK, italic=True)
        c.text(x, y0 + 100, str(year), 10.5, "middle", INK2)
    c.line(44, 122, 232, 122, SERIES[0], 2)
    _lines(c, 138, 92, ["extended to new claims:", "the rule arrives unchanged"], 11, "middle", INK2, 15)
    c.line(266, 122, 528, 122, SERIES[1], 2)
    _lines(c, 397, 92, ["each refusal to extend it", "turns the rule further"], 11, "middle", INK2, 15)
    c.line(562, 122, 676, 122, CRITICAL, 2)
    _lines(c, 619, 92, ["two-part test, then", "nearly 180 degrees"], 11, "middle", INK2, 15)
    _lines(c, 40, 328, ["rule at Bivens: a person whose constitutional rights a",
                         "federal officer violates may sue the officer for damages"], 11, "start", INK, 15)
    _lines(c, 680, 328, ["rule at Egbert: such violations almost", "never give rise to a damages suit"], 11, "end",
           INK, 15)
    c.text(16, 390, "schematic: dotted line = the rule's direction at Bivens", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def fig_10_1():
    williams, matched = 42, 34
    assert round(100 * (williams - matched) / matched) == 24
    p = reg("chapters/ch10_legal_failures.md", "10.1",
            "The four pathologies as the chapter defines them. Heuristic corruption: the estimate of remaining cost "
            "is the true estimate plus a bias tied to legally irrelevant features. Objective hijacking: the action "
            "that maximises a measurable proxy is not the one that maximises the intended objective. Local minimum: "
            "an established precedent sits in a basin, and the cost of overruling is a barrier between it and a "
            "better outcome. Gauge breaking: the outcome changes when a protected attribute is changed, here the 42 "
            "months of the worked example's defendant against 34 months for a similarly situated white defendant, "
            "24 percent more. The first three panels are schematics with curves chosen for illustration, and the "
            "fourth uses the numbers of the chapter's hypothetical case.",
            "## Chapter Summary")
    c = Canvas(720, 520, "Four ways the geometry of a legal system goes wrong")
    px, py, pw, ph = [20, 370], [46, 282], 330, 222

    def frame(i, j, num, name, formula):
        x, y = px[i], py[j]
        _rect(c, x, y, pw, ph, BOX, 0.35, 8, BORDER)
        c.text(x + 14, y + 24, f"{num}  {name}", 13, "start", INK, "600")
        c.text(x + 14, y + 42, formula, 11, "start", INK2, italic=True)
        return x + 30, y + 60, pw - 60, ph - 96

    # 1 heuristic corruption
    x, y, w, h = frame(0, 0, 1, "Heuristic corruption", "corrupted estimate = true estimate + bias ε(c)")
    true = [(x + w * t, y + h * (0.30 + 0.55 * t)) for t in [i / 40 for i in range(41)]]
    corr = [(xx, yy - h * (0.10 + 0.22 * math.exp(-((k / 40 - 0.5) / 0.22) ** 2))) for k, (xx, yy) in enumerate(true)]
    _poly(c, true, SERIES[0], 2)
    _poly(c, corr, SERIES[1], 2)
    k = 20
    c.line(true[k][0], true[k][1] - 3, corr[k][0], corr[k][1] + 3, INK3, 1.5, dash="3 3")
    c.text(true[k][0] + 8, (true[k][1] + corr[k][1]) / 2 + 4, "ε(c)", 11.5, "start", INK)
    c.text(x, true[0][1] + 20, "true", 11, "start", INK2)
    c.text(x, corr[0][1] - 10, "corrupted", 11, "start", INK2)
    c.text(x + w / 2, y + h + 26, "estimated remaining cost, case by case toward the goal →", 10.5, "middle", INK3)

    # 2 objective hijacking
    x, y, w, h = frame(1, 0, 2, "Objective hijacking", "argmax of the proxy ≠ argmax of the true objective")

    def bump(t, mu, s, amp):
        return amp * math.exp(-((t - mu) / s) ** 2)

    ts = [i / 80 for i in range(81)]
    f_true = [(x + w * t, y + h - h * bump(t, 0.32, 0.2, 0.85)) for t in ts]
    f_prox = [(x + w * t, y + h - h * bump(t, 0.70, 0.18, 0.95)) for t in ts]
    _poly(c, f_true, SERIES[0], 2)
    _poly(c, f_prox, SERIES[1], 2)
    for mu, col, lab, amp in ((0.32, SERIES[0], "true objective", 0.85), (0.70, SERIES[1], "proxy", 0.95)):
        xm = x + w * mu
        c.line(xm, y + h - h * amp, xm, y + h, col, 1.5, dash="3 3")
        c.text(xm, y + h - h * amp - 7, lab, 11, "middle", INK2)
    c.line(x, y + h, x + w, y + h, GRID, 1)
    c.text(x + w / 2, y + h + 26, "the actor's choice →", 10.5, "middle", INK3)

    # 3 local minimum
    x, y, w, h = frame(0, 1, 3, "Local minimum", "the overruling cost exceeds the gain from escaping")

    def well(u):
        return 0.5 * (u * u - 1) ** 2 + 0.22 * u

    us = [-1.55 + 3.1 * i / 120 for i in range(121)]
    lo, hi = min(well(u) for u in us), max(well(u) for u in us)
    land = [(x + w * (u + 1.55) / 3.1, y + h * (1 - 0.92 * (well(u) - lo) / (hi - lo))) for u in us]
    _poly(c, land, SERIES[0], 2)

    def at(u):
        return x + w * (u + 1.55) / 3.1, y + h * (1 - 0.92 * (well(u) - lo) / (hi - lo))

    u_loc = min((u for u in us if u > 0.3), key=well)
    u_glob = min((u for u in us if u < -0.3), key=well)
    u_bar = max((u for u in us if -0.6 < u < 0.6), key=well)
    assert well(u_glob) < well(u_loc) < well(u_bar)
    xl, yl = at(u_loc)
    c.dot(xl, yl - 7, CRITICAL, 5, title="the system, at the precedent")
    _lines(c, xl, yl + 16, ["established", "precedent"], 10.5, "middle", INK2, 13)
    xg, yg = at(u_glob)
    _lines(c, xg, yg + 16, ["better", "outcome"], 10.5, "middle", INK2, 13)
    xb, yb = at(u_bar)
    c.text(xb, yb - 10, "barrier: overruling cost", 10.5, "middle", INK2)

    # 4 gauge breaking
    x, y, w, h = frame(1, 1, 4, "Gauge breaking", "J(g · x) ≠ J(x) for a protected-class change g")
    base = y + h - 8
    scale = h * 0.85 / 45
    for i, (lab, v, col) in enumerate((("white defendant", matched, SERIES[0]), ("Williams", williams, SERIES[1]))):
        bx = x + 60 + i * 110
        c.rect(bx, base - v * scale, 24, v * scale, col, title=f"{lab}: {v} months")
        c.text(bx + 12, base - v * scale - 7, f"{v} months", 11, "middle", INK)
        c.text(bx + 12, base + 16, lab, 11, "middle", INK2)
    c.line(x, base, x + w, base, GRID, 1)
    c.text(x + w / 2, base + 32, "same offence, same criminal history: 24% more", 10.5, "middle", INK3)
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def fig_11_1():
    rows = ["Race", "Gender", "SES", "Age", "Citizenship"]
    cols = ["Sentence", "Bail", "Conviction rate", "Charge severity", "Departure rate"]
    v = [[0.187, 0.213, 0.038, 0.082, 0.104],
         [0.138, 0.091, 0.027, 0.051, 0.172],
         [0.159, 0.298, 0.058, 0.039, 0.083],
         [0.031, 0.042, 0.015, 0.021, 0.047],
         [0.068, 0.181, 0.036, 0.097, 0.062]]
    rsum = [sum(r) for r in v]
    csum = [sum(v[i][j] for i in range(5)) for j in range(5)]
    for got, want in zip(rsum, [0.624, 0.479, 0.637, 0.156, 0.444]):
        assert abs(got - want) < 1e-9
    for got, want in zip(csum, [0.583, 0.825, 0.174, 0.290, 0.468]):
        assert abs(got - want) < 1e-9
    total = sum(rsum)
    # The 25 cells, the row sums and the column sums all give 2.340. Step 4 of the chapter prints 2.520.
    assert abs(total - 2.340) < 1e-9 and abs(sum(csum) - 2.340) < 1e-9
    vmax = max(max(r) for r in v)
    assert vmax == 0.298
    p = reg("chapters/ch11_sentencing_disparities.md", "11.1",
            "The gauge violation tensor of the worked example, a hypothetical federal district with 2,000 drug "
            "sentencing cases. Each cell is the average relative change in one outcome (column) when one protected "
            "attribute of the defendant is swapped (row), and a deeper cell is a larger violation. The bars at the "
            "right are the row sums and the row at the foot holds the column sums, as the chapter prints them. Bail "
            "is the outcome that changes most, and the largest cell is socioeconomic status against bail, 0.298. "
            "The 25 cells sum to 2.340, as do the row sums and the column sums; the text of Step 4 prints 2.520 for "
            "this total. The numbers are hypothetical, not measured.",
            "### Step 5: Intervention Design")
    c = Canvas(720, 440, "A hypothetical district's gauge violation tensor: bail changes most")
    x0, y0, cw, ch = 118, 104, 84, 44
    c.text(x0 + 2.5 * cw, 62, "outcome", 11.5, "middle", INK2)
    for j, name in enumerate(cols):
        c.text(x0 + (j + 0.5) * cw, 90, name, 11, "middle", INK)
    c.text(20, y0 - 14, "attribute swapped", 11.5, "start", INK2)
    c.text(x0 + 5 * cw + 22, 90, "row sum", 11, "start", INK2)
    for i, name in enumerate(rows):
        y = y0 + i * ch
        c.text(x0 - 12, y + ch / 2 + 4, name, 11.5, "end", INK)
        for j in range(5):
            val = v[i][j]
            op = 0.06 + 0.62 * val / vmax
            c.add(f'<rect x="{x0 + j * cw + 2:.2f}" y="{y + 2:.2f}" width="{cw - 4}" height="{ch - 4}" rx="4" '
                  f'fill="{SERIES[1]}" fill-opacity="{op:.3f}"><title>{name} × {cols[j]}: {val:.3f}</title></rect>')
            c.text(x0 + (j + 0.5) * cw, y + ch / 2 + 4, f"{val:.3f}", 11.5, "middle", INK, "600" if val == vmax else "normal")
        bx = x0 + 5 * cw + 22
        c.hrect(bx, y + ch / 2 - 8, 96 * rsum[i] / max(rsum), 16, SERIES[0], title=f"{name}, row sum {rsum[i]:.3f}")
        c.text(bx + 96 * rsum[i] / max(rsum) + 8, y + ch / 2 + 4, f"{rsum[i]:.3f}", 11, "start", INK)
    yb = y0 + 5 * ch + 12
    c.line(x0, yb - 6, x0 + 5 * cw, yb - 6, BORDER, 1)
    c.text(x0 - 12, yb + 16, "column sum", 11, "end", INK2)
    for j in range(5):
        c.text(x0 + (j + 0.5) * cw, yb + 16, f"{csum[j]:.3f}", 11.5, "middle", INK,
               "600" if csum[j] == max(csum) else "normal")
    c.text(x0 + 5 * cw + 22, yb + 16, f"all cells: {total:.3f}", 11.5, "start", INK, "600")
    c.text(16, 430, "hypothetical values of the worked example; the cells sum to 2.340, where the chapter's text prints 2.520",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 12
def fig_12_1():
    p = reg("chapters/ch12_adversarial_system.md", "12.1",
            "Litigation as a two-player search, as the chapter defines it. The plaintiff seeks a least-cost path "
            "from the complaint to the remedy sought. The defendant can show that a branch has no path to that goal "
            "(a motion to dismiss removes the branch), remove an edge that rests on inadmissible evidence (a motion "
            "in limine), or establish a path to a goal of its own. A settlement is a vertex that both parties prefer "
            "to the expected result of continuing, reached without the rest of the search. This is a schematic, and "
            "the small graph is not a real case.",
            "## Burden of Proof as Graph Distance")
    c = Canvas(720, 430, "Litigation as a search by two players on one graph")
    c0, a, b, cc = (70, 196), (236, 92), (236, 196), (236, 300)
    d, e = (410, 132), (410, 268)
    r = 13

    def edge(p1, p2, col, width=2, dash=None, cut2=15):
        x1, y1, x2, y2 = _shorten(*p1, *p2, r + 2, cut2)
        _arrow(c, x1, y1, x2, y2, col, width, dash)
        return (x1 + x2) / 2, (y1 + y2) / 2

    mx, my = edge(c0, a, INK3, 1.5, "5 4")
    _cross(c, mx, my)
    _lines(c, 30, 96, ["motion to dismiss:", "no path to the goal,", "branch removed"], 11, "start", INK, 14)
    edge(c0, b, SERIES[0], 2.5)
    edge(b, d, SERIES[0], 2.5)
    edge(d, (560, 110), SERIES[0], 2.5, cut2=6)
    edge(c0, cc, INK3, 1.5)
    mx, my = edge(cc, e, INK3, 1.5, "5 4")
    _cross(c, mx, my)
    _lines(c, 300, 312, ["motion in limine:", "edge removed"], 11, "start", INK, 14)
    edge(b, e, SERIES[1], 2.5)
    edge(e, (560, 268), SERIES[1], 2.5, cut2=6)
    _carrow(c, (70, 214), (150, 400), (556, 374), SERIES[2], 2, "6 4")
    for (x, y), lab in ((c0, "c0"), (a, ""), (b, ""), (cc, ""), (d, ""), (e, "")):
        _circle(c, x, y, r, BOX, BORDER, 1.5)
        if lab:
            c.text(x, y + 4, lab, 10.5, "middle", INK, "600")
    c.text(70, 172, "complaint", 11, "middle", INK2)
    _node(c, 562, 84, 140, 52, ["plaintiff's goal", "the remedy sought"])
    _node(c, 562, 242, 140, 52, ["defendant's goal", "defence or counterclaim"])
    _node(c, 562, 350, 140, 48, ["settlement", "preferred by both"])
    legend(c, 20, 60, [("plaintiff's path", SERIES[0]), ("defendant's path", SERIES[1]), ("settlement shortcut", SERIES[2])])
    c.text(704, 420, "schematic", 10.5, "end", INK3, italic=True)
    c.save(p)


# Not drawn: the plotted point needs the defendant's estimate and the damages base,
# a calculation the chapter does not make. Kept for when the chapter states it.
def _held_12_2():
    p_plaintiff = 0.70            # EJAC's estimate that it prevails
    p_defendant = 1 - 0.35        # the City puts EJAC's chance at 35%, so its own at 65%
    damages, costs = 4.5, 3.0     # million dollars: damages EJAC seeks, combined litigation costs
    optimism = p_plaintiff + p_defendant - 1
    ratio = costs / damages
    assert abs(optimism - 0.35) < 1e-12 and abs(ratio - 2 / 3) < 1e-12
    assert costs > optimism * damages  # the condition of the text holds: the settlement region is not empty
    p = reg("chapters/ch12_adversarial_system.md", "12.2",
            "The settlement condition of the chapter: a settlement exists when the two parties' combined litigation "
            "costs exceed their combined optimism times the damages at stake. The horizontal axis is the combined "
            "optimism, the plaintiff's estimate of winning plus the defendant's estimate of winning, minus 1. The "
            "vertical axis is the combined cost as a fraction of the damages. Above the line a settlement exists. "
            "The point is the running example read into the formula: the plaintiff puts its chance at 70 percent and "
            "the City puts it at 35 percent, the combined costs are estimated at 3 million dollars, and the damages "
            "at stake are taken as the 4.5 million dollars sought. All of these are the example's hypothetical "
            "figures.",
            "## Appeals as Path Re-Evaluation")
    c = Canvas(720, 400, "Cases settle when costs outweigh the parties' combined optimism")
    ax = Axes(c, 80, 52, 520, 280, (0, 1), (0, 1), [0, 0.2, 0.4, 0.6, 0.8, 1], [0, 0.2, 0.4, 0.6, 0.8, 1],
              "combined optimism: both estimates of winning, minus 1", "combined cost / damages")
    c.add(f'<polygon points="{ax.X(0):.2f},{ax.Y(0):.2f} {ax.X(1):.2f},{ax.Y(1):.2f} {ax.X(0):.2f},{ax.Y(1):.2f}" '
          f'fill="{SERIES[0]}" fill-opacity="0.14"/>')
    c.line(ax.X(0), ax.Y(0), ax.X(1), ax.Y(1), SERIES[0], 2)
    c.text(ax.X(0.04), ax.Y(0.90), "a settlement exists", 12, "start", INK, "600")
    c.text(ax.X(0.04), ax.Y(0.90) + 17, "costs > optimism × damages", 11, "start", INK2, italic=True)
    c.text(ax.X(0.96), ax.Y(0.12), "no settlement", 12, "end", INK, "600")
    c.text(ax.X(0.96), ax.Y(0.12) + 17, "each side expects to do better at trial", 11, "end", INK2, italic=True)
    c.dot(ax.X(optimism), ax.Y(ratio), CRITICAL, 5.5, title=f"running example: optimism {optimism:.2f}, cost/damages {ratio:.2f}")
    _lines(c, ax.X(optimism) + 34, ax.Y(ratio) + 24, ["the running example", f"optimism {optimism:.2f}, cost / damages {ratio:.2f}"],
           11, "end", INK, 15)
    c.text(16, 390, "hypothetical figures of the running example", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 13
def fig_13_1():
    term, t_m, t_c = 60, 18, 19
    assert t_m < t_c and term - t_m == 42 and abs((term - t_m) / 12 - 3.5) < 1e-12
    p = reg("chapters/ch13_contract_law.md", "13.1",
            "The worked example on a time line, in months from the start of the five-year contract. Each party's "
            "line is solid while it is inside the region the contract defines. At month 18 the company restructures "
            "and the contracted role no longer exists: it leaves the region first, and because the role is central "
            "to the contract the breach is material. That breach extinguishes the non-compete obligation, so the "
            "employee's move to a competitor at month 19 crosses no boundary. The 42 months that remain, 3.5 years, "
            "are the term over which expectation damages are computed. The case is the chapter's hypothetical one.",
            "## The Relational Contract as Manifold Evolution")
    c = Canvas(720, 400, "Who crossed the contract's boundary first")
    x0, x1 = 150, 670

    def X(m):
        return x0 + (x1 - x0) * m / term

    for m in (0, 12, 24, 36, 48, 60):
        c.line(X(m), 80, X(m), 300, GRID, 1)
        c.text(X(m), 318, str(m), 11, "middle", INK2)
    c.text((x0 + x1) / 2, 338, "months from the start of the contract", 11.5, "middle", INK2)
    ym, yc = 138, 238
    _lines(c, 20, ym - 4, ["Meridian", "(the company)"], 11.5, "start", INK, 15, "600")
    _lines(c, 20, yc - 4, ["Chandrasekaran", "(the employee)"], 11.5, "start", INK, 15, "600")
    c.line(X(0), ym, X(t_m), ym, SERIES[0], 3)
    c.line(X(t_m), ym, X(term), ym, SERIES[0], 2, dash="2 6", opacity=0.8)
    c.dot(X(t_m), ym, CRITICAL, 5.5, title="month 18: the contracted role no longer exists")
    _lines(c, X(t_m) + 12, ym - 34, ["month 18: the role as contracted is withdrawn", "first breach, and material"],
           11, "start", INK, 15)
    c.line(X(0), yc, X(t_c), yc, SERIES[1], 3)
    c.line(X(t_c), yc, X(term), yc, SERIES[1], 2, dash="2 6", opacity=0.8)
    c.dot(X(t_c), yc, SERIES[1], 5.5, title="month 19: joins a competitor")
    _lines(c, X(t_c) + 12, yc - 34, ["month 19: joins a competitor", "no breach: the non-compete ended at month 18"],
           11, "start", INK, 15)
    yb = 278
    c.line(X(t_m), yb, X(term), yb, INK2, 1.5)
    c.line(X(t_m), yb - 6, X(t_m), yb + 6, INK2, 1.5)
    c.line(X(term), yb - 6, X(term), yb + 6, INK2, 1.5)
    c.text((X(t_m) + X(term)) / 2, yb - 8, "42 months of the term remain (3.5 years): expectation damages", 11, "middle",
           INK2)
    c.line(X(t_m), 80, X(t_m), 262, CRITICAL, 1.5, dash="5 4")
    legend(c, 150, 62, [("inside the contract's region (solid)", SERIES[0]), ("after leaving it (dotted)", INK3)])
    c.text(16, 390, "hypothetical case of the worked example", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 14
def fig_14_1():
    edges = {("US", "EU"): True, ("US", "CN"): False, ("EU", "CN"): False}  # data-protection layer

    def connected(a, b):
        seen, todo = {a}, [a]
        while todo:
            n = todo.pop()
            for (u, v), ok in edges.items():
                if ok and n in (u, v):
                    m = v if n == u else u
                    if m not in seen:
                        seen.add(m)
                        todo.append(m)
        return b in seen

    assert connected("EU", "US") and not connected("EU", "CN") and not connected("US", "CN")
    p = reg("chapters/ch14_international_law.md", "14.1",
            "The data-protection layer of the treaty network in the worked example. Each node is a national legal "
            "system and each edge is a treaty or equivalent instrument. The EU-US Data Privacy Framework joins the "
            "American and European systems. No treaty joins the American and Chinese systems on data protection, "
            "and there is no adequacy decision between the European Union and China. The company's data flow runs "
            "from the European Union through the United States to a facility in Shenzhen, and its second leg "
            "crosses a gap: no path in this layer, direct or indirect, reaches the Chinese system.",
            "## Sovereignty as Manifold Integrity")
    c = Canvas(720, 400, "No treaty edge reaches the Chinese system on data protection")
    us, eu, cn = (150, 290), (360, 90), (570, 290)
    w, h = 176, 58
    # treaty edges
    c.line(us[0] + 40, us[1] - h / 2, eu[0] - 50, eu[1] + h / 2, SERIES[0], 3)
    c.line(eu[0] + 50, eu[1] + h / 2, cn[0] - 40, cn[1] - h / 2, INK3, 1.5, dash="3 7")
    c.line(us[0] + w / 2, us[1] + 12, cn[0] - w / 2, cn[1] + 12, INK3, 1.5, dash="3 7")
    _lines(c, 222, 176, ["EU-US Data Privacy", "Framework (active)"], 11.5, "end", INK, 15)
    _lines(c, 498, 176, ["no adequacy", "decision"], 11.5, "start", INK, 15)
    c.text(360, 322, "no treaty", 11.5, "middle", INK)
    # data flow
    _arrow(c, eu[0] - 22, eu[1] + h / 2 + 6, us[0] + 68, us[1] - h / 2 - 4, SERIES[1], 2)
    _arrow(c, us[0] + w / 2 + 4, us[1] - 8, cn[0] - w / 2 - 6, cn[1] - 8, CRITICAL, 2)
    _cross(c, 360, 282, CRITICAL, 6)
    c.text(360, 264, "transfer across the gap", 11, "middle", INK2, italic=True)
    for (x, y), lines in ((us, ["United States", "the company's headquarters"]),
                          (eu, ["European Union", "the data subjects (GDPR)"]),
                          (cn, ["China", "the Shenzhen facility"])):
        _node(c, x - w / 2, y - h / 2, w, h, lines)
    legend(c, 20, 364, [("treaty edge", SERIES[0]), ("data flow, first leg", SERIES[1]), ("data flow across the gap", CRITICAL)])
    c.text(16, 390, "dotted lines: edges that do not exist", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 15
def fig_15_1():
    p = reg("chapters/ch15_ai_legal.md", "15.1",
            "The five steps of the pipeline that builds the judicial complex from case text, as the chapter sets "
            "them out. Each step feeds the next, and the fifth checks the whole against five criteria. When a "
            "criterion fails, the chapter's remedy is to go back: for the first criterion, to retrain the probes or "
            "redefine the dimensions. This is a schematic of the procedure. The chapter describes it for a "
            "hypothetical system and reports no run of it.",
            "### Step 1: Embedding")
    c = Canvas(720, 400, "From case text to a calibrated complex in five steps")
    steps = [
        ("1  Embedding", ["document to a", "vector e in ℝᵈ"]),
        ("2  Dimension scoring", ["eight linear probes:", "v in [0, 1]⁸"]),
        ("3  Covariance", ["8 × 8 matrix Σ,", "with shrinkage"]),
        ("4  Edge weights", ["citation, distance", "and outcome"]),
        ("5  Validation", ["five criteria,", "listed below"]),
    ]
    bw, gap, y = 126, 14, 96
    c.text(22, 76, "opinions, statutes, regulations", 11, "start", INK2, italic=True)
    for i, (name, sub) in enumerate(steps):
        x = 22 + i * (bw + gap)
        _node(c, x, y, bw, 70, [name] + sub, BOX, SERIES[0] if i == 4 else BORDER)
        if i:
            _arrow(c, x - gap + 1, y + 35, x - 2, y + 35, INK2, 1.5)
    xr = 22 + 4 * (bw + gap) + bw / 2
    xl = 22 + 1 * (bw + gap) + bw / 2
    _poly(c, [(xr, y + 70), (xr, y + 104), (xl, y + 104), (xl, y + 76)], INK3, 1.5, "5 4")
    _head(c, (xl, y + 104), (xl, y + 72), INK3, 1.5)
    c.text((xl + xr) / 2, y + 122, "if a criterion fails: retrain the probes or redefine the dimensions", 11, "middle",
           INK2, italic=True)
    c.line(22, 248, 698, 248, GRID, 1)
    c.text(22, 272, "the five validation criteria of step 5", 11.5, "start", INK, "600")
    crit = ["1  dimension independence: no pair of scores correlated above 0.7",
            "2  gauge invariance: scores unchanged under legally irrelevant changes",
            "3  topological consistency: no spurious Wilson loops on known-consistent chains",
            "4  retrieval accuracy: retrieved precedents match expert judgments",
            "5  calibration of distances: distances track expert ratings of similarity"]
    _lines(c, 22, 294, crit, 11, "start", INK2, 18)
    c.text(704, 390, "schematic", 10.5, "end", INK3, italic=True)
    c.save(p)


def fig_15_2():
    rivera = [0.7, 0.6, 0.9, 0.8, 0.7, 0.5, 0.6, 0.8]
    machine = [0.65, 0.55, 0.85, 0.75, 0.72, 0.48, 0.58, 0.77]
    gaps = [round(abs(a - b), 10) for a, b in zip(rivera, machine)]
    assert max(gaps) == 0.05 and max(gaps) <= 0.1  # "within 0.1 on every dimension"
    p = reg("chapters/ch15_ai_legal.md", "15.2",
            "The check of the running example: the judge's own scores for one of her decided cases against the "
            "scores the system assigns, on each of the eight dimensions (horizontal axis, 0 to 1). The two agree to "
            "within 0.05 on every dimension, inside the 0.1 the example treats as the expected margin. The system "
            "and its scores are the chapter's hypothetical example, not a measurement.",
            "### Step 3: Covariance Estimation")
    c = Canvas(720, 400, "Expert and machine scores for one case, dimension by dimension")
    ax = Axes(c, 230, 62, 420, 272, (0.4, 1.0), (0, 8), [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], [],
              "score on the dimension", "")
    for v in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    for k, name in enumerate(DIMS):
        y = ax.y0 + 34 * (k + 0.5)
        c.text(40, y + 4, f"d{k + 1}", 11.5, "start", INK, "600")
        c.text(66, y + 4, name, 11.5, "start", INK2)
        a, b = rivera[k], machine[k]
        c.line(ax.X(a), y, ax.X(b), y, INK3, 2)
        c.dot(ax.X(a), y, SERIES[0], 5, title=f"d{k + 1}, judge {a}")
        c.dot(ax.X(b), y, SERIES[1], 5, title=f"d{k + 1}, system {b}")
        lo, hi = min(a, b), max(a, b)
        c.text(ax.X(lo) - 10, y + 4, f"{lo:g}", 10.5, "end", INK)
        c.text(ax.X(hi) + 10, y + 4, f"{hi:g}", 10.5, "start", INK)
    legend(c, 230, 46, [("the judge's score", SERIES[0]), ("the system's score", SERIES[1])])
    c.text(16, 390, "hypothetical scores of the running example", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 16
def fig_16_1():
    links = [(1, 2, "affects"), (2, 5, "feeds into"), (3, 4, "intersects"), (4, 1, "is required for")]
    assert {n for a, b, _ in links for n in (a, b)} == {1, 2, 3, 4, 5}
    p = reg("chapters/ch16_open_questions.md", "16.1",
            "The five open problems and the four links between them that the chapter states. Metric calibration "
            "affects cross-jurisdictional invariance, which feeds into international coherence. The computability "
            "of the fundamental group intersects the problem of dynamic complexes, and dynamic complexes are "
            "required for metric calibration, because the metric must be recalibrated as the complex changes. The "
            "chapter concludes that solving any one fully would probably need progress on at least two others.",
            "### The Modesty Principle")
    c = Canvas(720, 400, "The five open problems depend on one another")
    w, h = 196, 56
    pos = {1: (36, 70), 2: (262, 70), 5: (488, 70), 4: (36, 270), 3: (488, 270)}
    names = {1: ["1  Metric calibration", "how to calibrate, how sensitive"],
             2: ["2  Cross-jurisdictional invariance", "are the dimensions universal"],
             3: ["3  Fundamental group", "is it computable"],
             4: ["4  Dynamic complexes", "a complex that changes in time"],
             5: ["5  International coherence", "many systems, one framework"]}
    for k, (x, y) in pos.items():
        _node(c, x, y, w, h, names[k], size=11.5)
    # 1 -> 2, 2 -> 5
    for a, b, lab in links[:2]:
        xa, ya = pos[a]
        xb, yb = pos[b]
        _arrow(c, xa + w + 2, ya + h / 2, xb - 3, yb + h / 2, SERIES[0], 2)
    c.text(249, 60, "affects", 11, "middle", INK)
    c.text(475, 60, "feeds into", 11, "middle", INK)
    _lines(c, 360, 148, ["the calibration must handle traditions", "with different dimensions"], 10.5, "middle",
           INK3, 14, italic=True)
    _lines(c, 586, 148, ["comparing positions across systems", "needs consistent dimensions"], 10.5, "middle",
           INK3, 14, italic=True)
    # 4 -> 1
    _arrow(c, 134, 268, 134, 130, SERIES[0], 2)
    _lines(c, 146, 196, ["is required for:", "the metric is recalibrated", "as the complex changes"], 11, "start", INK, 15)
    # 3 <-> 4
    c.line(240, 298, 480, 298, SERIES[1], 2)
    _head(c, (240, 298), (484, 298), SERIES[1], 2)
    _head(c, (480, 298), (236, 298), SERIES[1], 2)
    c.text(360, 288, "intersects", 11, "middle", INK)
    _lines(c, 360, 318, ["the fundamental group of a changing", "complex is harder than a static one's"], 10.5, "middle",
           INK3, 14, italic=True)
    legend(c, 36, 376, [("one problem bears on the next", SERIES[0]), ("the two intersect", SERIES[1])])
    c.save(p)

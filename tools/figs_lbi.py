"""Figures for the measured form of the Legal Bond Index (Chapters 8 and 15).

These three figures differ from the rest of the volume's figures in one respect: they draw
measured values, not illustrative ones. The values are those that the paper "The Legal Bond
Index" (in press, Journal of Science and Law) reports for COMPAS risk scores, as printed in
the chapter text, and they are conditional on the measured predictors. Every number drawn is
checked twice: `_printed` asserts that the chapter file prints it, and plain asserts check
the arithmetic statements the chapter makes about it. Nothing is drawn that the chapter
does not print.
"""

import os

from figkit import CRITICAL, GRID, INK, INK2, INK3, ROOT, SERIES, Axes, Canvas, reg

CH8 = "chapters/ch08_equal_protection.md"
CH15 = "chapters/ch15_ai_legal.md"


def _printed(chapter, *strings):
    """Assert that the chapter file prints each string, character for character."""
    with open(os.path.join(ROOT, chapter), encoding="utf-8") as f:
        text = f.read()
    for s in strings:
        assert s in text, f"{chapter} does not print: {s}"


def _whisker(c, x1, y1, x2, y2, col, cap=4):
    """An interval: a thin line with a short cap at each end."""
    c.line(x1, y1, x2, y2, col, 1.5, opacity=0.9)
    if abs(x1 - x2) < 0.01:
        c.line(x1 - cap, y1, x1 + cap, y1, col, 1.5)
        c.line(x2 - cap, y2, x2 + cap, y2, col, 1.5)
    else:
        c.line(x1, y1 - cap, x1, y1 + cap, col, 1.5)
        c.line(x2, y2 - cap, x2, y2 + cap, col, 1.5)


# ------------------------------------------------------------------ Figure 8.2
def fig_8_2():
    p = reg(CH8, "8.2",
            "The matched-neighborhood Legal Bond Index for COMPAS scores at the six neighborhood scales, for race "
            "and for sex. The horizontal axis is the scale k, the number of neighbors of each group, on a "
            "logarithmic scale. The vertical axis is the index, and the dashed line at 1 marks no excess. Each bar "
            "is the pointwise 95% interval. The curve for race lies above 1 at every scale, and the intervals for "
            "sex include 1 at scales up to 20. The values are those the paper reports for COMPAS scores, "
            "conditional on the measured predictors.",
            "### What Reduces the Figure")
    ks = [1, 5, 10, 20, 50, 100]
    race = [(1.045, 1.002, 1.089), (1.043, 1.010, 1.074), (1.041, 1.017, 1.068),
            (1.049, 1.027, 1.072), (1.060, 1.041, 1.079), (1.069, 1.053, 1.087)]
    sex = [(0.962, 0.935, 1.032), (1.012, 0.974, 1.043), (1.016, 0.987, 1.043),
           (1.021, 0.998, 1.044), (1.028, 1.008, 1.048), (1.041, 1.023, 1.060)]
    for k, (rv, rlo, rhi), (sv, slo, shi) in zip(ks, race, sex):
        _printed(CH8, f"| {k} | {rv:.3f} | {rlo:.3f} to {rhi:.3f} | {sv:.3f} | {slo:.3f} to {shi:.3f} |")
    _printed(CH8, "between 1.041 and 1.069", "every interval excludes 1",
             "not distinguishable from 1 at scales up to 20")
    assert min(v for v, _, _ in race) == 1.041 and max(v for v, _, _ in race) == 1.069
    assert all(lo > 1 for _, lo, _ in race)
    assert all(lo < 1 < hi for (_, lo, hi), k in zip(sex, ks) if k <= 20)

    c = Canvas(720, 400, "COMPAS: the index for race is above 1 at every scale")
    ax = Axes(c, 70, 62, 560, 262, (0.5, 135), (0.92, 1.10), ks, [0.92, 0.95, 1.00, 1.05, 1.10],
              "neighborhood scale k (neighbors of each group, log scale)", "Legal Bond Index (ratio)", xlog=True)
    y1 = ax.Y(1.0)
    c.line(ax.x0, y1, ax.x0 + ax.w, y1, INK3, 1.5, dash="4 4")
    c.text(ax.x0 + ax.w, y1 + 15, "1 = no excess", 10.5, "end", INK2, italic=True)
    for j, (name, rows, shift) in enumerate((("race", race, 0.94), ("sex", sex, 1.065))):
        col = SERIES[j]
        xs = [ax.X(k * shift) for k in ks]
        for x, (v, lo, hi) in zip(xs, rows):
            _whisker(c, x, ax.Y(lo), x, ax.Y(hi), col)
        c.polyline([(x, ax.Y(v)) for x, (v, _, _) in zip(xs, rows)], col, 2, title=name)
        for x, k, (v, lo, hi) in zip(xs, ks, rows):
            c.dot(x, ax.Y(v), col, 4.5, title=f"{name}, k = {k}: {v:.3f}, interval {lo:.3f} to {hi:.3f}")
        c.text(xs[-1] + 14, ax.Y(rows[-1][0]) + 4, f"{name}  {rows[-1][0]:.3f}", 11.5, "start", INK)
    # direct labels for the scale the chapter uses for its diagnostics
    c.text(ax.X(20 * 0.94) - 9, ax.Y(1.049) - 8, "1.049", 11, "end", INK)
    c.text(ax.X(1 * 0.94) - 10, ax.Y(1.045) + 4, "1.045", 11, "end", INK)
    c.text(ax.X(1 * 1.065) + 12, ax.Y(0.962) + 15, "0.962", 11, "start", INK)
    # legend
    lx, ly = 70, 48
    for label, col in (("race", SERIES[0]), ("sex", SERIES[1])):
        c.add(f'<rect x="{lx:.2f}" y="{ly - 9:.2f}" width="12" height="12" rx="3" fill="{col}"/>')
        c.text(lx + 18, ly + 1, label, 11.5, "start", INK2)
        lx += 70
    _whisker(c, lx + 6, ly - 10, lx + 6, ly + 4, INK2, 3)
    c.text(lx + 18, ly + 1, "pointwise 95% interval", 11.5, "start", INK2)
    c.text(16, 390, "Values the paper reports for COMPAS scores (n = 5,278), conditional on the measured predictors.",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ Figure 8.3
def fig_8_3():
    p = reg(CH8, "8.3",
            "The index for race at scale 20, unadjusted and estimated again under each specification that tightens "
            "the matching or forces parity between neighbors of the two races. The horizontal axis is the index. "
            "The dashed line at 1 marks no excess, and the dotted line at 1.015 is the center of the null "
            "distribution of the conditional randomization test. The unadjusted value is 1.049. Under matching "
            "parity the estimates fall to between 1.00 and 1.02. Intervals are drawn for the two rows whose "
            "interval the chapter prints. The values are those the paper reports for COMPAS scores, conditional on "
            "the measured predictors.",
            "### The Test")
    # (row label, value, (lo, hi) or None, n used or None, the chapter's table row or sentence)
    rows = [
        ("unadjusted (unrestricted)", 1.049, (1.027, 1.072), "5,278", "| Unrestricted | 1.049 | 5,278 |"),
        ("exact match on felony indicator", 1.050, None, "5,278",
         "| Exact match on the felony indicator, then Mahalanobis | 1.050 | 5,278 |"),
        ("caliper, 90th percentile", 1.022, None, "4,656", "| Caliper at the 90th percentile | 1.022 | 4,656 |"),
        ("neighborhoods of fixed radius", 1.022, None, "4,171", "| Neighborhoods of fixed radius | 1.022 | 4,171 |"),
        ("caliper, 75th percentile", 1.012, None, "3,826", "| Caliper at the 75th percentile | 1.012 | 3,826 |"),
        ("coarsened exact matching", 1.009, (1.000, 1.018), "3,159",
         "| Coarsened exact matching, then Mahalanobis | 1.009 | 3,159 |"),
        ("largest 5% of gaps left out", 1.009, None, None, "from 1.049 to 1.009"),
        ("matched on distance (lower bound)", 1.003, None, "5,278",
         "| Same-race comparators matched on distance | 1.003 | 5,278 |"),
    ]
    _printed(CH8, *[r[4] for r in rows])
    _printed(CH8, "| 20 | 1.049 | 1.027 to 1.072 |", "Its interval is 1.000 to 1.018",
             "falls to between 1.00 and 1.02", "centered at 1.015, not at 1.000", "reads its value as a lower bound")
    parity = [v for name, v, _, _, _ in rows[2:]]
    assert all(1.00 <= round(v, 2) <= 1.02 for v in parity)
    assert rows[0][1] == 1.049 and max(parity) < 1.049

    c = Canvas(720, 460, "COMPAS at k = 20: matching parity takes 1.049 down to 1.00 to 1.02")
    rh = 36
    ax = Axes(c, 250, 100, 330, rh * len(rows), (0.99, 1.08), (0, len(rows)),
              [1.00, 1.02, 1.04, 1.06, 1.08], [], "Legal Bond Index for race (ratio)", "")
    top, bot = ax.y0, ax.y0 + ax.h
    # the band the chapter states for matching parity
    c.add(f'<rect x="{ax.X(1.00):.2f}" y="{top:.2f}" width="{ax.X(1.02) - ax.X(1.00):.2f}" height="{ax.h:.2f}" '
          f'fill="{SERIES[1]}" fill-opacity="0.10"/>')
    for v in (1.02, 1.04, 1.06, 1.08):
        c.line(ax.X(v), top, ax.X(v), bot, GRID, 1)
    c.line(ax.X(1.0), top - 6, ax.X(1.0), bot, INK3, 1.5, dash="4 4")
    c.line(ax.X(1.015), top - 6, ax.X(1.015), bot, INK3, 1.5, dash="1 4")
    c.text(ax.X(1.0) - 5, top - 12, "1 = no excess", 10.5, "end", INK2, italic=True)
    c.text(ax.X(1.015) + 5, top - 12, "1.015 = center of the conditional null", 10.5, "start", INK2, italic=True)
    for i, (name, v, iv, n, _) in enumerate(rows):
        y = top + rh * (i + 0.5)
        col = SERIES[0] if i == 0 else SERIES[1]
        c.line(ax.x0, y, ax.x0 + ax.w, y, GRID, 1)
        c.text(ax.x0 - 12, y + 4, name, 11.5, "end", INK if i == 0 else INK2, "600" if i == 0 else "normal")
        if iv:
            _whisker(c, ax.X(iv[0]), y, ax.X(iv[1]), y, col)
        title = f"{name}: {v:.3f}" + (f", interval {iv[0]:.3f} to {iv[1]:.3f}" if iv else "")
        c.dot(ax.X(v), y, col, 5.5 if i == 0 else 5, title=title)
        c.text(ax.x0 + ax.w + 52, y + 4, f"{v:.3f}", 11.5, "end", INK, "600" if i == 0 else "normal")
        c.text(ax.x0 + ax.w + 122, y + 4, n if n else "", 10.5, "end", INK3)
    c.text(ax.x0 + ax.w + 52, top - 12, "index", 10.5, "end", INK3, italic=True)
    c.text(ax.x0 + ax.w + 122, top - 12, "defendants", 10.5, "end", INK3, italic=True)
    # legend
    lx, ly = 18, 52
    for label, col in (("unadjusted", SERIES[0]), ("tighter or equal matching", SERIES[1])):
        c.add(f'<circle cx="{lx + 6:.2f}" cy="{ly - 3:.2f}" r="5" fill="{col}"/>')
        c.text(lx + 18, ly + 1, label, 11.5, "start", INK2)
        lx += 18 + 7.0 * len(label) + 24
    _whisker(c, lx, ly - 3, lx + 22, ly - 3, INK2, 3)
    c.text(lx + 30, ly + 1, "95% interval, where the chapter prints one", 11.5, "start", INK2)
    c.text(16, 450, "Values the paper reports for COMPAS scores, conditional on the measured predictors. "
           "Shaded: 1.00 to 1.02.", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ Figure 15.3
def fig_15_3():
    p = reg(CH15, "15.3",
            "How often each significance test rejects at a nominal level of 5%, on synthetic scores with known "
            "structure built on the real COMPAS predictors and race labels. The vertical axis is the share of "
            "replicates rejected. In the two conditions where the score ignores race, a rejection is a false "
            "alarm. There the permutation test rejects 56.5% and 88.3% of the time, and the conditional randomization "
            "test 4.5% and 5.0%. In the other conditions a rejection is a correct detection. The values are those "
            "the paper reports for COMPAS scores, conditional on the measured predictors.",
            "### What This Chapter Takes from the Paper")
    # (label lines, permutation %, conditional %, blind to race?, the chapter's table row prefix)
    rows = [
        (["race-blind"], 56.5, 4.5, True, "| Race-blind | 1.009 | 56.5% | 4.5% |"),
        (["race-blind,", "predictor", "withheld"], 88.3, 5.0, True,
         "| Race-blind, predictor withheld | 1.015 | 88.3% | 5.0% |"),
        (["direct", "β = 0.25"], 88.3, 21.7, False, "| Direct, $\\beta = 0.25$ | 1.015 | 88.3% | 21.7% |"),
        (["direct", "β = 0.5"], 100.0, 85.0, False, "| Direct, $\\beta = 0.5$ | 1.027 | 100% | 85.0% |"),
        (["direct", "β = 1.0"], 100.0, 100.0, False, "| Direct, $\\beta = 1.0$ | 1.071 | 100% | 100% |"),
        (["proxy", "γ = 0.5"], 100.0, 100.0, False, "| Proxy, $\\gamma = 0.5$ | 1.052 | 100% | 100% |"),
        (["proxy", "γ = 1.0"], 100.0, 100.0, False, "| Proxy, $\\gamma = 1.0$ | 1.153 | 100% | 100% |"),
    ]
    _printed(CH15, *[r[4] for r in rows])
    _printed(CH15, "rejects on 56.5% of race-blind datasets at a nominal level of 5%",
             "The conditional test rejects on 4.5%")
    blind = [r for r in rows if r[3]]
    assert all(perm > 50 and crt <= 5.0 for _, perm, crt, _, _ in blind)
    assert all(perm >= crt for _, perm, crt, _, _ in rows)

    def pct(v):
        return f"{v:.0f}%" if v == 100 else f"{v:.1f}%"

    c = Canvas(720, 440, "False alarms: 56.5% for the permutation test, 4.5% conditional")
    ax = Axes(c, 64, 118, 626, 232, (0, len(rows)), (0, 100), (), [0, 25, 50, 75, 100], "",
              "replicates rejected (%)")
    base = ax.Y(0)
    slot = ax.w / len(rows)
    split = ax.x0 + slot * 2
    c.line(split, ax.y0 - 50, split, base + 58, INK3, 1, dash="2 4")
    c.text(ax.x0 + slot, ax.y0 - 42, "score ignores race", 11, "middle", INK, "600")
    c.text(ax.x0 + slot, ax.y0 - 27, "a rejection is a false alarm", 11, "middle", INK2)
    mid = split + (ax.x0 + ax.w - split) / 2
    c.text(mid, ax.y0 - 42, "race or a proxy enters the score", 11, "middle", INK, "600")
    c.text(mid, ax.y0 - 27, "a rejection is a detection", 11, "middle", INK2)
    y5 = ax.Y(5)
    c.line(ax.x0, y5, ax.x0 + ax.w, y5, CRITICAL, 1.5, dash="4 4")
    bw = 24
    for i, (lab, perm, crt, _, _) in enumerate(rows):
        cx = ax.x0 + slot * (i + 0.5)
        for j, v in enumerate((perm, crt)):
            x = cx - bw - 3 + j * (bw + 6)
            y = ax.Y(v)
            name = "permutation test" if j == 0 else "conditional randomization test"
            c.rect(x, y, bw, base - y, SERIES[j], title=f"{' '.join(lab)}, {name}: {pct(v)}")
            c.text(x + bw / 2, y - 6, pct(v), 10, "middle", INK)
        for n, s in enumerate(lab):
            c.text(cx, base + 17 + 14 * n, s, 11, "middle", INK2)
    # legend
    lx, ly = 64, 50
    for label, col in (("permutation test", SERIES[0]), ("conditional randomization test", SERIES[1])):
        c.add(f'<rect x="{lx:.2f}" y="{ly - 9:.2f}" width="12" height="12" rx="3" fill="{col}"/>')
        c.text(lx + 18, ly + 1, label, 11.5, "start", INK2)
        lx += 18 + 6.6 * len(label) + 24
    c.line(lx, ly - 3, lx + 24, ly - 3, CRITICAL, 1.5, dash="4 4")
    c.text(lx + 32, ly + 1, "nominal level, 5%", 11.5, "start", INK2)
    c.text(16, 430, "Values the paper reports for synthetic scores on the COMPAS predictors, "
           "conditional on the measured predictors.", 10.5, "start", INK3, italic=True)
    c.save(p)

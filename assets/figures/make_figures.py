"""Original teaching figures for the GLOBE ggplot2 tutorial.
Author: Julia Chacón Labella. License: CC BY 4.0.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch

rng = np.random.default_rng(7)
SP = ["#1b9e77", "#d95f02", "#7570b3"]          # species colours (Dark2)
INK = "#2b2b2b"
GREY = "#8a8a8a"
plt.rcParams["font.family"] = "DejaVu Sans"

# ---------------------------------------------------------------------------
# Figure 1: a ggplot is built in layers
# ---------------------------------------------------------------------------
def layers_figure(path):
    fig, ax = plt.subplots(figsize=(11, 9.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 9.5)
    ax.axis("off")

    W, S, H = 3.6, 1.2, 1.15    # plane width, skew and depth
    x0, base, gap = 0.4, 0.6, 1.65

    def P(u, v, lvl):
        return (x0 + u * W + v * S, base + lvl * gap + v * H)

    layers = [
        ("Data", "ggplot(data = penguins,", "#4e79a7"),
        ("Aesthetic mapping", "       aes(x = body_mass_g,\n           y = flipper_length_mm,\n           colour = species)) +", "#59a14f"),
        ("Geometry", "  geom_point() +", "#e15759"),
        ("Labels", "  labs(x = \"Body mass (g)\",\n       y = \"Flipper length (mm)\") +", "#b07aa1"),
        ("Theme", "  theme_bw()", "#9c755f"),
    ]

    # simulated penguin-like data, in plane coordinates (0-1)
    n = 18
    sp = np.repeat([0, 1, 2], n // 3)
    xs = np.clip(rng.normal([0.25, 0.4, 0.75][0], 0.1, n), 0.05, 0.95)
    xs = np.concatenate([rng.normal(m, 0.08, n // 3) for m in (0.25, 0.4, 0.75)])
    ys = 0.1 + 0.95 * (xs - 0.1) + rng.normal(0, 0.07, n)
    xs, ys = np.clip(xs, 0.08, 0.92), np.clip(ys, 0.1, 0.92)

    for lvl, (name, code, col) in enumerate(layers):
        corners = [P(0, 0, lvl), P(1, 0, lvl), P(1, 1, lvl), P(0, 1, lvl)]
        ax.add_patch(Polygon(corners, closed=True, facecolor="white",
                             edgecolor=col, linewidth=2.2, alpha=0.95,
                             zorder=10 + lvl))

        if lvl == 0:   # a small data table
            for i in range(1, 5):
                a, b = P(0.08, i / 5, lvl), P(0.92, i / 5, lvl)
                ax.plot([a[0], b[0]], [a[1], b[1]], color=col, lw=0.8, alpha=0.6, zorder=20)
            for j in range(1, 4):
                a, b = P(j / 4, 0.08, lvl), P(j / 4, 0.92, lvl)
                ax.plot([a[0], b[0]], [a[1], b[1]], color=col, lw=0.8, alpha=0.6, zorder=20)
        if lvl == 1:   # axes
            o, xe, ye = P(0.1, 0.1, lvl), P(0.92, 0.1, lvl), P(0.1, 0.92, lvl)
            ax.annotate("", xy=xe, xytext=o, zorder=21,
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6))
            ax.annotate("", xy=ye, xytext=o, zorder=21,
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6))
            ax.text(*P(0.55, 0.02, lvl), "x", color=col, fontsize=10, ha="center", va="top", zorder=21)
            ax.text(*P(0.12, 0.62, lvl), "y  ", color=col, fontsize=10, ha="right", zorder=21)
        if lvl == 2:   # points
            for xi, yi, si in zip(xs, ys, sp):
                px, py = P(xi, yi, lvl)
                ax.scatter(px, py, s=22, color=SP[si], zorder=22, edgecolor="none")
        if lvl == 3:   # labels
            ax.text(*P(0.5, 0.0, lvl), "Body mass (g)", color=col, fontsize=8.5,
                    ha="center", va="top", zorder=23)
            ax.text(*P(-0.1, 0.5, lvl), "Flipper\nlength (mm)", color=col, fontsize=8.5,
                    ha="right", va="center", zorder=23)
        if lvl == 4:   # grid and frame
            for t in (0.25, 0.5, 0.75):
                a, b = P(t, 0, lvl), P(t, 1, lvl)
                ax.plot([a[0], b[0]], [a[1], b[1]], color=col, lw=0.7, alpha=0.5, zorder=24)
                a, b = P(0, t, lvl), P(1, t, lvl)
                ax.plot([a[0], b[0]], [a[1], b[1]], color=col, lw=0.7, alpha=0.5, zorder=24)

        # badge, layer name and code on the right
        yc = base + lvl * gap + H / 2
        ax.add_patch(plt.Circle((6.15, yc), 0.22, color=col, zorder=30))
        ax.text(6.15, yc, str(lvl + 1), color="white", fontsize=11,
                fontweight="bold", ha="center", va="center", zorder=31)
        ax.plot([P(1, 0.5, lvl)[0] + 0.1, 5.85], [yc, yc], color=col, lw=1,
                ls=(0, (2, 3)), zorder=5)
        ax.text(6.55, yc + 0.28, name, color=col, fontsize=12.5,
                fontweight="bold", va="bottom")
        ax.text(6.55, yc + 0.18, code, family="DejaVu Sans Mono", fontsize=10.5,
                color=INK, va="top", linespacing=1.35)

    ax.text(5.5, 9.25, "A ggplot is built in layers", fontsize=17,
            ha="center", va="top", color=INK)
    ax.text(5.5, 8.8, "Each piece of code adds one element to the plot, from the data up",
            fontsize=10.5, ha="center", va="top", color=GREY)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2: which plot should I use?
# ---------------------------------------------------------------------------
def mini(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GREY)


def chooser_figure(path):
    fig = plt.figure(figsize=(12, 9.6))
    fig.text(0.5, 0.975, "Which plot should I use?", fontsize=18,
             ha="center", va="top", color=INK)
    fig.text(0.5, 0.94, "Start from what you want to show, then check the type of your variables",
             fontsize=11, ha="center", va="top", color=GREY)

    cards = [
        ("Distribution of one variable", "1 continuous", "#4e79a7", (0.03, 0.49)),
        ("Differences between groups", "1 continuous + 1 categorical", "#59a14f", (0.52, 0.49)),
        ("Relationship between two variables", "2 continuous", "#e15759", (0.03, 0.03)),
        ("Counts and values by category", "1 or 2 categorical (+ a value)", "#b07aa1", (0.52, 0.03)),
    ]
    cw, ch = 0.45, 0.42
    for title, vtype, col, (cx, cy) in cards:
        fig.patches.append(FancyBboxPatch((cx, cy), cw, ch, transform=fig.transFigure,
                                          boxstyle="round,pad=0,rounding_size=0.012",
                                          facecolor=col, alpha=0.08, edgecolor=col, lw=1.5))
        fig.text(cx + 0.02, cy + ch - 0.025, title, fontsize=13.5, fontweight="bold",
                 color=col, va="top")
        fig.text(cx + 0.02, cy + ch - 0.07, vtype, fontsize=10, color=INK, va="top",
                 bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=col, lw=0.8))

    def add(cx, cy, k, nk, name, func):
        pw = (0.41 - 0.03 * (nk - 1)) / nk
        a = fig.add_axes([cx + 0.025 + k * (pw + 0.03), cy + 0.06, pw, 0.22])
        func(a); mini(a)
        a.set_title(name, fontsize=10.5, color=INK, pad=6)
        fig.text(cx + 0.025 + k * (pw + 0.03) + pw / 2, cy + 0.025,
                 {"Histogram": "geom_histogram()", "Density plot": "geom_density()",
                  "Box plot": "geom_boxplot()", "Violin plot": "geom_violin()",
                  "Mean ± SE": "geom_pointrange()", "Scatter plot": "geom_point()",
                  "Scatter + trend": "geom_smooth()", "Bar plot": "geom_bar()",
                  "Heatmap": "geom_tile()"}[name],
                 family="DejaVu Sans Mono", fontsize=8.5, ha="center", color=GREY)

    x = rng.normal(0, 1, 400)
    groups = [rng.normal(m, s, 60) for m, s in ((3.7, 0.45), (3.7, 0.38), (5.1, 0.5))]

    # distribution
    c = (0.03, 0.49)
    add(*c, 0, 2, "Histogram", lambda a: a.hist(x, bins=14, color="#4e79a7", edgecolor="white"))
    def dens(a):
        g = np.linspace(-3.5, 3.5, 200)
        d = np.exp(-g ** 2 / 2)
        a.fill_between(g, d, color="#4e79a7", alpha=0.35); a.plot(g, d, color="#4e79a7")
        a.set_ylim(0, 1.1)
    add(*c, 1, 2, "Density plot", dens)

    # groups
    c = (0.52, 0.49)
    def box(a):
        bp = a.boxplot(groups, widths=0.5, patch_artist=True, medianprops=dict(color=INK))
        for p, col in zip(bp["boxes"], SP):
            p.set_facecolor(col); p.set_alpha(0.6)
    def vio(a):
        vp = a.violinplot(groups, showextrema=False)
        for p, col in zip(vp["bodies"], SP):
            p.set_facecolor(col); p.set_alpha(0.6)
    def ptr(a):
        m = [g.mean() for g in groups]; se = [g.std() / np.sqrt(len(g)) * 4 for g in groups]
        for i, (mm, ss, col) in enumerate(zip(m, se, SP)):
            a.errorbar(i + 1, mm, yerr=ss, fmt="o", color=col, ms=7, capsize=0, lw=2)
        a.set_xlim(0.4, 3.6)
    add(*c, 0, 3, "Box plot", box)
    add(*c, 1, 3, "Violin plot", vio)
    add(*c, 2, 3, "Mean ± SE", ptr)

    # relationship
    c = (0.03, 0.03)
    xx = rng.uniform(0, 10, 45); yy = 2 + 0.8 * xx + rng.normal(0, 1.3, 45)
    add(*c, 0, 2, "Scatter plot", lambda a: a.scatter(xx, yy, s=14, color="#e15759"))
    def trend(a):
        a.scatter(xx, yy, s=14, color="#e15759", alpha=0.5)
        b = np.polyfit(xx, yy, 1); g = np.linspace(0, 10, 10)
        a.fill_between(g, b[1] + b[0] * g - 1, b[1] + b[0] * g + 1, color=GREY, alpha=0.25)
        a.plot(g, b[1] + b[0] * g, color=INK, lw=1.8)
    add(*c, 1, 2, "Scatter + trend", trend)

    # counts
    c = (0.52, 0.03)
    def bars(a):
        a.bar([0, 1, 2], [44, 68, 124], color=SP, alpha=0.8, width=0.6)
    def heat(a):
        a.imshow(rng.gamma(1.5, 2, (6, 8)), cmap="viridis", aspect="auto")
        for s in ("left", "bottom"):
            a.spines[s].set_visible(False)
    add(*c, 0, 2, "Bar plot", bars)
    add(*c, 1, 2, "Heatmap", heat)

    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    layers_figure("ggplot_layers.png")
    chooser_figure("which_plot.png")

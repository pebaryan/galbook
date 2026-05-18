"""
GA Cheat Sheet — The Grade Hierarchy in One Image

A clean static illustration showing all geometric objects at once:
  Grade 0: Scalar
  Grade 1: Vectors (a, b)
  Grade 2: Bivector (a^b parallelogram)
  Grade 3: Trivector (a^b^c parallelepiped)

Designed to sit inline in Chapter 3 as a reference poster.
"""
from manim import *
import numpy as np

BG = "#1C1C1C"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FFFF00"
RED = "#FF6B6B"
PURPLE = "#C084FC"
WHITE = "#EAEAEA"
DIM = "#888888"
MONO = "Menlo"


class GACheatSheet(Scene):
    """All four grades in one frame, arranged left->right: scalar, vectors, bivector, trivector."""

    def construct(self):
        self.camera.background_color = BG

        # ── Title ──────────────────────────────────────────────────
        title = Text("Geometric Algebra: The Grade Hierarchy", font=MONO,
                     font_size=34, color=PRIMARY, weight=BOLD)
        title.to_edge(UP)
        self.add(title)

        subtitle = Text("scalar  ->  vector  ->  bivector  ->  trivector",
                        font=MONO, font_size=20, color=DIM)
        subtitle.next_to(title, DOWN, buff=0.15)
        self.add(subtitle)

        sec_y = 0.5

        # ── Section 0: Scalar ──────────────────────────────────────
        sec_x = -6.2

        gr0 = Text("Grade 0", font=MONO, font_size=16, color=DIM)
        gr0.move_to([sec_x, 2.3, 0])
        self.add(gr0)

        c = Circle(radius=0.3, color=WHITE, fill_opacity=0.2)
        c.move_to([sec_x, 0.8, 0])
        self.add(c)

        s = Text("5.2", font=MONO, font_size=28, color=WHITE)
        s.move_to(c.get_center())
        self.add(s)

        sn = Text("magnitude", font=MONO, font_size=14, color=DIM)
        sn.next_to(c, DOWN, buff=0.15)
        self.add(sn)

        # ── Section 1: Vectors ────────────────────────────────────
        sx = -2.8

        gr1 = Text("Grade 1", font=MONO, font_size=16, color=DIM)
        gr1.move_to([sx, 2.3, 0])
        self.add(gr1)

        a = np.array([1.2, 0.8, 0.0])
        b = np.array([-0.3, 1.5, 0.0])

        a_arr = Arrow(start=[0, 0, 0], end=a, color=SECONDARY,
                      stroke_width=10, max_tip_length_to_length_ratio=0.15)
        b_arr = Arrow(start=[0, 0, 0], end=b, color=RED,
                      stroke_width=10, max_tip_length_to_length_ratio=0.15)
        a_arr.shift([sx, sec_y, 0])
        b_arr.shift([sx, sec_y, 0])

        al = Text("a", font_size=32, color=SECONDARY)
        al.next_to(a_arr.get_end(), RIGHT, buff=0.1)
        bl = Text("b", font_size=32, color=RED)
        bl.next_to(b_arr.get_end(), UP, buff=0.05)

        self.add(a_arr, b_arr, al, bl)

        vn = Text("directions /", font=MONO, font_size=14, color=DIM)
        vn.next_to(a_arr, DOWN, buff=0.8)
        self.add(vn)
        vn2 = Text("word embeddings", font=MONO, font_size=14, color=DIM)
        vn2.next_to(vn, DOWN, buff=0.1)
        self.add(vn2)

        # ── Section 2: Bivector ────────────────────────────────────
        bx = 1.2

        gr2 = Text("Grade 2", font=MONO, font_size=16, color=DIM)
        gr2.move_to([bx, 2.3, 0])
        self.add(gr2)

        va = np.array([1.3, 0.4, 0.0])
        vb = np.array([0.2, 1.4, 0.0])

        # Parallelogram
        para = Polygon(
            np.zeros(3), va, va + vb, vb,
            color=PURPLE, stroke_width=4, fill_opacity=0.3,
        )
        para.shift([bx, sec_y, 0])
        self.add(para)

        # Arrows along edges
        abiv = Arrow(start=[0, 0, 0], end=va, color=SECONDARY,
                     stroke_width=6, max_tip_length_to_length_ratio=0.12)
        bbiv = Arrow(start=[0, 0, 0], end=vb, color=RED,
                     stroke_width=6, max_tip_length_to_length_ratio=0.12)
        abiv.shift([bx, sec_y, 0])
        bbiv.shift([bx, sec_y, 0])
        self.add(abiv, bbiv)

        wlab = Text("a \u2227 b", font_size=28, color=PURPLE, weight=BOLD)
        wlab.move_to([bx, sec_y - 1.3, 0])
        self.add(wlab)

        bn = Text("oriented plane", font=MONO, font_size=14, color=DIM)
        bn.next_to(wlab, DOWN, buff=0.1)
        self.add(bn)

        # Orientation arc
        arc = ArcBetweenPoints(
            va * 0.6, vb * 0.6, angle=0.4,
            color=ACCENT, stroke_width=3
        )
        arc.shift([bx, sec_y, 0])
        self.add(arc)

        # ── Section 3: Trivector ───────────────────────────────────
        tx = 5.2

        gr3 = Text("Grade 3", font=MONO, font_size=16, color=DIM)
        gr3.move_to([tx, 2.3, 0])
        self.add(gr3)

        p = np.array([1.0, 0.2, 0.0])
        q = np.array([0.1, 1.0, 0.0])
        r = np.array([-0.1, 0.1, 0.8])

        # Parallelepiped faces
        verts = [
            np.zeros(3), p, q, p + q,
            r, p + r, q + r, p + q + r,
        ]

        # Front face
        front = Polygon(verts[0], verts[1], verts[3], verts[2],
                        color=PURPLE, stroke_width=2, fill_opacity=0.15)
        # Back face
        back = Polygon(verts[4], verts[5], verts[7], verts[6],
                       color=PURPLE, stroke_width=2, fill_opacity=0.15)
        # Edges
        edges = VGroup()
        for i in range(4):
            edges.add(Line(verts[i], verts[i + 4], color=PURPLE, stroke_width=2))

        volume = VGroup(front, back, edges)
        volume.shift([tx, sec_y, 0])
        self.add(volume)

        # 3 vectors
        for vec, col, lab in [(p, SECONDARY, "a"), (q, RED, "b"), (r, ACCENT, "c")]:
            arr = Arrow(start=[0, 0, 0], end=vec, color=col,
                        stroke_width=6, max_tip_length_to_length_ratio=0.1)
            arr.shift([tx, sec_y, 0])
            self.add(arr)
            lbl = Text(lab, font_size=24, color=col)
            lbl.next_to(arr.get_end() + np.array([tx, sec_y, 0]), buff=0.1)
            self.add(lbl)

        tw = Text("a \u2227 b \u2227 c", font_size=24, color=PURPLE, weight=BOLD)
        tw.move_to([tx, sec_y - 1.5, 0])
        self.add(tw)

        tn = Text("oriented volume", font=MONO, font_size=14, color=DIM)
        tn.next_to(tw, DOWN, buff=0.1)
        self.add(tn)

        # ── Connecting arrows between sections ─────────────────────
        for cx in [-4.3, 0.0, 3.8]:
            arr = Arrow(
                start=[cx - 0.3, 0.8, 0],
                end=[cx + 0.3, 0.8, 0],
                color=DIM, stroke_width=2, max_tip_length_to_length_ratio=0.1,
            )
            self.add(arr)

        # ── Bottom formula ─────────────────────────────────────────
        formula = Text(
            "ab = a\u00b7b + a\u2227b",
            font_size=28, color=WHITE
        )
        formula.to_edge(DOWN, buff=0.5)
        self.add(formula)

        # ── Output ─────────────────────────────────────────────────
        self.wait(0.1)


if __name__ == "__main__":
    print("Render with:")
    print("  manim -qh ga_cheatsheet.py GACheatSheet")

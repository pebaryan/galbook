"""
King → Queen: Vector Offset vs Rotor — Chapter 7 illustration

Left panel: standard vector addition (king + gender offset ≈ queen)
Right panel: rotor sandwich (R · king · R~ = queen) with gender bivector
"""
from manim import *
import numpy as np

BG = "#1C1C1C"
PRIMARY = "#58C4DD"
GREEN = "#83C167"
ACCENT = "#FFFF00"
RED = "#FF6B6B"
PURPLE = "#C084FC"
ORANGE = "#FFA726"
WHITE = "#EAEAEA"
DIM = "#888888"
MONO = "Menlo"


class KingQueenRotor(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Title ──────────────────────────────────────────────────
        title = Text("King → Queen: Two Approaches", font=MONO,
                     font_size=30, color=PRIMARY, weight=BOLD)
        title.to_edge(UP)
        self.add(title)

        # ── Divider ────────────────────────────────────────────────
        divider = DashedLine(start=[0, -2.5, 0], end=[0, 2.5, 0], color=DIM, stroke_width=1)
        self.add(divider)

        # ══════════════════════════════════════════════════════════
        # LEFT PANEL: Vector Offset
        # ══════════════════════════════════════════════════════════
        lx = -3.5
        ly = 0.0

        panel1_title = Text("Vector offset", font=MONO, font_size=18, color=DIM)
        panel1_title.move_to([lx, 2.0, 0])
        self.add(panel1_title)

        # King vector
        k_vec = np.array([-0.8, 1.2, 0.0])
        k_arrow = Arrow(start=[lx, ly, 0], end=[lx + k_vec[0], ly + k_vec[1], 0],
                        color=GREEN, stroke_width=7, max_tip_length_to_length_ratio=0.12)
        k_lab = Text("king", font=MONO, font_size=16, color=GREEN, weight=BOLD)
        k_lab.next_to([lx + k_vec[0], ly + k_vec[1], 0], UP + RIGHT, buff=0.05)
        self.add(k_arrow, k_lab)

        # Gender offset vector
        g_vec = np.array([0.5, -1.0, 0.0])
        g_arrow = Arrow(start=[lx + k_vec[0] * 0.6, ly + k_vec[1] * 0.6, 0],
                        end=[lx + k_vec[0] * 0.6 + g_vec[0], ly + k_vec[1] * 0.6 + g_vec[1], 0],
                        color=ACCENT, stroke_width=5, max_tip_length_to_length_ratio=0.1)
        g_lab = Text("woman \u2212 man", font=MONO, font_size=13, color=ACCENT)
        g_lab.next_to([lx + k_vec[0] * 0.6 + g_vec[0] * 0.5,
                       ly + k_vec[1] * 0.6 + g_vec[1] * 0.5, 0],
                      LEFT, buff=0.05)
        self.add(g_arrow, g_lab)

        # Result: queen (approximate)
        q_vec = k_vec + g_vec
        q_arrow = Arrow(start=[lx, ly, 0],
                        end=[lx + q_vec[0], ly + q_vec[1], 0],
                        color=RED, stroke_width=5, max_tip_length_to_length_ratio=0.1,
                        stroke_opacity=0.6)
        q_lab = Text("queen (approx)", font=MONO, font_size=14, color=RED)
        q_lab.next_to([lx + q_vec[0], ly + q_vec[1], 0], DOWN + RIGHT, buff=0.05)
        self.add(q_arrow, q_lab)

        # Cross marks
        cx1 = lx - 0.8
        for i, label in enumerate([
            "X No geometric meaning",
            "X Different per word pair",
            "X Can't compose"
        ]):
            t = Text(label, font=MONO, font_size=11, color=RED)
            t.move_to([cx1, -1.0 - 0.4 * i, 0])
            self.add(t)

        # ══════════════════════════════════════════════════════════
        # RIGHT PANEL: Rotor
        # ══════════════════════════════════════════════════════════
        rx = 3.5
        ry = 0.0

        panel2_title = Text("Rotor transformation", font=MONO, font_size=18, color=DIM)
        panel2_title.move_to([rx, 2.0, 0])
        self.add(panel2_title)

        # Gender bivector plane (a 2D region)
        plane = Rectangle(width=2.8, height=2.8, color=PURPLE,
                          fill_opacity=0.1, stroke_width=1)
        plane.move_to([rx, ry, 0])
        self.add(plane)

        # Axes labels
        male_lab = Text("male", font=MONO, font_size=13, color=PURPLE)
        male_lab.move_to([rx - 1.6, ry + 0.3, 0])
        female_lab = Text("female", font=MONO, font_size=13, color=PURPLE)
        female_lab.move_to([rx + 1.6, ry - 0.3, 0])
        self.add(male_lab, female_lab)

        # King vector (pointing toward male region)
        rk_vec = np.array([-0.9, 0.7, 0.0])
        rk_arrow = Arrow(start=[rx, ry, 0], end=[rx + rk_vec[0], ry + rk_vec[1], 0],
                         color=GREEN, stroke_width=7, max_tip_length_to_length_ratio=0.12)
        rk_lab = Text("king", font=MONO, font_size=16, color=GREEN, weight=BOLD)
        rk_lab.next_to([rx + rk_vec[0], ry + rk_vec[1], 0], UP + LEFT, buff=0.05)
        self.add(rk_arrow, rk_lab)

        # Rotation arc
        rot_angle = -PI * 0.65
        start_angle = np.arctan2(rk_vec[1], rk_vec[0])
        arc = Arc(
            radius=1.0, start_angle=start_angle, angle=rot_angle,
            color=ACCENT, stroke_width=3
        )
        arc.move_to([rx, ry, 0])
        self.add(arc)

        # Rotor label on arc
        rotor_lab = Text("R = exp(\u03b8/2 \u00b7 B)", font=MONO, font_size=14, color=ACCENT)
        mid_angle = start_angle + rot_angle / 2
        rotor_lab.next_to([rx + 1.3 * np.cos(mid_angle),
                           ry + 1.3 * np.sin(mid_angle), 0],
                          UP, buff=0.15)
        self.add(rotor_lab)

        # Bivector label
        biv_lab = Text("B = male \u2227 female", font=MONO, font_size=13, color=PURPLE)
        biv_lab.move_to([rx, ry - 1.8, 0])
        self.add(biv_lab)

        # Queen result
        rq_vec = np.array([0.8, -0.9, 0.0])
        rq_arrow = Arrow(start=[rx, ry, 0], end=[rx + rq_vec[0], ry + rq_vec[1], 0],
                         color=RED, stroke_width=7, max_tip_length_to_length_ratio=0.12)
        rq_lab = Text("queen", font=MONO, font_size=16, color=RED, weight=BOLD)
        rq_lab.next_to([rx + rq_vec[0], ry + rq_vec[1], 0], DOWN + RIGHT, buff=0.05)
        self.add(rq_arrow, rq_lab)

        # Checkmarks
        ckx = rx - 0.8
        for i, label in enumerate([
            "Built-in geometric meaning",
            "Same R for any word pair",
            "Composes: R2(R1 x R1~)R2~"
        ]):
            t = Text(label, font=MONO, font_size=11, color=GREEN)
            t.move_to([ckx, -1.0 - 0.4 * i, 0])
            self.add(t)

        # ── Bottom formula ─────────────────────────────────────────
        formula = Text(
            "R \u00b7 king \u00b7 R\u0303 = queen       where       R = exp(\u03b8/2 \u00b7 B)",
            font_size=20, color=WHITE
        )
        formula.to_edge(DOWN, buff=0.5)
        self.add(formula)

        self.wait(0.1)


if __name__ == "__main__":
    print("manim -qh king_queen_rotor.py KingQueenRotor")

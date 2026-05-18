"""
Cat → Dog SLERP on a sphere — Chapter 2 illustration

Shows two word vectors on a hypersphere with the SLERP interpolation arc
between them, replacing the ASCII art diagram.
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


class CatDogSLERP(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Title ──────────────────────────────────────────────────
        title = Text("Word Vectors on a Hypersphere", font=MONO,
                     font_size=30, color=PRIMARY, weight=BOLD)
        title.to_edge(UP)
        self.add(title)

        subtitle = Text("What's halfway between cat and dog?", font=MONO,
                        font_size=18, color=DIM)
        subtitle.next_to(title, DOWN, buff=0.15)
        self.add(subtitle)

        # ── Sphere ─────────────────────────────────────────────────
        center = np.array([0.0, -0.3, 0.0])
        radius = 2.5

        sphere = Circle(radius=radius, color=DIM, stroke_width=2, fill_opacity=0.05)
        sphere.move_to(center)
        self.add(sphere)

        # Subtle grid lines on sphere
        for angle in np.linspace(0, TAU, 8, endpoint=False):
            g = DashedLine(
                center + radius * np.array([np.cos(angle), np.sin(angle), 0]),
                center - radius * np.array([np.cos(angle), np.sin(angle), 0]),
                color=DIM, stroke_width=0.5, dashed_ratio=0.3,
            )
            self.add(g)

        # ── Cat vector ─────────────────────────────────────────────
        cat_angle = 220 * DEGREES
        cat_vec = np.array([np.cos(cat_angle), np.sin(cat_angle), 0]) * radius
        cat_arrow = Arrow(
            start=center, end=center + cat_vec,
            color=SECONDARY, stroke_width=8,
            max_tip_length_to_length_ratio=0.12,
        )
        cat_lab = Text("cat", font=MONO, font_size=24, color=SECONDARY, weight=BOLD)
        cat_lab.next_to(center + cat_vec, DOWN + LEFT, buff=0.15)

        self.add(cat_arrow, cat_lab)

        # ── Dog vector ─────────────────────────────────────────────
        dog_angle = 320 * DEGREES
        dog_vec = np.array([np.cos(dog_angle), np.sin(dog_angle), 0]) * radius
        dog_arrow = Arrow(
            start=center, end=center + dog_vec,
            color=RED, stroke_width=8,
            max_tip_length_to_length_ratio=0.12,
        )
        dog_lab = Text("dog", font=MONO, font_size=24, color=RED, weight=BOLD)
        dog_lab.next_to(center + dog_vec, DOWN + RIGHT, buff=0.15)

        self.add(dog_arrow, dog_lab)

        # ── SLERP arc (great circle arc) ───────────────────────────
        arc = ArcBetweenPoints(
            center + cat_vec, center + dog_vec,
            angle=0,  # shortest path
            color=ACCENT, stroke_width=4,
        )
        self.add(arc)

        # ── Midpoint on arc ────────────────────────────────────────
        # SLERP midpoint at t=0.5
        mid_angle = (cat_angle + dog_angle) / 2
        mid_vec = np.array([np.cos(mid_angle), np.sin(mid_angle), 0]) * radius

        mid_dot = Dot(center + mid_vec, color=ACCENT, radius=0.08)
        mid_lab = Text("?", font=MONO, font_size=20, color=ACCENT, weight=BOLD)
        mid_lab.next_to(center + mid_vec, UP, buff=0.1)
        self.add(mid_dot, mid_lab)

        # ── Labels ─────────────────────────────────────────────────
        center_lab = Text("hypersphere surface", font=MONO, font_size=14, color=DIM)
        center_lab.next_to(center, DOWN, buff=0.3)
        self.add(center_lab)

        arc_lab = Text("SLERP path", font=MONO, font_size=14, color=ACCENT)
        arc_lab.next_to(center + mid_vec, LEFT, buff=0.3)
        self.add(arc_lab)

        # ── Formula ────────────────────────────────────────────────
        formula = Text(
            "SLERP(a, b, t) = sin((1-t)\u03c9)/sin(\u03c9) \u00b7 a + sin(t\u03c9)/sin(\u03c9) \u00b7 b",
            font_size=20, color=WHITE
        )
        formula.to_edge(DOWN, buff=0.5)
        self.add(formula)

        self.wait(0.1)


if __name__ == "__main__":
    print("manim -qh cat_dog_slerp.py CatDogSLERP")

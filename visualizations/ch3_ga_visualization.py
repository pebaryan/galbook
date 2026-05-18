"""
The Geometry of Meaning — Chapter 3 Visualization
===================================================

Three scenes illustrating Geometric Algebra foundations:
1. Geometric product: a·b + a∧b
2. Bivector as oriented plane
3. Trivector as oriented volume

No LaTeX required — uses Text() with monospace font.
"""

from manim import *
import numpy as np

# ── Constants ──────────────────────────────────────────────────────
BG = "#1C1C1C"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FFFF00"
RED = "#FF6B6B"
PURPLE = "#C084FC"
WHITE = "#EAEAEA"
MONO = "Menlo"
LIGHT = 0.4
DARK_LABEL = 0.6


def T(scene, text_str, **kwargs):
    """Create flat text that always faces the camera in 3D scenes.
    Pass 'self' (the scene) as the first argument."""
    t = Text(text_str, font=MONO, **kwargs)
    scene.add_fixed_in_frame_mobjects(t)
    return t


# ═══════════════════════════════════════════════════════════════════
# Scene 1: The Geometric Product
# ═══════════════════════════════════════════════════════════════════
class Scene1_GeometricProduct(ThreeDScene):
    """Two vectors a, b → dot product (scalar) + wedge product (bivector)."""

    def construct(self):
        self.camera.background_color = BG
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        # Let camera settle before any mobjects to avoid first-frame glitch
        self.wait(0.01)

        # ── Title ──
        title = T(self, "The Geometric Product", font_size=48, color=PRIMARY, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(1.0)

        # ── Two vectors ──
        a_vec = np.array([2.5, 0.5, 0.0])
        b_vec = np.array([0.5, 2.0, 0.5])

        a_label = T(self, "a", font_size=30, color=SECONDARY)
        b_label = T(self, "b", font_size=30, color=RED)

        a_arrow = Arrow3D(np.zeros(3), a_vec, color=SECONDARY, resolution=8)
        b_arrow = Arrow3D(np.zeros(3), b_vec, color=RED, resolution=8)

        a_label.next_to(a_vec, RIGHT, buff=0.2)
        b_label.next_to(b_vec, UP, buff=0.2)

        self.add_subcaption("Two vectors, a and b", duration=2)
        self.play(
            Create(a_arrow), Write(a_label),
            Create(b_arrow), Write(b_label),
            run_time=2.0
        )
        self.wait(1.0)

        # ── Dot product: scalar ──
        dot_val = np.dot(a_vec, b_vec)
        dot_title = T(self, "a . b  (dot product = scalar)", font_size=28, color=ACCENT)
        dot_title.to_edge(DOWN, buff=1.0)

        # Draw projection line
        b_on_a = (dot_val / np.dot(a_vec, a_vec)) * a_vec
        proj_line = DashedLine(start=b_vec, end=b_on_a, color=ACCENT, stroke_width=2)

        self.add_subcaption("The dot product captures alignment", duration=2)
        self.play(Write(dot_title), Create(proj_line), run_time=1.5)
        self.wait(1.5)

        # ── Wedge product: bivector ──
        wedge_title = T(self, 
            "a . b + a ^ b  (geometric product = multivector)",
            font_size=26, color=WHITE
        )
        wedge_title.next_to(dot_title, DOWN, buff=0.3, aligned_edge=LEFT)

        # Draw the parallelogram for a∧b
        parallelogram = Polygon(
            np.zeros(3), a_vec, a_vec + b_vec, b_vec,
            color=PURPLE, stroke_width=3, fill_opacity=0.25
        )

        wedge_note = T(self, 
            "a ^ b = oriented plane (bivector)",
            font_size=24, color=PURPLE, opacity=LIGHT
        )
        wedge_note.next_to(wedge_title, DOWN, buff=0.3, aligned_edge=LEFT)

        self.add_subcaption(
            "The wedge product creates an oriented plane - a bivector",
            duration=2
        )
        self.play(
            Create(parallelogram),
            FadeIn(wedge_title, shift=UP),
            run_time=2.0
        )
        self.wait(0.5)
        self.play(Write(wedge_note), run_time=1.0)
        self.wait(1.5)

        # ── Reveal formula ──
        formula_text = T(self, 
            "ab = a . b + a ^ b",
            font_size=40, color=ACCENT, weight=BOLD
        )
        formula_text.to_edge(DOWN, buff=0.3)
        self.add_subcaption("The geometric product combines both", duration=2)
        self.play(
            ReplacementTransform(wedge_title, formula_text),
            FadeOut(dot_title, shift=DOWN),
            FadeOut(wedge_note, shift=DOWN),
            run_time=2.0
        )
        self.wait(2.0)

        # ── Clean exit ──
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.5)


# ═══════════════════════════════════════════════════════════════════
# Scene 2: Bivector as Oriented Plane
# ═══════════════════════════════════════════════════════════════════
class Scene2_BivectorOrientation(ThreeDScene):
    """Show that a∧b = -b∧a — orientation matters."""

    def construct(self):
        self.camera.background_color = BG
        self.set_camera_orientation(phi=70 * DEGREES, theta=-30 * DEGREES)
        self.wait(0.01)

        # ── Title ──
        title = T(self, "Bivector = Oriented Plane", font_size=44, color=PRIMARY, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(1.0)

        # ── Vectors for first bivector a∧b ──
        a = np.array([2.5, 0.3, 0.0])
        b = np.array([0.3, 2.0, 0.0])

        a_arrow = Arrow3D(np.zeros(3), a, color=SECONDARY, resolution=8)
        b_arrow = Arrow3D(np.zeros(3), b, color=RED, resolution=8)

        label_a = T(self, "a", font_size=28, color=SECONDARY)
        label_b = T(self, "b", font_size=28, color=RED)
        label_a.next_to(a, RIGHT, buff=0.2)
        label_b.next_to(b, UP, buff=0.2)

        # Draw a∧b parallelogram
        para1 = Polygon(
            np.zeros(3), a, a + b, b,
            color=PURPLE, stroke_width=3, fill_opacity=0.3
        )

        # Label
        ab_label = T(self, "a ^ b", font_size=28, color=PURPLE, weight=BOLD)
        ab_label.move_to((a + b) / 2 + np.array([0.0, 0.3, 0.5]))

        self.add_subcaption("a wedge b creates an oriented plane", duration=2)
        self.play(
            Create(a_arrow), Write(label_a),
            Create(b_arrow), Write(label_b),
            run_time=1.5
        )
        self.play(Create(para1), Write(ab_label), run_time=1.5)
        self.wait(1.5)

        # ── Show orientation arrow ──
        orient_arc = ArcBetweenPoints(
            a / 1.5, b / 1.5, angle=0.4,
            color=ACCENT, stroke_width=4
        )
        orient_label = T(self, 
            "orientation", font_size=22, color=ACCENT, opacity=LIGHT
        )
        orient_label.next_to(orient_arc, RIGHT, buff=0.3)

        self.add_subcaption(
            "The bivector has a direction - orientation matters",
            duration=2
        )
        self.play(Create(orient_arc), Write(orient_label), run_time=1.5)
        self.wait(1.5)

        # ── Transform to b∧a (swap orientation) ──
        self.move_camera(phi=60 * DEGREES, theta=-20 * DEGREES, run_time=2.0)

        # New parallelogram for b∧a (same shape, flipped orientation)
        para2 = Polygon(
            np.zeros(3), b, a + b, a,
            color=RED, stroke_width=3, fill_opacity=0.3
        )

        ba_label = T(self, "b ^ a = -(a ^ b)", font_size=28, color=RED, weight=BOLD)
        ba_label.move_to((a + b) / 2 + np.array([0.0, -0.3, -0.5]))

        # Flip arc
        flip_arc = ArcBetweenPoints(
            b / 1.5, a / 1.5, angle=0.4,
            color=RED, stroke_width=4
        )

        self.add_subcaption(
            "Swap the order and the bivector flips - anti-symmetry",
            duration=2.5
        )
        self.play(
            ReplacementTransform(para1, para2),
            ReplacementTransform(ab_label, ba_label),
            ReplacementTransform(orient_arc, flip_arc),
            run_time=2.5
        )
        self.wait(2.0)

        # ── Clean exit ──
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.5)


# ═══════════════════════════════════════════════════════════════════
# Scene 3: Trivector as Oriented Volume
# ═══════════════════════════════════════════════════════════════════
class Scene3_TrivectorVolume(ThreeDScene):
    """Three vectors → oriented parallelepiped (trivector = volume)."""

    def construct(self):
        self.camera.background_color = BG
        self.set_camera_orientation(phi=65 * DEGREES, theta=-35 * DEGREES)
        self.wait(0.01)

        # ── Title ──
        title = T(self, "Trivector = Oriented Volume", font_size=44, color=PRIMARY, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(1.0)

        # ── Three vectors ──
        a = np.array([2.0, 0.2, 0.0])
        b = np.array([0.3, 1.8, 0.0])
        c = np.array([0.0, 0.2, 1.5])

        a_arrow = Arrow3D(np.zeros(3), a, color=SECONDARY, resolution=8)
        b_arrow = Arrow3D(np.zeros(3), b, color=RED, resolution=8)
        c_arrow = Arrow3D(np.zeros(3), c, color=ACCENT, resolution=8)

        label_a = T(self, "a", font_size=26, color=SECONDARY)
        label_b = T(self, "b", font_size=26, color=RED)
        label_c = T(self, "c", font_size=26, color=ACCENT)
        label_a.next_to(a, RIGHT, buff=0.2)
        label_b.next_to(b, UP, buff=0.2)
        label_c.next_to(c, OUT, buff=0.2)

        self.add_subcaption("Three vectors span a volume", duration=1.5)
        self.play(
            Create(a_arrow), Write(label_a),
            Create(b_arrow), Write(label_b),
            Create(c_arrow), Write(label_c),
            run_time=2.0
        )
        self.wait(1.0)

        # ── Build the parallelepiped ──
        verts = [
            np.zeros(3),
            a,
            b,
            a + b,
            c,
            a + c,
            b + c,
            a + b + c,
        ]

        # Front face (a, b plane)
        front = Polygon(
            verts[0], verts[1], verts[3], verts[2],
            color=PURPLE, stroke_width=2, fill_opacity=0.15
        )
        # Back face (offset by c)
        back = Polygon(
            verts[4], verts[5], verts[7], verts[6],
            color=PURPLE, stroke_width=2, fill_opacity=0.15
        )
        # Connecting edges
        edges = VGroup()
        for i in range(4):
            edges.add(Line(verts[i], verts[i + 4], color=PURPLE, stroke_width=2))

        volume = VGroup(front, back, edges)

        vol_label = T(self, "a ^ b ^ c  (trivector)", font_size=28, color=PURPLE, weight=BOLD)
        vol_label.move_to((a + b + c) / 2 + np.array([0.0, -0.5, 0.0]))

        self.add_subcaption(
            "The wedge product of three vectors creates a trivector - an oriented volume",
            duration=2
        )
        self.play(Create(volume), Write(vol_label), run_time=2.5)
        self.wait(1.0)

        # ── Rotate to show 3D structure ──
        self.add_subcaption(
            "A trivector has magnitude (volume) and orientation (handedness)",
            duration=2
        )
        self.move_camera(phi=55 * DEGREES, theta=-55 * DEGREES, run_time=3.0)
        self.wait(2.0)

        # ── Hierarchy text ──
        hierarchy = T(self, 
            "grade 0: scalar    grade 1: vector\n"
            "grade 2: bivector  grade 3: trivector",
            font_size=22, color=WHITE, opacity=DARK_LABEL
        )
        hierarchy.to_edge(DOWN, buff=0.5)

        self.add_subcaption(
            "Each grade encodes a different geometric object",
            duration=1.5
        )
        self.play(Write(hierarchy), run_time=1.5)
        self.wait(2.0)

        # ── Clean exit ──
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.5)


# ═══════════════════════════════════════════════════════════════════
# Render instructions
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Render with:")
    print("  manim -ql script.py Scene1_GeometricProduct  # draft")
    print("  manim -qh script.py Scene1_GeometricProduct  # production")
    print("  manim -ql script.py Scene2_BivectorOrientation")
    print("  manim -ql script.py Scene3_TrivectorVolume")
    print("")
    print("Stitch:")
    print("  cat > concat.txt << 'EOF'")
    print("  file 'media/videos/script/480p15/Scene1_GeometricProduct.mp4'")
    print("  file 'media/videos/script/480p15/Scene2_BivectorOrientation.mp4'")
    print("  file 'media/videos/script/480p15/Scene3_TrivectorVolume.mp4'")
    print("  EOF")
    print("  ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4")

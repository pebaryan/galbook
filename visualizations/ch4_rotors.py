from manim import *
import numpy as np


class Scene1_RotorSandwich(Scene):
    """Show the rotor sandwich product: x' = R x R_tilde"""
    def construct(self):
        title = Text("The Rotor Sandwich", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Show the formula
        formula = MathTex(r"x' = R \, x \, \tilde{R}", font_size=40)
        formula.shift(UP * 1.5)
        self.play(Write(formula))

        # Labels
        rotor_label = Text("Rotor", font_size=20, color=BLUE).next_to(formula[0][0:2], DOWN, buff=0.5)
        vector_label = Text("Vector", font_size=20, color=GREEN).next_to(formula[0][3], DOWN, buff=0.5)
        reverse_label = Text("Reverse", font_size=20, color=BLUE).next_to(formula[0][5:7], DOWN, buff=0.5)

        self.play(Write(rotor_label), Write(vector_label), Write(reverse_label))

        # Arrow showing flow
        flow_arrow = Arrow(LEFT * 4, RIGHT * 4, color=YELLOW, buff=0)
        flow_arrow.shift(DOWN * 0.5)
        flow_text = Text("Rotation happens here", font_size=18, color=YELLOW).next_to(flow_arrow, UP, buff=0.2)

        self.play(GrowArrow(flow_arrow), Write(flow_text))

        # Key insight
        insight = VGroup(
            Text("The sandwich preserves the grade:", font_size=18),
            Text("Vector in → Vector out", font_size=18, color=GREEN),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN)

        self.play(Write(insight))
        self.wait(4)


class Scene2_Rotation2D(Scene):
    """Concrete 2D rotation example: (1,0) rotated 90° to (0,1)"""
    def construct(self):
        title = Text("2D Rotation Example", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create axes
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], x_length=6, y_length=6)
        axes.shift(LEFT * 2)

        self.play(Create(axes))

        # Original vector
        vec_x = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(1.5, 0), buff=0, color=BLUE)
        label_x = Text("x = (1, 0)", font_size=18, color=BLUE).next_to(vec_x.get_end(), DOWN, buff=0.2)

        self.play(GrowArrow(vec_x), Write(label_x))

        # Rotated vector
        vec_rotated = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(0, 1.5), buff=0, color=GREEN)
        label_rotated = Text("x' = (0, 1)", font_size=18, color=GREEN).next_to(vec_rotated.get_end(), RIGHT, buff=0.2)

        # Arc showing rotation
        arc = Arc(radius=1.2, start_angle=0, angle=PI/2, arc_center=axes.coords_to_point(0, 0), color=YELLOW)
        angle_label = MathTex(r"90^", font_size=20, color=YELLOW).move_to(axes.coords_to_point(0.8, 0.8))

        self.play(Create(arc), Write(angle_label))
        self.play(GrowArrow(vec_rotated), Write(label_rotated))

        # Right side: rotor formula
        formula = VGroup(
            Text("Rotor:", font_size=16),
            MathTex(r"R = \cos(45^) + \sin(45^) \cdot e_{12}", font_size=22),
            Text(" ", font_size=12),
            Text("Sandwich:", font_size=16),
            MathTex(r"x' = R \cdot x \cdot \tilde{R}", font_size=22),
        ).arrange(DOWN, buff=0.3).shift(RIGHT * 3.5)

        self.play(Write(formula))

        result = Text("= e₂ (= north ✓)", font_size=18, color=GREEN).next_to(formula[-1], DOWN, buff=0.3)
        self.play(Write(result))

        self.wait(4)


class Scene3_QuaternionsAsBivectors(Scene):
    """Show quaternions i,j,k as 3D bivectors"""
    def construct(self):
        title = Text("Quaternions = 3D Rotors", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Left side: quaternion view
        quat_title = Text("Quaternions (Hamilton)", font_size=22, color=BLUE).shift(LEFT * 3.5 + UP * 2)
        quat_form = MathTex(r"q = w + xi + yj + zk", font_size=24)
        quat_form.next_to(quat_title, DOWN, buff=0.3)

        quat_rules = VGroup(
            Text("Mysterious rules:", font_size=16),
            MathTex(r"i = \sqrt{-1}", font_size=18),
            MathTex(r"ij = k,\; jk = i,\; ki = j", font_size=18),
        ).arrange(DOWN, buff=0.2).next_to(quat_form, DOWN, buff=0.4)

        self.play(Write(quat_title), Write(quat_form))
        self.play(Write(quat_rules))

        # Arrow pointing to GA view
        arrow = Arrow(LEFT * 1, RIGHT * 1, color=YELLOW, buff=0)
        arrow_label = Text("GA reveals", font_size=18, color=YELLOW).next_to(arrow, UP, buff=0.1)
        self.play(GrowArrow(arrow), Write(arrow_label))

        # Right side: GA view
        ga_title = Text("3D Rotors (Clifford)", font_size=22, color=GREEN).shift(RIGHT * 3.5 + UP * 2)
        ga_form = MathTex(r"R = w + x e_{23} + y e_{31} + z e_{12}", font_size=24)
        ga_form.next_to(ga_title, DOWN, buff=0.3)

        ga_rules = VGroup(
            Text("i, j, k are bivectors:", font_size=16),
            MathTex(r"i = e_{23},\; j = e_{31},\; k = e_{12}", font_size=18),
            Text("Planes of rotation!", font_size=16, color=YELLOW),
        ).arrange(DOWN, buff=0.2).next_to(ga_form, DOWN, buff=0.4)

        self.play(Write(ga_title), Write(ga_form))
        self.play(Write(ga_rules))

        # Key insight at bottom
        insight = Text(
            "Quaternions are rotors: q · v · q* rotates vector v",
            font_size=20,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(insight))
        self.wait(4)


class Scene4_RotorComposition(Scene):
    """Show that rotors compose by multiplication"""
    def construct(self):
        title = Text("Rotor Composition", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Vector being rotated
        vec = Arrow(ORIGIN, RIGHT * 2, buff=0, color=GREEN)
        vec_label = Text("v", font_size=24, color=GREEN).next_to(vec.get_end(), UP, buff=0.1)
        self.play(GrowArrow(vec), Write(vec_label))

        # First rotation
        R1_label = MathTex(r"R_1", font_size=28, color=BLUE).shift(UP * 1.5 + LEFT * 3)
        arrow1 = Arrow(R1_label.get_bottom(), vec.get_center() + UP * 0.3, color=BLUE)
        self.play(Write(R1_label), GrowArrow(arrow1))

        # Intermediate result
        vec_mid = Arrow(ORIGIN, UP * 2, buff=0, color=YELLOW)
        vec_mid_label = Text("v'", font_size=20, color=YELLOW).next_to(vec_mid.get_end(), RIGHT, buff=0.1)

        arc1 = Arc(radius=1.5, start_angle=0, angle=PI/2, color=BLUE)
        self.play(Create(arc1))
        self.play(Transform(vec.copy(), vec_mid), Write(vec_mid_label))

        # Second rotation
        R2_label = MathTex(r"R_2", font_size=28, color=RED).shift(UP * 1.5 + RIGHT * 3)
        arrow2 = Arrow(R2_label.get_bottom(), vec_mid.get_center() + RIGHT * 0.3, color=RED)
        self.play(Write(R2_label), GrowArrow(arrow2))

        # Final result
        vec_final = Arrow(ORIGIN, LEFT * 2, buff=0, color=PURPLE)
        vec_final_label = Text("v''", font_size=20, color=PURPLE).next_to(vec_final.get_end(), UP, buff=0.1)

        arc2 = Arc(radius=1.5, start_angle=PI/2, angle=PI/2, color=RED)
        self.play(Create(arc2))
        self.play(Transform(vec_mid.copy(), vec_final), Write(vec_final_label))

        # Formula at bottom
        formula = VGroup(
            MathTex(r"v'' = R_2 \cdot (R_1 \cdot v \cdot \tilde{R}_1) \cdot \tilde{R}_2", font_size=26),
            Text("= (R₂ R₁) · v · (R̃₁ R̃₂)", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN)

        self.play(Write(formula))

        key_point = Text("Rotors compose by multiplication: R_total = R₂ R₁", font_size=18, color=YELLOW).next_to(formula, UP, buff=0.3)
        self.play(Write(key_point))

        self.wait(4)


class Scene5_RotorVsMatrix(Scene):
    """Compare rotor and matrix representations"""
    def construct(self):
        title = Text("Rotor vs Matrix: 90° Rotation", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Left side: Rotor
        rotor_title = Text("Rotor", font_size=24, color=BLUE).shift(LEFT * 4 + UP * 1.5)
        rotor_eq = MathTex(r"R = 0.707 + 0.707 \cdot e_{12}", font_size=22)
        rotor_eq.next_to(rotor_title, DOWN, buff=0.3)

        rotor_info = VGroup(
            Text("2 numbers + bivector", font_size=16),
            Text("Plane: e₁₂ (explicit!)", font_size=16, color=GREEN),
            Text("Angle: built into coeffs", font_size=16),
        ).arrange(DOWN, buff=0.2).next_to(rotor_eq, DOWN, buff=0.4)

        self.play(Write(rotor_title), Write(rotor_eq))
        self.play(Write(rotor_info))

        # Divider
        divider = Line(UP * 2, DOWN * 2, color=GRAY)
        self.play(Create(divider))

        # Right side: Matrix
        matrix_title = Text("Matrix", font_size=24, color=RED).shift(RIGHT * 4 + UP * 1.5)
        matrix_eq = MathTex(r"M = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}", font_size=24)
        matrix_eq.next_to(matrix_title, DOWN, buff=0.3)

        matrix_info = VGroup(
            Text("4 entries (2×2)", font_size=16),
            Text("Plane: implicit", font_size=16, color=RED),
            Text("Pattern encodes rotation", font_size=16),
        ).arrange(DOWN, buff=0.2).next_to(matrix_eq, DOWN, buff=0.4)

        self.play(Write(matrix_title), Write(matrix_eq))
        self.play(Write(matrix_info))

        # Bottom comparison
        comparison = Text(
            "Both rotate vectors ✓  |  Rotor keeps geometric structure ✓",
            font_size=20,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(comparison))
        self.wait(4)


class Scene6_RotorInterpolation(Scene):
    """Show rotor interpolation vs SLERP"""
    def construct(self):
        title = Text("Rotor Interpolation vs SLERP", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Arc with points
        arc = Arc(radius=2.5, start_angle=PI/6, angle=PI*2/3, color=BLUE)
        self.play(Create(arc))

        # Start and end points
        start_point = arc.point_from_proportion(0)
        end_point = arc.point_from_proportion(1)

        dot_a = Dot(start_point, color=BLUE, radius=0.12)
        dot_b = Dot(end_point, color=BLUE, radius=0.12)
        label_a = MathTex(r"a", font_size=24).next_to(dot_a, UR, buff=0.1)
        label_b = MathTex(r"b", font_size=24).next_to(dot_b, UL, buff=0.1)

        self.play(Create(dot_a), Create(dot_b), Write(label_a), Write(label_b))

        # Interpolation parameter
        t_tracker = ValueTracker(0)

        # Moving point
        moving_dot = Dot(arc.point_from_proportion(0), color=YELLOW, radius=0.1)
        moving_label = MathTex(r"x(t)", font_size=20, color=YELLOW)
        moving_label.add_updater(lambda m: m.next_to(moving_dot, DOWN, buff=0.2))

        self.play(Create(moving_dot), Write(moving_label))

        # Animate interpolation
        moving_dot.add_updater(
            lambda d: d.move_to(arc.point_from_proportion(t_tracker.get_value()))
        )

        self.play(t_tracker.animate.set_value(1), run_time=3, rate_func=linear)

        # Remove updaters
        moving_dot.remove_updater(moving_dot.updaters[0])
        moving_label.remove_updater(moving_label.updaters[0])

        # Right side: formulas
        formulas = VGroup(
            Text("Rotor Interpolation:", font_size=18, color=GREEN),
            MathTex(r"R(t) = R^t", font_size=22),
            Text(" ", font_size=12),
            Text("SLERP (vector only):", font_size=18, color=RED),
            MathTex(r"x(t) = \frac{\sin((1-t)\omega)}{\sin(\omega)}a + \frac{\sin(t\omega)}{\sin(\omega)}b", font_size=18),
            Text(" ", font_size=12),
            Text("Key difference:", font_size=18, color=YELLOW),
            Text("Rotor keeps the plane!", font_size=20, color=YELLOW),
        ).arrange(DOWN, buff=0.2).shift(RIGHT * 3.5 + UP * 0.5)

        self.play(Write(formulas))

        # SLERP loses info note
        note = Text(
            "SLERP discards the bivector → loses rotation plane",
            font_size=16,
            color=GRAY
        ).to_edge(DOWN)

        self.play(Write(note))
        self.wait(4)


if __name__ == "__main__":
    # Render commands:
    # manim -qh ch4_rotors.py Scene1_RotorSandwich
    # manim -qh ch4_rotors.py Scene2_Rotation2D
    # manim -qh ch4_rotors.py Scene3_QuaternionsAsBivectors
    # manim -qh ch4_rotors.py Scene4_RotorComposition
    # manim -qh ch4_rotors.py Scene5_RotorVsMatrix
    # manim -qh ch4_rotors.py Scene6_RotorInterpolation
    pass

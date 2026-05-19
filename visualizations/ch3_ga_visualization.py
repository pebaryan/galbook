from manim import *
import numpy as np


class Scene1_GeometricProduct(Scene):
    """Show the geometric product: ab = a·b + a∧b"""
    def construct(self):
        title = Text("The Geometric Product", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Two vectors
        vec_a = Arrow(ORIGIN, RIGHT * 2 + UP * 1, buff=0, color=BLUE)
        vec_b = Arrow(ORIGIN, RIGHT * 2.5 + DOWN * 0.5, buff=0, color=GREEN)

        label_a = Text("a", font_size=24, color=BLUE).next_to(vec_a.get_end(), UR, buff=0.1)
        label_b = Text("b", font_size=24, color=GREEN).next_to(vec_b.get_end(), DR, buff=0.1)

        self.play(GrowArrow(vec_a), Write(label_a))
        self.play(GrowArrow(vec_b), Write(label_b))

        # Show dot product (scalar part)
        dot_eq = MathTex(r"a \cdot b = \text{scalar}", font_size=28, color=YELLOW)
        dot_eq.shift(LEFT * 4 + UP * 1)
        self.play(Write(dot_eq))

        # Projection line
        proj_line = DashedLine(vec_b.get_end(), vec_a.get_end() * 0.7, color=GRAY)
        self.play(Create(proj_line))

        # Show wedge product (bivector part)
        wedge_eq = MathTex(r"a \wedge b = \text{bivector}", font_size=28, color=ORANGE)
        wedge_eq.shift(LEFT * 4 + DOWN * 1)
        self.play(Write(wedge_eq))

        # Parallelogram for wedge product
        parallelogram = Polygon(
            ORIGIN,
            vec_a.get_end(),
            vec_a.get_end() + vec_b.get_end(),
            vec_b.get_end(),
            fill_color=ORANGE,
            fill_opacity=0.3,
            stroke_color=ORANGE
        )
        self.play(Create(parallelogram))

        # Full geometric product equation
        full_eq = MathTex(r"ab = a \cdot b + a \wedge b", font_size=32)
        full_eq.to_edge(DOWN)
        self.play(Write(full_eq))

        note = Text("Dot product (scalar) + Wedge product (bivector)", font_size=18, color=YELLOW).next_to(full_eq, UP, buff=0.3)
        self.play(Write(note))
        self.wait(4)


class Scene2_BivectorOrientation(Scene):
    """Show bivector orientation and antisymmetry: a∧b = −b∧a"""
    def construct(self):
        title = Text("Bivector Orientation", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Left side: a ∧ b
        left_title = Text("a ∧ b", font_size=28).shift(LEFT * 3.5 + UP * 2)
        self.play(Write(left_title))

        vec_a1 = Arrow(ORIGIN + LEFT * 3.5, RIGHT * 1.5 + UP * 0.5 + LEFT * 3.5, buff=0, color=BLUE)
        vec_b1 = Arrow(ORIGIN + LEFT * 3.5, RIGHT * 2 + DOWN * 0.3 + LEFT * 3.5, buff=0, color=GREEN)

        label_a1 = Text("a", font_size=20, color=BLUE).next_to(vec_a1.get_end(), UR, buff=0.1)
        label_b1 = Text("b", font_size=20, color=GREEN).next_to(vec_b1.get_end(), DR, buff=0.1)

        parallelogram1 = Polygon(
            ORIGIN + LEFT * 3.5,
            vec_a1.get_end(),
            vec_a1.get_end() + (vec_b1.get_end() - (ORIGIN + LEFT * 3.5)),
            vec_b1.get_end(),
            fill_color=ORANGE,
            fill_opacity=0.4,
            stroke_color=ORANGE
        )

        # Orientation arc (counter-clockwise)
        arc1 = Arc(radius=0.8, start_angle=PI/6, angle=PI/3, arc_center=ORIGIN + LEFT * 3.5, color=YELLOW)
        arrow1 = Arrow(arc1.get_end(), arc1.get_end() + UP * 0.3 + RIGHT * 0.2, buff=0, color=YELLOW)

        self.play(GrowArrow(vec_a1), GrowArrow(vec_b1), Write(label_a1), Write(label_b1))
        self.play(Create(parallelogram1))
        self.play(Create(arc1), GrowArrow(arrow1))

        # Right side: b ∧ a
        right_title = Text("b ∧ a", font_size=28).shift(RIGHT * 3.5 + UP * 2)
        self.play(Write(right_title))

        vec_b2 = Arrow(ORIGIN + RIGHT * 3.5, RIGHT * 2 + DOWN * 0.3 + RIGHT * 3.5, buff=0, color=GREEN)
        vec_a2 = Arrow(ORIGIN + RIGHT * 3.5, RIGHT * 1.5 + UP * 0.5 + RIGHT * 3.5, buff=0, color=BLUE)

        label_b2 = Text("b", font_size=20, color=GREEN).next_to(vec_b2.get_end(), DR, buff=0.1)
        label_a2 = Text("a", font_size=20, color=BLUE).next_to(vec_a2.get_end(), UR, buff=0.1)

        parallelogram2 = Polygon(
            ORIGIN + RIGHT * 3.5,
            vec_b2.get_end(),
            vec_b2.get_end() + (vec_a2.get_end() - (ORIGIN + RIGHT * 3.5)),
            vec_a2.get_end(),
            fill_color=RED,
            fill_opacity=0.4,
            stroke_color=RED
        )

        # Orientation arc (clockwise)
        arc2 = Arc(radius=0.8, start_angle=PI/3, angle=-PI/3, arc_center=ORIGIN + RIGHT * 3.5, color=YELLOW)
        arrow2 = Arrow(arc2.get_end(), arc2.get_end() + DOWN * 0.3 + RIGHT * 0.2, buff=0, color=YELLOW)

        self.play(GrowArrow(vec_b2), GrowArrow(vec_a2), Write(label_b2), Write(label_a2))
        self.play(Create(parallelogram2))
        self.play(Create(arc2), GrowArrow(arrow2))

        # Key equation
        eq = MathTex(r"a \wedge b = - (b \wedge a)", font_size=32)
        eq.to_edge(DOWN)
        self.play(Write(eq))

        note = Text("Antisymmetry: swapping vectors reverses orientation", font_size=18, color=YELLOW).next_to(eq, UP, buff=0.3)
        self.play(Write(note))
        self.wait(4)


class Scene3_TrivectorVolume(Scene):
    """Show trivector as oriented volume"""
    def construct(self):
        title = Text("Trivectors: Oriented Volume", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Three vectors
        vec_a = Arrow(ORIGIN, RIGHT * 2 + UP * 0.5, buff=0, color=BLUE)
        vec_b = Arrow(ORIGIN, RIGHT * 1.5 + DOWN * 1, buff=0, color=GREEN)
        vec_c = Arrow(ORIGIN, UP * 2 + LEFT * 0.5, buff=0, color=RED)

        label_a = Text("a", font_size=20, color=BLUE).next_to(vec_a.get_end(), RIGHT, buff=0.1)
        label_b = Text("b", font_size=20, color=GREEN).next_to(vec_b.get_end(), DOWN, buff=0.1)
        label_c = Text("c", font_size=20, color=RED).next_to(vec_c.get_end(), UP, buff=0.1)

        self.play(GrowArrow(vec_a), GrowArrow(vec_b), GrowArrow(vec_c))
        self.play(Write(label_a), Write(label_b), Write(label_c))

        # Show parallelepiped (3D box)
        # Base parallelogram
        base = Polygon(
            ORIGIN,
            vec_a.get_end(),
            vec_a.get_end() + vec_b.get_end(),
            vec_b.get_end(),
            fill_color=ORANGE,
            fill_opacity=0.2,
            stroke_color=ORANGE
        )
        self.play(Create(base))

        # Top parallelogram (shifted by c)
        c_vec = vec_c.get_end() - ORIGIN
        top = Polygon(
            ORIGIN + c_vec,
            vec_a.get_end() + c_vec,
            vec_a.get_end() + vec_b.get_end() + c_vec,
            vec_b.get_end() + c_vec,
            fill_color=ORANGE,
            fill_opacity=0.2,
            stroke_color=ORANGE
        )
        self.play(Create(top))

        # Side edges
        edge1 = Line(ORIGIN, ORIGIN + c_vec, color=GRAY)
        edge2 = Line(vec_a.get_end(), vec_a.get_end() + c_vec, color=GRAY)
        edge3 = Line(vec_b.get_end(), vec_b.get_end() + c_vec, color=GRAY)
        edge4 = Line(vec_a.get_end() + vec_b.get_end(), vec_a.get_end() + vec_b.get_end() + c_vec, color=GRAY)

        self.play(Create(edge1), Create(edge2), Create(edge3), Create(edge4))

        # Volume label
        volume_text = Text("a ∧ b ∧ c = trivector (volume)", font_size=24, color=PURPLE)
        volume_text.to_edge(DOWN)
        self.play(Write(volume_text))

        # Orientation indicator
        orientation = Text("Right-hand rule orientation", font_size=18, color=YELLOW).next_to(volume_text, UP, buff=0.3)
        self.play(Write(orientation))
        self.wait(4)


class Scene4_MultivectorComponents(Scene):
    """Show all components of a multivector"""
    def construct(self):
        title = Text("Multivector Components", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Display components vertically
        components = VGroup(
            MathTex(r"\text{Scalar} = 5", font_size=24, color=YELLOW),
            MathTex(r"\text{Vector} = 3e_1 + 2e_2 + e_3", font_size=24, color=BLUE),
            MathTex(r"\text{Bivector} = 4e_{12} + 2e_{23}", font_size=24, color=GREEN),
            MathTex(r"\text{Trivector} = 7e_{123}", font_size=24, color=RED),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        components.shift(UP * 0.5)

        for comp in components:
            self.play(Write(comp))
            self.wait(0.5)

        # Full multivector equation
        full = MathTex(
            r"M = \underbrace{5}_{\text{scalar}} + \underbrace{3e_1 + 2e_2}_{\text{vector}} + \underbrace{4e_{12}}_{\text{bivector}} + \underbrace{7e_{123}}_{\text{trivector}}",
            font_size=28
        )
        full.to_edge(DOWN)
        self.play(Write(full))

        note = Text("A multivector contains components of all grades", font_size=18, color=YELLOW).next_to(full, UP, buff=0.3)
        self.play(Write(note))
        self.wait(4)


if __name__ == "__main__":
    # Render commands:
    # manim -qh ch3_ga_visualization.py Scene1_GeometricProduct
    # manim -qh ch3_ga_visualization.py Scene2_BivectorOrientation
    # manim -qh ch3_ga_visualization.py Scene3_TrivectorVolume
    # manim -qh ch3_ga_visualization.py Scene4_MultivectorComponents
    pass

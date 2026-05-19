from manim import *
import numpy as np


class Scene1_WordsOnSphere(Scene):
    """Words as points on a spherical planet"""
    def construct(self):
        title = Text("Words on a Spherical Planet", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Create a circle representing the sphere (2D view)
        sphere = Circle(radius=2.5, color=BLUE, fill_opacity=0.2)
        sphere.shift(DOWN * 0.3)

        self.play(Create(sphere))

        # Add words as points around the circle
        words = {
            "king": 45 * DEGREES,
            "queen": 15 * DEGREES,
            "man": 75 * DEGREES,
            "woman": 105 * DEGREES,
        }

        word_dots = VGroup()
        word_labels = VGroup()

        for word, angle in words.items():
            pos = sphere.point_at_angle(angle)
            dot = Dot(pos, color=YELLOW, radius=0.1)
            label = Text(word, font_size=18).next_to(dot, UP if angle > 45 * DEGREES else DOWN, buff=0.2)

            word_dots.add(dot)
            word_labels.add(label)

        self.play(FadeIn(word_dots), Write(word_labels))

        # Show angle between king and queen
        king_angle = words["king"]
        queen_angle = words["queen"]
        arc = Arc(radius=1.5, start_angle=queen_angle, angle=king_angle - queen_angle, color=RED, arc_center=sphere.get_center())
        angle_label = Text("angle = similarity", font_size=14, color=RED).move_to(sphere.get_center() + UP * 1)

        self.play(Create(arc), Write(angle_label))

        note = Text("Each word is a point on the sphere's surface", font_size=18, color=YELLOW).to_edge(DOWN)
        self.play(Write(note))
        self.wait(4)


class Scene2_GreatCircleRoute(Scene):
    """Show SLERP as great circle navigation"""
    def construct(self):
        title = Text("Great Circle Navigation (SLERP)", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 2D representation of sphere surface
        circle = Circle(radius=3, color=BLUE, fill_opacity=0.1)
        self.play(Create(circle))

        # Points
        cat_point = Dot(circle.point_at_angle(PI/4), color=ORANGE, radius=0.12)
        dog_point = Dot(circle.point_at_angle(-PI/4), color=ORANGE, radius=0.12)

        cat_label = Text("cat", font_size=20).next_to(cat_point, UR, buff=0.2)
        dog_label = Text("dog", font_size=20).next_to(dog_point, DR, buff=0.2)

        self.play(Create(cat_point), Create(dog_point), Write(cat_label), Write(dog_label))

        # Great circle arc
        arc = Arc(radius=3, start_angle=-PI/4, angle=PI/2, color=GREEN)
        self.play(Create(arc))

        # Show halfway point
        halfway = Dot(circle.point_at_angle(0), color=YELLOW, radius=0.1)
        halfway_label = Text("halfway?", font_size=16, color=YELLOW).next_to(halfway, RIGHT, buff=0.3)

        self.play(Create(halfway), Write(halfway_label))

        # Contrast with straight line (cutting through)
        straight_line = DashedLine(cat_point.get_center(), dog_point.get_center(), color=RED, dash_length=0.1)
        straight_label = Text("straight line (wrong)", font_size=14, color=RED).move_to(straight_line.get_center() + LEFT * 0.8)

        self.play(Create(straight_line), Write(straight_label))

        # SLERP formula
        formula = MathTex(r"\text{SLERP}(a, b, t) = \frac{\sin((1-t)\omega)}{\sin(\omega)} a + \frac{\sin(t\omega)}{\sin(\omega)} b", font_size=24)
        formula.to_edge(DOWN)

        self.play(Write(formula))

        note = Text("Follow the surface, not the shortcut", font_size=18, color=YELLOW).next_to(formula, UP)
        self.play(Write(note))
        self.wait(4)


class Scene3_DifferentJourneys(Scene):
    """Show different transformation types as different directions"""
    def construct(self):
        title = Text("Different Kinds of Journeys", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Central starting point
        center = Dot(ORIGIN, color=WHITE, radius=0.15)
        center_label = Text("king", font_size=22).next_to(center, DOWN, buff=0.3)
        self.play(Create(center), Write(center_label))

        # Different transformations as arrows in different directions
        transformations = [
            ("queen", UP * 2.5, "gender", PURPLE),
            ("kings", RIGHT * 2.5, "plural", GREEN),
            ("crown", UP * 1.5 + RIGHT * 1.5, "related", BLUE),
            ("servant", DOWN * 2, "opposite", RED),
        ]

        arrows = VGroup()
        labels = VGroup()
        type_labels = VGroup()

        for word, direction, transform_type, color in transformations:
            arrow = Arrow(center.get_center(), center.get_center() + direction, buff=0.2, color=color)
            word_text = Text(word, font_size=18, color=color).next_to(center.get_center() + direction, direction, buff=0.2)
            type_text = Text(f"({transform_type})", font_size=12, color=color).next_to(word_text, direction, buff=0.1)

            arrows.add(arrow)
            labels.add(word_text)
            type_labels.add(type_text)

        # Animate each arrow separately
        for i in range(len(arrows)):
            self.play(
                GrowArrow(arrows[i]),
                Write(labels[i]),
                Write(type_labels[i]),
                run_time=0.8
            )
            self.wait(0.3)

        note = Text("Each transformation is a journey in a different direction", font_size=18, color=YELLOW).to_edge(DOWN)
        self.play(Write(note))
        self.wait(4)


class Scene4_CompositionProblem(Scene):
    """Show why simple addition fails for irregular forms"""
    def construct(self):
        title = Text("When Simple Directions Fail", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Regular case: walk -> walks
        regular = Text("Regular:", font_size=20, color=GREEN).shift(UP * 1.5 + LEFT * 4)
        regular_example = Text("walk  + plural  →  walks  ✓", font_size=18).next_to(regular, RIGHT, buff=0.5)

        self.play(Write(regular), Write(regular_example))

        # Irregular case: child -> children
        irregular = Text("Irregular:", font_size=20, color=RED).shift(UP * 0.5 + LEFT * 4)
        irregular_fail = Text("child  + plural  →  childs  ✗", font_size=18, color=RED).next_to(irregular, RIGHT, buff=0.5)
        irregular_correct = Text("(should be: children)", font_size=16, color=YELLOW).next_to(irregular_fail, RIGHT, buff=0.3)

        self.play(Write(irregular), Write(irregular_fail), Write(irregular_correct))

        # Non-commuting example
        noncommute = Text("Non-commuting:", font_size=20, color=ORANGE).shift(DOWN * 0.8 + LEFT * 3)

        path1 = Text("happy → unhappy → unhappiness", font_size=16).shift(DOWN * 1.5 + LEFT * 2)
        path2 = Text("happy → happiness → unhappiness", font_size=16).shift(DOWN * 2.2 + LEFT * 2)

        self.play(Write(noncommute))
        self.play(Write(path1))
        self.play(Write(path2))

        # The insight
        insight = Text(
            "The journey matters. Not just start and end.",
            font_size=20,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(insight))
        self.wait(4)


class Scene5_GPSvsCompass(Scene):
    """GPS (coordinates only) vs Compass + Map (coordinates + orientation)"""
    def construct(self):
        title = Text("GPS vs Compass + Map", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Left side: SLERP / GPS
        slerp_title = Text("SLERP (GPS)", font_size=24, color=BLUE).shift(LEFT * 4 + UP * 2)
        slerp_desc = VGroup(
            Text("You are at:", font_size=16),
            Text("40.7N, 74.0W", font_size=20, color=YELLOW),
            Text("That's it.", font_size=16),
        ).arrange(DOWN, buff=0.5).next_to(slerp_title, DOWN, buff=0.4)

        self.play(Write(slerp_title))
        self.play(Write(slerp_desc))

        # Right side: GA / Compass
        ga_title = Text("Geometric Algebra", font_size=24, color=GREEN).shift(RIGHT * 4 + UP * 2)
        ga_desc = VGroup(
            Text("You are at:", font_size=16),
            Text("40.7N, 74.0W", font_size=20, color=YELLOW),
            Text("Facing: 53 west of north", font_size=16),
            Text("Plane of travel: known", font_size=16),
            Text("Can continue to any destination", font_size=16),
        ).arrange(DOWN, buff=0.5).next_to(ga_title, DOWN, buff=0.4)

        self.play(Write(ga_title))
        self.play(Write(ga_desc))

        # Divider
        divider = Line(UP * 3, DOWN * 2, color=GRAY)
        self.play(Create(divider))

        # Bottom comparison
        comparison = Text(
            "Coordinates alone vs. Coordinates + Orientation + Plane",
            font_size=20,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(comparison))
        self.wait(4)


if __name__ == "__main__":
    # Render commands:
    # manim -qh ch2_traveling_world.py Scene1_WordsOnSphere
    # manim -qh ch2_traveling_world.py Scene2_GreatCircleRoute
    # manim -qh ch2_traveling_world.py Scene3_DifferentJourneys
    # manim -qh ch2_traveling_world.py Scene4_CompositionProblem
    # manim -qh ch2_traveling_world.py Scene5_GPSvsCompass
    pass

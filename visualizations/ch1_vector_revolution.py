from manim import *


class Scene1_OneHotEncoding(Scene):
    """Show one-hot encoding as a sparse vector"""
    def construct(self):
        title = Text("One-Hot Encoding", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Vocabulary
        vocab = ["king", "queen", "man", "woman", "apple"]
        words = VGroup(*[Text(w, font_size=24) for w in vocab]).arrange(DOWN, buff=0.4).shift(LEFT * 4)

        # One-hot vectors
        vectors = VGroup()
        for i in range(len(vocab)):
            vec = VGroup()
            for j in range(5):
                if j == i:
                    cell = Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.8)
                    label = Text("1", font_size=18, color=WHITE)
                else:
                    cell = Square(side_length=0.5, fill_color=GRAY, fill_opacity=0.2)
                    label = Text("0", font_size=18, color=GRAY)
                label.move_to(cell.get_center())
                vec.add(VGroup(cell, label))
            vec.arrange(RIGHT, buff=0.05)
            vectors.add(vec)

        vectors.arrange(DOWN, buff=0.3).shift(RIGHT * 1.5)

        self.play(Write(words))
        self.play(Create(vectors))
        self.wait(2)

        note = Text("Extremely sparse • No notion of similarity", font_size=20, color=YELLOW).to_edge(DOWN)
        self.play(Write(note))
        self.wait(3)


class Scene2_2DEmbeddingSpace(Scene):
    """Show 2D toy embedding space with royalty and gender axes"""
    def construct(self):
        title = Text("2D Embedding Space", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Axes
        axes = Axes(
            x_range=[-0.2, 1.2],
            y_range=[-1.2, 1.2],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": True}
        )
        labels = axes.get_axis_labels(x_label="royalty", y_label="gender")

        self.play(Create(axes), Write(labels))

        # Points
        points = {
            "king":   Dot(axes.coords_to_point(0.9, 0.8), color=BLUE, radius=0.12),
            "queen":  Dot(axes.coords_to_point(0.9, -0.8), color=PURPLE, radius=0.12),
            "man":    Dot(axes.coords_to_point(0.1, 0.7), color=GREEN, radius=0.12),
            "woman":  Dot(axes.coords_to_point(0.1, -0.7), color=ORANGE, radius=0.12),
        }

        labels = {
            "king":   Text("king", font_size=20).next_to(points["king"], RIGHT),
            "queen":  Text("queen", font_size=20).next_to(points["queen"], RIGHT),
            "man":    Text("man", font_size=20).next_to(points["man"], RIGHT),
            "woman":  Text("woman", font_size=20).next_to(points["woman"], RIGHT),
        }

        for name in points:
            self.play(Create(points[name]), Write(labels[name]), run_time=0.6)

        self.wait(2)

        # Show vector difference
        arrow1 = Arrow(points["king"].get_center(), points["queen"].get_center(), buff=0.2, color=RED)
        arrow2 = Arrow(points["man"].get_center(), points["woman"].get_center(), buff=0.2, color=RED)

        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(2)

        eq = MathTex(r"\text{king} - \text{man} + \text{woman} \approx \text{queen}", font_size=28).to_edge(DOWN)
        self.play(Write(eq))
        self.wait(4)


class Scene3_VectorArithmetic(Scene):
    """Animate the vector arithmetic"""
    def construct(self):
        title = Text("Geometric Transformation", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Simple number line style animation
        equation = MathTex(
            r"\vec{k} - \vec{m} + \vec{w} \approx \vec{q}",
            font_size=48
        )
        self.play(Write(equation))
        self.wait(2)

        explanation = Text(
            "The gender direction is captured as a vector you can add or subtract",
            font_size=22
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(4)


if __name__ == "__main__":
    # Render command example:
    # manim -qh ch1_vector_revolution.py Scene1_OneHotEncoding
    pass
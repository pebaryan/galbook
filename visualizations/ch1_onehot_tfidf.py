from manim import *


class OneHotVsTFIDF(Scene):
    """Compare one-hot encoding vs TF-IDF representation"""
    def construct(self):
        title = Text("Pre-Vector Era Representations", font_size=32).to_edge(UP)
        self.play(Write(title))

        # === ONE-HOT SECTION ===
        onehot_title = Text("One-Hot Encoding", font_size=24, color=BLUE).shift(UP * 2 + LEFT * 3.5)
        self.play(Write(onehot_title))

        vocab = ["king", "queen", "man", "woman", "apple"]
        words = VGroup(*[Text(w, font_size=20) for w in vocab]).arrange(DOWN, buff=0.35).shift(LEFT * 5.5)

        vectors = VGroup()
        for i in range(len(vocab)):
            vec = VGroup()
            for j in range(5):
                if j == i:
                    cell = Square(side_length=0.45, fill_color=BLUE, fill_opacity=0.85)
                    label = Text("1", font_size=16, color=WHITE)
                else:
                    cell = Square(side_length=0.45, fill_color=GRAY, fill_opacity=0.15)
                    label = Text("0", font_size=16, color=GRAY)
                label.move_to(cell.get_center())
                vec.add(VGroup(cell, label))
            vec.arrange(RIGHT, buff=0.03)
            vectors.add(vec)

        vectors.arrange(DOWN, buff=0.25).shift(LEFT * 2.2)

        self.play(Write(words), Create(vectors), run_time=2)
        self.wait(1.5)

        note1 = Text("Sparse • No similarity", font_size=18, color=YELLOW).next_to(vectors, DOWN, buff=0.3)
        self.play(Write(note1))
        self.wait(2)

        # === TF-IDF SECTION ===
        tfidf_title = Text("TF-IDF", font_size=24, color=GREEN).shift(UP * 2 + RIGHT * 3.5)
        self.play(Write(tfidf_title))

        tfidf_words = VGroup(*[Text(w, font_size=20) for w in vocab]).arrange(DOWN, buff=0.35).shift(RIGHT * 1.5)

        # Simulated TF-IDF weights (visual bars)
        tfidf_values = [0.82, 0.75, 0.41, 0.38, 0.29]  # example weights
        bars = VGroup()
        for i, val in enumerate(tfidf_values):
            bar = Rectangle(
                width=val * 2.5,
                height=0.35,
                fill_color=GREEN,
                fill_opacity=0.8,
                stroke_color=GREEN
            )
            bar.next_to(tfidf_words[i], RIGHT, buff=0.2)
            bars.add(bar)

        self.play(Write(tfidf_words), Create(bars), run_time=2)
        self.wait(1.5)

        note2 = Text("Weighted importance • Still no geometry", font_size=18, color=YELLOW).next_to(bars, DOWN, buff=0.3)
        self.play(Write(note2))
        self.wait(3)

        # Conclusion
        conclusion = Text(
            "Both treat words as independent symbols — no relationships captured",
            font_size=20, color=RED
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(4)
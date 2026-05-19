from manim import *
import numpy as np


class Scene1_ZipfsLaw(Scene):
    """Zipf's law: word frequency vs rank showing the long tail"""
    def construct(self):
        title = Text("Zipf's Law", font_size=36).to_edge(UP)
        subtitle = Text("A few words dominate, most are rare", font_size=20, color=GRAY).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))

        # Axes
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 1.2, 0.2],
            x_length=9,
            y_length=5,
            axis_config={"include_tip": True}
        ).shift(DOWN * 0.3)

        x_label = Text("word rank", font_size=18).next_to(axes.x_axis, DOWN)
        y_label = Text("frequency", font_size=18).next_to(axes.y_axis, LEFT).rotate(90 * DEGREES)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Zipf curve: y = 1/x (normalized)
        zipf_curve = axes.plot(lambda x: 1/(x+1) if x > 0 else 1, x_range=[0.1, 100], color=BLUE)

        self.play(Create(zipf_curve), run_time=2)

        # Annotations
        top_words = Text('"the", "and", "to"...', font_size=16, color=GREEN).move_to(axes.coords_to_point(10, 0.85))
        tail_words = Text("millions of rare words...", font_size=16, color=RED).move_to(axes.coords_to_point(70, 0.15))

        self.play(Write(top_words))
        self.play(Write(tail_words))

        # Coverage note - position above the axis label to avoid overlap
        coverage = Text("50K words cover 95% of tokens, but miss the long tail", font_size=18, color=YELLOW)
        coverage.next_to(axes, DOWN, buff=0.8)
        self.play(Write(coverage))
        self.wait(4)


class Scene2_OOVProblem(Scene):
    """Out-of-vocabulary problem illustration"""
    def construct(self):
        title = Text("The OOV Problem", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Vocabulary box
        vocab_box = Rectangle(width=4, height=4, color=BLUE)
        vocab_label = Text("Vocabulary\n(50,000 words)", font_size=20).move_to(vocab_box.get_center())
        vocab_group = VGroup(vocab_box, vocab_label).shift(LEFT * 3)

        self.play(Create(vocab_box), Write(vocab_label))

        # Some known words inside
        known_words = ["the", "and", "king", "walk"]
        known_group = VGroup(*[Text(w, font_size=16, color=GREEN) for w in known_words])
        known_group.arrange(DOWN, buff=0.3).move_to(vocab_box.get_center() + UP * 0.5)
        self.play(FadeIn(known_group))

        # Unknown word outside
        unknown = Text('"cryptocurrency"', font_size=28, color=RED).shift(RIGHT * 3)
        question = Text("???", font_size=36, color=RED).next_to(unknown, DOWN)

        self.play(Write(unknown))
        self.play(Write(question))

        # Arrow showing exclusion
        cross = Cross(unknown, stroke_color=RED, stroke_width=3)
        self.play(Create(cross))

        note = Text("Unknown token → no vector → no meaning", font_size=20, color=YELLOW).to_edge(DOWN)
        self.play(Write(note))
        self.wait(4)


class Scene3_SubwordTokenization(Scene):
    """Show how words are broken into subword pieces"""
    def construct(self):
        title = Text("Subword Tokenization", font_size=36).to_edge(UP)
        self.play(Write(title))

        examples = [
            ('"cryptocurrency"', ["crypto", "##currency"]),
            ('"unhappiness"', ["un", "##happy", "##ness"]),
            ('"ChatGPT"', ["Chat", "##G", "##PT"]),
        ]

        y_pos = 2
        for word, pieces in examples:
            # Original word
            word_text = Text(word, font_size=24).shift(UP * y_pos + LEFT * 4)
            self.play(Write(word_text))

            # Arrow
            arrow = Arrow(word_text.get_right(), word_text.get_right() + RIGHT * 1.5, buff=0.2)
            self.play(GrowArrow(arrow))

            # Token pieces
            tokens = VGroup(*[Text(t, font_size=20, color=BLUE) for t in pieces])
            tokens.arrange(RIGHT, buff=0.3).shift(UP * y_pos + RIGHT * 2)

            # Box around tokens
            token_box = SurroundingRectangle(tokens, buff=0.2, color=BLUE)

            self.play(Write(tokens), Create(token_box))

            y_pos -= 1.5

        note = Text("Unknown words become compositions of known pieces", font_size=20, color=YELLOW).to_edge(DOWN)
        self.play(Write(note))
        self.wait(4)


class Scene4_Compositionality(Scene):
    """Show how subword vectors add up to form word vectors"""
    def construct(self):
        title = Text("Compositionality via Addition", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Show vector addition
        # crypto vector
        crypto_rect = Rectangle(width=2, height=0.8, fill_color=BLUE, fill_opacity=0.3, color=BLUE)
        crypto_label = Text("crypto", font_size=20).move_to(crypto_rect.get_center())
        crypto = VGroup(crypto_rect, crypto_label).shift(LEFT * 3 + UP * 1)

        # currency vector
        curr_rect = Rectangle(width=2, height=0.8, fill_color=GREEN, fill_opacity=0.3, color=GREEN)
        curr_label = Text("##currency", font_size=20).move_to(curr_rect.get_center())
        curr = VGroup(curr_rect, curr_label).shift(LEFT * 3 + DOWN * 1)

        self.play(Create(crypto), Create(curr))

        # Plus signs
        plus1 = Text("+", font_size=36).next_to(crypto, RIGHT, buff=0.5)
        plus2 = Text("+", font_size=36).next_to(curr, RIGHT, buff=0.5)
        self.play(Write(plus1), Write(plus2))

        # Equals
        equals = Text("=", font_size=36).shift(LEFT * 0.5)
        self.play(Write(equals))

        # Result
        result_rect = Rectangle(width=3, height=1.2, fill_color=PURPLE, fill_opacity=0.5, color=PURPLE)
        result_label = Text('"cryptocurrency"', font_size=22, color=WHITE).move_to(result_rect.get_center())
        result = VGroup(result_rect, result_label).shift(RIGHT * 2.5)

        self.play(Create(result))

        # Math notation
        math = MathTex(r"\vec{v}_{\text{crypto}} + \vec{v}_{\text{currency}} = \vec{v}_{\text{cryptocurrency}}", font_size=28).to_edge(DOWN)
        self.play(Write(math))

        insight = Text(
            "Words are no longer points. They are expressions.",
            font_size=20,
            color=YELLOW
        ).next_to(math, UP)
        self.play(Write(insight))

        self.wait(4)


if __name__ == "__main__":
    # Render commands:
    # manim -qh ch1_subword_tokenization.py Scene1_ZipfsLaw
    # manim -qh ch1_subword_tokenization.py Scene2_OOVProblem
    # manim -qh ch1_subword_tokenization.py Scene3_SubwordTokenization
    # manim -qh ch1_subword_tokenization.py Scene4_Compositionality
    pass

from manim import *


class ElizaRuleBased(Scene):
    """Visual explanation of ELIZA and rule-based chatbots"""
    def construct(self):
        title = Text("Rule-Based & Template Systems", font_size=32).to_edge(UP)
        self.play(Write(title))

        # ELIZA section
        eliza = Text("ELIZA (1966)", font_size=24, color=BLUE).shift(UP * 2 + LEFT * 4)
        self.play(Write(eliza))

        # Input
        input_box = RoundedRectangle(height=0.8, width=4, color=WHITE)
        input_text = Text('"I feel sad"', font_size=20).move_to(input_box.get_center())
        input_group = VGroup(input_box, input_text).shift(LEFT * 4 + UP * 0.5)

        self.play(Create(input_box), Write(input_text))

        # Pattern matching
        pattern = Text('Pattern: "I feel X"', font_size=18, color=YELLOW).next_to(input_group, DOWN, buff=0.4)
        self.play(Write(pattern))

        # Rule arrow
        arrow = Arrow(pattern.get_bottom(), pattern.get_bottom() + DOWN * 0.8, buff=0.1)
        self.play(GrowArrow(arrow))

        # Template response
        template = Text('Template: "Why do you feel X?"', font_size=18, color=GREEN).next_to(arrow, DOWN)
        self.play(Write(template))

        # Output
        output_box = RoundedRectangle(height=0.8, width=4.5, color=GREEN)
        output_text = Text('"Why do you feel sad?"', font_size=20).move_to(output_box.get_center())
        output_group = VGroup(output_box, output_text).shift(LEFT * 4 + DOWN * 1.8)

        self.play(Create(output_box), Write(output_text))
        self.wait(2)

        # ALICE / AIML section
        alice = Text("ALICE (AIML)", font_size=24, color=PURPLE).shift(UP * 2 + RIGHT * 3.5)
        self.play(Write(alice))

        # AIML structure
        aiml_box = RoundedRectangle(height=3.2, width=5.5, color=PURPLE, fill_opacity=0.1).shift(RIGHT * 3.5)
        aiml_title = Text("AIML Template", font_size=18, color=PURPLE).move_to(aiml_box.get_top() + DOWN * 0.3)

        category = Text(
            '<category>\n  <pattern>I FEEL *</pattern>\n  <template>\n    Why do you feel <star/>?\n  </template>\n</category>',
            font_size=14, font="Monospace", line_spacing=1.1
        ).move_to(aiml_box.get_center())

        self.play(Create(aiml_box), Write(aiml_title), Write(category))
        self.wait(3)

        # Key limitation
        limitation = Text(
            "No understanding — only clever string replacement",
            font_size=20, color=RED
        ).to_edge(DOWN)
        self.play(Write(limitation))
        self.wait(4)
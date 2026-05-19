from manim import *


class ElizaRuleBased(Scene):
    """Visual explanation of ELIZA and rule-based chatbots"""
    def construct(self):
        title = Text("Rule-Based & Template Systems", font_size=32).to_edge(UP)
        self.play(Write(title))

        # ═══════════════════════════════════════════════════════════
        # LEFT: ELIZA (1966)
        # ═══════════════════════════════════════════════════════════
        eliza = Text("ELIZA (1966)", font_size=22, color=BLUE).shift(UP * 2.3 + LEFT * 4)
        self.play(Write(eliza))

        # Input
        input_box = RoundedRectangle(height=0.7, width=3.8, color=WHITE, stroke_width=2)
        input_text = Text('"I feel sad"', font_size=18).move_to(input_box.get_center())
        input_group = VGroup(input_box, input_text).shift(LEFT * 4 + UP * 0.8)
        self.play(Create(input_box), Write(input_text))

        # Pattern matching
        pattern_box = RoundedRectangle(height=0.55, width=3.2, color=YELLOW, fill_opacity=0.15)
        pattern_text = Text('Pattern: "I feel X"', font_size=15, color=YELLOW).move_to(pattern_box.get_center())
        pattern_group = VGroup(pattern_box, pattern_text).next_to(input_group, DOWN, buff=0.3)
        self.play(Create(pattern_box), Write(pattern_text))

        # Arrow
        arrow = Arrow(pattern_group.get_bottom(), pattern_group.get_bottom() + DOWN * 0.5, buff=0.1, color=WHITE)
        self.play(GrowArrow(arrow))

        # Template
        template_box = RoundedRectangle(height=0.55, width=3.6, color=GREEN, fill_opacity=0.15)
        template_text = Text('Template: "Why feel X?"', font_size=14, color=GREEN).move_to(template_box.get_center())
        template_group = VGroup(template_box, template_text).next_to(arrow, DOWN, buff=0.15)
        self.play(Create(template_box), Write(template_text))

        # Output
        output_box = RoundedRectangle(height=0.7, width=4, color=GREEN, stroke_width=2)
        output_text = Text('"Why do you feel sad?"', font_size=17).move_to(output_box.get_center())
        output_group = VGroup(output_box, output_text).next_to(template_group, DOWN, buff=0.3)
        self.play(Create(output_box), Write(output_text))
        self.wait(1.5)

        # ═══════════════════════════════════════════════════════════
        # RIGHT: ALICE / AIML (formalized version)
        # ═══════════════════════════════════════════════════════════
        alice = Text("ALICE / AIML", font_size=22, color=PURPLE).shift(UP * 2.3 + RIGHT * 3.5)
        self.play(Write(alice))

        # Same flow but formalized
        # Input
        r_input_box = RoundedRectangle(height=0.7, width=3.8, color=WHITE, stroke_width=2)
        r_input_text = Text('"I feel sad"', font_size=18).move_to(r_input_box.get_center())
        r_input_group = VGroup(r_input_box, r_input_text).shift(RIGHT * 3.5 + UP * 0.8)
        self.play(Create(r_input_box), Write(r_input_text))

        # Pattern match (formal)
        r_pattern_box = RoundedRectangle(height=0.55, width=3.2, color=YELLOW, fill_opacity=0.15)
        r_pattern_text = Text('Match: I FEEL *', font_size=15, color=YELLOW).move_to(r_pattern_box.get_center())
        r_pattern_group = VGroup(r_pattern_box, r_pattern_text).next_to(r_input_group, DOWN, buff=0.3)
        self.play(Create(r_pattern_box), Write(r_pattern_text))

        # Arrow
        r_arrow = Arrow(r_pattern_group.get_bottom(), r_pattern_group.get_bottom() + DOWN * 0.5, buff=0.1, color=WHITE)
        self.play(GrowArrow(r_arrow))

        # Template (formal)
        r_template_box = RoundedRectangle(height=0.55, width=3.6, color=GREEN, fill_opacity=0.15)
        r_template_text = Text('Response: Why feel <star>?', font_size=14, color=GREEN).move_to(r_template_box.get_center())
        r_template_group = VGroup(r_template_box, r_template_text).next_to(r_arrow, DOWN, buff=0.15)
        self.play(Create(r_template_box), Write(r_template_text))

        # Output
        r_output_box = RoundedRectangle(height=0.7, width=4, color=GREEN, stroke_width=2)
        r_output_text = Text('"Why do you feel sad?"', font_size=17).move_to(r_output_box.get_center())
        r_output_group = VGroup(r_output_box, r_output_text).next_to(r_template_group, DOWN, buff=0.3)
        self.play(Create(r_output_box), Write(r_output_text))
        self.wait(1.5)

        # AIML XML box (below the flow, showing the code)
        aiml_box = RoundedRectangle(height=2.2, width=5, color=PURPLE, fill_opacity=0.08, stroke_width=1.5)
        aiml_box.shift(RIGHT * 3.5 + DOWN * 2.2)

        aiml_code = Text(
            '<category>\n'
            '  <pattern>I FEEL *</pattern>\n'
            '  <template>Why do you feel <star/>?</template>\n'
            '</category>',
            font_size=12,
            font="Monospace",
            line_spacing=1.05,
            color=WHITE
        ).move_to(aiml_box.get_center())

        aiml_label = Text("(XML representation)", font_size=11, color=GRAY).next_to(aiml_box, DOWN, buff=0.1)

        self.play(Create(aiml_box), Write(aiml_code), Write(aiml_label))
        self.wait(2)

        # Key limitation at bottom
        limitation = Text(
            "Both use pattern matching — no real understanding of meaning",
            font_size=20, color=RED
        ).to_edge(DOWN)
        self.play(Write(limitation))
        self.wait(4)
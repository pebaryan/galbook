"""
Chapter 5: The Attention Mechanism - Visualizations
"""

from manim import *

class Scene1_QueryKeyValue(Scene):
    """Scene 1: Each word produces Q, K, V vectors"""
    def construct(self):
        # Title
        title = Text("Every Word Becomes Three Vectors", font_size=36)
        title.to_edge(UP)
        self.add(title)
        
        # Three words
        words = VGroup(
            Text("The", font_size=32, color=WHITE),
            Text("cat", font_size=32, color=WHITE),
            Text("sat", font_size=32, color=WHITE)
        )
        words.arrange(RIGHT, buff=2)
        words.shift(UP * 1.5)
        self.add(words)
        
        # Colors for Q, K, V
        q_color = BLUE
        k_color = GREEN
        v_color = RED
        
        # Arrows and labels for each word
        for i, word in enumerate(words):
            # Query arrow
            q_arrow = Arrow(
                word.get_bottom(),
                word.get_bottom() + DOWN * 1.2 + LEFT * 0.8,
                color=q_color,
                buff=0.1
            )
            q_label = Text("Q", font_size=24, color=q_color)
            q_label.next_to(q_arrow.get_end(), LEFT, buff=0.2)
            
            # Key arrow
            k_arrow = Arrow(
                word.get_bottom(),
                word.get_bottom() + DOWN * 1.2,
                color=k_color,
                buff=0.1
            )
            k_label = Text("K", font_size=24, color=k_color)
            k_label.next_to(k_arrow.get_end(), DOWN, buff=0.2)
            
            # Value arrow
            v_arrow = Arrow(
                word.get_bottom(),
                word.get_bottom() + DOWN * 1.2 + RIGHT * 0.8,
                color=v_color,
                buff=0.1
            )
            v_label = Text("V", font_size=24, color=v_color)
            v_label.next_to(v_arrow.get_end(), RIGHT, buff=0.2)
            
            self.add(q_arrow, q_label, k_arrow, k_label, v_arrow, v_label)
        
        # Equation at bottom
        equation = MathTex(
            r"\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V",
            font_size=28
        )
        equation.to_edge(DOWN, buff=0.5)
        self.add(equation)
        
        # Legend
        legend = VGroup(
            Text("Query: What am I looking for?", font_size=20, color=q_color),
            Text("Key: What do I have to offer?", font_size=20, color=k_color),
            Text("Value: What information do I carry?", font_size=20, color=v_color)
        )
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_corner(DL, buff=0.5)
        self.add(legend)
        
        self.wait(0.5)


class Scene2_AttentionScores(Scene):
    """Scene 2: Computing attention scores between words"""
    def construct(self):
        # Title
        title = Text("Computing Attention Scores", font_size=36)
        title.to_edge(UP)
        self.add(title)
        
        # Words arranged vertically (processing "sat")
        words = VGroup(
            Text("The", font_size=28),
            Text("cat", font_size=28),
            Text("sat", font_size=28, color=YELLOW)
        )
        words.arrange(DOWN, buff=1)
        words.shift(LEFT * 3)
        self.add(words)
        
        # "sat" is the query - draw attention to it
        sat_highlight = SurroundingRectangle(words[2], color=YELLOW, buff=0.2)
        self.add(sat_highlight)
        
        # Attention scores visualization
        scores_title = Text("Attention Scores for 'sat'", font_size=24)
        scores_title.next_to(words, RIGHT, buff=2)
        scores_title.align_to(words, UP)
        self.add(scores_title)
        
        # Score bars
        scores_data = [
            ("The", 0.1, GRAY),
            ("cat", 0.6, GREEN),
            ("sat", 0.3, BLUE)
        ]
        
        score_bars = VGroup()
        for i, (word, score, color) in enumerate(scores_data):
            # Word label
            word_label = Text(word, font_size=20)
            word_label.shift(RIGHT * 1.5 + UP * (1 - i * 0.8))
            
            # Bar
            bar = Rectangle(
                height=0.3,
                width=score * 4,
                fill_color=color,
                fill_opacity=0.8,
                stroke_color=color
            )
            bar.next_to(word_label, RIGHT, buff=0.3)
            bar.align_to(word_label, DOWN)
            
            # Score label
            score_label = Text(f"{score:.1f}", font_size=18)
            score_label.next_to(bar, RIGHT, buff=0.2)
            
            score_bars.add(word_label, bar, score_label)
        
        self.add(score_bars)
        
        # Explanation
        explanation = VGroup(
            Text("cat gets high attention (subject)", font_size=18, color=GREEN),
            Text("sat attends to itself", font_size=18, color=BLUE),
            Text("The gets low attention (article)", font_size=18, color=GRAY)
        )
        explanation.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.next_to(score_bars, DOWN, buff=0.5)
        explanation.shift(LEFT * 0.5)
        self.add(explanation)
        
        # Connection arrows showing the flow
        for i, score in enumerate([0.1, 0.6, 0.3]):
            if score > 0.2:  # Only draw for significant scores
                arrow = CurvedArrow(
                    words[2].get_right(),
                    words[i].get_right(),
                    color=YELLOW,
                    angle=-0.3 if i < 2 else 0,
                    stroke_width=2
                )
                self.add(arrow)
        
        self.wait(0.5)


class Scene3_MultiHeadAttention(Scene):
    """Scene 3: Multiple attention heads in parallel"""
    def construct(self):
        # Title
        title = Text("Multi-Head Attention: Many Perspectives", font_size=36)
        title.to_edge(UP)
        self.add(title)
        
        # Input words
        input_words = VGroup(
            Text("The", font_size=24),
            Text("cat", font_size=24),
            Text("sat", font_size=24)
        )
        input_words.arrange(RIGHT, buff=0.8)
        input_words.shift(UP * 2)
        self.add(input_words)
        
        # Three attention heads side by side
        heads = VGroup()
        head_colors = [BLUE, GREEN, RED]
        head_names = ["Syntax", "Semantics", "Coreference"]
        
        for i, (color, name) in enumerate(zip(head_colors, head_names)):
            # Head box
            box = Rectangle(
                width=3,
                height=2,
                fill_color=color,
                fill_opacity=0.2,
                stroke_color=color,
                stroke_width=2
            )
            box.shift(DOWN * 0.5 + LEFT * 3.5 + RIGHT * i * 3.5)
            
            # Head label
            label = Text(f"Head {i+1}: {name}", font_size=20, color=color)
            label.next_to(box, UP, buff=0.2)
            
            # Mini attention visualization inside each box
            dots = VGroup()
            for j in range(3):
                for k in range(3):
                    # Random-ish attention pattern
                    opacity = 0.3 + 0.5 * ((j + k + i) % 2)
                    dot = Dot(
                        point=box.get_center() + UP * 0.5 + RIGHT * 0.8 * (k - 1) + DOWN * 0.5 * j,
                        radius=0.08,
                        color=color,
                        fill_opacity=opacity
                    )
                    dots.add(dot)
            
            heads.add(box, label, dots)
        
        self.add(heads)
        
        # Arrows from input to heads
        for i in range(3):
            for j, color in enumerate(head_colors):
                arrow = Arrow(
                    input_words[i].get_bottom(),
                    heads[j*3].get_top() + LEFT * 0.8 + RIGHT * 0.8 * i,
                    color=color,
                    buff=0.1,
                    stroke_width=1
                )
                self.add(arrow)
        
        # Concatenation and output
        concat_arrow = Arrow(
            heads[1].get_bottom(),
            heads[1].get_bottom() + DOWN * 1,
            color=WHITE,
            buff=0.2
        )
        self.add(concat_arrow)
        
        concat_text = Text("Concatenate → Linear → Output", font_size=20)
        concat_text.next_to(concat_arrow, DOWN, buff=0.2)
        self.add(concat_text)
        
        # Explanation
        explanation = VGroup(
            Text("Each head learns different relationships:", font_size=18),
            Text("• Subject-verb agreement", font_size=16),
            Text("• Semantic similarity", font_size=16),
            Text("• Pronoun references", font_size=16)
        )
        explanation.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        explanation.to_corner(DL, buff=0.3)
        self.add(explanation)
        
        self.wait(0.5)


class Scene4_LimitationVsGA(Scene):
    """Scene 4: Standard attention (linear) vs GA attention (interaction)"""
    def construct(self):
        # Title
        title = Text("The Limitation: Linear vs Interaction", font_size=34)
        title.to_edge(UP)
        self.add(title)
        
        # Left side: Standard Attention
        std_title = Text("Standard Attention", font_size=26, color=BLUE)
        std_title.shift(UP * 2 + LEFT * 3.5)
        self.add(std_title)
        
        std_eq = MathTex(r"\text{Output} = \sum_i w_i v_i", font_size=24)
        std_eq.next_to(std_title, DOWN, buff=0.3)
        self.add(std_eq)
        
        # Visual: blending
        std_visual = VGroup()
        colors = [BLUE_A, BLUE_B, BLUE_C]
        for i, color in enumerate(colors):
            rect = Rectangle(
                width=0.8,
                height=0.8,
                fill_color=color,
                fill_opacity=0.7,
                stroke_color=BLUE
            )
            rect.shift(LEFT * 4.5 + RIGHT * i * 1 + DOWN * 0.5)
            std_visual.add(rect)
        
        # Plus signs
        plus1 = Text("+", font_size=24).next_to(std_visual[0], RIGHT, buff=0.1)
        plus2 = Text("+", font_size=24).next_to(std_visual[1], RIGHT, buff=0.1)
        std_visual.add(plus1, plus2)
        
        arrow = Arrow(
            std_visual.get_right(),
            std_visual.get_right() + RIGHT * 1,
            color=BLUE
        )
        std_visual.add(arrow)
        
        result = Rectangle(
            width=0.8,
            height=0.8,
            fill_color=BLUE_D,
            fill_opacity=0.7,
            stroke_color=BLUE
        )
        result.next_to(arrow, RIGHT, buff=0.2)
        std_visual.add(result)
        
        self.add(std_visual)
        
        std_desc = VGroup(
            Text("• Weighted sum", font_size=18),
            Text("• Blends existing vectors", font_size=18),
            Text("• No transformation", font_size=18),
            Text("✓ Captures relevance", font_size=18, color=GREEN)
        )
        std_desc.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        std_desc.next_to(std_visual, DOWN, buff=0.5)
        std_desc.shift(LEFT * 0.5)
        self.add(std_desc)
        
        # Right side: GA Attention
        ga_title = Text("Geometric Attention", font_size=26, color=GREEN)
        ga_title.shift(UP * 2 + RIGHT * 3.5)
        self.add(ga_title)
        
        ga_eq = MathTex(r"\text{Output} = Q \cdot V_{\text{agg}}", font_size=24)
        ga_eq.next_to(ga_title, DOWN, buff=0.3)
        self.add(ga_eq)
        
        # Visual: geometric product creates new structure
        ga_visual = VGroup()
        
        # Two multivectors
        mv1 = Circle(radius=0.5, color=GREEN_A, fill_opacity=0.5)
        mv1.shift(RIGHT * 2 + DOWN * 0.5)
        mv1_label = Text("Q", font_size=20, color=GREEN_A)
        mv1_label.next_to(mv1, UP, buff=0.1)
        
        mv2 = Circle(radius=0.5, color=GREEN_B, fill_opacity=0.5)
        mv2.shift(RIGHT * 3.5 + DOWN * 0.5)
        mv2_label = Text("V", font_size=20, color=GREEN_B)
        mv2_label.next_to(mv2, UP, buff=0.1)
        
        ga_visual.add(mv1, mv1_label, mv2, mv2_label)
        
        # Multiplication symbol
        mult = Text("\u00d7", font_size=28).move_to((mv1.get_center() + mv2.get_center()) / 2)
        ga_visual.add(mult)
        
        arrow2 = Arrow(
            mv2.get_right(),
            mv2.get_right() + RIGHT * 0.8,
            color=GREEN
        )
        ga_visual.add(arrow2)
        
        # Result: creates bivector (new structure!)
        result_mv = VGroup(
            Circle(radius=0.4, color=GREEN_C, fill_opacity=0.3),
            Text("+", font_size=16),
            Rectangle(width=0.6, height=0.4, color=YELLOW, fill_opacity=0.5)  # Bivector!
        )
        result_mv.arrange(RIGHT, buff=0.1)
        result_mv.next_to(arrow2, RIGHT, buff=0.2)
        ga_visual.add(result_mv)
        
        bivector_label = Text("(new bivector!)", font_size=14, color=YELLOW)
        bivector_label.next_to(result_mv[2], DOWN, buff=0.1)
        ga_visual.add(bivector_label)
        
        self.add(ga_visual)
        
        ga_desc = VGroup(
            Text("• Geometric product", font_size=18),
            Text("• Creates new structure", font_size=18),
            Text("• Bivector interactions", font_size=18),
            Text("✓ Captures transformation", font_size=18, color=GREEN)
        )
        ga_desc.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        ga_desc.next_to(ga_visual, DOWN, buff=0.5)
        ga_desc.shift(RIGHT * 0.5)
        self.add(ga_desc)
        
        # Divider
        divider = Line(
            start=UP * 2.5,
            end=DOWN * 3,
            color=GRAY,
            stroke_width=1
        )
        self.add(divider)
        
        # Bottom note
        note = Text(
            "Standard attention blends. Geometric attention transforms.",
            font_size=20,
            color=YELLOW
        )
        note.to_edge(DOWN, buff=0.3)
        self.add(note)
        
        self.wait(0.5)


# Render command:
# manim -qh ch5_attention.py Scene1_QueryKeyValue Scene2_AttentionScores Scene3_MultiHeadAttention Scene4_LimitationVsGA

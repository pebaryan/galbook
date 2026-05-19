"""
Chapter 8: Multivector Hypothesis - Visualizations
"""

from manim import *

class Scene1_RedCarComposition(Scene):
    """Scene 1: 'red car' composition via geometric product"""
    def construct(self):
        title = Text("Composition: 'red car'", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # "red" multivector
        red_box = Rectangle(width=1.5, height=2, fill_color=RED, fill_opacity=0.2, stroke_color=RED)
        red_box.shift(LEFT * 4 + UP * 0.5)
        
        red_label = Text('"red"', font_size=20, color=RED)
        red_label.next_to(red_box, UP, buff=0.2)
        
        red_grades = VGroup(
            Text("scalar:", font_size=14),
            Text("intensity", font_size=12),
            Text("vector:", font_size=14),
            Text("color", font_size=12)
        )
        red_grades.arrange(DOWN, buff=0.1)
        red_grades.move_to(red_box)
        
        self.add(red_box, red_label, red_grades)
        
        # Multiplication symbol
        mult = Text("\u00b7", font_size=36, color=YELLOW)
        mult.shift(LEFT * 2.5)
        self.add(mult)
        
        # "car" multivector
        car_box = Rectangle(width=1.5, height=2, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        car_box.shift(LEFT * 1 + UP * 0.5)
        
        car_label = Text('"car"', font_size=20, color=BLUE)
        car_label.next_to(car_box, UP, buff=0.2)
        
        car_grades = VGroup(
            Text("scalar:", font_size=14),
            Text("object", font_size=12),
            Text("vector:", font_size=14),
            Text("vehicle", font_size=12),
            Text("bivector:", font_size=14),
            Text("affordances", font_size=12)
        )
        car_grades.arrange(DOWN, buff=0.08)
        car_grades.move_to(car_box)
        
        self.add(car_box, car_label, car_grades)
        
        # Arrow to result
        arrow = Arrow(LEFT * 0.2, RIGHT * 1.5, color=YELLOW)
        self.add(arrow)
        
        # Result multivector
        result_box = Rectangle(width=2.5, height=2.2, fill_color=PURPLE, fill_opacity=0.2, stroke_color=PURPLE)
        result_box.shift(RIGHT * 3)
        
        result_label = Text("Result", font_size=18, color=PURPLE)
        result_label.next_to(result_box, UP, buff=0.2)
        
        # Show grade terms
        result_terms = VGroup(
            Text("scalar: compatibility", font_size=12),
            Text("vector: weighted vehicle", font_size=12),
            Text("bivector: 'red-car' plane", font_size=12, color=YELLOW),
            Text("  (new structure!)", font_size=11, color=YELLOW)
        )
        result_terms.arrange(DOWN, buff=0.1)
        result_terms.move_to(result_box)
        
        self.add(result_box, result_label, result_terms)
        
        # Bottom note
        note = Text(
            "Geometric product creates bivector structure that didn't exist in inputs",
            font_size=16,
            color=YELLOW
        )
        note.to_edge(DOWN, buff=0.3)
        self.add(note)
        
        self.wait(0.5)


class Scene2_MultivectorVocabulary(Scene):
    """Scene 2: King, queen, not as multivectors with different grades"""
    def construct(self):
        title = Text("Transformations in the Vocabulary", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Three multivectors side by side
        words = [
            ("king", ["scalar: 0.85", "vector: royalty", "bivector: —"], BLUE),
            ("queen", ["scalar: 0.85", "vector: royalty", "bivector: gender"], PURPLE),
            ("not", ["scalar: —", "vector: —", "bivector: negation"], RED)
        ]
        
        for i, (word, grades, color) in enumerate(words):
            x_pos = LEFT * 4 + RIGHT * i * 3
            
            # Box
            box = Rectangle(width=2, height=2.2, fill_color=color, fill_opacity=0.15, stroke_color=color)
            box.shift(x_pos)
            
            # Word label
            label = Text(f'"{word}"', font_size=20, color=color)
            label.next_to(box, UP, buff=0.2)
            
            # Grade components
            grade_texts = VGroup()
            for j, g in enumerate(grades):
                t = Text(g, font_size=12)
                if "bivector" in g and "—" not in g:
                    t.set_color(YELLOW)
                grade_texts.add(t)
            
            grade_texts.arrange(DOWN, buff=0.15)
            grade_texts.move_to(box)
            
            self.add(box, label, grade_texts)
        
        # Arrows showing transformation
        transform_arrow = CurvedArrow(
            LEFT * 3 + DOWN * 1.5,
            RIGHT * 1 + DOWN * 1.5,
            angle=-0.3,
            color=YELLOW
        )
        self.add(transform_arrow)
        
        transform_label = Text("gender rotor", font_size=14, color=YELLOW)
        transform_label.next_to(transform_arrow, DOWN, buff=0.1)
        self.add(transform_label)
        
        # Applied to others
        apply_text = Text(
            "Same rotor: actor→actress, waiter→waitress, hero→heroine",
            font_size=14,
            color=GREEN
        )
        apply_text.to_edge(DOWN, buff=0.4)
        self.add(apply_text)
        
        self.wait(0.5)


class Scene3_RotorVsOffset(Scene):
    """Scene 3: Rotor transformation vs vector offset"""
    def construct(self):
        title = Text("Analogy: Rotor vs Vector Offset", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Left: Vector offset (approximate)
        vec_label = Text("Vector Space", font_size=20, color=RED)
        vec_label.shift(UP * 2 + LEFT * 3.5)
        self.add(vec_label)
        
        # King + offset
        king_vec = Arrow(LEFT * 5, LEFT * 4, color=BLUE, buff=0)
        king_label = Text("king", font_size=16).next_to(king_vec, UP, buff=0.1)
        
        offset_vec = Arrow(LEFT * 4, LEFT * 3, color=GRAY, buff=0)
        offset_label = Text("+ offset", font_size=14, color=GRAY).next_to(offset_vec, UP, buff=0.1)
        
        result_vec = Arrow(LEFT * 3, LEFT * 2, color=PURPLE, buff=0)
        result_label = Text("≈ queen", font_size=16).next_to(result_vec, UP, buff=0.1)
        
        vec_group = VGroup(king_vec, king_label, offset_vec, offset_label, result_vec, result_label)
        vec_group.shift(UP * 0.5)
        self.add(vec_group)
        
        # Problems
        problems = VGroup(
            Text("Problems:", font_size=14, color=RED),
            Text("• Different offsets for different pairs", font_size=12),
            Text("• Statistical correlation only", font_size=12),
            Text("• Can't compose offsets", font_size=12)
        )
        problems.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        problems.next_to(vec_group, DOWN, buff=0.5)
        self.add(problems)
        
        # Right: Rotor (exact)
        rotor_label = Text("GA Space", font_size=20, color=GREEN)
        rotor_label.shift(UP * 2 + RIGHT * 3.5)
        self.add(rotor_label)
        
        # Rotor formula
        formula = MathTex(r"R · 	ext{king} · 	ilde{R} = 	ext{queen}", font_size=20)
        formula.shift(RIGHT * 3.5 + UP * 0.5)
        self.add(formula)
        
        # Same rotor for man
        formula2 = MathTex(r"R · 	ext{man} · 	ilde{R} = 	ext{woman}", font_size=20)
        formula2.next_to(formula, DOWN, buff=0.3)
        self.add(formula2)
        
        # R is the same
        r_label = Text("Same R works for all!", font_size=14, color=GREEN)
        r_label.next_to(formula2, DOWN, buff=0.3)
        self.add(r_label)
        
        # Advantages
        advantages = VGroup(
            Text("Advantages:", font_size=14, color=GREEN),
            Text("• Exact geometric relationship", font_size=12),
            Text("• Single shared transformation", font_size=12),
            Text("• Rotors compose naturally", font_size=12)
        )
        advantages.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        advantages.next_to(r_label, DOWN, buff=0.3)
        self.add(advantages)
        
        # Divider
        divider = Line(UP * 2.5, DOWN * 3, color=GRAY)
        self.add(divider)
        
        self.wait(0.5)


class Scene4_CliffordFrameAttention(Scene):
    """Scene 4: Clifford Frame Attention mechanism"""
    def construct(self):
        title = Text("Clifford Frame Attention", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Standard attention (left)
        std_label = Text("Standard Attention", font_size=18, color=RED)
        std_label.shift(UP * 2 + LEFT * 4)
        self.add(std_label)
        
        # Q, K, V as vectors
        std_qkv = VGroup(
            Text("Q · Kᵀ  →  scalar", font_size=14),
            Text("↓", font_size=14),
            Text("softmax → weights", font_size=14),
            Text("↓", font_size=14),
            Text("Σ wᵢVᵢ  →  output", font_size=14)
        )
        std_qkv.arrange(DOWN, buff=0.15)
        std_qkv.shift(LEFT * 4)
        self.add(std_qkv)
        
        std_note = Text("(linear, no new structure)", font_size=12, color=GRAY)
        std_note.next_to(std_qkv, DOWN, buff=0.2)
        self.add(std_note)
        
        # CFA (right)
        cfa_label = Text("Clifford Frame Attention", font_size=18, color=GREEN)
        cfa_label.shift(UP * 2 + RIGHT * 3)
        self.add(cfa_label)
        
        # Q, K, V as multivectors
        cfa_qkv = VGroup(
            Text("⟨Q · reverse(K)⟩₀  →  score", font_size=14),
            Text("(includes bivector contrib)", font_size=11, color=YELLOW),
            Text("↓", font_size=14),
            Text("softmax → weights", font_size=14),
            Text("↓", font_size=14),
            Text("Q · V_agg  →  output", font_size=14),
            Text("(geometric product!)", font_size=11, color=GREEN)
        )
        cfa_qkv.arrange(DOWN, buff=0.12)
        cfa_qkv.shift(RIGHT * 3)
        self.add(cfa_qkv)
        
        cfa_note = VGroup(
            Text("Creates new grade structure:", font_size=12),
            Text("vector · vector → bivector", font_size=11, color=YELLOW)
        )
        cfa_note.arrange(DOWN, buff=0.05)
        cfa_note.next_to(cfa_qkv, DOWN, buff=0.2)
        self.add(cfa_note)
        
        # Divider
        divider = Line(UP * 2.5, DOWN * 3, color=GRAY)
        self.add(divider)
        
        # Bottom: code snippet
        code = Text(
            "score = torch.matmul(Q, K * grade_signs)",
            font_size=12,
            color=WHITE
        )
        code2 = Text(
            "output = geometric_product(Q, V_agg) + V_agg",
            font_size=12,
            color=WHITE
        )
        code_group = VGroup(code, code2)
        code_group.arrange(DOWN, buff=0.1)
        code_group.to_edge(DOWN, buff=0.4)
        self.add(code_group)
        
        self.wait(0.5)


# Render command:
# manim -qh ch8_multivector_hypothesis.py Scene1_RedCarComposition Scene2_MultivectorVocabulary Scene3_RotorVsOffset Scene4_CliffordFrameAttention

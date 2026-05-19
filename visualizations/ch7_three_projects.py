"""
Chapter 7: Three Projects - Visualizations
"""

from manim import *

class Scene1_HiddenInformation(Scene):
    """Scene 1: The problem of hidden bivector information"""
    def construct(self):
        title = Text("The Problem: Hidden Information", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # SLERP projection
        slerp_label = Text("SLERP (Standard)", font_size=22, color=RED)
        slerp_label.shift(UP * 2 + LEFT * 3.5)
        self.add(slerp_label)
        
        # Input: full multivector
        mv_full = Circle(radius=1, color=BLUE, fill_opacity=0.2)
        mv_full.shift(LEFT * 3.5)
        
        # Show grades inside
        grades = VGroup(
            Text("scalar", font_size=12),
            Text("vector", font_size=12),
            Text("bivector", font_size=12, color=YELLOW)
        )
        grades.arrange(DOWN, buff=0.1)
        grades.move_to(mv_full)
        
        self.add(mv_full, grades)
        
        # Arrow showing projection
        arrow = Arrow(
            mv_full.get_right(),
            RIGHT * 0.5,
            color=RED
        )
        self.add(arrow)
        
        arrow_label = Text("grade-1 projection", font_size=14, color=RED)
        arrow_label.next_to(arrow, UP, buff=0.1)
        self.add(arrow_label)
        
        # Output: just vector
        vector_out = Arrow(ORIGIN, RIGHT, color=BLUE, buff=0)
        vector_out.shift(RIGHT * 1.5)
        self.add(vector_out)
        
        lost = Text("bivector lost!", font_size=14, color=RED)
        lost.next_to(vector_out, DOWN, buff=0.3)
        self.add(lost)
        
        # Result: ceiling
        ceiling = VGroup(
            Text("Result:", font_size=16),
            Text("62.90% accuracy", font_size=16, color=RED),
            Text("(can't see why)", font_size=14, color=GRAY)
        )
        ceiling.arrange(DOWN, buff=0.1)
        ceiling.next_to(vector_out, RIGHT, buff=0.8)
        self.add(ceiling)
        
        # Bottom: rotor keeps it
        rotor_text = VGroup(
            Text("Rotor approach:", font_size=16, color=GREEN),
            Text("Keep full multivector", font_size=14),
            Text("→ Regularize geometry", font_size=14),
            Text("→ 70.70% accuracy", font_size=16, color=GREEN)
        )
        rotor_text.arrange(DOWN, buff=0.1)
        rotor_text.to_edge(DOWN, buff=0.5)
        self.add(rotor_text)
        
        self.wait(0.5)


class Scene2_Breakthrough(Scene):
    """Scene 2: The breakthrough - bivector regularization"""
    def construct(self):
        title = Text("The Breakthrough: Geometric Regularization", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Before: clustered embeddings
        before_label = Text("Before: Clustered", font_size=20, color=RED)
        before_label.shift(UP * 2 + LEFT * 3)
        self.add(before_label)
        
        # Clustered dots
        np.random.seed(42)
        before_dots = VGroup()
        for i in range(8):
            angle = np.random.uniform(0, PI/3)
            r = np.random.uniform(0.5, 1.5)
            dot = Dot(
                point=LEFT * 3 + UP * 0.5 + np.array([np.cos(angle)*r*0.5, np.sin(angle)*r*0.5, 0]),
                radius=0.08,
                color=RED
            )
            before_dots.add(dot)
        self.add(before_dots)
        
        before_note = Text("entangled, overlapping", font_size=12, color=GRAY)
        before_note.next_to(before_dots, DOWN, buff=0.3)
        self.add(before_note)
        
        # Arrow
        arrow = Arrow(LEFT, RIGHT, color=YELLOW).shift(UP * 0.5)
        arrow_label = Text("orthogonality loss", font_size=14, color=YELLOW)
        arrow_label.next_to(arrow, UP, buff=0.1)
        self.add(arrow, arrow_label)
        
        # After: orthogonal embeddings
        after_label = Text("After: Orthogonal", font_size=20, color=GREEN)
        after_label.shift(UP * 2 + RIGHT * 3)
        self.add(after_label)
        
        # Orthogonal arrangement
        after_dots = VGroup()
        angles = [0, PI/4, PI/2, 3*PI/4, PI, 5*PI/4, 3*PI/2, 7*PI/4]
        for angle in angles:
            dot = Dot(
                point=RIGHT * 3 + UP * 0.5 + np.array([np.cos(angle)*1.2*0.4, np.sin(angle)*1.2*0.4, 0]),
                radius=0.08,
                color=GREEN
            )
            after_dots.add(dot)
        self.add(after_dots)
        
        after_note = Text("geometrically separable", font_size=12, color=GRAY)
        after_note.next_to(after_dots, DOWN, buff=0.3)
        self.add(after_note)
        
        # Result
        result = VGroup(
            Text("62.90% → 70.70%", font_size=24, color=GREEN),
            Text("Same model, better geometry", font_size=16)
        )
        result.arrange(DOWN, buff=0.2)
        result.to_edge(DOWN, buff=0.5)
        self.add(result)
        
        self.wait(0.5)


class Scene3_MemoryProblem(Scene):
    """Scene 3: Linear memory growth vs constant memory"""
    def construct(self):
        title = Text("The Problem: Linear Memory with Depth", font_size=30)
        title.to_edge(UP)
        self.add(title)
        
        # Standard transformer
        std_label = Text("Standard Transformer", font_size=20, color=RED)
        std_label.shift(UP * 2 + LEFT * 3.5)
        self.add(std_label)
        
        # Stacked layers
        layers = VGroup()
        for i in range(5):
            box = Rectangle(width=2, height=0.4, fill_color=BLUE, fill_opacity=0.3)
            box.shift(LEFT * 3.5 + UP * (1 - i * 0.5))
            label = Text(f"Layer {i+1}", font_size=12)
            label.move_to(box)
            layers.add(VGroup(box, label))
        self.add(layers)
        
        # Arrows between
        for i in range(4):
            arrow = Arrow(
                layers[i][0].get_bottom(),
                layers[i+1][0].get_top(),
                buff=0.05,
                stroke_width=1
            )
            self.add(arrow)
        
        # Memory representation
        memory = VGroup()
        for i in range(5):
            rect = Rectangle(width=0.3, height=0.8 - i*0.1, fill_color=RED, fill_opacity=0.5)
            rect.shift(LEFT * 1.5 + UP * 0.5 + RIGHT * i * 0.4)
            memory.add(rect)
        
        mem_label = Text("Memory stores all layers", font_size=14, color=RED)
        mem_label.next_to(memory, DOWN, buff=0.2)
        self.add(memory, mem_label)
        
        # DEQ approach
        deq_label = Text("DEQ (Deep Equilibrium)", font_size=20, color=GREEN)
        deq_label.shift(UP * 2 + RIGHT * 3)
        self.add(deq_label)
        
        # Single layer with iteration
        deq_box = Rectangle(width=2, height=0.8, fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN)
        deq_box.shift(RIGHT * 3)
        deq_text = Text("f(x) → iterate", font_size=14)
        deq_text.move_to(deq_box)
        self.add(deq_box, deq_text)
        
        # Iteration arrows
        iterations = VGroup()
        for i in range(3):
            arrow = CurvedArrow(
                deq_box.get_top() + LEFT * 0.3 + RIGHT * i * 0.3,
                deq_box.get_top() + LEFT * 0.2 + RIGHT * i * 0.3,
                angle=-PI/3,
                color=GREEN,
                stroke_width=1
            )
            iterations.add(arrow)
        self.add(iterations)
        
        iter_label = Text("Iterate to convergence", font_size=12, color=GREEN)
        iter_label.next_to(deq_box, DOWN, buff=0.3)
        self.add(iter_label)
        
        # Single memory block
        single_mem = Rectangle(width=0.5, height=0.6, fill_color=GREEN, fill_opacity=0.5)
        single_mem.shift(RIGHT * 5)
        single_label = Text("Constant\nmemory", font_size=12, color=GREEN)
        single_label.next_to(single_mem, DOWN, buff=0.2)
        self.add(single_mem, single_label)
        
        # Divider
        divider = Line(UP * 2.5, DOWN * 2, color=GRAY)
        self.add(divider)
        
        # Bottom note
        note = Text(
            "DEQ: unbounded effective depth, constant memory",
            font_size=18,
            color=YELLOW
        )
        note.to_edge(DOWN, buff=0.3)
        self.add(note)
        
        self.wait(0.5)


class Scene4_IntegratedStack(Scene):
    """Scene 4: The integrated GA stack"""
    def construct(self):
        title = Text("Toward a GA-Native Language Model", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Three layers stacked vertically
        
        # Layer 1: Optimization (gamuon)
        opt_box = Rectangle(width=5, height=1, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        opt_box.shift(UP * 2)
        opt_label = Text("Optimization: gamuon", font_size=18, color=BLUE)
        opt_label.move_to(opt_box)
        opt_desc = Text("Geometric optimizer", font_size=12, color=GRAY)
        opt_desc.next_to(opt_box, DOWN, buff=0.1)
        self.add(opt_box, opt_label, opt_desc)
        
        # Arrow down
        arrow1 = Arrow(opt_box.get_bottom(), UP * 0.5, color=WHITE)
        self.add(arrow1)
        
        # Layer 2: Architecture (gattrlm / gaflowlm)
        arch_box = Rectangle(width=5, height=1.2, fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN)
        arch_box.shift(UP * 0)
        
        arch_title = Text("Architecture", font_size=18, color=GREEN)
        arch_title.shift(UP * 0.3)
        
        arch_options = VGroup(
            Text("gattrlm: Clifford DEQ", font_size=12),
            Text("gaflowlm: Rotor flow", font_size=12)
        )
        arch_options.arrange(DOWN, buff=0.1)
        arch_options.shift(DOWN * 0.2)
        
        self.add(arch_box, arch_title, arch_options)
        
        # Arrow down
        arrow2 = Arrow(arch_box.get_bottom(), DOWN * 1.5, color=WHITE)
        self.add(arrow2)
        
        # Layer 3: Attention (CFA - future)
        att_box = Rectangle(width=5, height=1, fill_color=PURPLE, fill_opacity=0.2, stroke_color=PURPLE)
        att_box.shift(DOWN * 2)
        att_label = Text("Attention: Clifford Frame", font_size=18, color=PURPLE)
        att_label.move_to(att_box)
        att_desc = Text("Geometric product attention", font_size=12, color=GRAY)
        att_desc.next_to(att_box, DOWN, buff=0.1)
        self.add(att_box, att_label, att_desc)
        
        # Foundation label
        foundation = Text("All operating on multivectors", font_size=16, color=YELLOW)
        foundation.to_edge(DOWN, buff=0.3)
        self.add(foundation)
        
        self.wait(0.5)


# Render command:
# manim -qh ch7_three_projects.py Scene1_HiddenInformation Scene2_Breakthrough Scene3_MemoryProblem Scene4_IntegratedStack

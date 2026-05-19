"""
Chapter 6: Explorations - Visualizations
"""

from manim import *

class Scene1_SymmetryProblem(Scene):
    """Scene 1: The problem of learning 3D symmetry from data"""
    def construct(self):
        # Title
        title = Text("The Problem: Learning Symmetry from Data", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Left side: Standard approach
        std_label = Text("Standard Approach", font_size=24, color=RED)
        std_label.shift(UP * 2 + LEFT * 3.5)
        self.add(std_label)
        
        # Input: 3D coordinates
        coords = VGroup(
            Text("(1.2, 3.4, 0.8)", font_size=18),
            Text("(2.1, 1.5, 1.2)", font_size=18),
            Text("(0.5, 2.8, 1.5)", font_size=18)
        )
        coords.arrange(DOWN, buff=0.3)
        coords.shift(LEFT * 3.5 + UP * 0.5)
        self.add(coords)
        
        # Arrow showing rotation needed
        arrow = Arrow(
            coords.get_bottom() + DOWN * 0.3,
            coords.get_bottom() + DOWN * 1.2,
            color=RED
        )
        self.add(arrow)
        
        # Must learn from data
        learn_text = VGroup(
            Text("Must learn:", font_size=16, color=RED),
            Text("Rotate input →", font_size=16),
            Text("Rotate output", font_size=16)
        )
        learn_text.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        learn_text.next_to(arrow, DOWN, buff=0.2)
        self.add(learn_text)
        
        # Waste of capacity
        waste = Text("(millions of examples)", font_size=14, color=GRAY)
        waste.next_to(learn_text, DOWN, buff=0.2)
        self.add(waste)
        
        # Right side: GA approach
        ga_label = Text("GA Approach", font_size=24, color=GREEN)
        ga_label.shift(UP * 2 + RIGHT * 3.5)
        self.add(ga_label)
        
        # Multivector representation
        mv_box = Rectangle(
            width=3, height=2,
            fill_color=GREEN, fill_opacity=0.2,
            stroke_color=GREEN
        )
        mv_box.shift(RIGHT * 3.5)
        self.add(mv_box)
        
        mv_content = VGroup(
            Text("Multivector", font_size=18, color=GREEN),
            Text("scalar: weight", font_size=14),
            Text("vector: position", font_size=14),
            Text("bivector: orientation", font_size=14)
        )
        mv_content.arrange(DOWN, buff=0.15)
        mv_content.move_to(mv_box.get_center())
        self.add(mv_content)
        
        # Built-in equivariance
        builtin = VGroup(
            Text("Built-in:", font_size=16, color=GREEN),
            Text("Rotate multivector", font_size=16),
            Text("= automatic output rotation", font_size=16)
        )
        builtin.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        builtin.next_to(mv_box, DOWN, buff=0.3)
        self.add(builtin)
        
        # Divider
        divider = Line(
            start=UP * 2.5,
            end=DOWN * 3,
            color=GRAY
        )
        self.add(divider)
        
        # Bottom note
        note = Text(
            "GA encodes symmetry in the algebra, not the training data",
            font_size=18,
            color=YELLOW
        )
        note.to_edge(DOWN, buff=0.3)
        self.add(note)
        
        self.wait(0.5)


class Scene2_StructureProblem(Scene):
    """Scene 2: Structured generation - coordinates vs frames"""
    def construct(self):
        title = Text("The Problem: Generating Valid Structures", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Protein backbone sketch - left side
        std_label = Text("Coordinate Diffusion", font_size=22, color=RED)
        std_label.shift(UP * 2 + LEFT * 3.5)
        self.add(std_label)
        
        # Chaotic coordinates
        np.random.seed(42)
        dots = VGroup()
        for i in range(8):
            x = np.random.uniform(-1.5, 1.5)
            y = np.random.uniform(-1, 1)
            dot = Dot(point=LEFT * 3.5 + UP * 0.5 + RIGHT * x + DOWN * y, 
                     radius=0.08, color=RED)
            dots.add(dot)
        
        # Connect with messy lines
        for i in range(len(dots) - 1):
            line = Line(dots[i].get_center(), dots[i+1].get_center(),
                       color=RED, stroke_width=2)
            self.add(line)
        self.add(dots)
        
        # Problems
        problems = VGroup(
            Text("Problems:", font_size=16, color=RED),
            Text("• Invalid bond angles", font_size=14),
            Text("• Steric clashes", font_size=14),
            Text("• Unphysical structures", font_size=14)
        )
        problems.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        problems.next_to(dots, DOWN, buff=0.5)
        self.add(problems)
        
        # GA approach - right side
        ga_label = Text("SE(3) Frames in GA", font_size=22, color=GREEN)
        ga_label.shift(UP * 2 + RIGHT * 3.5)
        self.add(ga_label)
        
        # Ordered frames as multivectors
        frames = VGroup()
        for i in range(5):
            # Frame = position + orientation
            pos = RIGHT * 3.5 + UP * 0.8 + DOWN * i * 0.5
            
            # Small coordinate frame
            x_axis = Arrow(pos, pos + RIGHT * 0.3, color=BLUE, buff=0)
            y_axis = Arrow(pos, pos + UP * 0.3, color=GREEN, buff=0)
            
            frame = VGroup(x_axis, y_axis)
            frames.add(frame)
            
            # Connection to next
            if i < 4:
                connector = Line(
                    pos + DOWN * 0.2,
                    pos + DOWN * 0.5,
                    color=GREEN
                )
                self.add(connector)
        
        self.add(frames)
        
        # Frame label
        frame_text = Text("Each frame = multivector", font_size=14, color=GREEN)
        frame_text.next_to(frames, RIGHT, buff=0.3)
        self.add(frame_text)
        
        # Advantages
        advantages = VGroup(
            Text("Advantages:", font_size=16, color=GREEN),
            Text("• Geometric product enforces constraints", font_size=14),
            Text("• Invalid → high-grade terms", font_size=14),
            Text("• Physical by construction", font_size=14)
        )
        advantages.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        advantages.next_to(frames, DOWN, buff=0.5)
        self.add(advantages)
        
        # Divider
        divider = Line(
            start=UP * 2.5,
            end=DOWN * 3,
            color=GRAY
        )
        self.add(divider)
        
        # Bottom
        note = Text(
            "GA keeps track of relationships that raw coordinates lose",
            font_size=18,
            color=YELLOW
        )
        note.to_edge(DOWN, buff=0.3)
        self.add(note)
        
        self.wait(0.5)


class Scene3_CompositionProblem(Scene):
    """Scene 3: Compositional semantics - blending vs interaction"""
    def construct(self):
        title = Text("The Problem: Composition Without Transformation", font_size=30)
        title.to_edge(UP)
        self.add(title)
        
        # Standard attention
        std_label = Text("Standard Attention", font_size=22, color=RED)
        std_label.shift(UP * 2 + LEFT * 3.5)
        self.add(std_label)
        
        # Words
        red = Text('"red"', font_size=20, color=RED)
        car = Text('"car"', font_size=20, color=BLUE)
        
        words = VGroup(red, Text("+", font_size=20), car)
        words.arrange(RIGHT, buff=0.3)
        words.shift(LEFT * 3.5 + UP * 0.5)
        self.add(words)
        
        # Arrow
        arrow = Arrow(words.get_bottom(), words.get_bottom() + DOWN * 0.8, color=RED)
        self.add(arrow)
        
        # Result - just blending
        result = Text('"red" + "car"', font_size=18, color=PURPLE)
        result.next_to(arrow, DOWN, buff=0.2)
        self.add(result)
        
        # Problem list
        problems = VGroup(
            Text("Linear blending:", font_size=14, color=RED),
            Text("• No new structure created", font_size=14),
            Text("• Meaning is sum, not interaction", font_size=14),
            Text("• Can't represent 'red-car-ness'", font_size=14)
        )
        problems.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        problems.next_to(result, DOWN, buff=0.3)
        self.add(problems)
        
        # GA approach
        ga_label = Text("Geometric Product", font_size=22, color=GREEN)
        ga_label.shift(UP * 2 + RIGHT * 3.5)
        self.add(ga_label)
        
        # Multivector representations
        red_mv = VGroup(
            Rectangle(width=1.2, height=0.5, fill_color=RED, fill_opacity=0.3),
            Text("red", font_size=14)
        )
        red_mv[1].move_to(red_mv[0])
        red_mv.shift(RIGHT * 2.5 + UP * 0.5)
        
        car_mv = VGroup(
            Rectangle(width=1.2, height=0.7, fill_color=BLUE, fill_opacity=0.3),
            Text("car", font_size=14)
        )
        car_mv[1].move_to(car_mv[0])
        car_mv.shift(RIGHT * 4.5 + UP * 0.5)
        
        self.add(red_mv, car_mv)
        
        # Grade labels
        red_grades = VGroup(
            Text("scalar: intensity", font_size=10),
            Text("vector: color", font_size=10)
        )
        red_grades.arrange(DOWN, buff=0.05)
        red_grades.next_to(red_mv, DOWN, buff=0.1)
        self.add(red_grades)
        
        car_grades = VGroup(
            Text("scalar: object", font_size=10),
            Text("vector: vehicle", font_size=10),
            Text("bivector: affordances", font_size=10)
        )
        car_grades.arrange(DOWN, buff=0.05)
        car_grades.next_to(car_mv, DOWN, buff=0.1)
        self.add(car_grades)
        
        # Multiplication arrow
        mult_arrow = Arrow(
            red_mv.get_right() + RIGHT * 0.2,
            car_mv.get_left() + LEFT * 0.2,
            color=GREEN
        )
        self.add(mult_arrow)
        mult_label = Text("geometric product", font_size=12, color=GREEN)
        mult_label.next_to(mult_arrow, UP, buff=0.1)
        self.add(mult_label)
        
        # Result with bivector
        result_box = VGroup(
            Rectangle(width=1.5, height=0.8, fill_color=PURPLE, fill_opacity=0.3),
            VGroup(
                Text("scalar", font_size=10),
                Text("vector", font_size=10),
                Text("+ bivector!", font_size=10, color=YELLOW)
            )
        )
        result_box[1].arrange(DOWN, buff=0.05)
        result_box[1].move_to(result_box[0])
        result_box.shift(RIGHT * 3.5 + DOWN * 1.5)
        self.add(result_box)
        
        # Output arrow
        out_arrow = Arrow(
            car_mv.get_bottom() + DOWN * 0.8,
            result_box.get_top(),
            color=GREEN
        )
        self.add(out_arrow)
        
        # Advantage
        advantage = Text(
            "Creates new bivector: 'red-car relationship'",
            font_size=14,
            color=GREEN
        )
        advantage.next_to(result_box, DOWN, buff=0.2)
        self.add(advantage)
        
        # Divider
        divider = Line(
            start=UP * 2.5,
            end=DOWN * 3,
            color=GRAY
        )
        self.add(divider)
        
        # Bottom
        note = Text(
            "Words don't just align (dot product) — they interact (geometric product)",
            font_size=16,
            color=YELLOW
        )
        note.to_edge(DOWN, buff=0.3)
        self.add(note)
        
        self.wait(0.5)


class Scene4_UnifyingPattern(Scene):
    """Scene 4: The unifying pattern across domains"""
    def construct(self):
        title = Text("The Unifying Pattern", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Three columns
        domains = ["3D Reasoning", "Protein Gen", "Language"]
        problems = [
            ["Raw coordinates", "Learn E(3) symmetry"],
            ["Raw coordinates", "Learn physical constraints"],
            ["Vector embeddings", "Learn composition"]
        ]
        solutions = [
            "Cl(3,0,1) multivectors",
            "SE(3) frames",
            "Grade-separated multivectors"
        ]
        
        colors = [BLUE, GREEN, PURPLE]
        
        for i, (domain, problem, solution, color) in enumerate(zip(domains, problems, solutions, colors)):
            x_pos = LEFT * 4 + RIGHT * i * 4
            
            # Domain label
            domain_label = Text(domain, font_size=20, color=color)
            domain_label.shift(x_pos + UP * 2)
            self.add(domain_label)
            
            # Problem box
            problem_box = VGroup()
            for j, p in enumerate(problem):
                t = Text(p, font_size=14, color=GRAY)
                problem_box.add(t)
            problem_box.arrange(DOWN, buff=0.1)
            problem_box.shift(x_pos + UP * 0.5)
            self.add(problem_box)
            
            # Arrow
            arrow = Arrow(
                x_pos + DOWN * 0.2,
                x_pos + DOWN * 0.8,
                color=color
            )
            self.add(arrow)
            
            # Solution
            solution_text = Text(solution, font_size=14, color=color)
            solution_text.shift(x_pos + DOWN * 1.2)
            self.add(solution_text)
        
        # Connecting lines between columns
        line1 = Line(
            LEFT * 4 + DOWN * 1.2,
            LEFT * 0 + DOWN * 1.2,
            color=YELLOW,
            stroke_width=1
        )
        line2 = Line(
            LEFT * 0 + DOWN * 1.2,
            RIGHT * 4 + DOWN * 1.2,
            color=YELLOW,
            stroke_width=1
        )
        self.add(line1, line2)
        
        # Unifying principle
        principle = Text(
            "Same principle: encode domain structure in the algebra",
            font_size=20,
            color=YELLOW
        )
        principle.shift(DOWN * 2)
        self.add(principle)
        
        # Bottom question
        question = Text(
            "Can we build a language model that thinks in geometric algebra?",
            font_size=18,
            color=WHITE
        )
        question.to_edge(DOWN, buff=0.5)
        self.add(question)
        
        self.wait(0.5)


# Render command:
# manim -qh ch6_explorations.py Scene1_SymmetryProblem Scene2_StructureProblem Scene3_CompositionProblem Scene4_UnifyingPattern

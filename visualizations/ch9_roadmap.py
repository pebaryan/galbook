"""
Chapter 9: Roadmap - Visualizations
"""

from manim import *

class Scene1_IntegratedStack(Scene):
    """Scene 1: The integrated GA stack showing how pieces connect"""
    def construct(self):
        title = Text("The Integrated Stack", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Three main components arranged horizontally with arrows
        
        # gamuon (Optimization)
        gamuon_box = Rectangle(width=2.5, height=1.5, fill_color=BLUE, fill_opacity=0.3, stroke_color=BLUE)
        gamuon_box.shift(LEFT * 4 + UP * 0.5)
        
        gamuon_title = Text("gamuon", font_size=20, color=BLUE)
        gamuon_title.move_to(gamuon_box.get_center() + UP * 0.3)
        
        gamuon_desc = Text("Grade-aware", font_size=14)
        gamuon_desc2 = Text("optimizer", font_size=14)
        gamuon_desc.move_to(gamuon_box.get_center() + DOWN * 0.15)
        gamuon_desc2.next_to(gamuon_desc, DOWN, buff=0.05)
        
        self.add(gamuon_box, gamuon_title, gamuon_desc, gamuon_desc2)
        
        # gaflowlm (Generation)
        flow_box = Rectangle(width=2.5, height=1.5, fill_color=GREEN, fill_opacity=0.3, stroke_color=GREEN)
        flow_box.shift(UP * 0.5)
        
        flow_title = Text("gaflowlm", font_size=20, color=GREEN)
        flow_title.move_to(flow_box.get_center() + UP * 0.3)
        
        flow_desc = Text("Rotor flow", font_size=14)
        flow_desc2 = Text("matching", font_size=14)
        flow_desc.move_to(flow_box.get_center() + DOWN * 0.15)
        flow_desc2.next_to(flow_desc, DOWN, buff=0.05)
        
        self.add(flow_box, flow_title, flow_desc, flow_desc2)
        
        # gattrlm (Architecture)
        attr_box = Rectangle(width=2.5, height=1.5, fill_color=PURPLE, fill_opacity=0.3, stroke_color=PURPLE)
        attr_box.shift(RIGHT * 4 + UP * 0.5)
        
        attr_title = Text("gattrlm", font_size=20, color=PURPLE)
        attr_title.move_to(attr_box.get_center() + UP * 0.3)
        
        attr_desc = Text("Clifford DEQ", font_size=14)
        attr_desc2 = Text("attractor", font_size=14)
        attr_desc.move_to(attr_box.get_center() + DOWN * 0.15)
        attr_desc2.next_to(attr_desc, DOWN, buff=0.05)
        
        self.add(attr_box, attr_title, attr_desc, attr_desc2)
        
        # Arrows showing they all feed into CFA
        arrow1 = Arrow(gamuon_box.get_bottom(), DOWN * 1.5 + LEFT * 2, color=YELLOW, buff=0.1)
        arrow2 = Arrow(flow_box.get_bottom(), DOWN * 1.5, color=YELLOW, buff=0.1)
        arrow3 = Arrow(attr_box.get_bottom(), DOWN * 1.5 + RIGHT * 2, color=YELLOW, buff=0.1)
        
        self.add(arrow1, arrow2, arrow3)
        
        # CFA at the bottom
        cfa_box = Rectangle(width=6, height=1, fill_color=YELLOW, fill_opacity=0.3, stroke_color=YELLOW)
        cfa_box.shift(DOWN * 2)
        
        cfa_title = Text("Clifford Frame Attention", font_size=18, color=YELLOW)
        cfa_title.move_to(cfa_box.get_center() + UP * 0.15)
        
        cfa_desc = Text("Geometric product attention mechanism", font_size=12)
        cfa_desc.move_to(cfa_box.get_center() + DOWN * 0.25)
        
        self.add(cfa_box, cfa_title, cfa_desc)
        
        # Foundation text
        foundation = Text("Shared geometric vocabulary: rotors, multivectors, grade-wise operations", font_size=14, color=WHITE)
        foundation.to_edge(DOWN, buff=0.3)
        self.add(foundation)
        
        self.wait(0.5)


class Scene2_RoadmapTimeline(Scene):
    """Scene 2: The roadmap timeline showing stages 4-7"""
    def construct(self):
        title = Text("The Road Ahead", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Timeline base
        timeline = Line(LEFT * 5, RIGHT * 5, color=GRAY)
        timeline.shift(DOWN * 0.5)
        self.add(timeline)
        
        # Stages
        stages = [
            ("Stage 4", "GA-Native\nAttention", "CFA integration", GREEN, LEFT * 3.5),
            ("Stage 5", "Full GA\nLanguage Model", "1B+ params,\ntrained from scratch", BLUE, LEFT * 1),
            ("Stage 6", "Multimodal\nGrounding", "Cl(4,1) for\n3D + vision", PURPLE, RIGHT * 1.5),
            ("Stage 7", "Inference\nPipeline", "GA quantization,\nCUDA kernels", RED, RIGHT * 4)
        ]
        
        for stage_num, stage_name, desc, color, pos in stages:
            # Stage marker on timeline
            dot = Dot(point=pos + DOWN * 0.5, radius=0.1, color=color)
            self.add(dot)
            
            # Stage number above
            num_text = Text(stage_num, font_size=14, color=color)
            num_text.next_to(dot, UP, buff=0.3)
            self.add(num_text)
            
            # Stage name and description
            name = Text(stage_name, font_size=12, color=color)
            desc_text = Text(desc, font_size=10, color=GRAY)
            
            # Alternate above/below timeline
            if pos[0] < 0:
                name.next_to(num_text, UP, buff=0.2)
                desc_text.next_to(name, UP, buff=0.1)
            else:
                name.next_to(dot, DOWN, buff=0.3)
                desc_text.next_to(name, DOWN, buff=0.1)
            
            self.add(name, desc_text)
        
        # Time indicators
        time_labels = VGroup(
            Text("Near-term", font_size=12, color=GREEN),
            Text("Medium-term", font_size=12, color=BLUE),
            Text("Long-term", font_size=12, color=RED)
        )
        time_labels.arrange(RIGHT, buff=3)
        time_labels.to_edge(DOWN, buff=0.5)
        self.add(time_labels)
        
        self.wait(0.5)


class Scene3_HonestAssessment(Scene):
    """Scene 3: The honest assessment - challenges as questions"""
    def construct(self):
        title = Text("Open Questions", font_size=32)
        title.to_edge(UP)
        self.add(title)
        
        # Left side: Challenges
        challenges_label = Text("Challenges", font_size=20, color=RED)
        challenges_label.shift(UP * 2 + LEFT * 3.5)
        self.add(challenges_label)
        
        challenges = VGroup(
            Text("• Computational cost (2^k scaling)", font_size=14),
            Text("• Small research field", font_size=14),
            Text("• Sudoku ≠ real language", font_size=14),
            Text("• No proven equivariance for NLP", font_size=14),
            Text("• Hardware not optimized for GA", font_size=14)
        )
        challenges.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        challenges.next_to(challenges_label, DOWN, buff=0.3)
        self.add(challenges)
        
        # Arrow in middle
        arrow = Arrow(LEFT, RIGHT, color=YELLOW).shift(DOWN * 0.5)
        arrow_label = Text("become", font_size=14, color=YELLOW)
        arrow_label.next_to(arrow, UP, buff=0.1)
        self.add(arrow, arrow_label)
        
        # Right side: Questions
        questions_label = Text("Research Questions", font_size=20, color=GREEN)
        questions_label.shift(UP * 2 + RIGHT * 3.5)
        self.add(questions_label)
        
        questions = VGroup(
            Text("? Does compression preserve geometry?", font_size=14),
            Text("? What are the best practices?", font_size=14),
            Text("? Does it scale to 50K vocabularies?", font_size=14),
            Text("? What symmetry group for language?", font_size=14),
            Text("? Can custom CUDA close the gap?", font_size=14)
        )
        questions.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        questions.next_to(questions_label, DOWN, buff=0.3)
        self.add(questions)
        
        # Bottom note
        note = Text(
            "Not reasons to stop. Reasons to be rigorous about what we measure.",
            font_size=16,
            color=YELLOW
        )
        note.to_edge(DOWN, buff=0.4)
        self.add(note)
        
        self.wait(0.5)


# Render command:
# manim -qh ch9_roadmap.py Scene1_IntegratedStack Scene2_RoadmapTimeline Scene3_HonestAssessment

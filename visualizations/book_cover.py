"""
Book Cover Illustration for "The Geometry of Meaning"
"""

from manim import *
import numpy as np

class BookCover(Scene):
    def construct(self):
        # Dark background
        self.camera.background_color = "#0a0a0f"
        
        # Title at top
        title = Text("THE GEOMETRY OF MEANING", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.8)
        self.add(title)
        
        subtitle = Text("How Geometric Algebra Is Changing the Way Machines Understand Language", 
                       font_size=20, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.add(subtitle)
        
        # Central geometric composition
        # Create a sphere with words orbiting
        sphere = Sphere(radius=1.5, resolution=(32, 32))
        sphere.set_color(BLUE)
        sphere.set_opacity(0.1)
        sphere.shift(DOWN * 0.5)
        self.add(sphere)
        
        # Words as points on the sphere
        words = ["king", "queen", "man", "woman", "red", "car", "run", "fast"]
        colors = [BLUE, PURPLE, BLUE, PURPLE, RED, BLUE, GREEN, GREEN]
        
        for i, (word, color) in enumerate(zip(words, colors)):
            # Position on sphere surface
            phi = np.pi * (0.3 + 0.4 * (i // 4))
            theta = 2 * np.pi * (i % 4) / 4 + np.pi/8
            
            x = 1.5 * np.sin(phi) * np.cos(theta)
            y = 1.5 * np.sin(phi) * np.sin(theta) - 0.5
            z = 1.5 * np.cos(phi)
            
            pos = np.array([x, y, z])
            
            # Word label
            word_text = Text(word, font_size=14, color=color)
            word_text.move_to(pos * 1.3)
            self.add(word_text)
            
            # Dot on sphere
            dot = Dot(point=pos, radius=0.06, color=color)
            self.add(dot)
        
        # Rotor arrows showing transformations
        # King -> Queen (gender transformation)
        rotor_arc = ArcBetweenPoints(
            np.array([1.5 * 0.7, 1.5 * 0.7 - 0.5, 0]),
            np.array([-1.5 * 0.7, 1.5 * 0.7 - 0.5, 0]),
            angle=PI/3,
            color=YELLOW
        )
        self.add(rotor_arc)
        
        rotor_label = Text("rotor", font_size=12, color=YELLOW)
        rotor_label.move_to(np.array([0, 1.8, 0]))
        self.add(rotor_label)
        
        # Multivector grade layers (concentric circles showing grade structure)
        grades = VGroup()
        for i, (grade_name, color) in enumerate([
            ("scalar", WHITE),
            ("vector", BLUE),
            ("bivector", GREEN),
            ("trivector", RED)
        ]):
            radius = 2.5 + i * 0.15
            circle = Circle(radius=radius, color=color, stroke_width=1, stroke_opacity=0.3)
            circle.shift(DOWN * 0.5)
            grades.add(circle)
            
            # Label on the right
            label = Text(grade_name, font_size=10, color=color, opacity=0.5)
            label.move_to(np.array([radius + 0.2, -0.5 + (i-1.5)*0.2, 0]))
            grades.add(label)
        
        self.add(grades)
        
        # Geometric product visualization (small in corner)
        gp_box = VGroup(
            Rectangle(width=1.2, height=0.6, fill_color=DARK_GRAY, fill_opacity=0.5),
            MathTex(r"a \cdot b = a \wedge b", font_size=16, color=WHITE)
        )
        gp_box[1].move_to(gp_box[0])
        gp_box.to_corner(DR, buff=0.5)
        self.add(gp_box)
        
        # Author/publisher area at bottom
        bottom_text = Text("Pebaryan  |  2026", font_size=14, color=GRAY)
        bottom_text.to_edge(DOWN, buff=0.5)
        self.add(bottom_text)
        
        # Decorative elements - small geometric shapes
        for i in range(8):
            angle = i * PI / 4
            pos = np.array([np.cos(angle) * 3.2, np.sin(angle) * 3.2 - 0.5, 0])
            shape = Dot(point=pos, radius=0.03, color=GRAY, opacity=0.5)
            self.add(shape)
        
        self.wait(0.5)


class BookCoverMinimal(Scene):
    """Simpler, more minimal cover design"""
    def construct(self):
        self.camera.background_color = "#0d1117"
        
        # Title
        title = Text("THE GEOMETRY", font_size=56, color=WHITE)
        title.to_edge(UP, buff=1.2)
        self.add(title)
        
        title2 = Text("OF MEANING", font_size=56, color=WHITE)
        title2.next_to(title, DOWN, buff=0.1)
        self.add(title2)
        
        # Subtitle
        subtitle = Text("How Geometric Algebra Is Changing Machine Language Understanding", 
                       font_size=18, color="#8b949e")
        subtitle.next_to(title2, DOWN, buff=0.4)
        self.add(subtitle)
        
        # Central icon: Rotor in 3D
        # Bivector plane
        plane = Polygon(
            [-1.5, -0.5, 0],
            [1.5, -0.5, 0],
            [1.5, 1.5, 0],
            [-1.5, 1.5, 0],
            fill_color=BLUE,
            fill_opacity=0.1,
            stroke_color=BLUE,
            stroke_width=2
        )
        self.add(plane)
        
        # Vector being rotated
        vector_before = Arrow(ORIGIN, RIGHT, color=WHITE, buff=0, stroke_width=3)
        vector_before.shift(DOWN * 0.5)
        self.add(vector_before)
        
        label_before = Text("word", font_size=16, color=WHITE)
        label_before.next_to(vector_before, DOWN, buff=0.2)
        self.add(label_before)
        
        # Rotation arc
        arc = Arc(radius=1, start_angle=0, angle=PI/2, color=YELLOW, stroke_width=3)
        arc.shift(DOWN * 0.5)
        self.add(arc)
        
        # Vector after rotation
        vector_after = Arrow(ORIGIN, UP, color=GREEN, buff=0, stroke_width=3)
        vector_after.shift(DOWN * 0.5)
        self.add(vector_after)
        
        label_after = Text("meaning", font_size=16, color=GREEN)
        label_after.next_to(vector_after, RIGHT, buff=0.2)
        self.add(label_after)
        
        # Rotor label
        rotor_text = MathTex(r"R \cdot x \cdot \tilde{R}", font_size=20, color=YELLOW)
        rotor_text.move_to(np.array([0.8, 0.5, 0]))
        self.add(rotor_text)
        
        # Bottom info
        author = Text("Pebaryan", font_size=16, color="#8b949e")
        author.to_edge(DOWN, buff=0.8)
        self.add(author)
        
        self.wait(0.5)


class BookCoverGeometric(Scene):
    """Abstract geometric design"""
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        
        # Title
        title = Text("THE GEOMETRY OF MEANING", font_size=42, color=WHITE)
        title.to_edge(UP, buff=0.6)
        self.add(title)
        
        # Abstract composition: intersecting geometric shapes
        # Central sphere
        center = Dot(ORIGIN, radius=0.1, color=WHITE)
        self.add(center)
        
        # Concentric circles representing grades
        for i, color in enumerate([BLUE, GREEN, YELLOW, RED]):
            radius = 0.5 + i * 0.4
            circle = Circle(radius=radius, color=color, stroke_width=2, stroke_opacity=0.6)
            self.add(circle)
        
        # Bivector planes (intersecting)
        plane1 = Rectangle(width=3, height=3, fill_color=BLUE, fill_opacity=0.1, 
                          stroke_color=BLUE, stroke_width=1)
        plane1.rotate(PI/6, axis=UP)
        self.add(plane1)
        
        plane2 = Rectangle(width=3, height=3, fill_color=GREEN, fill_opacity=0.1,
                          stroke_color=GREEN, stroke_width=1)
        plane2.rotate(PI/6, axis=RIGHT)
        self.add(plane2)
        
        # Words positioned at intersections
        word_positions = [
            ("language", UP * 1.5, WHITE),
            ("geometry", DOWN * 1.5, YELLOW),
            ("meaning", LEFT * 1.8, GREEN),
            ("algebra", RIGHT * 1.8, BLUE),
        ]
        
        for word, pos, color in word_positions:
            text = Text(word, font_size=20, color=color)
            text.move_to(pos)
            self.add(text)
        
        # Connecting lines
        connections = [
            (UP * 1.5, DOWN * 1.5),
            (LEFT * 1.8, RIGHT * 1.8),
            (UP * 1.5, LEFT * 1.8),
            (UP * 1.5, RIGHT * 1.8),
            (DOWN * 1.5, LEFT * 1.8),
            (DOWN * 1.5, RIGHT * 1.8),
        ]
        
        for start, end in connections:
            line = DashedLine(start, end, color=GRAY, stroke_width=1, stroke_opacity=0.3)
            self.add(line)
        
        # Subtitle at bottom
        subtitle = Text("How Geometric Algebra Is Changing the Way Machines Understand Language",
                       font_size=16, color="#a0a0a0")
        subtitle.to_edge(DOWN, buff=0.8)
        self.add(subtitle)
        
        self.wait(0.5)


# Render command for high quality cover:
# manim -qh book_cover.py BookCoverMinimal
# Then extract final frame

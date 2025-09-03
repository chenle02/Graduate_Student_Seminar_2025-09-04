import random

import numpy as np
from manim import *

from Longest_increasing_subsequence.lis_dp import lis_dp


class LisLppPrototypeScene(Scene):
    """
    Manim scene for visualizing the connection between LIS and LPP (prototype).
    Based on the updated plan in Animation-LIS-LPP.md.
    """

    def construct(self):
        author_text = Text("Le Chen@Auburn, 2025/09", font_size=20).to_corner(DOWN + RIGHT, buff=0.5)
        self.add(author_text)

        N = 4
        p = [2, 0, 3, 1]
        points_coords = [(i, p[i]) for i in range(N)]

        # Scene setup
        title = Text(f"LIS and LPP (N={N})", font_size=36).to_edge(UP)
        perm_text_mobs = VGroup(*[Text(str(x), font_size=28) for x in p])
        perm_text_mobs.arrange(RIGHT, buff=0.4).next_to(title, DOWN)
        self.play(Write(title), Write(perm_text_mobs))

        # Create grid
        grid = NumberPlane(
            x_range=(-1, N, 1),
            y_range=(-1, N, 1),
            x_length=5,
            y_length=5,
            axis_config={"include_tip": False, "stroke_opacity": 0.3},
            x_axis_config={"numbers_to_include": np.arange(0, N)},
            y_axis_config={"numbers_to_include": np.arange(0, N)},
        ).center()

        grid_labels = grid.get_axis_labels(x_label="i", y_label="p_i")
        self.play(Create(grid), Write(grid_labels))
        self.wait(0.5)

        # Plot points
        dots = VGroup(*[Dot(grid.c2p(x, y), color=BLUE) for x, y in points_coords])
        self.play(Create(dots))
        self.wait(0.5)

        # LIS for p = [2, 0, 3, 1] is [0, 1] at indices 1, 3
        lis_indices = [1, 3]
        lis_seq = [p[i] for i in lis_indices]
        lis_points_coords = [points_coords[i] for i in lis_indices]

        # Highlight LIS in text and on grid
        self.play(
            *[perm_text_mobs[i].animate.set_color(RED) for i in lis_indices],
            *[dots[i].animate.set_color(RED).scale(1.2) for i in lis_indices],
            *[dots[i].animate.set_color(GRAY).set_opacity(0.5) for i in range(N) if i not in lis_indices],
        )
        self.wait(0.5)

        # Draw path
        path = VGroup()
        path_points = [(0,0)] + lis_points_coords
        
        for i in range(len(path_points) - 1):
            start_point = path_points[i]
            end_point = path_points[i+1]
            corner_point = (end_point[0], start_point[1])
            
            p1 = grid.c2p(*start_point)
            p2 = grid.c2p(*corner_point)
            p3 = grid.c2p(*end_point)
            
            path.add(Line(p1, p2, color=YELLOW, stroke_width=6))
            path.add(Line(p2, p3, color=YELLOW, stroke_width=6))

        self.play(Create(path))
        self.wait(0.5)

        # Display LIS text
        lis_text_str = f"LIS: {lis_seq}, Length: {len(lis_seq)}"
        lis_text = Text(lis_text_str, font_size=28).next_to(perm_text_mobs, DOWN)
        self.play(Write(lis_text))
        self.wait(2)


class LisLppScene(Scene):
    """
    Manim scene for visualizing the connection between LIS and LPP (N=8).
    """

    def construct(self):
        author_text = Text("Le Chen@Auburn, 2025/09", font_size=20).to_corner(DOWN + RIGHT, buff=0.5)
        self.add(author_text)

        N = 8
        p = list(range(N))
        random.shuffle(p)
        points_coords = [(i, p[i]) for i in range(N)]

        # Scene setup
        title = Text(f"LIS and LPP (N={N})", font_size=36).to_edge(UP)
        perm_text_mobs = VGroup(*[Text(str(x), font_size=28) for x in p])
        perm_text_mobs.arrange(RIGHT, buff=0.4).next_to(title, DOWN)
        self.play(Write(title), Write(perm_text_mobs))

        # Create grid
        grid = NumberPlane(
            x_range=(-1, N, 1),
            y_range=(-1, N, 1),
            x_length=7,
            y_length=7,
            axis_config={"include_tip": False, "stroke_opacity": 0.3},
            x_axis_config={"numbers_to_include": np.arange(0, N)},
            y_axis_config={"numbers_to_include": np.arange(0, N)},
        ).center()

        grid_labels = grid.get_axis_labels(x_label="i", y_label="p_i")
        self.play(Create(grid), Write(grid_labels))
        self.wait(1)

        # Plot points
        dots = VGroup(*[Dot(grid.c2p(x, y), color=BLUE) for x, y in points_coords])
        self.play(Create(dots))
        self.wait(1)

        # Compute LIS
        lis_len, lis_seq, _, prev, end_idx = lis_dp(p)
        lis_indices = []
        k = end_idx
        while k != -1:
            lis_indices.append(k)
            k = prev[k]
        lis_indices.reverse()
        lis_points_coords = [points_coords[i] for i in lis_indices]

        # Highlight LIS
        self.play(
            *[perm_text_mobs[i].animate.set_color(RED) for i in lis_indices],
            *[dots[i].animate.set_color(RED).scale(1.2) for i in lis_indices],
            *[dots[i].animate.set_color(GRAY).set_opacity(0.5) for i in range(N) if i not in lis_indices],
        )
        self.wait(1)

        # Draw path
        path = VGroup()
        path_points = [(0,0)] + lis_points_coords
        
        # Path between points
        for i in range(len(path_points) - 1):
            start_point = path_points[i]
            end_point = path_points[i+1]
            corner_point = (end_point[0], start_point[1])
            
            p1 = grid.c2p(*start_point)
            p2 = grid.c2p(*corner_point)
            p3 = grid.c2p(*end_point)
            
            path.add(Line(p1, p2, color=YELLOW, stroke_width=5))
            path.add(Line(p2, p3, color=YELLOW, stroke_width=5))

        # Extend path to right boundary
        if lis_points_coords:
            last_lis_point = lis_points_coords[-1]
            if last_lis_point[0] < N - 1:
                p_start = grid.c2p(*last_lis_point)
                p_end = grid.c2p(N - 1, last_lis_point[1])
                path.add(Line(p_start, p_end, color=YELLOW, stroke_width=5))

        self.play(Create(path))
        self.wait(1)

        # Display LIS text
        lis_text_str = f"LIS: {lis_seq}, Length: {lis_len}"
        lis_text = Text(lis_text_str, font_size=28).next_to(perm_text_mobs, DOWN)
        self.play(Write(lis_text))
        self.wait(3)
import random

import numpy as np
from manim import *

from Longest_increasing_subsequence.lis_dp import lis_dp


class LisLppPrototypeScene(Scene):
    """
    Manim scene for visualizing the connection between LIS and LPP (prototype).
    Based on the plan in Animation-LIS-LPP.md.
    """

    def construct(self):
        author_text = Text("Le Chen@Auburn, 2025/09", font_size=20).to_corner(DOWN + RIGHT, buff=0.5)
        self.add(author_text)
        N = 4
        p = [3, 1, 4, 2]
        points_coords = [(i + 1, p[i]) for i in range(N)]

        # Scene setup
        title = Text(f"LIS and Last-Passage Percolation (N={N})", font_size=36).to_edge(
            UP
        )
        self.play(Write(title))

        # Create grid
        grid = NumberPlane(
            x_range=(0, N + 1, 1),
            y_range=(0, N + 1, 1),
            x_length=5,
            y_length=5,
            axis_config={"include_tip": False, "stroke_opacity": 0.3},
            x_axis_config={"numbers_to_include": np.arange(1, N + 1)},
            y_axis_config={"numbers_to_include": np.arange(1, N + 1)},
        ).center()

        grid_labels = grid.get_axis_labels(x_label="i", y_label="p_i")
        self.play(Create(grid), Write(grid_labels))
        self.wait(0.5)

        # Plot points
        dots = VGroup(*[Dot(grid.c2p(x, y), color=BLUE) for x, y in points_coords])
        self.play(Create(dots))
        self.wait(0.5)

        # As per plan, use LIS [3, 4] which corresponds to indices 0 and 2
        lis_indices = [0, 2]
        lis_seq = [p[i] for i in lis_indices]
        lis_points_coords = [points_coords[i] for i in lis_indices]

        lis_dots = VGroup(*[dots[i] for i in lis_indices])
        non_lis_dots = VGroup(*[dots[i] for i in range(N) if i not in lis_indices])

        self.play(
            lis_dots.animate.set_color(RED).scale(1.2),
            non_lis_dots.animate.set_color(GRAY).set_opacity(0.5),
        )
        self.wait(0.5)

        # Draw path
        path = VGroup()
        start_point = lis_points_coords[0]
        end_point = lis_points_coords[1]
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
        lis_text = Text(lis_text_str, font_size=28).next_to(grid, UP, buff=0.3)
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
        # Generate a random permutation
        p = list(range(1, N + 1))
        random.shuffle(p)

        points_coords = [(i + 1, p[i]) for i in range(N)]

        # Scene setup
        title = Text(
            f"LIS and Last-Passage Percolation (N={N})", font_size=36
        ).to_edge(UP)
        perm_text = Text(f"Permutation: {p}", font_size=24).next_to(title, DOWN)
        self.play(Write(title), Write(perm_text))

        # Create grid
        grid = NumberPlane(
            x_range=(0, N + 2, 1),
            y_range=(0, N + 2, 1),
            x_length=7,
            y_length=7,
            axis_config={"include_tip": False, "stroke_opacity": 0.3},
            x_axis_config={"numbers_to_include": np.arange(1, N + 1)},
            y_axis_config={"numbers_to_include": np.arange(1, N + 1)},
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

        lis_dots = VGroup(*[dots[i] for i in lis_indices])
        non_lis_dots = VGroup(*[dots[i] for i in range(N) if i not in lis_indices])

        self.play(
            lis_dots.animate.set_color(RED).scale(1.2),
            non_lis_dots.animate.set_color(GRAY).set_opacity(0.5),
        )
        self.wait(1)

        # Draw path
        path = VGroup()
        for i in range(len(lis_points_coords) - 1):
            start_point = lis_points_coords[i]
            end_point = lis_points_coords[i + 1]

            corner_point = (end_point[0], start_point[1])

            p1 = grid.c2p(*start_point)
            p2 = grid.c2p(*corner_point)
            p3 = grid.c2p(*end_point)

            path.add(Line(p1, p2, color=YELLOW, stroke_width=5))
            path.add(Line(p2, p3, color=YELLOW, stroke_width=5))

        self.play(Create(path))
        self.wait(1)

        # Display LIS text
        lis_text_str = f"LIS: {lis_seq}, Length: {lis_len}"
        lis_text = Text(lis_text_str, font_size=28).next_to(perm_text, DOWN)
        self.play(Write(lis_text))
        self.wait(3)

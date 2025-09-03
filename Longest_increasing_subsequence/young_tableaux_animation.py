import numpy as np
from manim import *

from Longest_increasing_subsequence.lis_dp import lis_dp
from Longest_increasing_subsequence.rsk_algorithm import rsk_build_tableau


class PermutationToLISScene(Scene):
    def construct(self):
        N = 4
        p = [3, 1, 4, 2]

        title = Text(f"Permutation to LIS (N={N})", font_size=36).to_edge(UP)
        perm_text = Text(f"π = {p}", font_size=28).next_to(title, DOWN)
        self.play(Write(title), Write(perm_text))

        grid = NumberPlane(
            x_range=(0, N + 1, 1),
            y_range=(0, N + 1, 1),
            x_length=5,
            y_length=5,
        ).next_to(perm_text, DOWN)
        self.play(Create(grid))

        points_coords = [(i + 1, p[i]) for i in range(N)]
        dots = VGroup(*[Dot(grid.c2p(x, y), color=BLUE) for x, y in points_coords])
        self.play(Create(dots))

        lis_len, lis_seq, _, _, _ = lis_dp(p)
        # Hardcode which LIS to show for consistency
        lis_indices = [1, 3]  # for LIS [1, 2]

        lis_dots = VGroup(*[dots[i] for i in lis_indices])
        non_lis_dots = VGroup(*[dots[i] for i in range(N) if i not in lis_indices])

        self.play(lis_dots.animate.set_color(RED), non_lis_dots.animate.set_color(GRAY))

        path = VGroup()
        lis_points_coords = [points_coords[i] for i in lis_indices]
        for i in range(len(lis_points_coords) - 1):
            start_point = lis_points_coords[i]
            end_point = lis_points_coords[i + 1]
            path.add(
                Line(grid.c2p(*start_point), grid.c2p(*end_point), color=RED, stroke_width=6)
            )
        self.play(Create(path))

        lis_text = Text(f"LIS Length = {lis_len}", font_size=28).next_to(grid, DOWN)
        self.play(Write(lis_text))
        self.wait(2)


class RSKInsertionScene(Scene):
    def construct(self):
        N = 4
        p = [3, 1, 4, 2]

        title = Text(f"RSK Insertion (π = {p})", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Placeholder for the RSK animation
        placeholder_text = Text("RSK animation coming soon...", font_size=48)
        self.play(Write(placeholder_text))
        self.wait(2)

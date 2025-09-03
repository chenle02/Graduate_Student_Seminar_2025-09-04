import random

import numpy as np
from manim import *

from Longest_increasing_subsequence.lis_dp import lis_dp


class LisLppMultiSampleScene(Scene):
    # To be configured by subclasses
    N = 4
    NUM_SAMPLES = 3
    GRID_XLEN = 5
    GRID_YLEN = 5
    GRID_SCALE = 1.0

    def construct(self):
        author_text = Text("Le Chen@Auburn, 2025/09", font_size=20).to_corner(
            DOWN + RIGHT, buff=0.5
        )
        self.add(author_text)

        title = Text(f"LIS and LPP (N={self.N})", font_size=36).to_edge(UP)
        self.add(title)

        for i in range(self.NUM_SAMPLES):
            # --- Setup for one sample ---

            p = list(range(self.N))
            random.shuffle(p)
            points_coords = [(j, p[j]) for j in range(self.N)]

            perm_text_mobs = VGroup(*[Text(str(x), font_size=28) for x in p])
            perm_text_mobs.arrange(RIGHT, buff=0.4).next_to(title, DOWN)

            grid = (
                NumberPlane(
                    x_range=(0, self.N - 1, 1),
                    y_range=(0, self.N - 1, 1),
                    x_length=self.GRID_XLEN,
                    y_length=self.GRID_YLEN,
                    axis_config={"include_tip": False, "stroke_opacity": 0.3},
                    x_axis_config={"numbers_to_include": np.arange(0, self.N)},
                    y_axis_config={
                        "numbers_to_include": np.arange(0, self.N),
                        "label_direction": LEFT,
                    },
                )
                .next_to(perm_text_mobs, DOWN, buff=0.2)
                .scale(self.GRID_SCALE)
            )

            self.play(Write(perm_text_mobs), Create(grid))

            dots = VGroup(
                *[Dot(grid.c2p(x, y), color=BLUE) for x, y in points_coords]
            )
            self.play(Create(dots))

            # --- LIS ---
            lis_len, lis_seq, _, prev, end_idx = lis_dp(p)
            lis_indices = []
            k = end_idx
            while k != -1:
                lis_indices.append(k)
                k = prev[k]
            lis_indices.reverse()
            lis_points_coords = [points_coords[j] for j in lis_indices]

            # --- Highlight ---
            self.play(
                *[perm_text_mobs[j].animate.set_color(RED) for j in lis_indices],
                *[dots[j].animate.set_color(RED).scale(1.2) for j in lis_indices],
                *[
                    dots[j].animate.set_color(GREEN).scale(1.2)
                    for j in range(self.N)
                    if j not in lis_indices
                ],
            )
            self.wait(0.5)

            # --- Path ---
            path = VGroup()
            path_points = [(0, 0)] + lis_points_coords
            if lis_points_coords:
                for j in range(len(path_points) - 1):
                    start_point = path_points[j]
                    end_point = path_points[j + 1]
                    corner = (end_point[0], start_point[1])
                    path.add(
                        Line(grid.c2p(*start_point), grid.c2p(*corner), color=YELLOW)
                    )
                    path.add(
                        Line(grid.c2p(*corner), grid.c2p(*end_point), color=YELLOW)
                    )

                last_lis_point = lis_points_coords[-1]
                if last_lis_point[0] < self.N - 1:
                    path.add(
                        Line(
                            grid.c2p(*last_lis_point),
                            grid.c2p(self.N - 1, last_lis_point[1]),
                            color=YELLOW,
                        )
                    )
            self.play(Create(path))
            self.wait(0.5)

            # --- LIS Length Text ---
            lis_text = Text(f"L = {lis_len}", font_size=28).next_to(
                perm_text_mobs, RIGHT, buff=0.5
            )
            self.play(Write(lis_text))
            self.wait(2)

            # --- Clear sample ---
            self.play(
                FadeOut(perm_text_mobs),
                FadeOut(grid),
                FadeOut(dots),
                FadeOut(path),
                FadeOut(lis_text),
            )


class LisLppPrototypeScene(LisLppMultiSampleScene):
    N = 4
    NUM_SAMPLES = 3
    GRID_XLEN = 5
    GRID_YLEN = 5
    GRID_SCALE = 1.0


class LisLppScene(LisLppMultiSampleScene):
    N = 8
    NUM_SAMPLES = 3
    GRID_XLEN = 6
    GRID_YLEN = 6
    GRID_SCALE = 0.9

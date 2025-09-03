import numpy as np
from manim import *

from Longest_increasing_subsequence.lis_dp import lis_dp
from Longest_increasing_subsequence.rsk_algorithm import rsk_build_tableau, rsk_insert_animated


def pad_tableau(tableau, fill=""):
    """
    Pad a ragged Young tableau to a rectangular array so Manim's Table accepts it.
    Each row is extended with `fill` up to the maximum row length.
    """
    if not tableau:
        return [[fill]]
    width = max(len(row) for row in tableau) or 1
    return [row + [fill] * (width - len(row)) for row in tableau]


def to_str_rect(tableau):
    """Return a rectangular table of strings suitable for Manim's Table."""
    padded = pad_tableau(tableau, fill="")
    return [[str(cell) for cell in row] for row in padded]


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
        p = [4, 2, 5, 1, 3]
        title = Text(f"Forward RSK: π = {p}", font_size=36).to_edge(UP)
        self.play(Write(title))

        p_tableau_data = []
        q_tableau_data = []

        p_table = Table([[""]]).to_edge(LEFT, buff=1)
        q_table = Table([[""]]).to_edge(RIGHT, buff=1)
        p_label = Text("P =").next_to(p_table, UP)
        q_label = Text("Q =").next_to(q_table, UP)
        self.play(Write(p_label), Write(q_label), Create(p_table), Create(q_table))

        perm_mobs = VGroup(*[Text(str(x)) for x in p]).arrange(RIGHT).next_to(title, DOWN)
        self.play(Write(perm_mobs))

        for k, x in enumerate(p):
            self.play(Indicate(perm_mobs[k]))

            x_mob = perm_mobs[k].copy()
            self.play(x_mob.animate.move_to(p_table.get_rows()[0]))

            new_p_tableau, path = rsk_insert_animated(p_tableau_data, x)

            # For now, just transform to the new table.
            # Manim's Table requires rows of equal length; pad with blanks
            new_p_table = Table(
                to_str_rect(new_p_tableau),
                include_outer_lines=True,
            ).move_to(p_table.get_center())

            # Update Q table
            new_cell_pos = path[-1][:2]
            while len(q_tableau_data) < len(new_p_tableau):
                q_tableau_data.append([])
            for i in range(len(new_p_tableau)):
                while len(q_tableau_data[i]) < len(new_p_tableau[i]):
                    q_tableau_data[i].append("")

            q_tableau_data[new_cell_pos[0]][new_cell_pos[1]] = k + 1
            # Ensure Q is also rectangular (already enforced above, but safe to pad)
            new_q_table = Table(
                to_str_rect(q_tableau_data),
                include_outer_lines=True,
            ).move_to(q_table.get_center())

            self.play(
                Transform(p_table, new_p_table),
                Transform(q_table, new_q_table),
                FadeOut(x_mob)
            )
            self.wait(1)
            p_tableau_data = new_p_tableau

from manim import *
import random
import re
from Longest_increasing_subsequence.lis_dp import lis_dp

class LisRandomPermutationsBase(Scene):
    # To be configured by subclasses
    N = 8
    M = 6
    TITLE_TEXT = "LIS in Random Permutations"
    FONT_SIZE = 24

    def construct(self):
        author_text = Text("Le Chen@Auburn, 2025/09", font_size=20).to_corner(DOWN + RIGHT, buff=0.5)
        self.add(author_text)

        # 1. Scene Setup
        title = Text(self.TITLE_TEXT, font_size=40).to_edge(UP)
        params = Text(f"N = {self.N}, M = {self.M}", font_size=32).next_to(title, DOWN)
        self.play(Write(title), Write(params))
        self.wait(1)

        # Two-row layout
        rows = VGroup(*[VGroup() for _ in range(2)])
        rows.arrange(DOWN, buff=1.5).next_to(params, DOWN, buff=0.5)

        # Store mobjects for each of the 2 display rows
        row_mobjects = [VGroup(), VGroup()]

        # Animation loop for M permutations
        for i in range(self.M):
            current_row_index = i % 2
            
            # Clear the row before drawing
            if len(row_mobjects[current_row_index]) > 0:
                self.play(FadeOut(row_mobjects[current_row_index]), run_time=0.5)
                row_mobjects[current_row_index].remove_all_subobjects()

            # Generate and display permutation
            perm = list(range(self.N))
            random.shuffle(perm)
            perm_mobs = VGroup(*[Text(str(x), font_size=self.FONT_SIZE) for x in perm])
            perm_mobs.arrange(RIGHT, buff=0.4).move_to(rows[current_row_index])
            
            self.play(Write(perm_mobs))
            row_mobjects[current_row_index].add(perm_mobs)

            # LIS Highlighting
            lis_len, lis_seq, _, _, _ = lis_dp(perm)
            lis_elements = set(lis_seq)
            
            highlight_anims = []
            for mob in perm_mobs:
                num_val = int(mob.text)
                if num_val in lis_elements:
                    highlight_anims.append(mob.animate.set_color(GREEN))
                else:
                    highlight_anims.append(mob.animate.set_opacity(0.3))
            
            self.play(*highlight_anims)

            # Display LIS Length
            length_text = Text(f"Length = {lis_len}", font_size=self.FONT_SIZE).next_to(perm_mobs, RIGHT, buff=0.5)
            self.play(Write(length_text))
            row_mobjects[current_row_index].add(length_text)

            self.wait(1)

        self.wait(3)

class LisPermutationsSmall(LisRandomPermutationsBase):
    N = 8
    M = 6
    TITLE_TEXT = "LIS in Random Permutations (N=8)"
    FONT_SIZE = 30

class LisPermutationsLarge(LisRandomPermutationsBase):
    N = 16
    M = 5
    TITLE_TEXT = "LIS in Random Permutations (N=16)"
    FONT_SIZE = 24

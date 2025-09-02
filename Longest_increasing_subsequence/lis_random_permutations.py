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

        # Grid layout
        rows = VGroup()
        for _ in range(self.M):
            # Create a VGroup for each row to hold the numbers
            row_group = VGroup()
            rows.add(row_group)
        
        rows.arrange(DOWN, buff=0.7).next_to(params, DOWN, buff=0.5)
        
        # Animation loop
        all_length_texts = VGroup()
        for i in range(self.M):
            # 2.1 Generate and Display Permutation
            perm = list(range(self.N))
            random.shuffle(perm)
            
            perm_mobs = VGroup(*[Text(str(x), font_size=self.FONT_SIZE) for x in perm])
            perm_mobs.arrange(RIGHT, buff=0.4).move_to(rows[i])
            rows[i].add(perm_mobs)

            self.play(Write(perm_mobs), run_time=0.5)
            self.wait(0.2)

            # 2.2 LIS Highlighting
            lis_len, lis_seq, _, _, _ = lis_dp(perm)
            
            # Create a set of the LIS *elements* for quick lookup
            lis_elements = set(lis_seq)
            
            highlight_anims = []
            for mob in perm_mobs:
                num_val = int(mob.text)
                if num_val in lis_elements:
                    highlight_anims.append(mob.animate.set_color(GREEN))
                else:
                    highlight_anims.append(mob.animate.set_opacity(0.3))
            
            self.play(*highlight_anims, run_time=0.5)
            self.wait(0.2)

            # 2.3 Display LIS Length
            length_text = Text(f"Length = {lis_len}", font_size=self.FONT_SIZE).next_to(perm_mobs, RIGHT, buff=0.5)
            all_length_texts.add(length_text)
            self.play(Write(length_text), run_time=0.3)
            self.wait(0.5)

        # Final summary text (optional)
        avg_len = sum(int(re.search(r'\d+', lt.text).group()) for lt in all_length_texts) / self.M
        avg_text = Text(f"Average LIS Length: {avg_len:.2f}", font_size=32).to_edge(DOWN)
        self.play(Write(avg_text))

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

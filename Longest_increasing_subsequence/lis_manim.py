from manim import *
from Longest_increasing_subsequence.lis_dp import lis_dp, vdc_example


class LisDPScene(Scene):
    def construct(self):
        arr = vdc_example()
        n = len(arr)

        nums = VGroup(*[Text(str(x), font_size=36) for x in arr])
        nums.arrange(RIGHT, buff=0.6).to_edge(UP, buff=1)

        idxs = VGroup(*[Text(str(i), font_size=24, color=GRAY_D) for i in range(n)])
        for i in range(n):
            idxs[i].next_to(nums[i], DOWN, buff=0.15)

        dp_vals = [1] * n
        prev_idx = [-1] * n
        dp_mobs = VGroup(*[Text("1", font_size=32, color=BLUE_D) for _ in range(n)])
        for i in range(n):
            dp_mobs[i].next_to(idxs[i], DOWN, buff=0.2)

        self.play(FadeIn(nums), FadeIn(idxs), FadeIn(dp_mobs))
        self.wait(0.2)

        highlight_i = None
        highlight_j = None
        pred_arrows = [None] * n

        best_len_text = Text("best len: 1", font_size=28).to_corner(UR).shift(LEFT * 0.3 + DOWN * 0.2)
        self.play(FadeIn(best_len_text))

        best_len = 1
        best_end = 0

        for i in range(n):
            if highlight_i:
                self.play(FadeOut(highlight_i), run_time=0.1)
            highlight_i = SurroundingRectangle(nums[i], color=YELLOW, buff=0.1)
            self.play(Create(highlight_i), run_time=0.15)

            best_dp_i = 1
            best_pred = -1

            for j in range(i):
                if highlight_j:
                    self.play(FadeOut(highlight_j), run_time=0.05)
                highlight_j = SurroundingRectangle(nums[j], color=LIGHT_GREY, buff=0.1)
                self.play(Create(highlight_j), run_time=0.05)

                cond = arr[j] < arr[i]
                if cond and dp_vals[j] + 1 > best_dp_i:
                    best_dp_i = dp_vals[j] + 1
                    best_pred = j

                    new_dp = Text(str(best_dp_i), font_size=32, color=BLUE_D)
                    new_dp.move_to(dp_mobs[i])
                    self.play(Transform(dp_mobs[i], new_dp), run_time=0.08)

                    if pred_arrows[i] is not None:
                        self.play(FadeOut(pred_arrows[i]), run_time=0.05)
                    arrow = Arrow(start=nums[i].get_bottom(), end=nums[j].get_top(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.08)
                    pred_arrows[i] = arrow
                    self.play(Create(arrow), run_time=0.08)

            dp_vals[i] = best_dp_i
            prev_idx[i] = best_pred

            if dp_vals[i] > best_len:
                best_len = dp_vals[i]
                best_end = i
                new_best = Text(f"best len: {best_len}", font_size=28)
                new_best.move_to(best_len_text)
                self.play(Transform(best_len_text, new_best), run_time=0.08)

        if highlight_j:
            self.play(FadeOut(highlight_j), run_time=0.05)
        if highlight_i:
            self.play(FadeOut(highlight_i), run_time=0.05)

        lis_title = Text("Reconstruct LIS", font_size=32, color=GREEN_D).next_to(dp_mobs, DOWN, buff=0.8)
        self.play(FadeIn(lis_title))

        k = best_end
        lis_indices = []
        while k != -1:
            lis_indices.append(k)
            k = prev_idx[k]
        lis_indices.reverse()

        lis_group = VGroup()
        for idx in lis_indices:
            dup = nums[idx].copy().set_color(GREEN)
            lis_group.add(dup)
        lis_group.arrange(RIGHT, buff=0.6).next_to(lis_title, DOWN, buff=0.4)

        anims = []
        for m, idx in zip(lis_group, lis_indices):
            anims.append(Indicate(nums[idx], color=GREEN, scale_factor=1.05, run_time=0.2))
            anims.append(Flash(nums[idx], line_length=0.15, color=GREEN, run_time=0.2))
        if anims:
            self.play(*anims)
        self.play(*[nums[idx].animate.set_color(GREEN) for idx in lis_indices], run_time=0.2)
        self.play(FadeIn(lis_group), run_time=0.2)

        length_text = Text(f"LIS length = {len(lis_indices)}", font_size=30, color=GREEN)
        length_text.next_to(lis_group, DOWN, buff=0.3)
        self.play(FadeIn(length_text))
        self.wait(0.6)

    

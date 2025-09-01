from manim import *

class LisDPSceneGemini(Scene):
    """
    A Manim scene to visualize the Longest Increasing Subsequence (LIS)
    algorithm using dynamic programming, based on the storyboard in the README.
    """
    def construct(self):
        # 1. Setup the scene
        # Van der Corput sequence from the README
        arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        n = len(arr)

        # --- Mobjects for visualization ---
        title = Text("Longest Increasing Subsequence (DP)", font_size=40).to_edge(UP)
        
        # Input sequence numbers
        nums = VGroup(*[Text(str(x), font_size=32) for x in arr])
        nums.arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=0.5)

        # Indices below numbers
        indices = VGroup(*[Text(str(i), font_size=24, color=GREY) for i in range(n)])
        for i in range(n):
            indices[i].next_to(nums[i], DOWN, buff=0.2)

        # DP array visualization
        dp_label = Text("dp:", font_size=32, color=BLUE).next_to(indices, DOWN, buff=0.7, aligned_edge=LEFT)
        dp_mobs = VGroup(*[Text("1", font_size=32, color=BLUE) for _ in range(n)])
        for i in range(n):
            dp_mobs[i].next_to(indices[i], DOWN, buff=0.6)

        # Predecessor array visualization
        prev_label = Text("prev:", font_size=32, color=YELLOW).next_to(dp_label, DOWN, buff=0.7, aligned_edge=LEFT)
        prev_mobs = VGroup(*[Text("-", font_size=32, color=YELLOW) for _ in range(n)])
        for i in range(n):
            prev_mobs[i].next_to(dp_mobs[i], DOWN, buff=0.6)
            
        self.play(FadeIn(title), FadeIn(nums), FadeIn(indices), FadeIn(dp_label), FadeIn(dp_mobs), FadeIn(prev_label), FadeIn(prev_mobs))
        self.wait(1)

        # --- DP Algorithm Logic ---
        dp = [1] * n
        prev = [-1] * n
        arrows = [None] * n

        # 2. Main DP loop animation
        for i in range(n):
            i_box = SurroundingRectangle(nums[i], color=ORANGE, buff=0.1)
            self.play(Create(i_box), run_time=0.2)
            
            for j in range(i):
                j_box = SurroundingRectangle(nums[j], color=GREY, buff=0.1)
                self.play(Create(j_box), run_time=0.1)

                # Check the LIS condition
                if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                    # Update DP value and predecessor
                    dp[i] = dp[j] + 1
                    prev[i] = j

                    # Animate the update
                    self.play(Indicate(nums[j], color=GREEN), Indicate(nums[i], color=GREEN), run_time=0.3)
                    
                    new_dp_val = Text(str(dp[i]), font_size=32, color=BLUE).move_to(dp_mobs[i])
                    new_prev_val = Text(str(j), font_size=32, color=YELLOW).move_to(prev_mobs[i])
                    
                    if arrows[i]:
                        self.play(FadeOut(arrows[i]), run_time=0.1)
                    
                    arrow = Arrow(
                        start=prev_mobs[i].get_center(), 
                        end=dp_mobs[j].get_center() + UP*0.2,
                        buff=0.1, stroke_width=3, color=YELLOW,
                        max_tip_length_to_length_ratio=0.1
                    )
                    arrows[i] = arrow

                    self.play(
                        Transform(dp_mobs[i], new_dp_val),
                        Transform(prev_mobs[i], new_prev_val),
                        Create(arrows[i]),
                        run_time=0.4
                    )

                self.play(FadeOut(j_box), run_time=0.1)
            self.play(FadeOut(i_box), run_time=0.2)

        self.wait(1)

        # 3. Reconstruct the LIS
        reconstruct_title = Text("Reconstructing LIS", font_size=36).next_to(prev_mobs, DOWN, buff=1)
        self.play(Write(reconstruct_title))
        
        # Find the end of the LIS
        best_len = 0
        end_index = -1
        for i in range(n):
            if dp[i] > best_len:
                best_len = dp[i]
                end_index = i

        # Trace back and highlight
        lis_indices = []
        curr = end_index
        while curr != -1:
            lis_indices.append(curr)
            curr = prev[curr]
        lis_indices.reverse()

        # Show the reconstruction process
        highlights = VGroup()
        for idx in reversed(lis_indices):
            highlight = SurroundingRectangle(nums[idx], color=GREEN, buff=0.1)
            highlights.add(highlight)
            self.play(Create(highlight), run_time=0.2)
            if prev[idx] != -1:
                self.play(Indicate(arrows[idx], scale_factor=1.2), run_time=0.5)

        # Display the final LIS
        lis_text = VGroup(*[nums[i].copy().set_color(GREEN) for i in lis_indices])
        lis_text.arrange(RIGHT, buff=0.5).next_to(reconstruct_title, DOWN, buff=0.5)
        
        final_text = Text(f"LIS Length = {best_len}", font_size=32).next_to(lis_text, DOWN, buff=0.5)

        self.play(TransformFromCopy(highlights, lis_text), run_time=1)
        self.play(Write(final_text))
        self.wait(3)

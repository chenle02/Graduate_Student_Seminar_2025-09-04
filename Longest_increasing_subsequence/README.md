# Longest Increasing Subsequence (LIS)

- Source: https://en.wikipedia.org/wiki/Longest_increasing_subsequence

## Overview

Given a sequence of numbers, the Longest Increasing Subsequence (LIS) is a subsequence with strictly increasing values and maximum possible length. We will implement a dynamic programming solution and produce a short Manim animation illustrating how the DP values evolve on a classic example.

## Example (Van der Corput)

In the first 16 terms of the binary Van der Corput sequence:

```
0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15
```

One LIS is:

```
0, 2, 6, 9, 11, 15
```

This subsequence has length 6. Other LIS solutions of equal length include:

```
0, 4, 6, 9, 11, 15
0, 2, 6, 9, 13, 15
0, 4, 6, 9, 13, 15
```

## Approach

- DP O(n^2): For each index `i`, compute `dp[i] = 1 + max(dp[j])` over all `j < i` with `a[j] < a[i]`. Track predecessors to reconstruct one LIS. This is straightforward to explain and animate.
- Optional O(n log n): Patience sorting with binary search on tails for better performance. If time allows, we can mention this variant on a follow-up slide, but the animation will focus on the O(n^2) DP because it is more visual.

## Deliverables

- `Longest_increasing_subsequence/lis_dp.py`: DP solver (computes `length` and one LIS).
- `Longest_increasing_subsequence/lis_manim.py`: Manim scene animating the DP computation on the example above.
- Exported video placed at `videos/LIS_DP_VdC.mp4` and referenced in the slide deck.

## Requirements

- Python 3.10+
- Manim Community (e.g., `pip install manim`)
- NumPy (optional but convenient)

## How to Run (animation)

### Original Animation

From the repository root:

```sh
manim -pqh Longest_increasing_subsequence/lis_manim.py LisDPScene
```

Expected output is an MP4 generated under Manim's `media` folder. Copy or move the rendered file to `videos/LIS_DP_VdC.mp4`. Example:

```sh
mkdir -p videos
cp media/videos/lis_manim/1080p60/LisDPScene.mp4 videos/LIS_DP_VdC.mp4
```

### Gemini-Generated Animation

This version was created by Gemini and includes an author credit overlay.

From the repository root:

```sh
manim -pqh Longest_increasing_subsequence/lis_manim_gemini.py LisDPSceneGemini
```

Expected output is an MP4 generated under Manim's `media` folder. Copy or move the rendered file to `videos/LIS_DP_VdC_gemini.mp4`. Example:

```sh
mkdir -p videos
cp media/videos/lis_manim_gemini/1080p60/LisDPSceneGemini.mp4 videos/LIS_DP_VdC_gemini.mp4
```

## Storyboard (Manim)

1. Show the full input sequence horizontally; label indices.
2. Introduce arrays `dp[i]` and `prev[i]` beneath the numbers.
3. Iterate `i = 0..n-1`; for each `i`, sweep `j = 0..i-1`:
   - Highlight `a[j]` and `a[i]` when checking `a[j] < a[i]`.
   - If better, animate `dp[i]` updating and an arrow from `i` to `j`.
4. Keep a running highlight on the current best `(length, end_index)`.
5. Reconstruct LIS by following `prev` pointers backwards; highlight chosen elements.
6. Conclude with the LIS laid out and the length displayed.

## Slide Integration

- Add a slide with a brief LIS definition and embed the exported video via a `<video>` tag that points to `videos/LIS_DP_VdC.mp4`.
- Keep paths relative and use HTTPS for any external links per repo guidelines.

## Notes

- The DP variant is ideal for teaching; the O(n log n) approach can be summarized afterward if needed.
- Keep assets under `Longest_increasing_subsequence/` while iterating; only move the final MP4 into `videos/` to avoid churn.

## References

- Wikipedia: Longest increasing subsequence — https://en.wikipedia.org/wiki/Longest_increasing_subsequence

# Animation Plan: LIS in Random Permutations

This document outlines the plan for a Manim animation that visualizes the Longest Increasing Subsequence (LIS) across multiple random permutations.

### 1. Scene Setup

- **Title:** The animation will start with a clear title, such as "Longest Increasing Subsequence in Random Permutations".
- **Parameters:** The input parameters, `N` (Sequence Length) and `M` (Number of Permutations), will be displayed at the top of the screen.
- **Two-Row Layout:** The scene will feature two rows to display permutations in an alternating fashion.

### 2. Animation Flow (Alternating Rows)

The animation will cycle through all `M` permutations, alternating between the two rows on screen.

1.  **Generate and Display:**
    - For each permutation `i` from `0` to `M-1`:
    - The animation will focus on row `i % 2`.
    - Any previous content in that row will fade out.
    - A new random permutation of numbers from `0` to `N-1` is generated and displayed in the active row.

2.  **LIS Highlighting:**
    - After a brief pause, the LIS for the new permutation is highlighted.
    - Numbers in the LIS will change to a bright color (e.g., GREEN).
    - All other numbers will be dimmed.

3.  **Display LIS Length:**
    - A text object showing the length of the LIS (e.g., "Length: 7") will appear to the right of the current permutation.

The previous permutation in the other row remains on screen for comparison until it is its turn to be replaced.

### 3. Final Scene

- The animation concludes after the `M`-th permutation is displayed and its LIS length is shown. There is no final grid; the animation is a continuous, looping process.

### 4. Animation Variants

To best illustrate the concept, we will create two separate animations with different parameters using this alternating-row style.

**Variant 1: Small Example**
- **N:** 8
- **M:** 6
- **Goal:** A quick and clear demonstration with multiple, easy-to-read permutations.

**Variant 2: Large Example**
- **N:** 16
- **M:** 5
- **Goal:** A more visually impressive demonstration with longer sequences.
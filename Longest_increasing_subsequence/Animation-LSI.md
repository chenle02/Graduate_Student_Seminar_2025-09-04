# Animation Plan: LIS in Random Permutations

This document outlines the plan for a Manim animation that visualizes the Longest Increasing Subsequence (LIS) across multiple random permutations.

### 1. Scene Setup

- **Title:** The animation will start with a clear title, such as "Longest Increasing Subsequence in Random Permutations".
- **Parameters:** The input parameters, `N` (Sequence Length) and `M` (Number of Permutations), will be displayed at the top of the screen.
- **Grid Layout:** A grid of `M` rows will be pre-rendered to serve as containers for the permutations.

### 2. Animation Flow (Row by Row)

The animation will process one permutation at a time, moving from top to bottom. For each of the `M` rows:

1.  **Generate and Display Permutation:**
    - A random permutation of numbers from `0` to `N-1` is generated.
    - The numbers will be animated appearing one by one in the current row.

2.  **LIS Highlighting:**
    - After a brief pause, the LIS for the current permutation will be highlighted.
    - The numbers that form the LIS will change color to a bright, prominent color (e.g., GREEN).
    - All other numbers will be dimmed by reducing their opacity or changing their color to something muted (e.g., GREY).

3.  **Display LIS Length:**
    - A text object showing the length of the LIS (e.g., "Length: 7") will appear to the right of the permutation.

### 3. Final Scene

- After all `M` rows are processed, the final scene will display the complete grid. Each row will show a permutation with its LIS highlighted and the corresponding length next to it.
- **Optional:** A concluding text can be added at the bottom to show the average LIS length across all `M` trials, connecting the visualization to the mathematical concept of the expected LIS length.

### 4. Animation Variants

To best illustrate the concept, we will create two separate animations with different parameters.

**Variant 1: Small Example**
- **N:** 8
- **M:** 6
- **Goal:** A quick and clear demonstration with multiple, easy-to-read permutations.

**Variant 2: Large Example**
- **N:** 16
- **M:** 5
- **Goal:** A more visually impressive demonstration with longer sequences, providing a good comparison to the main LIS animation.

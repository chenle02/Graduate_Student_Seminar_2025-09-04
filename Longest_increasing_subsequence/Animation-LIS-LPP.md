# Animation Plan: LIS and Last-Passage Percolation

This animation will visualize the connection between the Longest Increasing Subsequence (LIS) of a random permutation and a simple Last-Passage Percolation (LPP) model.

### Scene 1: Permutation and Grid

1.  **Grid and Permutation Setup**:
    *   Use Manim to create a grid for `[0, ..., N-1] x [0, ..., N-1]`. For `N=8`, this is an 8x8 grid with axes labeled 0 to 7.
    *   Generate a random permutation `p` of `[0, ..., N-1]`.
    *   Display the permutation as text above the grid (e.g., `p = [2, 5, 0, 6, 3, 7, 1, 4]`).
2.  **Plot Points**:
    *   Animate plotting dots at coordinates `(i, p_i)` for `i` from 0 to `N-1`.

### Scene 2: Identifying the Longest Increasing Subsequence (LIS)

1.  **Highlight LIS**:
    *   Compute the LIS of the permutation.
    *   In the text representation of `p` above the grid, highlight the numbers belonging to the LIS.
    *   On the grid, highlight the dots corresponding to the LIS (e.g., in red).
    *   Fade out the non-LIS dots (e.g., to gray).
2.  **Display LIS**:
    *   Show the subsequence and its length as text.

### Scene 3: LIS as a Directed Path in a Grid

1.  **Connect the Dots**:
    *   Change title to "LIS as a Longest Path".
    *   Draw a path on the grid lines starting from `(0,0)`.
    *   The path connects to the first LIS point, then connects the LIS points in sequence, and finally extends from the last LIS point to the right boundary (`x = N-1`).
    *   The path must only move right or up.
    *   For two consecutive LIS points `(i, p_i)` and `(j, p_j)`, the path goes from `(i, p_i)` right to `(j, p_i)`, then up to `(j, p_j)`.
    *   The path from `(0,0)` to the first LIS point `(i_1, p_{i_1})` will go right to `(i_1, 0)` then up to `(i_1, p_{i_1})`.
    *   The path from the last LIS point `(i_k, p_{i_k})` will go right to `(N-1, p_{i_k})`.

### Multi-Sample Animation

To better illustrate the variability, the final animation will show 3 random samples for each case (N=4 and N=8).

**Approach:**
- Each scene (`LisLppPrototypeScene` and `LisLppScene`) will contain a loop that runs 3 times.
- Inside the loop, the animation for a single sample will be generated as described in the scenes above.
- Between each sample, the scene will be cleared (or faded out) before the next sample is shown.
- A counter "Sample x/3" will be displayed to indicate the current sample number.

### Prototype with N=4

The prototype will demonstrate the animation on 3 random samples with `N=4`.

*   **Permutation**: For each sample, a new random permutation `p` of `[0, 1, 2, 3]` will be generated.
*   **Animation**: The animation will follow the steps described in Scene 1-3 for each sample.


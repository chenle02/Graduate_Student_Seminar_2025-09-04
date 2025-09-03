# Animation Plan: LIS and Last-Passage Percolation

This animation will visualize the connection between the Longest Increasing Subsequence (LIS) of a random permutation and a simple Last-Passage Percolation (LPP) model.

### Scene 1: Permutation as a Point Set

1.  **Grid Setup**:
    *   Use Manim to create an 8x8 grid with axes labeled 1 to 8.
    *   Add a title: "Random Permutation".
2.  **Generate and Plot**:
    *   Generate a random permutation `p` of `[1, ..., 8]`.
    *   Animate plotting dots at coordinates `(i, p_i)` for `i` from 1 to 8.

### Scene 2: Identifying the Longest Increasing Subsequence (LIS)

1.  **Highlight LIS**:
    *   Change title to "Longest Increasing Subsequence (LIS)".
    *   Compute the LIS and highlight the corresponding dots (e.g., in red).
    *   Fade out the non-LIS dots (e.g., to gray).
2.  **Display LIS**:
    *   Show the subsequence and its length as text, e.g., "LIS: [2, 4, 6, 8], Length: 4".

### Scene 3: LIS as a Directed Path in a Grid

1.  **Connect the Dots**:
    *   Change title to "LIS as a Longest Path".
    *   Draw a path on the grid lines that connects the LIS points. The path must only move right or up.
    *   For two consecutive LIS points `(i, p_i)` and `(j, p_j)`, the path goes from `(i, p_i)` right to `(j, p_i)`, then up to `(j, p_j)`.
2.  **Frame as LPP**:
    *   This path represents the "longest path" through the sites, connecting LIS to Last-Passage Percolation.

### Scene 4: Visualizing the Underlying Structure

1.  **Forbidden Regions**:
    *   To clarify the "increasing" constraint, for each point `(i, p_i)` in the permutation, briefly shade the "forbidden" rectangle of points `(x, y)` where `x > i` and `y < p_i`.
    *   Animate to show that points in an increasing subsequence cannot be in each other's forbidden region.
2.  **Final Picture**:
    *   End with the clean LIS path from Scene 3, reinforcing the LPP connection.

### Prototype with N=4

For a quicker prototype, we can use `N=4`.

*   **Permutation**: Let's use `p = [3, 1, 4, 2]`. The points are `(1,3), (2,1), (3,4), (4,2)`.
*   **LIS**: The LIS is `[1, 2]` (from `p_2=1, p_4=2`) or `[3, 4]` (from `p_1=3, p_3=4`). Let's use `[3, 4]`. The LIS points are `(1,3)` and `(3,4)`.
*   **Path**: The path will connect `(1,3)` and `(3,4)`. It goes right from `(1,3)` to `(3,3)`, then up to `(3,4)`.
*   **Animation Steps**:
    1.  Show the 4x4 grid and the 4 points.
    2.  Highlight `(1,3)` and `(3,4)` in red, dim the other two points.
    3.  Draw the path from `(1,3)` to `(3,3)` to `(3,4)`.
    4.  Display "LIS: [3, 4], Length: 2".


# Animation Plan: RSK Correspondence

This animation provides a detailed, step-by-step visualization of the Robinson-Schensted-Knuth (RSK) correspondence for a single permutation. It will show both the forward insertion process to build the Young tableaux (P and Q) and the backward process to recover the original permutation.

*   **Permutation**: `π = (4, 2, 5, 1, 3)`
*   **N = 5**

---

## Scene 1: Forward RSK - Building the Tableaux

This scene animates the step-by-step construction of the P and Q tableaux.

*   **Initial Setup**:
    *   Display the permutation `π = (4, 2, 5, 1, 3)` at the top.
    *   Create two empty tables side-by-side, labeled "P" and "Q".
    *   A number from the permutation will be shown as the "current number" to be inserted.

*   **Animation Loop (k=1 to 5)**:
    For each number `x = π(k)`:
    1.  **Highlight Current Number**: The number `x` from the permutation and the step counter `k` are highlighted.
    2.  **Insertion into P**:
        *   Animate `x` moving towards the first row of tableau P.
        *   **Bumping**: If `x` bumps an element `y`, `y` is highlighted, moves out of the row, and `x` takes its place. The bumped element `y` then becomes the new number to be inserted into the next row. This process is repeated until a number is appended to a row.
        *   **Appending**: When a number is appended, a new cell is created and the number animates into it.
    3.  **Updating Q**:
        *   Simultaneously with the "append" step in P, a new cell is created in Q in the same position.
        *   The step number `k` animates into this new cell.
    4.  **Pause and Recap**: Briefly pause to show the state of P and Q after each step.

---

## Scene 2: Backward RSK - Recovering the Permutation

This scene animates the reverse process, starting with the final P and Q tableaux from Scene 1.

*   **Initial Setup**:
    *   Display the final P and Q tableaux.
    *   Create an empty list for the recovered permutation `π'`.

*   **Animation Loop (k=5 down to 1)**:
    For each step `k`:
    1.  **Find k in Q**: Highlight the cell in Q containing `k`.
    2.  **Extract from P**:
        *   Highlight the corresponding cell in P. The number in this cell, `x`, is extracted.
        *   The cells in both P and Q are removed or faded out.
    3.  **Reverse Bumping**:
        *   Animate `x` moving up to the row above.
        *   **Replacement**: Find the rightmost element `y < x`. Highlight `y`, move it out, and let `x` take its place. The extracted `y` becomes the new `x` for the next row up.
        *   This is repeated until the top row is processed.
    4.  **Eject Permutation Element**:
        *   The final value of `x` ejected from the top row is an element of the original permutation.
        *   Animate this number moving to its correct position in the `π'` list.
    5.  **Pause and Recap**: Briefly pause to show the state of P, Q, and the recovered permutation.

---

## Final Result

*   The animation concludes by showing the fully recovered permutation `π' = (4, 2, 5, 1, 3)`, matching the original.

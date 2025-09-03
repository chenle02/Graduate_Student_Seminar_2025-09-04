# 🎥 Animation Plan: LIS, Young Tableaux, and the Corner Growth Model

This animation visualizes the correspondence:

**Permutation → Longest Increasing Subsequence → Young Tableau (via RSK) → Corner Growth Model**

---

## 🧠 Conceptual Overview

| Concept                                  | Description                                                                 |
| ---------------------------------------- | --------------------------------------------------------------------------- |
| **LIS (Longest Increasing Subsequence)** | The longest subsequence of a permutation where the values strictly increase |
| **RSK Correspondence**                   | A bijection between permutations and pairs of Young tableaux (P, Q)         |
| **Young Tableau**                        | A grid-based structure with increasing rows and columns                     |
| **Corner Growth Model**                  | A random growth process linked to Last Passage Percolation (LPP)            |

---

## 🎬 Scene-by-Scene Breakdown

### 🎞️ Scene 1: Introduction

* **Title Card**: "From Permutations to Growth Models"
* **Narration** (optional):

  > “Let’s explore how the longest increasing subsequence of a permutation connects to combinatorics and probability.”
* **Visual**: Display a simple permutation:
  `π = [3, 1, 4, 2, 5]`

---

### 🎞️ Scene 2: Plotting the Permutation

* **Grid View**:

  * Plot each pair $(i, \pi_i)$ as a dot in 2D
  * Draw arrows or dots from left to right
* **Highlight LIS**:

  * Show the LIS (e.g., \[3, 4, 5]) in red
  * Draw a path connecting the LIS dots
* **Text Label**:

  * "Longest Increasing Subsequence (LIS) = 3"

---

### 🎞️ Scene 3: RSK Insertion → Young Tableau

* **Step-by-step RSK Insertion**:

  * For each element in the permutation:

    * Insert into the first row
    * If necessary, bump to next row (animation: bump box down)
* **Display the tableau**:

  * Animate cells sliding into place
  * Use colors or numbers to show order of insertion
* **Narration**:

  > “The Robinson–Schensted algorithm builds a tableau whose first row length equals the LIS.”

---

### 🎞️ Scene 4: Tableau → Corner Growth Model

* **Young Tableau Shape**:

  * Treat tableau as a staircase Young diagram
* **Corner Growth Animation**:

  * Fill in boxes one by one at corners (Young diagram style)
  * Animate growth with delays between additions
* **Optional**:

  * Assign weights to each cell (simulate random variables)
  * Show Last Passage Path from (0,0) to (n,n)
* **Narration**:

  > “This growth process corresponds to the corner growth model or last passage percolation.”

---

### 🎞️ Scene 5: Summary & Connections

* **Split-Screen Layout**:
  \| Left: Permutation & LIS | Middle: Young Tableau | Right: Corner Growth |
* **Show arrows** connecting all three structures
* **Narration**:

  > “Permutation statistics, combinatorics, and stochastic growth are deeply linked through this beautiful correspondence.”

---

### 🎞️ Optional Scene 6: Scaling Limit & Tracy–Widom

* **Show animation for large `n`**:

  * Simulate large random permutations
  * Plot scaled Young tableaux (rotated)
* **Overlay Limit Shape**:

  * Parabola or arctic curve
* **Narration**:

  > “As size grows, these shapes converge to a deterministic limit. The fluctuations follow the Tracy–Widom distribution.”

---

## 🎬 Animation Cases

To make the animation concrete, we will produce two versions: a small prototype for clarity and a larger one for visual appeal.

### Prototype Case (N=4)

*   **Permutation**: Use a fixed permutation, e.g., `π = [3, 1, 4, 2]`.
*   **LIS**: The LIS is `[1, 2]` or `[3, 4]`. We will highlight one of them.
*   **Young Tableau**: Show the step-by-step RSK insertion for `[3, 1, 4, 2]`.
    *   `3`: `[[3]]`
    *   `1`: `[[1]]`, `3` is bumped. `[[1], [3]]`
    *   `4`: `[[1, 4], [3]]`
    *   `2`: `[[1, 2], [3]]`, `4` is bumped. `[[1, 2], [3, 4]]`
*   **Goal**: Clearly illustrate the mechanics of the RSK algorithm and its connection to the LIS length.

### Main Case (N=8)

*   **Permutation**: Use a random permutation of `[1, ..., 8]`.
*   **LIS**: Dynamically compute and highlight the LIS.
*   **Young Tableau**: Show a faster, more fluid animation of the RSK insertion.
*   **Corner Growth**: Animate the growth of the resulting Young diagram shape.
*   **Goal**: Demonstrate the concepts on a more visually interesting example and show the typical shape that emerges.

---

## 🛠️ Technical Notes

* **Framework**: `manim` (Community Edition v0.19+)
* **Key Tools**:

  * `Table`, `Grid`, `Dot`, `SurroundingRectangle`, `Transform`
  * Custom Python module for RSK insertion logic

---

## 📁 Suggested Project Structure

```
RSK_Growth_Model/
├── scenes/
│   ├── intro_scene.py
│   ├── plot_permutation.py
│   ├── rsk_insertion.py
│   ├── corner_growth.py
│   └── summary_scene.py
├── utils/
│   └── rsk_algorithm.py
├── assets/
│   └── audio/, images/
├── main.py
└── requirements.txt
```

---

## 📚 References

* Aldous & Diaconis: "Longest Increasing Subsequences: From Patience Sorting to the Baik-Deift-Johansson Theorem"
* Baik, Deift, Johansson (1999): "On the distribution of the length of the longest increasing subsequence of random permutations"
* Tracy & Widom: Distribution functions arising in random matrix theory
* Sagan: *The Symmetric Group*

---

Would you like a **starter `manim` script** for any scene (e.g. RSK or LIS plot)?

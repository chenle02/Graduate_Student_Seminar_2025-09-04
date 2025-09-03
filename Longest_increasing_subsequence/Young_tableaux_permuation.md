
Awesome—let’s do a fully worked RSK example with **$N=5$**, showing **both** the forward (insertion + bumping) and the backward (reverse bumping) procedures **step by step**.

I’ll use the permutation

$$
\pi=(4,\,2,\,5,\,1,\,3).
$$

Notation: rows/cols are **1-indexed**. For forward RSK, in each step $k$ we insert $\pi(k)$.

* **Bump rule (forward):** In a row, find the **leftmost** entry $>\!x$; replace it by $x$ and bump the old entry down to the next row. If none is $>\!x$, append $x$ to the end of the row (this creates the new box).
* **Recording $Q$:** Put $k$ in the **same position** where the new box is created in $P$.
* **Reverse bump rule (backward):** Start from the box in $Q$ labeled $k$; delete that box in both $P,Q$ and set $x$ to the deleted entry from $P$. Then, moving **upward** row by row, in each previous row replace the **rightmost** entry **< $x$** with $x$, and set $x$ to the value you replaced. When you finish the top row, the final $x$ you “eject” is $\pi(k)$.

---

# Forward RSK (build $P,Q$)

We start with $P=\varnothing, Q=\varnothing$.

### Step 1 (insert $4$, $k=1$)

* Row 1 empty ⇒ append 4 (new box at $(1,1)$).
* $P=\big[\,[4]\,\big]$
* $Q=\big[\,[1]\,\big]$

### Step 2 (insert $2$, $k=2$)

* Row 1: $[4]$. Leftmost $>\!2$ is **4** at col 1. Replace $4\to 2$, **bump 4** down.
* Row 2 empty ⇒ append 4 (new box at $(2,1)$).
* $P=\big[\,[2],\,[4]\,\big]$
* $Q=\big[\,[1],\,[2]\,\big]$
* Bump path: $(1,1): 4\mapsto 2$ → append 4 to row 2.

### Step 3 (insert $5$, $k=3$)

* Row 1: $[2]$. No entry $>\!5$ ⇒ **append** 5 at $(1,2)$.
* $P=\big[\,[2,5],\,[4]\,\big]$
* $Q=\big[\,[1,3],\,[2]\,\big]$

### Step 4 (insert $1$, $k=4$)

* Row 1: $[2,5]$. Leftmost $>\!1$ is **2** at $(1,1)$. Replace $2\to 1$, bump **2** down.
* Row 2: $[4]$. Leftmost $>\!2$ is **4** at $(2,1)$. Replace $4\to 2$, bump **4** down.
* Row 3 empty ⇒ append 4 at $(3,1)$ (**new box is here**).
* $P=\big[\,[1,5],\,[2],\,[4]\,\big]$
* $Q=\big[\,[1,3],\,[2],\,[4]\,\big]$
* Bump path: $(1,1):2\mapsto1$, then $(2,1):4\mapsto2$, then append 4 to row 3.

### Step 5 (insert $3$, $k=5$)

* Row 1: $[1,5]$. Leftmost $>\!3$ is **5** at $(1,2)$. Replace $5\to 3$, bump **5** down.
* Row 2: $[2]$. No entry $>\!5$ ⇒ **append** 5 at $(2,2)$ (**new box is here**).
* $P=\big[\,[1,3],\,[2,5],\,[4]\,\big]$
* $Q=\big[\,[1,3],\,[2,5],\,[4]\,\big]$

**Final forward result**

$$
P=\begin{array}{|c|c|}
\hline 1 & 3\\\hline
2 & 5\\\hline
4\\\cline{1-1}
\end{array},
\qquad
Q=\begin{array}{|c|c|}
\hline 1 & 3\\\hline
2 & 5\\\hline
4\\\cline{1-1}
\end{array}.
$$

---

# Backward (inverse RSK: recover $\pi$)

We now go **from $k=5$ down to $1$**. At each step:

1. Find the cell with $k$ in $Q$.
2. Delete that cell in $Q$ and the corresponding cell in $P$; set $x$ to the deleted entry from $P$.
3. Move **upward**: in each previous row, find the **rightmost** entry **< $x$**, replace it by $x$, and set $x$ to the replaced value.
4. When you finish the top, the final $x$ is $\pi(k)$.

We’ll keep showing the resulting $P$ after each step.

### $k=5$

* In $Q$, **5** is at $(2,2)$. Delete that box in both $P,Q$; in $P$ it held **5**, so $x=5$.
* Go up to row 1: rightmost entry < $5$ is **3** at $(1,2)$. Replace $3\to 5$; set $x=3$.
* No more rows above → **output $\pi(5)=3$**.
* $P$ becomes $\big[\,[1,5],\,[2],\,[4]\,\big]$; $Q$ becomes $\big[\,[1,3],\,[2],\,[4]\,\big]$.

### $k=4$

* In $Q$, **4** is at $(3,1)$. Delete; in $P$ that cell had **4**, so $x=4$.
* Row 2: rightmost entry < $4$ is **2** at $(2,1)$. Replace $2\to 4$; set $x=2$.
* Row 1: rightmost entry < $2$ is **1** at $(1,1)$. Replace $1\to 2$; set $x=1$.
* Top reached → **output $\pi(4)=1$**.
* $P$ becomes $\big[\,[2,5],\,[4]\,\big]$; $Q$ becomes $\big[\,[1,3],\,[2]\,\big]$.

### $k=3$

* In $Q$, **3** is at $(1,2)$. Delete; in $P$ that cell had **5**, so $x=5$.
* No row above (we deleted from row 1) → **output $\pi(3)=5$**.
* $P$ becomes $\big[\,[2],\,[4]\,\big]$; $Q$ becomes $\big[\,[1],\,[2]\,\big]$.

### $k=2$

* In $Q$, **2** is at $(2,1)$. Delete; in $P$ that cell had **4**, so $x=4$.
* Row 1: rightmost entry < $4$ is **2** at $(1,1)$. Replace $2\to 4$; set $x=2$.
* Top reached → **output $\pi(2)=2$**.
* $P$ becomes $\big[\,[4]\,\big]$; $Q$ becomes $\big[\,[1]\,\big]$.

### $k=1$

* In $Q$, **1** is at $(1,1)$. Delete; in $P$ that cell had **4**, so $x=4$.
* No row above → **output $\pi(1)=4$**.
* $P$ becomes empty; $Q$ becomes empty.

**Recovered permutation (in order $k=1\to5$)**:

$$
\pi=(4,\,2,\,5,\,1,\,3),
$$

exactly what we started with.

---

## Tiny recap of the rules

* **Forward (bump):** in each row, replace the **leftmost** entry $>\!x$ and bump it down; if none, append $x$.
* **Record $Q$:** put the step index $k$ where the final append occurs.
* **Backward (reverse bump):** from the box labeled $k$, delete and set $x$ to that entry; going upward, replace the **rightmost** entry **< $x$** with $x$ and pass its old value upward. The final ejected $x$ is $\pi(k)$.

If you want, I can turn this exact example into a **Manim animation script** that highlights the bump path at each step and keeps $P$ and $Q$ side-by-side.

# 👉 Simultaneous Equations Solver


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


Simple tool to solve systems of equations

## ℹ️ Requirements
- Numpy (for solving using matrices)
- String (native Python module)

## 💡 How it works
- Systems of equations can be modelled as matrices in order to solve them
- The concept and example illustrated below explain the calculations that occur:

[//]: # "General Formula"
$$
A
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
= C
$$

$$
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
= A^{-1} C
$$

### Example

[//]: # "Example equations"
$$ 3x+2y-z=11 $$

$$ 2x-3y+z=7 $$

$$ 5x+y-2z=12 \\ $$


[//]: # "Example solving steps"
$$
\therefore
\begin{bmatrix}
3 & 2 & -1 \\
2 & -3 & 1\\
5 & 1 & -2
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
=\
\begin{bmatrix}
11 \\
7 \\
12
\end{bmatrix} \\
$$

[//]: # "Example solving steps contd."

$$
\therefore
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
=\
\begin{bmatrix}
3 & 2 & -1 \\
2 & -3 & 1\\
5 & 1 & -2
\end{bmatrix}^{-1}
\begin{bmatrix}
11 \\
7 \\
12
\end{bmatrix}
=\
\begin{bmatrix}
4 \\
2 \\
5
\end{bmatrix} \\
$$

### Solutions

$$ x=4 \\ $$

$$ y=2 \\ $$

$$ z=5 $$

## 👎 Limitations
- Only supports three variables at the moment
- Doesn't currently support float inputs 

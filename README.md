# Polynomial

Polynomial class in python (w/ NumPy)

- [Polynomial](#polynomial)
  - [Normal polynomials](#normal-polynomials)
    - [User defined polynomials](#user-defined-polynomials)
    - [Zeroed polynomials](#zeroed-polynomials)
  - [Abstract polynomials](#abstract-polynomials)
  - [Polynomial solutions](#polynomial-solutions)
    - [Interpolation](#interpolation)
      - [Lagrange interpolation](#lagrange-interpolation)
    - [Solving polynomials](#solving-polynomials)

## Normal polynomials

- user defined
- zeroed

### User defined polynomials

Polynomials with *specific* coefficients. That means, that the number of coefficient is finite ($\exists _{\epsilon>0}\forall_{n>\epsilon\land n \in \N} \,\,c_n=0$ but program doesn't store infinitely many zeroes. Array stops at last non-zero coefficient) and every coefficient has a value (known and saved in memory as a number).

Example being in a form of
$$
x^4+5x^3-3x+15
$$
and can be written as a product
$$
\begin{bmatrix}
    15 \\ -3 \\ 0 \\ 5 \\ 1
\end{bmatrix}\cdot
\begin{bmatrix}
    1 \\ x \\ x^2 \\ x^3 \\ x^4
\end{bmatrix}
$$
So the only information we need to store is a coefficients vector $\vec{c}$.

For the ease of use, program stores coeffixients in reversed order. This has both antvantages and disadvantages, but reversing the vector is not something hard, so ok so what.

### Zeroed polynomials

Polynomials with zeroed coefficients vector ($\vec{c}=0\Rightarrow \vec c \cdot \vec x = 0\cdot \vec x = 0$). This polynomial still has an order, so it can be used in arithmetics.
> This solution for zeroed polynomial arythmetics is not the final one will be deprecated.

## Abstract polynomials

- approximates
- user-defined
  - recursive
  - inductive
- zeroed

## Polynomial solutions

- interpolation
  - Lagrange interpolation
- solving polynomials

### Interpolation

#### Lagrange interpolation

This is pretty big. So Lagrange came up with this genius idea of [polynomial interpolation](https://en.wikipedia.org/wiki/Polynomial_interpolation):
$$
l_{n,i} = \prod_{j\neq i}\frac{x-x_j}{x_i-x_j} \\
w = \sum_{i=0}^ny_il_{n,i}(x)
$$

### Solving polynomials

Idea behind it is pretty simple. It's a combination of root-finding algorithm with polynomial division. This problem is hard mainly from the numeric perspective.

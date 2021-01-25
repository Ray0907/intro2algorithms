# Integer Arithmetic, Karatsuba Multiplication

- Irrationals
  - Catelan number
    - Set P of balanced parentheses strings are recursively defined as
      1.  λ ∈ P (λ is empty string)
      2.  If α, β ∈ P, then (α)β ∈ P
    - Every nonempty balanced paren string can be obtained via Rule 2 from a unique α, β
      pair.
    - For example, (()) ()() obtained by ( () ) ()()
  - Enumeration
    - Cn: number of balanced parentheses strings with exactly n pairs of parentheses
      C0 = 1 (empty string)
    - Cn+1 ?
    - The first Catalan numbers for n = 0, 1, 2, 3, ... are
      1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452
- Newton's method - Find root of f(x) = 0 through successive approximation e.g., f(x) = x^2 − a
  - Quadratic convergence, ] digits doubles. Of course, in order to use Newton’s method,
    we need high-precision division. We'll start with multiplication and cover division in
    Lecture 12.
- High Precision Multiplication
  - two n-digit numbers (radix r = 2, 10)
  - 0 <= x,y < r^n
  - x = x1 · r^(n/2) + x0 (x1 = high half)
  - y = y1 · r^(n/2) + y0 (x0 = low half)
  - 0 <= x0, x1 < r^(n/2)
  - 0 <= y0,y1 < r^(n/2)
  - z = x _ y =x1y1 _ r^n + (x0* y1 + x1* y0)^r(n/2) + x0 \* y0
  - 4 multiplications of half-sized #'s =⇒ quadratic algorithm θ(n^2) time
- Karatsuba's algorithm

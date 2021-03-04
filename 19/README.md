# Dynamic Programming I: Fibonacci, Shortest Paths

## Dynamic Programming (DP)

- powerful algorithmic design technique
- careful brute force
- recursion + re-use

## Fibonacci Numbers

- Naive Algorithm

      > fib(n):
      	if n ≤ 2: return f = 1
      	else: return f = fib(n − 1) + fib(n − 2)
        =>
        T(n) = T(n − 1) + T(n − 2) + O(1) ≥ Fn ≈ ϕn
      ≥ 2T(n − 2) + O(1) ≥ 2^n/2(exponential time)

- Memoized DP Algorithm

        > memo = { }
        fib(n):
        	if n in memo: return memo[n]
          if n < 2: f = 1
        	else:
          	f = fib(n − 1) + fib(n − 2)
        		memo[n] = f
        		return f

  - fib(k) only recurses first time called, ∀k
  - only n nonmemoized calls: k = n, n − 1, . . . , 1
  - memoized calls free (Θ(1) time)
  - Θ(1) time per call (ignoring recursion)
  - POLYNOMIAL
  - DP ≈ recursion + memoizatio
  - memoize (remember) & re-use solutions to subproblems that help solve problem
    - in Fibonacci, subproblems are F1, F2, . . . , Fn
  - time = # of subproblems · time/subproblem
  - Fibonacci: # of subproblems is n, and time/subproblem is Θ(1) = Θ(n) (ignore
    recursion!).

## Shortest Paths

- Recursive formulation: δ(s, v) = min{w(u, v) + δ(s, u) (u, v) ∈ E}
- Memoized DP algorithm: takes infinite time if cycles!
- works for directed acyclic graphs in O(V + E)

## Optimal Sub-structure

- DP takes the advantage of the optimal sub-structure of a problem. A problem has an optimal substructure if the optimum answer to the problem contains optimum answer to smaller sub-problems.

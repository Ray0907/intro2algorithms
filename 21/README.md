# DP III: Parenthesization, Edit Distance, Knapsack

### Parenthesization

- Optimal evaluation of associative expression A[0] · A[1] · · · A[n − 1] — e.g., multiplying
  rectangular matrices

### Edit Distance

1. subproblems: c(i, j) = edit-distance(x[i :], y[j :]) for 0 ≤ i < |x|, 0 ≤ j < |y| => Θ(|x| · |y|) subproblems
2. guess whether, to turn x into y, (3 choices)
   - x[i] deleted
   - y[j] inserted
   - x[i] replaced by y[j]
3. recurrence: c(i, j) = maximum of
   - cost(delete x[i]) + c(i + 1, j) if i < |x|
   - cost(insert y[j]) + c(i, j + 1) if j < |y|
   - cost(replace x[i] → y[j]) + c(i + 1, j + 1) if i < |x|&j < |y|
   - base case: c(|x|, |y|) = 0 => Θ(1) time per subproblem
4. topological order: DAG in 2D table
   - bottom-up OR right to left
   - only need to keep last 2 rows/columns => linear space
   - total time = Θ(|x| · |y|)
5. original problem: c(0, 0)

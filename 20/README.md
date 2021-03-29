# Dynamic Programming II: Text Justification, Blackjack

- DP ≈ **_careful brute force_**
- DP ≈ guessing + recursion + memoization
- DP ≈ shortest paths in some DAG
- time = # subproblems × time/subproblem

### 5 easy steps to DP

1. define subproblems -> # subproblems
2. guess (part of solution) -> choices of guess
3. relate subproblem solutions -> time/ subproblem
4. recurse & memoize(check subproblem recurrence is acyclic i.e. has topological order) OR building DP table bottom-up -> total time
5. solve the original problem

### Text Justification

- Split text into **_good_** lines
  - Define badness(i, j) for line of words[i : j].
    For example, ∞ if total length > page width, else (page width − total length)
  - goal: split words into lines to min P badness
  1. subproblem = min. badness for suffix words[i :]
     ⇒ # subproblems = Θ(n) where n = # words
  2. guessing = where to end first line, say i : j
     ⇒ # choices = n − i = O(n)
  3. recurrence
     - DP[i] = min(badness (i, j) + DP[j] for j in range (i + 1, n + 1))
     - DP[n] = 0
       ⇒ time per subproblem = Θ(n)
  4. order: for i = n, n − 1, . . . , 1, 0
     total time = Θ(n^2)
  5. solution = DP[0]

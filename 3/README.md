# Insertion Sort and Merge Sort

## Why sorting

- Obvious applications

  - Organize an MP3 library
  - Maintain a telephone directory

- Problems that become easy once items are
  in sorted order - Find a median, or find closest pairs - Binary search, identify statistical outliers

- Non-obvious applications
  - Data compression: sorting finds duplicates
  - Computer graphics: rendering scenes front to back

## Insertion Sort

- For i = 1,2,3....., n. Insert A[i] into sorted array A[0, L-1] by pairwise swaps down to the current position.

Running time ? theta(n^2) because theta(n^2) compares and theta(n^2) swaps
e.g. when input is A = [n, n − 1, n − 2, . . . , 2, 1]

Do a binary search on A[0: n-1] already sorted. binary search take theta(log n) time However, shifting the elements after insertion will still take theta(n) time.

Complexity: O(n logn) comparisons (n2) swaps

e.g. when input is A = [n, n − 1, n − 2, . . . , 2, 1]

## Merge sort

- divide and conquer (array A size n)
  1.  split to L = [0,1,... (n/2) -1] and R size (2/n)
  2.  sored array L' and R'
  3.  Merge array L' and R'
- theta(n) complexity

- Complexity: T(n) = C1(divide) + 2T(n/2)(recursive) + Cn(merge) = (l+ (logn)) \_Cn
  => theta(n\*logn)

## Recurrence solving

# Recitation

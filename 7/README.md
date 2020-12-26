# Counting Sort, Radix Sort, Lower Bounds for Sorting

### Comparison model

- all input items are black boxes (ADTs)
- only operation allowed are comparisons (=, <, >, >=, , =>, ....)
- time const = #comparisons

### Decision tree

- any comparison algorithm can be viewed as a tree of all possible comparisons and their outcomes, and resulting answer. for any particular n
- e.g. binary search

| decision tree      |          algorithm          |
| ------------------ | :-------------------------: |
| internal node      | binary decision(comparison) |
| leaf               |        found answer         |
| root-to-leaf       |      algorithm execute      |
| path leagth(depth) |        running time         |
| heigth of tree     |   worst-case running time   |

### searching lower bound

- n preprocessed items
- finding a given item among them in comparison model requires lg(n) in worst case.
- Proof
  - decision tree is binary and must have >= n leaves, one for each answer => height >= lg(n)
- Sorting lower bound
  - decision tree is binary and # leaves >= # possible answers = n! => height >= lg(n!)

### linear time sorting (integer sorting)

- assume n keys sorting are integers {0, 1, 2,..., k-1} and each fits in a word
- can do a lot more than comparisons
- for k= n^O(1) you can sort O(n) time

### counting sort

    L = array of k empty lists
    > for j in range(n):
        L[key(A[j])].append(A[j])
    output = []
    for i in range(k):
        output.extend(L[i])

- O(n +k)

### radix sort

- imagine each integer as base b => # digits = d = logb (k) digits ∈ {0, 1, . . . , b − 1}
- sort (all n items) by least significant digit
- sort by most significant digit
- sort by digit using counting sort O(n+b)
- Total time O((n+b)\* d) = O(n+b logb(k))
- min when b = O(n) => O(nlogn(k))
- if k <= n^c then O(nc)

### Recitation

| Sorting        | Omega(n) | stability |
| -------------- | :------: | :-------: |
| insertion sort |  O(n^2)  |  stable   |
| merge sort     | O(n lgn) |  stable   |
| heap sort      | O(n lgn) | unstable  |
| counting sort  |  O(n+k)  |  stable   |
| radix sort     |   O(n)   |  stable   |

- comparison model : at least Omega(n lgn)
- sort stability: A sorting algorithm is stable if elements with the same key appear in the output array in the same
  order as they do in the input array

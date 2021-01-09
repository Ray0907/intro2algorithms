# Heaps and Heap sort

## Priority queue

- implements a set S of elements, each of element associated with a key.
  - insert(S, x): insert element x into set S.
  - max(S): return element of S with the largest key.
  - extract_max(S): return element of S with the largest and remove it from S.
  - increase_key(S, x, k): increase the value of x's key to the new value k.

## Heap

- An array, visualized as a nearly complete binary tree

### Heap as a tree

- root of tree: first element in the array, corresponding to i = 1
- parent(i) =i/2: returns index of node's parent
- left(i)=2i: returns index of node's left child
- right(i)=2i+1: returns index of node's right child

### Max-heap property

- the key of a node is >= the keys of its children.

### Min-heap property

### Heap operations

- build_max_heap: produced a max heap from an unordered array.

- max_heapify: correct a single violation of the heap property in a subtree's root.

[heap](https://github.com/Ray0907/intro2algorithms/blob/master/4/static/heap.png)

>

    // Max_heapify(A, i): Assum    that the tree rooted at le     (i) and right(i) are ma       heaps.
    > Max_heapify(A, 2);
    > heap_size = 10
    > Exchange A[2] with A[4]
    > Call Max_heapify A[4]
    > Exchange A[4] with A[8]
    > no more call
    > time max_heapify O(lg n)

    // Max_Heapify Pseudocode
    l = left(i)
    r = right(i)
    if (l <= heap-size(A) and A[l] > A[i])
        then largest = l else largest = i
    if (r <= heap-size(A) and A[r] > A[largest])
        then largest = r
    if largest = i
        then exchange A[i] and A[largest]
            Max_Heapify(A, largest)

### Build_Max_Heap

- Converts A[1…n] to a max heap

  >

      Build_Max_Heap(A):
          for i= n/2 downto 1
              do Max_Heapify(A, i)

- Why start at n/2?
  - Because elements A[n/2 + 1 … n] are all leaves of the tree
    2i > n, for i > n/2 + 1
- O(n log n)

- Observe Max_Heapify takes O(1) for nodes that are one level above the leaves and in general O(l) time for nodes that are l level above the leaves.
- n/4 nodes with level 1, n/8 with level 2 and so on till we have one root node that is lg n levels
  above the leaves.

- Total amount of work in the for loop can be summed as:
  n/4 (1 c) + n/8 (2 c) + n/16 (3 c) + … + 1 (lg n c)
- Setting n/4 = 2k
  and simplifying we get:
  c 2^k
  ( 1/2^0* 2/2^1* 3/2^2\* … (k+1)/2^k) (The term is brackets is bounded by a **\_constant!**)
- This means that Build_Max_Heap is O(n)

### Heap-Sort

- Build Max Heap from unordered array
- Find max element A[1]
- swap elements A[n] with a[i], now max element is at the end of the array.
- Discard node n from heap (decreasing heap size)
- New root may violate max heap property, but its
  children are max heaps. Run max_heapify to fix this

- Go to Step 2 unless heap is empty

- Running time:
  after n iterations the Heap is empty
  every iteration involves a swap and a max_heapify
  operation; hence it takes O(log n) time

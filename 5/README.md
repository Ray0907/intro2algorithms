# Binary Search Trees, BST Sort

- Runway reservation system

  - Airport with a single runway

    - Reservations for future landing
    - Reserve request specifiy landing time t
    - Add t to the set R if no other landings are scheduled within k minutes.
    - Remove from set R after plane lands.
    - |R| = n
    - O(lg n)
    - Unsorted list/ array
    - Insert in O(1) without check , check taken O(n) time

    - Sorted list: Appending and sorting takes Θ(n lg n) time. However, it is possible to insert new time/plane rather than append and sort but insertion takes Θ(n) time. A k minute check can be done in O(1) once the insertion point is found.
    - Sorted array: It is possible to do binary search to find place to insert in
      O(lg n) time. Using binary search, we find the smallest i such that R[i] ≥ t,
      i.e., the next larger element. We then compare R[i] and R[i − 1] against t.
      Actual insertion however requires shifting elements which requires Θ(n) time.
    - Unsorted list/array: k minute check takes O(n) time.
    - Min-Heap: It is possible to insert in O(lg n) time. However, the k minute
      check will require O(n) time.
    - Dictionary or Python Set: Insertion is O(1) time. k minute check takes
      Ω(n) time

    - key Lesson: Need fast insertion into sorted list.

- Binary search Tree

  - properties: Each node x in the binary tree has a key key(x). Nodes other than the root have a parent p(x). Nodes may have a left child lef t(x) and/or a right child right(x). Theseare pointers unlike in a heap.
    The invariant is: for any node x, for all nodes y in the left subtree of x, key(y) ≤
    key(x). For all nodes y in the right subtree of x key(y) ≥ key(x).
    ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/5/bst.png)

    - new requirement: Rank(t): How many planes are scheduled to land at times ≤ t? The new requirement
      necessitates a design amendment.
      ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/5/bst_1.png)

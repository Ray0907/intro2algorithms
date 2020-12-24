# AVL Trees, AVL Sort

### Recall: Binary Search Trees (BSTs)

- rooted binary tree
- each node has
  - key
  - left pointer
  - right pointer
  - parent pointer
  - height of the tree = length (# edges) of longest downward path to a leaf
  - height of a node = length of the longest path from it down to a leaf = max{height(right child), height(left child)} + 1

### AVL trees

- require heights of left and right child of every node to differ by at most +-1

- AVL trees are balanced:
  - worst case is when right sbutree has height
    1 more than left for every node.
- AVL insert
  - simple BST insert
  - ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/6/avl_insert_ex1.png)
  - ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/6/avl_insert_ex2.png)
  - ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/6/avl_rotation.png)
  - ![]
  - fix AVL property
- if x's right child is right-heavy or balanced

- AVL sort

  - Insert n items Θ(lg n)
  - in-order traveral Θ(n)

- Abstract data type
  - insert & delete
  - min
  - successor / predecessor

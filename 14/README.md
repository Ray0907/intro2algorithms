# Depth-First Search (DFS), Topological Sort

- Depth-First Search
  - recusively explore graph, backtracking as necessary.
  - Depth First Search Algorithm
    - follow path until you get stuck
    - backtrack along breadcrumbs until reach unexplored neighbor
    - recursively explore
    - careful not to repeat a vertex
- Edge Classification
  - tree edge(parent pointer) visit new vertex via edge
  - forward edge: node -> descendant in tree
  - backward edge: node -> ancestor in tree
  - cross edge: between two non ancestor-related subtrees.
- Cycle Testing
  - Graph G has a cycle <=> DFS has a back edge
- Job scheduling
  - Given Directed Acylic Graph (DAG), where vertices represent tasks & edges represent
    dependencies, order tasks without violating dependencies
- Topological Sort

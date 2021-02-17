# Single-Source Shortest Paths Problem

- Weighted Graphs
- General Approach
- Negative Edges
- Optimal Substructure

## Motivation

- Shortest way to drive from A to B Google maps "get directions"
- Formulation: Problem on a weighted graph G(V, E, w) V: vertex, E: edge W: weight. W, E -> R
- Two algorithms
  - Dijkstra O(V lg V + E) : non-negative edge weights
  - Bellman Ford O(V E) is a general algorithm
- Weighted Graphs
  v0 -- p --> vk means p is a path from v0 to vk . (v0 ) is a path from v to v of weight 0

## Negative-Weight Edges

- Natural in some applications (e.g., logarithms used for weights)
- Some algorithms disallow negative weight edges (e.g., Dijkstra)
- If you have negative weight edges, you might also have negative weight cycles -> may make certain shortest paths undefined!

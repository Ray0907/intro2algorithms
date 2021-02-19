# Dijkstra

- d[v] is the length of the current shortest path from starting vertex s. Through a
  process of relaxation, d[v] should eventually become δ(s, v), which is the length of the
  shortest pathfrom s to v. Π[v] is the predecessor of v in the shortest path from s to
  v
- Basic operation in shortest path computation is the **_relaxation operation_**

      > RELAX(u, v, w)
      	if d[v] > d[u] + w(u, v)
      		then d[v] ← d[u] + w(u, v)
      			pi[v] ← u

- Relaxation is Safe

  - Lemma: The relaxation algorithm maintains the invariant that d[v] ≥ δ(s, v) for all v ∈ V
  - Proof: By induction on the number of steps.
    - Consider RELAX(u, v, w). By induction d[u] ≥ δ(s, u). By the triangle inequality, δ(s, v) ≤ δ(s, u) + δ(u, v). This means that δ(s, v) ≤ d[u] + w(u, v), since
      d[u] ≥ δ(s, u) and w(u, v) ≥ δ(u, v). So setting d[v] = d[u] + w(u, v) is safe.

- DAGs(Directed Acyclic Graph)

  - is a directed graph with no directed cycles
  - Can't have negative cycles because there are no cycles!
  - Topologically sort the DAG. Path from u to v implies that u is before v in the
    linear ordering.
  - One pass over vertices in topologically sorted order relaxing each edge that leaves each vertex. Θ(V + E) time

- Dijkstra’s Algorithm - For each edge (u, v)  E, assume w(u, v) ≥ 0, maintain a set S of vertices whose final shortest path weights have been determined. Repeatedly select u  V − S with
  minimum shortest path estimate, add u to S, relax all edges out of u.

      > Pseudo-code
      	Dijkstra (G, W, s) //uses priority queue Q
      		Initialize (G, s)
      		S ← φ
      		Q ← V [G] //Insert into Q
      		while Q = φ
      			do u ← EXTRACT-MIN(Q) //deletes u from Q
      			S = S ∪ {u}
      			for each vertex v  Adj[u]
      				do RELAX (u, v, w) ← this is an implicit 		DECREASE KEY operation

- Dijkstra Complexity
  - Θ(v) inserts into priority queue
  - Θ(v) EXTRACT MIN operations
  - Θ(E) DECREASE KEY operations
  - array impl
    - Θ(v) time for extra min
    - Θ(1) for decrease key
    - Total: Θ(V.V + E.1) = Θ(V
      ^2 + E) = Θ(V^2)
  - Binary min-heap
    - Θ(lg V ) for extract min
    - Θ(lg V ) for decrease key
    - Total: Θ(V lg V + E lg V )
  - Fibonacci heap
    - Θ(lg V ) for extract min
    - Θ(1) for decrease key
    - amortized cost Total: Θ(V lg V + E)

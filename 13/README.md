# Breadth-First Search

- graph search
  - explore a graph
- Recall
  - Graph G = (V, E)
  - E = set of edges i.e. vertex pairs (v, w)
    - ordered pair => directed edge of graph
    - unordered pair => undirected
- applications

  - web crawlering
  - social networking
  - network broadcast
  - garbage collection
  - model checking
  - checking mathematical conjectures
  - solving puzzles and games

- pocket cube

  - Consider a 2 2 2 Rubik’s cube - vertex for each possible state - edge for each basic move (e.g., 90 degree turn) from one state to another - undirected: moves are reversible - vertices = 8! · 3^8 = 264, 539, 520 where 8! comes from having 8 cubelets in arbitrary positions and 3^8 comes as each cubelet has 3 possible twists.

- Graph Representations (data structures)
  - Adjacency lists
    - Array Adj of |V| linked lists
    - for each vertex u ∈ V, Adj[u] stores u's neighbors => {u ∈ v | (u, v) ∈ E}
  - object-oriented
    - u.neighbors = Adj[u]
  - implicit representation
    - Adj[u] is a function
    - v.neighbors() is a method
- Breadth-First Search

  - visit all nodes reachable from given s ∈ V
  - O(V + E) time
  - look at nodes reachable in O moves, 1 moves, 2 moves ...
  - careful to avoid duplicated.

- Breadth-First-Search Algorithm

        BFS (V,Adj,s) # See CLRS for queue-based implementation

        	level = { s: 0 }
        	parent = {s : None }
        	i = 1
        	frontier = [s] # previous level, i − 1
        	while frontier:
        		next = [ ] # next level, i
        		for u in frontier:
        			for v in Adj [u]:
        				if v not in level: # not yet seen
        				level[v] = i ] = level[u] + 1
        				parent[v] = u
        				next.append(v)
        		frontier = next
        		i + =1

- shortest path
  - for every vertex v, fewest edges to get from s to v is
    - level[v] if v assigned level
    - ∞ else
  - parent pointers form shortest-path tree = union of such a shortest path for each v
    - to find shortest path, take v, parent[v], parent[parent[v]], etc., until s (or None)

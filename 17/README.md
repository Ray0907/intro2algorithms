# Bellman-Ford

    > Bellman-Ford
    	Initialize()
    	for i = 1 to |V| -1
    		for each edge(u, v) ∈ E
    			Relax(u, v)
    		for each edge(u, v) ∈ E
    			do if d[v] > d[u] + w(u, v)
    				then report a negative-weight cycle exists

- Theorem: If G= (V, E) contains no negative weight cycle, then after Bellman-Ford executes d[v] = δ(s, v) for all v ∈ V .

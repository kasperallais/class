# Dijkstra's Algorithm
- The principle behind Dijkstra's algorithm is that if s, ..., x, ..., t is a shortest path from s to t, then s, ..., x had better be a shortest path from s to x
- Proof Contradiction
    - Shorter path from s to x
    - Would imply shorter path from s to t
- Edges must have non-negative weights
- A lot like BFS except that instead of using a simple queue, we use a priority queue based on the distance from the source
- Initialization
    - Set each d[v] = inf (except d[s] = 0)
    - Set each parent[v] to nil
- Output 
    - parent [v] is v's parent in "shortest path tree"
    - d[v]: shortest path distance from s

# Dijkstra's Pseudocode

	S = { } // Visited processed nodoes
	Q = V[G] // Q is min PQ on distance
	while (Q not empty)
		u = Extract-Min(Q)
		S = S ∪ {u} // Add to processed
		for each vertex v adjacent to u // Relax
			if d[v]>d[u]+w(u,v)
				d[v] = d[u] + w(u, v) //Decrease Key
				parent[v] = u

# Breaking down Extract-Min
- Store data in a min priority queue
	- An abstract data type that supports
		- Insert
		- Extract-Min
		- Decrease-Key

# Iterations
- Iteration 1
	- Q = (A,0), (B,inf), (C, inf) S = null
- Iteration 2
	- Q = (B,5), (F,12), (G,7), ... S = {(A,0)}
- Iteration 3
	- Q = (G,7), (F,12), (C,12), ... S = {(A,0),(B,5)}
- Iteration 4
	- Q = (F,11), (C,11), (E,10), ... S = {A,B,G}
- Iteration 5
	- Q = (F,11), (C,11), (D,12), ... S = {A,B,E,G}
- Iteration 6
	- Q = (F,11), (D,12), ... S = {A,B,C,E,G}
- Iteration 7
	- Q = (D,12), ... S = {A,B,C,E,F,G}

# Runtime
- Initializing Q: Cost of creating PQ - could be cost of n insertions
- n iterations of while loop, so n Extract-Min calls
- Aggregate (like BFS) m iterations of inner for loop
- At most m RELAX ops, so at most m Decrease-Key calls
- Runtime influenced by the implementation of the priority queue

# Heaps Review - Min Heap
- A binary heap is defined to be a binary tree with a key in each node such that

# Minimum Spanning Tree
- A tree is a connected graph with no cycles
- A spanning tree is a sub graph of G which has the same set of vertices of G and is a tree
- A minimum spanning tree of a weighted graph G is the spanning tree of G whose edges sum to minimum weight

# Greedy Algorithms
- In greedy algorithms, we make the decision of what next to do by selecting the best local option from all available choice - without regard to the global structure
- To use a greedy algorithm the problem must:
    - Satisfy the greedy choice property: a globally optimal solution can be achieved from ALWAYS making the locally optimal choice
    - Exhibit the optimal substructure: Solution to the larger problem can be built from solutions to its sub problems

# Prim's Algorithm Pseudocode

    Prim-MST (G)
        select an arbitrary vertex s to start the tree from
        while (there are still non-tree veritices)
            select min wt edge between tree and non-tree vertex
            add selected edge and vertex to the tree T_prim

# MST-PRIM (G, w, r)

    for each vertex u ∈ G.V
        key[u] = ∞
        parent[u] = NIL
    key[r] = 0
    Q = Ø
    for each vertex u ∈ G
        INSERT(Q, u)
    while Q ≠ Ø
        u = EXTRACT-MIN(Q)
        for each vertex v adjacent to u
            if v ∈ Q and w(u, v) < key [v]
                parent[v] = u
                key[v]= w(u, v)
                DECREASE-KEY(Q, v, w(u, v))

# Kruskal's Algorithm
- Kruskal's algorithm is also greedy
- It repeatedly adds the smallest edge to the spanning tree that does not create a cycle


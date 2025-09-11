# Shortest Paths in Unweighted Graphs
- In an unweighted graph, the cost of a path is just the number of edges on the shortest path, which can be found in O(n+m) time via BFS

# Shortest Paths in Weighted Graphs
- The length of a path between two vertices is the sum of the weight of the edges on a path
- BFS will not work on weighted graphs because sometimes visiting more edges can lead to shorter distance
- There can be an exponential number of shortest paths between two nodes - so we cannot report al shortest paths efficiently

# Terminology: Relaxing an Edge
- Relaxing an edge(u,v) means testing if the shortest path to v SO FAR contains the vertex u

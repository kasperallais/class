Terminology
- G(V,E) - G represents the Graph that is composed of the vertex set, V, and the edge set, E
- Sparse Graph - Many more vertices than edges
- Dense Graph - Lots of edges (i.e. the number of edges is approaching V^2 where V is the number of vertices)
Big-O Notation for Space Complexity
- Big-O notation for space complexity measures the maximum memory or storage required by an algorithm as a function of the input size n
- Includes Both Fixed and Dynamic Space
- Space complexity is usually analyzed for the worst-case input scenario to provide an upper bound
- Reminder: Big-O notation represents an upper bound
Big-O Notation for Time Complexity
- Big-O notation for time complexity quantifies the maximum number of operations an algorithm performs as a function of the input size 
- Describes how the runtime grows as the input size, increases, constant factors and lower-order terms
- Time complexity typically evaluates the worst-case performance to provide an upper bound on execution time
Traversing Graphs
- One of the most fundamental graph problems is to traverse every edge and vertex in a graph
- For efficiency, we must make sure we visit each edge at most twice
- There are two primary traversal algorithms: breadth-first search (BFS) and depth-first search (DFS)
- Breadth-first search is appropriate if we are interested in shortest paths on unweighted graphs

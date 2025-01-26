# The One Queue
- All these search algorithms are the same except for fringe strategies
    - Conceptually, all fringes are priority queues
    - Partially, for DFS and BFS, you can avoid the log(n) overhead from an actual priority queue, by using stacks and queues
    - Can even code one implementation that takes a variable queuing object

# Uniform Cost Search
- Strategy: Expand lowest path cost
- The good: 
    - UCS is complete and optimal
- The bad:
    - Explores options in every "direction"
    - No information about goal location

# Search Heuristics
- A heuristic is:
    - A function that estimates how close a state is to a goal
    - Designed for a particular search problem

# Greedy Search
- Strategy: Expand a node that you think is the closest to the goal state
    - Heuristic: Estimate of distance to nearest goal for each state
- A common case:
    - Best-first takes you straight to the (wrong) destination
- Worst-case: like a badly-guided DFS

# Admissible Heuristics
- A heuristic h is admissible (optimistic) if:
    - 0 <= h(n) <= h^*(n)
    - where h^*(n) is the true cost to the nearest goal
- Coming up with admissible heuristics is most of what's involved in using A* in practice

# Properties of A*
- Complete? Yes, unless there an infinite nodes with f<=f(G)
- Time cost? Exponential in [relative error in h x length of solution]
- Space Usage? All nodes kept in memory (exponential)
- Optimal? Yes

# Intuition for A*
- Search often explore narrowly around 'straight line' path
    - Performs well when actual path matches heuristics
    - Get around small detours easily
- May explore large space w/ poor heuristics or long detours
- Implication
    - Not real time!
    - Normally fast, sometimes slow

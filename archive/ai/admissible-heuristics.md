# A* Applications
- Video games
- Pathing / routing problems
- Resource planning problems
- Robot motion planning

# Trivial Heuristics, Dominance
- Dominance: h_a > h_c, if
    - for all n: h_a(n) >= h_c(n)
- Heuristics for a semi-lattice
    - Max of admissible heuristics is admissible
    - h(n) = max(h_a(n), h_b(n))
- Trivial Heuristics
    - Bottom of lattice is the zero heuristic
    - Top of lattice is the exact heuristic

# Graph Search & Duplicate Noes
- Idea: Never expand a state twice
- How to implement
    - Tree search + set of expanded states
    - Expand the search tree node-by-node, but before expanding a node, check to make sure its state has never been expanded before
    - If not new, skip it, if new add to closed set
- Important: Store the closed set as a set not a list

# Consistency of Heuristics
- Main idea: estimated heuristic costs <= actual costs
    - Admissibility: heuristic cost <= actual cost to goal
        - h(A) <= actual cost from A to G
    - Consistency: heuristic "arc" cost <= actual cost for each arc
        - h(A) - h(C) <= cost (A to C)
- Consequences of consistency
    - The f value along a path never decreases
        - h(A) <= cost(A to c) + h(C)
    - A* graph search is optimal

# Optimality 
- Tree search
    - A* is optimal if heuristic is admissible
    - UCS is a special case
- Graph search
    - A* optimal if heuristic is consistent
    - UCS optimal (h=0 is consistent)
- Consistency implies admissibility
- In general, most natural admissible heuristics tend to be consistent, especially if from relaxed problems

# Creating Admissible Heuristics
- Most of the work in solving hard search problems optimally is in coming up with admissible heuristics
- Often, admissible heuristics are solution to relaxed problems, where new actions are available
- Inadmissible heuristics are often useful too

# Relaxed Problems
- Can derive admissible heuristics from solutions to relaxed problems
    - Start with full problem
    - Ignore some rules
    - Derive solution cost for simplified problem
- Relaxation is key to brand-and-bound algorithms

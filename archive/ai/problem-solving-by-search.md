# Reflex Agents
- Choose action based on current percept (and maybe memory)
- May have memory or a model of the world's current state
- Do not consider the future consequences of their actions
- Consider how the world IS
- Can a reflex agent be rational? Depends on the problem

# Planning Agents
- Ask 'what if'
- Decision based on consequences of actions
- Must have a model of how the world evolves in response to actions
- Must formulate a goal
- Consider how the world WOULD BE
- Optimal vs. Complete Planning
- Planning vs. Replanning
    - Open Loop vs. Closed Loop

# Search Problems
- A search problem consists of:
    - A state space
    - A successor function
    - An (additive) path cost
    - A start state and a goal test
- Specification
    - Problem = (successor fun, path cost, start state, goal test)
- A solution is a sequence of actions which transforms the start state to a goal state

# Search Problems are Models
- You cannot include everything, you have to approximate

# What's in a State Space
- The world state includes every last detail of the environment
- A search state keeps only the details needed for planning (abstraction)
- Problem: Pathing
    - States: (x,y) location
    - Actions: NSEW
    - Successor: Update Location Only
    - Goal Test: is (x,y)=END
- Problem: Eat-All-Dots
    - States: {(x,y), dot booleans}
    - Actions: NSEW
    - Successor: update location and possibly a dot boolean

# State Space Graphs and Search Trees
- State Space Graph: Abstraction of how state can change
    - States are unique and cycles exist
- Search Tree: Represents steps of search process
    - States can repeat & no cycles

# State Space Graphs
- A mathematical representation of a search problem
    - Nodes are world configurations
    - Arcs represent successors
    - The goal test is a set of goal nodes
- In a state space graph, each state occurs only once!
- We can rarely build this full graph in memory, but it's a useful idea

# Searching with a Search Tree
- Search
    - Expand out potential plans (tree nodes)
    - Maintain a fringe of partial plans under consideration
    - Try to expand as few tree nodes as possible

# General Tree Search
- Important Ideas:
    - Fringe
    - Expansion
    - Exploration Strategy

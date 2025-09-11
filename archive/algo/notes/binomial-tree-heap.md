# Binomial Trees
- B_k is degree k binomial tree

# Binomial Heap
- A binomial heap is a collection of binomial trees each of which satisfies the min-heap priority
- Key properties:
    - A binomial heap is a forest of binomial trees
    - A binomial heap contains at most one binomial tree of each order k

# Node Structure
- Degree
    - Number of children
- Child
    - Pointer to one of the node's children
    - Null iff node has no child
- Sibling
    - Used for circular linked list of siblings
- Data

# Homework Note
- Proof by Induction

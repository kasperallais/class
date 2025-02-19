# Reductions
- Consider the following algorithm to solve Problem A using an algorithm for Problem B:
- Algorithm-For-A(X)
    - Convert X to an instance of Problem B, Y
    - Call Algorithm-For-B on Y to solve this instance
    - Return the answer of Algorithm-For-B(Y) as the answer
- Such a translation from instances of one type of problem to instances of another type such that answers are preserved is called a reduction

# Implication
- Suppose a reduction translates X to Y in O(P(n))
    - If Algorithm-For-B ran in O(Q(n)). What is the runtime for solving Problem A?
    - O(P(n)) + O(Q(n))

# Another Implication
- Reduce A to B, and A cannot be solves faster than L(n). Problem B is going to have the same kind of lower bound 
- Omega(L(n) - P(n))

# What is a hard problem?
- Intuitively a problem in in P, if it can be solved in time polynomial in the size of the input
- A problem is in NP if, given the answer, it is possible to verify that the answer is correct within time polynomial in the size of the input

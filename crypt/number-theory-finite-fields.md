# Introduction
- Will mainly introduce finite fields
- Of increasing importance in cryptography
- Concern operations on numbers

# Divisors
- Say a non-zero number b divides a if for some m have a = mb
- That is b divides into a with no remainder
- Denote this b | a
- and say that b is a divisor of a

# Properties of Divisibiltiy
- If a | 1, then a = +-1
- If a | b and b | a, then a = +-b
- Any b != 0 divides 0
- If a | b and b | c, then a | c
- If b | g and b | h, then b | (mg + nh)

# Integer Division Algorithm
- Divide non-negative integer a (dividend) by positive integer n (divisor) get integer q (quotient) and integer r (remainder) such that:
    - q = qn+ r where 0 <= r < n
- r is "a mod n", also referred to as a residue
- q and r are unique

# Greatest Common Divisor (GCD)
- A common problem in number theory
- gcd (a,b) of a and b is the largest integer that divides both a and b
- Define gcd(0, 0) = 0, gcd(a, 0) = |a| for a!=0
- Often want no common factors (except 1), define such numbers as relatively prime

# Euclidean Algorithm
- A simple procedure for finding d = gcd(a, b)
- gcd(|a|, |b|) = gcd(a ,b) = gcd(b, a)
- No harm to assume a >= b > 0
- Euclid(a,b)
    - if (b = 0) then return a;
    - else return Euclid(b, a mod b);



# Set Operations
- Relational database theory is based on mathematical set theory

# Set Refresher
- A set is a mathematical object that represents a collection of distinct values
- Sets can be defined by some property that values have in common, or simply by listing all of the values in the set
- The union of two sets is another set: the set containing all values that are in either set
- A union of values is related to the Boolean OR operator
- The Intersection of two sets is a set again 
- This time containing only values which appear in both of the original sets
- The intersection is the boolean AND operator

# Tables as sets
- In the original conception of relational databases, tables and the results of data retrieval queries were intended to be true sets
- For performance reasons, SQL databases allow duplicate rows in both tables and in the result of queries

# Union
- Set union in SQL is an operation on two SELECT queries
- The query is written as one SELECT query, followed by the keyword UNION, followed by another SELECT query
- The two query results must be compatible in the sense that they must both return the same number of columns, and the columns should have compatible types

    SELECT * FROM books WHERE title LIKE 'W%'
    UNION
    SELECT * FROM books WHERE publication_year = 1995;

    SELECT *
    FROM books
    WHERE title LIKE 'W%'
    OR publication_year = 1995;

- In this case, the queries return the same results
- When we use UNION, SQL treats it as a true set operation and returns a distinct set of row
- To be completely equivalent, we should use the DISTINCT keyword in the second query

# Intersection
- Set intersection is SQL is accomplished by the keyword INTERSECT

    SELECT * FROM books WHERE title LIKE 'W%'
    INTERSECT
    SELECT * FROM books WHERE publication_year = 1995;

# Set Difference
- Set difference is SQL is accomplished by the keyword EXCEPT

    SELECT * FROM books WHERE title LIKE 'W%'
    EXCEPT
    SELECT * FROM books WHERE publication_year = 1995;



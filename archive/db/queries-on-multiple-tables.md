# Simple Joins
- We start our FROM clause with table 1, then use the JOIN keyword to bring in table 2, followed by the ON keyword, and finally a Boolean condition explaining to SQL which rows from 1 go with which rows from 2.
- The boolean condition after ON is known as a join condition
- Join conditions always compare an expression on one table with an expression on another table

    SELECT *
    FROM
        s
        JOIN t on sy=ty
    ;

- Two tables can be related via multiple columns rather than just one in each table
- To join them, you would use a compound join condition using AND
- Join conditions do not have to be equality 
- JOIN clauses are considered to be sub-clauses of the FROM clause

    SELECT *
    FROM
        s
        JOIN t on sy=ty
    WHERE tz = 'blue';

# Name collisions and ambiguity
- When two columns from tables involved in a join have the same name, we say that the column names collide
- When a naming collision occurs, we cannot use the column name by itself as an expression in any part of our query, because the database will not know which table's column you mean

# Qualified names
- There is an easy way to specify a particular column in a particular table: simply give the table name first, followed by a period, or dot and then column name
- You can also use the asterisk shortcut to mean all columns in a specific table
- Such expressions using both the table name and the column name are known as qualified column names, and can be used with any database

# Aliasing
- SQL provides facilities to change the names of tables and columns within the context of a single query

    SELECT
        title,
        floor ((publication_year + 99) / 100) AS century
    FROM simple_books;
 
# Reserved names, names with spaces, or mixed-case names
- Usually, names of things are case-insensitive and do not contain spaces
- It is possible, however, to use names which are case-sensitive and which contain spaces

    SELECT 42 AS "The Answer";

- Reserved names may also need to be put inside double quotes when used as column or table names

# Identity columns
- If we want to make a connection between data in one table and data in another using a join, we need the tables to share some data elements in common
- For some types of data, some element of the data is unique for every possible data item and can be used as an identifier for the data in a database

# Table relationships
- One of the strengths of relational database compared to earlier database systems is that relationships are not explicitly stored in the database
- One important advantage of the relational approach is that you can easily express queries concerning relationships which were not anticipated by the designer of the database

# One-to-one
- One-to-one describes a relationship between two types of data
- If we think of each data type as having it's own table, then each row in one table has a well-defined relationship with at most one row in the other table, and vice versa
- Sometimes each row in a table has exactly one corresponding row in the other table

# One-to-many
- One-to-many refers to the case when rows in one table correspond to some number of rows in another table, but rows in the second table only correspond to at most one row in the first table

# Many-to-many
- Many-to-many implies that rows in one table may correspond to multiple rows in the other table

# Inner and outer joins
- When relational database programmers use the word 'join' without any qualifiers, they almost always mean the type of join we have been describing above, in which the result only contains rows that match on both sides of the join
- This type of join is more formally known as an inner join
- There are three types of outer join: left, right, and full
- These are implemented with key phrases LEFT [OUTER] JOIN, RIGHT [OUTER] JOIN, and FULL [OUTER] JOIN
- In an outer join, all rows from one or both tables are returned, depending on the type of outer join
- In a left outer join, all the rows from the table on the left-hand side of the LEFT JOIN key phrase are returned, but only matching rows are returned from the right-hand side table
- RIGHT JOIN does the opposite, while FULL JOIN returns all rows from both tables involved in the join

# Implicit join syntax
- The ability to do inner joins existed in SQL long before the JOIN keyword and related key phrases
  
    SELECT * FROM s, t
    WHERE sy = ty;


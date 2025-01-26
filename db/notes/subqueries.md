# Subqueries
- A subquery is simply a SELECT query enclosed with parentheses and nested within another query or statement
- This subquery expression evaluates to a scalar, a row, a column, or a table, depending on the query results and the context in which the subquery appears

# Scalars, rows, and tables
- Scalar values are simple values of a single type, such as 42 or 'hello'
- We can also work with row values in SQL
- A row is just an ordered list of values
- We can write down a literal row by putting a comma-separated list of expression between parentheses

    (1, 'hello', 3.1415)

- Rows can be used in comparison expression
- Beyond rows, we can also think in terms of tables as values

# Boolean expressions using subqueries
- We can use a subquery in place of a scalar expression as long as we know the subquery will return a single row and column
- If multiple rows are returned by the subquery, the query will result in an error
- However, if zero rows are returned from the subquery, the result is considered to be NULL, rather than an error

    SELECT * FROM book
    WHERE (author_id, publication_year) =
        (SELECT author_id, publication_year
        FROM books
        WHERE title = 'The Hundred Thousand Kingdoms')
    ;

# Table of Column result
- When a query can return multiple rows, we have a different set of operators to work with

# IN
- The IN operator lets us compare some expression to every row returned from a subquery
- If the expression equals any result from the subquery, then the IN expression evaluates to True
- SQL also provides the NOT IN operator as simply the Boolean inverse of IN

    SELECT * FROM books WHERE book_id NOT IN
        (SELECT book_id FROM books_awards)
    ;

- The IN operator also works with row expression, when we want to compare against multiple column subquery results
- IN also has a useful application that does not involve subquery
- If we follow IN with a comma-separated list of expression inside parentheses, the operator will test the expression to the left of IN against every expression listed in the parentheses

# ALL, ANY, and SOME
- We can alternately use comparison operators in conjunction with the ALL or ANY or SOME keywords to compare an expression against the results of a subquery

    SELECT * FROM books WHERE book_id = ANY
        (SELECT book_id FROM books_awards);

- SOME is just a synonym for ANY
- The IN operator when used with subqueries is equivalent to = ANY
- In contrast, ALL requires that every row returned the subquery passes the comparison test
- The NOT IN operator is equivalent to <> ALL

# Use in statements
- Subqueries do not have to be used only within other SELECT queries
- The use of subqueries within the WHERE clause of DELETE and UPDATE statements can be very powerful, often making up for the fact that we cannot do joins within those types of statements

    DELETE FROM authors
    WHERE author_id NOT IN
        (SELECT author_id FROM books);

# Correlated subqueries
- It is possible to contruct subqueries that are dependent on the outer query
- When a subquery references some attribute from the outer query in an expression, we say that the subquery is correlated with the outer query

# EXISTS
- The EXISTS operator precedes a subquery which is the only operand
- An EXISTS expression evaluates to true only if the subquery returns one or more rows
- The actual data from the subquery is ignored, so you can put anything you want in the SELECT clause

# Subqueries in other clauses
- Subqueries returning scalars can be useful in SELECT clauses and in the SET clauses of UPDATE statements
- Subqueries returning tables can also be used in place of named tables in the FROM clause of a SELECT clause.

# SET
- Used in the SET clause of an UPDATE statement, subqueries provide a way to work around the issue that we cannot use joins in an UPDATE
- If we want ot update rows in some table with data drom a second table, we can simply use a subquery to obtain the proper value

    UPDATE books
    SET publication_year =
        (SELECT MIN(publication_year)
        FROM editions
        WHERE books.book_id = editions.book_id)
    ;

# FROM
- Subqueries can also be used within the FROM clause of a select query, in which case the subquery result acts like a table containing exactly the data returned from the subquery 
- In this usage, the subquery expression must be given a name using aliasing

# Comparison with JOINS
- Subqueries are comparable to joins in the sense that they both involve multiple tables
- There are many cases in which a subquery can substitute for a join or vice-versa
- First, of course, is that short of using SELECT clause subqueries, you can only return data that actually appears in the outer query's table


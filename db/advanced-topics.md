# Views
- A view is a database object that acts as a saved SELECT query, the result of which can be queried directly as if it were a table
- The data itself is not stored; the query that the view represents must be executed each time the view is queried

    CREATE VIEW book_editions AS
    SELECT
      a.name AS author,
      b.title,
      e.publication_year,
      e.publisher,
      e.publisher_location,
      e.title AS published_title,
      e.pages,
      e.isbn10,
      e.isbn13
    FROM
      editions AS e
      JOIN books AS b ON b.book_id = e.book_id
      JOIN authors AS a ON a.author_id = b.author_id
    ;

    SELECT author, published_title, publication_year, publisher
    FROM book_editions
    WHERE title = 'The Two Towers';

- To remove a view, use the DROP VIEW statement

    DROP VIEW book_editions;

# Common Table Expressions
- CTEs let us define a SELECT query and assign it a name for use within the context of a larger SELECT query
- Multiple CTEs may be used within a query
- Unlike views, CTEs only exist for the lifetime of the query in which they are defined
- Unlike subqueries, CTEs may not be correlated with the main query
- CTEs are defined prior to the main SELECT clause, using the WITH clause
        
    WITH
      name1 AS
        (select query 1),
      name2 AS
        (select query 2),
      ...
    SELECT ...

# Window Functions
- Window functions provide a mechanism for reporting information related to some grouping of data while also listing individual rows
- In general, all aggregate functions are available as window functions, and there are additional functions that relate a row to its membership to the group

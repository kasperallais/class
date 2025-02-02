Filtering rows: the WHERE clause
- Retrieving all of the data from a table is useful, but often not what we want, especially if the table is very large
- To see just a subset of rows, we include a WHERE clause in our query
- The WHERE clause consists of the keywork WHERE followed by an expression that evaluates to true or false
- The WHERE clause is placed after the FROM clause
- 'SELECT * FROM simple_books WHERE genre = 'romance';'
Ordering data: the ORDER BY clause
- One suprising fact about relational databases is that the rows in a table are not necessarily ordered in any particular fashion
- In fact, relational DBMSes are permitted to store data in whatever fashin is most convinient or efficient, as well as to retrieve data however is most convinient
- SQL provides a mechanism by which we can put rows in order by whatever criteria we wish
- This is accomplished by the ORDER BY clause, which always comes last in any query
- The key phrase ORDER BY is followed by a comma-separated list of expressions, which must evaluate to some type that can be put in order: numbers, character strings, dates, etc.
- By default, numbers are sorted from smallest to largest, and dates from earliest to latest
- Character strings are a bit trickier, because different databases order them different
- SQLite, the dialect we are ussing, default to lexicograhic ordering on ASCII values
- Ordering is initially applied using the first expression after the ORDER BY keyword
- If any two rows are equal according to that first expressing, and there are additional expression in the ORDER BY clause, the next expression, and so forth
- '''SELECT author,title,genre
FROM simple_books
ORDER BY genre, title;'''
- 'SELECT * FROM simple_books ORDER BY publication_year DESC;'
Retrieving unique rows: the DISTINCT keyword
- Query that SELECT a subset of the column of a table can easily end up with duplicate results; this may or may not be desired
- SQL provides the keyword DISTINCT, that can be added after the SELECT keyword and tells SQL that we only want unique results, and if there are any duplicateas, it should discard them
- 'SELECT DISTINCT genre FROM simple_books'

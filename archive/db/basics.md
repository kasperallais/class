Databases and Database Systems
- Database - an organized collection of data
- Database Management System (DBMS) - The software that manages the storage of data in a database and provides facilities for searching, retrieving, and modifying data in a database
- The word "database" is frequently used as a shorthand to mean both a database and the DBMS managing it
Tables
- While relational databases can contain many types of objects, the object type that store data is a table
- Each table in the database has a name, which usually provides some indication of what kind of data can be found in the table
- The table structure is defined by the table's columns, each of which has a name and an associated data type
- The actual data is contained in the rows of the table; each row is one data point and has a value for each column of the table
Structured Query Language (SQL)
- An important characteristic of modern databases is that they abstract low-level operations on files, tables, indexes, and so forth into high-level requests to the DBMS
- Requests to the database are typically expressed in a query language
- Query languages are a type of programming language, but are different from most in that query languages tend to be declarative rather than imperative
- Wheras imperative languages require the prorammer to specify exactly what steps to take to perform a task, declarative languages simply describe a desired outcome
- SQL is the most popular query language for relational databases, and is an example of a declarative language
- Even though a standard exists for SQL, relational databases have slightly different implementations of the relational model
- The basic element of SQL is the statement or query
- While a distinction can be made between these two, it is common to use the terms interchangeably
Retrieving data using SELECT
- In it's simplest form, the SELECT statement can be used to retrieve all data from a table
- 'SELECT * FROM fruit_stand'
- The statement above is said to have two clauses; a clause is a part of a SQL statement, usually starting with a SQL keyword
- The two clauses in the statement above are SELECT and FROM
Retrieving specific columns
- Above, we retrived all the columns of a table, which may not be the desired result
- 'SELECT price, item FROM fruit_stand'
Creating tables and adding data
- '''CREATE TABLE fruit_stand (
    item TEXT,
    price NUMERIC,
    unit TEXT,
);'''
- As soon as you create this table, you can query it using SELECT
- However, there will not be any data in the table yet
- To add data to the table, use INSERT statements
    - 'INSERT INTO my_purchase VALUES ('apple', 2, 6.98);'
SQL statement rules and conventions
- SQL statements are properly terminated by semicolons
- In some software tools, single statements are allowed to be unterminated
- To some extent, the name of things also act as if they are case-insensitive
Comments
- SQL provides for two types of comments, which we will occasionally use to annotate queries in this book
- Any text between /* and */ forms a multi-line comment
- Single-line comments start with two dashes


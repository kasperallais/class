Data Types
- The SQL standard defines several basic data type with which columns can be associated
- While most of the basic types exist in all relational database systems, actual implementatoin of the types varies quite a bit
- Most database systems defined addional, non-standard type for various uses
- Unusually, SQLite is dynamically typed, and you can store values of any type in any column no matter how the column is defined
- For all those reasons, you will want to consult your database system's documentatoin to understand the types available to you
Numbers
- SQL provides support for several different types of numbers, each with different applications and limitations
Integers
- SQL defines three integer types: INTEGER, SMALLINT, and BIGINT
Exact decimal numbers
- Decimal number types allow for exact storage of numbers that have digits to the right of the decimal point
- These are exact and permit exact mathematical operations where possible
- The two defined types for SQL are NUMERIC and DECIMAL, which are synonyms of each other
- These types may be defined with parameters representing precision and scale, where precision is the number of significant digits that can be stored, and scale is the number of digits following the decimal point
Floating point numbers
- Floating point numbers allow for possibly inexact storage of real numbers, similar to the IEE 754 specification
- The SQL standard defined the types FLOAT, REAL, and DOUBLE PRECISION
Character String Types
- The type CHARACTER is used for fixed-length strings
- The type CHAR is followed by parentheses enclosing the length of the string
- All values in a column of type CHAR(4), must contain exactly 4 characters
- Attempting to store strings longer than n usaully results in an error
- CHARACTER VARYING is usually abbreviated as VARCHAR, and is used for strings of varying length up to some maximum, which must be specified just as with the CHAR type
- One disadvantage to VARCHAR is the need to predict the maximum length of string that you might need to store
- Many databases now implement some type of arbitrary length charcter string type, often named TEXT
Date and time types
- Management of date and time data is a very complicated affair
- Calendars change over time and differ among cultures, time zones vary geographically, and "leap" adjustments to the calendar and clock occur irregularly
- SQL provides very robust date and time storage types along with operations on these types that allow for very precise storage and management of these values
- There is no standard syntax for date and time literals in SQL
- Using this format, dates can be compared which also means we can put data in order by date columns
- Time values can be trickier due to the possible inclusion of time zones, but we will avoid these complications by simply ignoring them
Additional data types
- SQL defines a boolean data type (BOOLEAN) which can store the literal values True and False,
- SQL also defines types to hold binary data
- SQL provides for user-defined types; that is, custom data types created by the database user for specific applications
Creating tables
- Once we have chosen the types for our columns, we can create a table using a CREATE TABLE statement
Creating a table from scratch
- Use the CREATE TABLE command to create a table
- ''' CREATE TABLE (
    column1 type1,
    column2 type2,
    ...
); '''
Dropping tables
- We cannot CREATE a table when it already exists
- We need to remove the object before re-creating it
- Removing an object from the database is called dropping the object, and is accomplished using the DROP statement
- 'DROP TABLE test;'
- Most database implement an extension to DROP that lets us remove the table if and only if it exists, without an error if it does not exist
- 'DROP TABLE IF EXISTS test;'
Creating a table from a query
- SELECT is essentially the same thing as a table
- The result is not named and exists only temporarily
Default and auto increments
- Table columns can be defined with additional properties that can enhance usage of the database in different ways
- Another property we can add to a column is a default expression - an expression producing a value that will be provided by the database only when we do not provide a value
- 'greeting VARCHAR(15) DEFAULT 'Hello';'
- More commonly, we will use an expression, typically calling a function of some sort
- A common usage for this is to record the date and time when a record is added to the database
- 'created_at VARCHAR(20) DEFAULT CURRENT_TIMESTAMP;'
- Default columns are also commonly used in combination with a special kind of database called a sequence, which simply generates sequential integers


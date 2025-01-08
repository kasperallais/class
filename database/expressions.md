Expressions
- An expression in SQL is a thing that can be evaluated - anything that results in a value
- Expressions are are in most clauses of a SQL query
Column Expressions
- The use of a column name in a SQL statement produces a special expression which evaluates to the value stored in that column for the current row being processed
- So when we run
- ''' SELECT *
FROM simple_books
WHERE author = 'J.R.R Tolkien' '''
- the query execution examines each row of the table simple_books in turn to evaluate the expression author = 'J.R.R Tolkien'
- This expression compared the value of the author column to the literal value 'J.R.R Tolkien' using the = operator
- If the two are the same, the overall expression evaluates to True, and the row is included in the output; otherwise, the row is excluded
Literals
- Literals are simple values expressed in a form that the database recognizes and understands
- There a only a few basic types of literals in SQL, although these can be converted to many different types within a database
    - Numbers: these are expressed in the usual fashion, for example, -1, 3.14159, 0.0008. Depending on the database, you may also be able to use numeric literals in scientific notation or other formats, for instance, 6.02e23
    - Character strings: these are strings of characters enclosed in single quotes, for example, 'apple'. If you need to express a literal character string which contains a single quote, you simply write the single quote twice; this is tricky to read, but produces the desired result
    - Boolean values: True or False. However, not all implementation of SQL support boolean values
    - Date and time values. The accepted notations for dates and times vary widely among different SQL implementations
    - The special value NULL
- You can ask for literal expressions in the SELECT clause - this is sometimes useful
Operators and functions
- SQL defines a number of useful operations in various types
- Some of these use simple operators, as in mathematical expressions, while others take the form of functions
Comparison operators
- We've already seen the equality operator used to test if some column is equal to a literal value in the WHERE clause of queries. We could instead test for inequality using the (<>) operator
- Though it is non-standard, most databases also recognize != as an inequality operators
- We can also test to see if value is less than (<), greater than (>), less than or equal to (<=), or greater than or equal to (>=) some other value
- There is also a ternary operator, BETWEEN, that tests if a value is between two other values
Mathematics
- You can expect the basic arithmetic operators to work with any numeric values: addition (+), subtraction (-), multiplication (*), and division (/) are standard
- Your database may implement others, but make sure you read the documentation for your database to ensure other operators do what you think they do 
- The SQL standard additionally provides functions for many useful mathematical operations, such as logarithms (log, ln, log10), exponentials (exp), square root (sqrt), modulus (mod), floor and ceiling (floor, ceiling or ceil), trigonometric functions (sin, cos, etc.), and more.
- You will most likely find yourself using mathematical operators in SQL if you are working with numerical data such as financial or scientific records
- The AS keyword lets us rename a column in the output of our query
Character string operators and functions
- SQL provides two very useful string operators
- The operator || is used for string concatenation
- The LIKE operator is a Boolean operator that is used almost exclusively in the WHERE clause
- LIKE provides very simple pattern matching capabilities in SQL
- A pattern is just a string that can contain regular text and special wild card characters, which can match one or many unspecified characters
- The two wild cards are %, which can match any string of zero or more characters, and _, which can match exactly one of any character 
- Normal text matches itself exactly
- In addition to these operators, SQL provides a number of useful functions that act on character strings
- The functions upper and lower convert strings to all uppercase or lowercase characters, respectively
- Not all languages distinguish between uppercase and lowercase, of course, so all these functions may not be acceptable in certain locales
- SQL also provides functions for tasks such as substring extraction or replacement, find the location of a substring, trimming white space from the front and/or back of a string, and many more
Boolean operators
- SQL provides logical operators that operate on Boolean values
- These operators are AND, OR, and NOT, which perform the logical operations that their names imply
- These logical operators allow us to build up complex Boolean expression from simple Boolean expressions to express the particular logical conditions we wanat for our WHERE clause
- For more complex expressions involving combinations of AND, OR, and NOT, we may need to use parentheses to make our meaning clear
- In SQL, NOT is applied before AND, and AND is applied before OR
Date and time operators and functions
- Date and time data are extremely important in many database applications, such as those supporting governmental or financial institutions
- SQL provides extensive functionality for managing dates and times
NULL
- In many database applications, it is sometimes necessary to record the absence of information on some aspect of a piece of data
- These notions of data entries that are not applicable or unknown are captured with a special value in SQL: NULL
- NULL values represent the absence of information
- NULL does ont tell us the reason the data is missing - whether it is not applicable or simply unknown
- If this distinction is important for your database, you will need to use extra columns to indicate the meaning of the NULL, or use some value other than NULL
- A very important consequence of this behavior is that NULL values cannot be usefully compared with anything, even other NULL values
- That is, an expression like x = NULL is never True even if x itself contains NULL
- To find out if a value is NULL or not NULL required special operators: IS NULL and IS NOT NULL
- NULL values can sometime lead us astray
- Because Boolean expressions can result in True, False, or NULL, we say that SQL has three-valued logic
Ordering and NULLs
- Given that you cannot meaningfully compare NULL with other values, what happens when we ORDER BY a column containing NULL values
- It depends on which implementation we are using
Conditional expressions
- SQL provides expressions for doing simple conditional logic
- The basic conditional expressions in SQL s the CASE expression, which comes in two forms
- In the most general form, CASE lets you specify what the expression should evaluate to depending on a list of conditions
- The CASE keyword comes first, followed by one or more WHEN clauses giving a condition and the desired result if the condition is true
- The first true condition determines the result that will be returned
- If none of the conditoins evaluate to True, then the ELSE result is used, if provided, or NULL if there is no ELSE clause
- The expression is finished with the END keyword
- Using a CASE expression would be one way to output books with their categories, although it depends on knowledge of all the possible genres in our database
- A more data-driven way would be to look up categories in another database table using a join
- Additionally, there are two functions that perform specialized conditional logic
- The COALESCE function takes a variable number of arguments
- The result of the functoin is the first non-NULL expression in the argument list, or NULL if all arguments are NULL
- Finally, the NULLIF function takes two arguments: if the arguments are equal, the function results in NULL, otherwise it results in the first argument

# Adding data using INSERT
- To add rows to a table in a database, we use a statement starting with the keyword INSERT
- In it's simplest form, INSERT lets you add a single row to a table by providing a value for each column in the table as defined

    INSERT INTO bookstore_sales
    VALUES (970, 1455, '2021-08-14', 'cash');

# Specifying columns
- Performing the insert as we did above works fine when we know for certain how a table has been defined in a database
- However, tables change over time in practice, which may result in columns appearing in a different order, or in more columns being added to the table
- If this happens, old SQL code that makes assumptions about the table structure will break

    INSERT INTO bookstore_sales (receipt_number, stock_number, date_sold, payment)
    VALUES (971, 1429, '2021-08-15', 'trade-in');

# Inserting multiple rows
- It is perfectly valid to do multiple INSERT statements to add multiple rows of data, SQL also lets you provide multiple rows in a single INSERT statement

    INSERT INTO bookstore_sales (stock_number, payment)
    VALUES
        (1444, 'credit card')
        (1435, 'cash')
        (1453, 'credit card')
    ;

# Inserting query results
- SQL also provides the capability of providing values via SELECT query

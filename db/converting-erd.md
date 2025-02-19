# Entities
- The first step in building a relational database from an ERD is creating a table from each entity in the data model

# Regular Entities
- First, decide on a name for the table
- Most attributes should be converted to columns in the new table
- Do not create columns for derived attributes, as these values are not intended to be stored
- Do not create values for multivalued columns attributes
- As with entities, you will need to decide on a name for each new column, which does not have to be the same as the attribute name
- You will also need to specify a type and any constraints for the column
- Choose a key attribute and use the column created from it as the primary key for the new table

# Weak Entities
- Weak entities are converted into table in nearly the same way as regular entities
- However, recall that a weak entity has no identifying key attribute

# Relationships
- Relationships can be handled using a few different approaches, depending on the cardinality ratio of the relationship

# Many-to-many
- Create a cross-reference table
- Given a table A and B, we create a cross-reference table with columns corresponding to the primary keys of A and B
- Each row in the cross-reference table stores one unique pairing of a primary key value from A with a primary key value from B
- Each row thus represents a single connection between one row in A with one row in B

# One-to-many
- Observing that rows on the "many" side of the relationship can be associated with at most one row from the "one" side, we can choose to capture the relationship by storing the primary key of the "one" side table in the "many" side table.

# One-to-one
- One-to-one relationships can be considered a special case of one-to-many relationships
- In most cases, it will be preferable to borrow the primary key from one table as a foreign key for the other table

# Higher arity relationships
- For relationships with three or more participants, a cross-reference table incorporating primary keys from each of the participating tables is the best choice

# Multivalued attributes
- Multivalued attributes can be used to model a few different scenarios
- In the simplest case, a multivalued attribute is used when a list of arbitrary values need to be stored, but there is no particular expectation that the values will be examined in a search of a database
- When there is a need to query the values associated with a multivalued attribute, the best choice may be to make a simple table with two columns, one for the primary key of the owning table, and one for the values themselves

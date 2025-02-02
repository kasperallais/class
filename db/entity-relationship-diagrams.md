# Entity-Relationship Diagrams
- ERDs define a graphical language for data modeling at a high level of abstraction

# Basic Model
- ERDs are concerned with entities and relationships between them
- Each of these elements and its related elements are denoted using simple shapes containing text labels and connected with straight lines

# Entities 
- Entities represent things or objects with independent existence; persons, products, and companies are some examples
- Entities act much like the "nouns" of our visual modeling language
- Entities are denoted by rectangles

# Attributes
- Entities are further described by their properties, or attributes
- Attributes are denoted by ovals and attacked to their entities with straight lines

# Keys
- Every entity has at least one attribute that uniquely identifies instances of the entity 
- ERDs allow for multiple key attributes

# Relationships
- Two or more entities may participate in a relationship
- Relationships act like the "verbs" in our modeling language

# Cardinality ratios and participation
- Cardinality ratios let us indicate the general number of instances of an entity that map to another entity on the other side of the relationship
- The cardinalities defined by the basic model are 1 and N
- A cardinality of 1 actually means "zero or one"
- A cardinality of N means "zero, one, or many 

# Participation
- An entity is said to have total participation in a relationship if every instance of the entity of the entity must be matched with instances of the other entity in the relationship
- This is shown using a double line
- An alternative to total participation, denoted using a single line, is partial participation

# Recursive relationships
- Relationships can exist between an entity and itself

# Weak entities
- When an entity is dependent on another entity of full identification, the dependent entity is called a weak entity, and we notate it using a rectangle with doubled outline
- The weak entity has only a partial, or weak key
- We also call out the relationship that the weak entity depends on for its identity, to distinguish it from any other relationships the weak entity participates in
- We call this relationship the identifying relationship, and draw it as a diamond with a doubled outline

# Composite Attributes
- The use of a composite attribute is essential in cases where our key is itself composed of multiple attributes

# Multivalued Attributes
- Some properties of entities are not simple values, but lists or sets of values

# Derived Attributes
- Entities may have important properties that we want to note on our data model, but which we would prefer to compute from other values in the data model, rather than store in our database
- We model these calculated properties using a dashed outline

# Relationship attributes
- While most attributes, are attacked to entities, we cal also attach attributes to relationships
- We do this when an attribute properly applies to a combination of entities, rather than to a single entity

# Higher-arity relationships
- While most relationships are binary, you may run into cases where you need to relate three (or more) entities

# Analysis
- A crucial first step in the design of any software is understanding the requirements of your project
    - The data domain
    - User needs
    - Data sources
    - Application Requirements

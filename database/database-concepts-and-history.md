What is data? What is a database?
- Data
    - Record
    - Measurements
    - Facts
- Database
    - Anything storing data
        - Paper records
        - "Flat" files
        - Formatted files
        - Internal storage representation for a DBMS
    - Usually implied: some kind of organization of the data
DBMS
- Database Management System
- The software that managed a database
    - Data retrieval
    - Data manipulation
    - Access
    - Security and Privacy
    - Reliability, integrity, consistency
- In casual usage, database = DBMS
Early Data Storage
- Typical approach: define application-specific fixed-length "record"
- Within the record, fixed-length "fields"
- Byte-for-byte equivalent of structure in application memory
- Store record on some storage medium
    - Punch Card
    - Paper or magnetic tape
    - Disk
Data Access
- Punch cards/tape
    - Little idea
    - Very different algorithms required
- Files on disk
    - Store records contiguously
    - If you want record n, multiply by record size to find byte offset from start of file
    - Special "index" files for fast searches of some files
Some Issues
- Record definition hard coded in software; what if definition needed to change?
    - Re-write, rebuild, test all software
    - Write special code to migrate data from old to new format
- Performance   
    - Sequential search expensive, unless you hold all data in memory
    - Could make an index -but then have to maintain index as well
- Flexible access - how do we add/insert/delete
- Application Specific
    - Hard coded for record type
    - Must write similar code over and over for different applications
Modern Databases
- Some typical properties:
    - Self-describing
    - Program-data separation
    - Storage abstraction
    - Network multi-user access
Self-Describing
- Without knowing the record structure, can you figure out what data is being stored?
- You need the record definition
Metadata
- Store structure Definitions with data
    - The metadata is store in the database catalog
    - The catalog is in the same format as any other data
        - Thus, the catalog metadata is store in the catalog
Program-Data Separation
- Programs can evolve independently of data
- Without separation, a change to definition
- Follows from self-describing
Data Abstraction
- A modern of DBMS is much like a bank - you don't get (or need) the keys to the safe
Network Multi-user Access
- Name kind of says it all
- Eliminates bottlenecks
- Requires sophisticated transaction control
    - Updates from one user should not destroy updates from another user
    - Airline ticketing example
Network databases
- Integrated Data Store
    - Graph-based storage of records
    - All records keyed with unique ID
        - Disk location computable from ID
        - Allowed fast navigation between records linked by ID
    - Later standardized as CODASYL
Hierarchical Model
- Information Management System
    - Invented at IBM
    - Created for Apollo
- Record form a tree structure
Navigational DBMS
- Network and hierarchical model are "navigational"
    - Access to records is predicated on knowing key

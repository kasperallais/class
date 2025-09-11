# Using a DBMS
- The client software can instead be a web app

# psql
- Preferred client for this class
- Command Line Interface (CLI)
- PostgreSQL specific
- Strengths:
    - Running scripts (files containing SQL commands)
    - Bulk of loading data 

# Launching psql
- Starting: command line
    - psql postgresql://<your userid>@ada.mines.edu/csci403

# Using psql
- For queries, just type in the query and end it with a semi-colon:
    SELECT *
    FROM artists;

# psql Commands
- \? - Show summary of all psql commands
- \h - Summary of SQL "commands"
- \h <command> - Documentation on <command>


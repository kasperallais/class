Searching with CMD
- 'where' will help us find files that are in our environment variable path
- To ensure we dig through all directories within that path, we can use the /R switch
Using Wildcards
- 'where /R C:\Users\student\ star.csv'
Basic Find
- 'find' is used to search for text strings or their absence within a file or files
- 'find "password" "C:\Users\student\not-passwords.txt'
- We can modify the way find searches using several switches 
- The /V modifier can change our search from a matching clause to a Not clause
- We can also use the /N switch to display line numbers for us and the /I display to ignore case sensitivity
- If we need something more specific, 'findstr' is what we need
- 'findstr' is closer to grep
Evaluating and sorting files
- Use 'comp', 'fc', and 'sort' commands
- 'comp' will check each byte withing two files looking for their differences and then displays where they start
- We can use the /A modifier if we want to see the differences in ASCII format
- The /L modifier can also provide us with line numbers
- 'fc' differs in that it will show you which lines are different, not just an individual character or byte that is different on each line
- 'sort' example: sort.exe .\file-1.md /O .\sort-1.md
- /unique flag will return only unique entries

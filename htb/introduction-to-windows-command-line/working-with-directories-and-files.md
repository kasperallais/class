Create A New Directory
- Use 'md' or 'mkdir' commands
Delete Directories
- Deleting directories can be accomplished using the 'rd' or 'rmdir' commands
- 'RD /S' will delete the contents in the directory too
Modifying
- 'move', 'Robocopy', and 'xcopy' can copy and make changes to directories and their structure
- 'move' works the same way as 'mv' in bash 
- 'xcopy' works the same way as 'cp' in bash 
- 'robocopy' is xcopy's successor built with much more capability
List Files & View Their Contents
- 'more' - view contents of a file or the results of another command printed to it one screen at a time
- 'more /S' - for files with many blank lines, crunches down blank space to a single line to make it easier to view
Sending a command output to More
- 'ipconfig /all | more'
Simple File Output
- 'type' - shows file output as a single line
- 'type passwords.txt >> secrets.txt' - redirect output from type into another file
Create and modify a file
- Several options - echo, fsutil, ren, rename and replace
Echo to Create and Append Files
- 'echo Check out this text > demo.txt' - Write to file (overwrite)
- 'echo More text for our demo file >> demo.txt' - Append to file
Fsutil to Create a file
- 'fsutil file createNew for-sure.txt 222' - Create a file called for-sure.txt
Rename A file
- 'ren demo.txt superdemo.txt' - Rename demo.txt to superdemo.txt
Input / Output
- We can utilize the <, >, |, and & to send input and output from the console and files to where we need them
- With >, we can push the output of a command to file (will create the file if it does not exist)
- With >>, we can append to a file 
- To pass a file into a command use <
- To pipe between command we can use |
- To issue multiple command at once we can use &
- If we care about the first command succeeding before running the second, we can use &&
- You can accomplish the opposite of this using || 
Deleting Files
- Use 'del' or 'erase' 
- Can take multiple arguments to delete multiple files at once


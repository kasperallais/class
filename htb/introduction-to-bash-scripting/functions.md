Functions
- Functions are an essential part of script and programs, as they are used to execute recurring commands
Method 1
''' function name {
    <commands>
} '''
Method 2
''' name() {
    <commands>
} '''
Method 3
Parameter Passing
- Some functions should be designed so that they can be used with a fixed structure of the values or at least only with a fix format
''' #!/bin/bash

function print_pars {
	echo $1 $2 $3
}

one="First parameter"
two="Second parameter"
three="Third parameter"

print_pars "$one" "$two" "$three" '''

Return Values
- When we start a new process, each child process returns a return code to the parents process at its termination
- 1 - General Errors
- 2 - Misuse of shell builtins
- 126 - Command invoked cannot execute
- 127 - Command not found
- 128 - Invalid argument to exit
- 128 + n - Fatal error signal 'n'
- 130 - Script Terminated by Control-C
- 255\* Exit status out of range
- To get the value of a function back, we can use several methods like return, echo, or a variable

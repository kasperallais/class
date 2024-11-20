What an environment variable is
- Environment variables are settings that are often applied globally to our hosts
- They can be accessed by most users and applications on the host and are used to run scripts and speed up how applications function and reference data
- When referenced they are called like so, '%SUPER_IMPORTANT_VARIABLE%'
Variable Scope
- Scope is a programming concept that refers to where variables can be accessed or referenced
    - Global:
        - Global variables are accessible globally. In this context, the global scope lets us know that we can access and reference the data stored inside the variable from anywhere within a program
    - Local:
        - Local variables are only accessible within a local context. Local means that the data stored within these variables can only be accessed and referenced within the function or context in which it has been declared
- These variables can be separated into their defined scope know as System and User scopes. There is also one more scope called the Process scope
Using Set and Echo to View Variables
- You can use 'set' to print all available environment variables on the system
- You can also use it to find an environment variable's value: 'set %SYSTEMROOT%
- 'echo' is also used to show environment variables
Managing Environment Variables
- Use 'set' and 'setx'
- The 'set' utility only manipulates environment variables in the current comment line session
- The 'setx' makes permanent changes to environment variables
Creating Variables
- Example: 'set DCIP=172.16.5.2'
- Example 2: 'setx DCIP 172.16.5.2'
Editing Variables
- Just use 'set' and 'setx' again and it overwrites
Removing Variables
- Clear variables by making them equal to nothing
- Example: 'setx DCIP ""' 

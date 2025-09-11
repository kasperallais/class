# Why learn C in Operating Systems?
- C is the dominant language for many operating systems today
    - Linux Kernel - 100% C
    - Darwin Kernel - 80% C
    - Windows Kernel - mostly C, some C++ and C#
- C gives you minimal layers of abstraction
    - Ability to use system calls directly
    - Manual memory management
- You already know some C
    - C is an approximate subset of C++

# Linux is the assumption
- Open Source means we know more about how it works, and hence we can show you how it works

# Hello World in C

    #include <stdio.h>

    int main(int argc, char *argv[])
    {
        printf("Hello, World!\n");
        return 0;
    }

# Compiling and running a C program

    cc test.c -o test
    ./test

- All project in this course will come with a pre-written Makefile in the starter code

# Arrays

    int some[10] \\ Array of 10 integers, named "some" (Unitialized)
    int another[10] = { 0 } \\ Array of 10 integers, named "another". User special syntax to initialize all values to zero
    int more[] = { 1,2,3 } \\ Array of 3 integers, named "more". Initial values are 1, 2, and 3

# Pointers
- & operation ("reference operator") - get the memory address of a value
- * operator ("dereference operator") - get the value at a memory address
- We denote the type of a memory address by appending * to the regular type
- Array access is really just a dereference

# How can we use pointers?
- Function which mutate a variable
    - Unlike C++, C only has pass-by-value
    - This means to mutate the caller's variables, we must pass a pointer to the variable

# The NULL Pointer
- NULL is a special value defined to address 0, to indicate the non-presence of data

# C Memory Model
- Stack Memory 
    - The function's arguments and local variables
    - Created when the function is called by advancing the stack pointer, and destroyed by reverting the stack pointer to the previous location when the function returns
- Static Memory
    - Using the "static" keyword
    - There is only one copy of this variable for the entire program
    - Created when the program starts, and destroyed when the program exists
    - The initial value is assigned when the program starts, not each time the function is called
    - Memory exists for whole program, safe to return from a function
- Heap Memory
    - Memory you can allocate and free whenever you wish
    - malloc(size): allocate some memory and return a pointer to the base of it
    - free(ptr): pass base address from malloc call, memory is returned to the OS

# Inherent Dangers of Explicit Heap Memory
- If we ge tto choose when we allocate and free memory, we accidentaly might
    - Memory Leak - Forget to free memory we have allocated
    - Use after free - Use a pointer after we have freed the memory region already, getting invalid data, or causing corruption
    - Double-free - free a memory region twice, causing corruption if we have allocated something else there already

# Strings in C
- Strings in C are represented as a pointer to the base of the string, and end with a null-terminator

# Printing to the console (printf)
- printf takes a format string, followed by arguments to be replaced in the format string

# Making composite types (struct)
- 'struct' allows you to create data structures composed of many fields

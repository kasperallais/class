# Time-Sharing Systems
- Can be used to handle multiple interactive jobs
- Processor time is shared among multiple users
- Multiple users simultaneously access the system through terminals
- The OS interleaves the execution of each user program in a short burst or quantum of computation

# Batch Multiprogramming vs. Time Sharing
- Batch Multiprogramming - Maximize processor use and job control language commands provided with the job
- Time Sharing - Minimize response time and commands entered at the terminal

# Compatible Time-Sharing Systems (CTSS)
- One of the first time-sharing operating systems
- Developed at MIT by a group known as project MAC
- How was time slicing implemented
    - System clock generates interrupt at a rate of approximatively one every 0.2 seconds
    - At each interrupt OS regained control and could assign processor to another user
    - At regular time intervals the current user would be pre-empted, and another user loaded in
    - Old user programs and data were written out to disk
    - Old user program code and data were restored in main memory when that program was next given a turn

# Modern O/S
- Operating System are among the most complex pieces of software ever developed

# Process
- Fundamental to the structure of operating systems
- A process can be defined as:
    - A program in execution
    - An instance of a running program
    - The entity that can be assigned to, and executed on, a processor
    - A unit of activity characterized by a single sequential thread of execution, a current state, and an associated state set of system resources

# The need for 'Process'
- Three major lines of computer system development create problems in timing and synchronization that contributed to the development
- Utilization
    - Processor is switched among the various programs residing in main memory
- Responsiveness
    - Be responsive to the individual user but be able to support many users simultaneously
- Priority
    - A number of users are entering queries or updates against a database

# Components of a Process
- The execution context is essential
    - It is the internal data by which the OS is able to supervise and control the process
    - Include the contents of the various process registers
    - Includes information such as the priority of the process and whether the process is waiting for the completion of a particular I/O event
- A process contains tree components
    - An executable program
    - The associated data needed by the program
    - The execution context of the program

# Process Management
- The entire state of the process at any instant contained in its context
- The process index register indicates that process B is executing
- Process A was previously executing but has been temporarily interrupted

# Memory Management
- The OS has five principal storage management responsibilities
    - Process Isolation
    - Automatic allocation and management
    - Support of modular programming
    - Protection and access control
    - Long-term storage

# Virtual Memory
- A facility that allows programs to address memory from a logical point of view, without regard to the amount of main memory physically available
- Conceived to meet the requirements of having multiple user jobs reside in main memory concurrently

# Paging
- Allows processes to be comprised of a number of fixed-size blocks, called pages
- Program references a word by means of a virtual address
    - Consists of a page number an offset within the page
    - Each page may be located anywhere in main memory

# Scheduling and Resource Management
- Key responsibility of an OS is managing resources
- Resource allocation policies must consider:
    - Efficiency
    - Fairness
    - Differential Responsiveness

# Causes of Errors
- Improper synchronization
    - A program must wait until the data available in a buffer
    - Improper design of the signaling mechanism can result in loss or duplication
- Failed mutual exclusion
    - More than one user or program attempts to make use of a shared resource at the same time
    - Only one routine at a time allowed to perform an update against the file
- Non-determinate program operation
    - Program execution is interleaved by the processor when memory is shared
    - The order in which programs are scheduled may affect their outcome
- Deadlocks
    - It is possible for two or more programs to be hung up waiting for each other
    - May depend on the chance timing of resource allocation and release

# Different Architectural Approaches
- Demands on operating systems require new ways or organizing the OS

# Microkernel Architecture
- Assigns only a few essential functions to the kernel
    - Address spaces
    - Interprocess Communication (IPC)
    - Basic Scheduling
- The approach
    - Simplifies implementation
    - Provides flexibility
    - Is well suited to a distributed/edge environment

# OS Design
- Distributed Operating System
    - Provides the illusion of  
         A single main memory space
         - Single secondary memory space
         - Unified access facilities
- Object-Oriented Design
    - Used for adding modular extensions to a small kernel
    - Enables programmers to customize an operating system without distrusting system integrity
    - Eases the development of distributed tools and full-blown distributed operating systems

# Symmetric Multiprocessing
- Term that refers to a computer hardware architecture and also to the OS behavior that exploits that architecture
- Several processes can run in parallel
- Multiple processor are transparent to the user
    - These processors share same main memory and I/O facilities
    - All processor can perform the same functions
- The OS takes care of scheduling of processes on individual processors and of synchronization among processor

# Multiprogramming v.s. Multiprocessing
- With multiprogramming, only one process can execute at a time; meanwhile all other processes are waiting for the processor
- With multiprocessing, more than one process can be running simultaneously, each on a different processor

# Multithreading
- Technique in which a process, executing an application, is divide dinto threads that can run concurrently

# Grand Central Dispatch
- Developer must decide what pieces can or should be executed simultaneously or in parallel


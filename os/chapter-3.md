# OS Management of Application Execution
- Resources are made available to multiple applications
- The processor and I/O devices can be used efficiently

# Process State Queues
- The OS maintains the PCBs of all the processes in state queues
- The OS places the PCBs of all the processes in the same execution state in the same queue
- When the OS changes the state of a process, the TCP is unlinked from its current queue and moved to its new state queue
- The OS can use different policies to manage each queue

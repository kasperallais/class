What is a Networking Model 
- Networking models categorize and provide a structure for networking protocols and standards
- A set of logical rules defining how network devices and software should work
OSI Model 
- 'Open Systems Interconnection' model
- A conceptual model that categorizes and standardizes the different functions in a network
- Created by the 'International Organization for Standardization' (ISO)
- Function are divided into 7 Layers
OSI Model - Application Layer
- This layer is closest to the end user
- Interacts with software applications, for example your web browser
- HTTP and HTTPS are Layer 7 protocols
- Functions of Layer 7 include:
    - Identifying communication partners
    - Synchronizing communication
- Data moves through the OSI stack before getting to the other user
- Process called encapsulation 
- When data reaches the other device it is de-encapsulated
OSI Model - Presentation Layer
- Data in the application layer is in 'application format'
- It needs to be 'translated' to a different format to be sent over the network
- The Presentation Layer's job is to translate between application and network formats
- For example, encryption of data as it is send, and decryption of data as it is received
- Also translated between different Application-Layer formats
OSI Model - Session Layer
- Controls dialogues between communicating hosts
- Establishes, manages, and terminates connections between the local application and the remote application
OSI Model - The Upper Layers
- Network Engineers don't usually work with the top 3 layers
- Application developers work with the top layers of the OSI model to connect their applications over networks
OSI Model - Transport Layer
- Segments and reassembles data for communication between end hosts
- Breaks large pieces of data into smaller segments which can be more easily sent over the network and are less likely to cause transmission problems if errors occur
- Provide host-to-host communication
OSI Model - Network Layer
- Provides connectivity between end hosts on different networks
- Provides logical addressing
- Provides path selection between source and destination
- Routers operate at Layer 3
OSI Model - Encapsulation
- Layer 4 adds a header called an 'L4 header' and that makes the payload into a segment
- Layer 3 adds a header called an 'L3 header' and that makes the payload into a packet
OSI Model - Data Link Layer
- Provides node-to-node connectivity and data transfer
- Defines how data is formatted for transmission over a physical medium
- Detects and correct Physical Layer errors
- Uses Layer 2 addressing, separate from Layer 3 addressing
- Switches operate at Layer 2
- This layer adds a header and a trailer
- Payload is now called a frame 
OSI Model - Physical Layer
- Defines physical characteristics of the medium used to transfer data between devices
- Digital bits are converted into electrical or radio
OSI Model - PDUs
- Data, Segment, Packet, and Frame are called PDUs (Protocol Data Units)
TCP/IP Suite
- Conceptual model and set of communications protocols used in the Internet and other networks
- Known as TCP/IP because those are two of the foundational protocols in the suite
- Developed by the Department of Defense through DARPA
- Similar structure to the OSI model, but with fewer layers
- This is the model actually in use in modern networks
OSI vs TCP/IP
- OSI Application, Presentation, and Session layers are equivalent to the Application Layer in the TCP/IP suite
- OSI Transport Layer maps to TCP/IP Transport Layer
- OSI Network Layer maps to Internet Layer
- OSI Data Link and Physical Layers map to Link Layer
TCP/IP Suite
- Routers do not need the Upper two layers
- Only Internet and Link Layers
How to Renew IP addresses
- 'ipconfig /renew'

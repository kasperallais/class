Common Protocols
- Internet protocols are standardized rules and guidelines defined by RFCs that specify how devices on a network could communicate with each other
- They ensure that devices on a network can exchange information consistently and reliably, regardless of the hardware and software used. For devices to communicate on a network, they need to be connected through a communication channel, such as wired or wireless connection
- The devices then exchange information using a set of standardized protocols that define the format and structure of the data being transmitted
- The two main types of connections used on networks are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)
Transmission Control Protocol
- TCP is a connection-oriented protocol that establishes a virtual connection between two devices before transmitting data by using a Three-Way-Handshake
- This connection is maintained until the data transfer is complete, and the devices can continue to send data back and forth as long as the connection is active
User Datagram Protocol
- UDP is a connectionless protocol, which means it does not establish a virtual connection before transmitting data
- Instead, it sends the data packets to the destination without checking to see if they were received
- UDP is faster than TCP but less reliable because there is no guarantee that the packets will reach their destination
ICMP
- Internet Control Message Protocol is a protocol used by devices to communicate with each other on the Internet for various purposes, including error reporting and status information
- It sends request and messages between devices, which can be used to report errors or provide status information
ICMP Requests
- A request is a message sent by one device to another to request information or perform a specific action
ICMP Messages
- A message in ICMP can either be a request or a reply
- In addition to ping requests and responses, ICMP support other types of messages, such as error messages, destination unreachable, and time exceeded messages
- These messages are used to communicate various types of information and errors between devices on the network
- Another crucial part of ICMP for us is the Time-To-Live (TTL) field in the ICMP packet header that limits the packet's lifetime as it travels through the network
- It prevents packets from circulating indefinitely on the network in the event of routing loops
- Each time a packet passes through a router, the router decrements the TTL value by 1
- When the TTL value reaches 0, the router discards the packet and sends an ICMP Time Exceeded message back to the sender
- We can also use TTL to determine the number of hops a packet has taken and the approximate distance to the destination
VoIP
- Voice over Internet Protocol is a method of transmitting voice and multimedia communications
- The most common VoIP ports are TCP/5060 and TCP/5061, which are used for the Session Initiation Protocol (SIP)
- However, the port TCP/1720 may also be used by some VoIP system for the H.323 protocol, a set of standards for multimedia communication over packet-based networks
Information Disclosure
- SIP allows us to enumerate existing users for potential attacks
- This can be done for various purposes, such as determining a user's availability, finding out information about the user's capabilities or services, or performing brute-force attacks on user accounts later on
- One of the possible way to enumerate users is in the SIP OPTIONS request
- It is a method used to request information about the capabilities of a SIP server or user agents, such as the types of media it supports, the codecs it can decode, and other details
- The OPTIONS request can probe a SIP service or user agent for information or test its connectivity and availability


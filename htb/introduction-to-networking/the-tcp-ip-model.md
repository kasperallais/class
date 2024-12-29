The TCP/IP Model
- The TCP/IP model is also a layered reference model, often referred to as the Internet Protocol Suite
- The term TCP/IP stands for the two protocols Transmission Control Protocol (TCP) and Internet Protocol (IP)
- IP is located within the network layer and TCP is located within the transport layer of the OSI layer model
TCP/IP Layers
- Application - Allows applications to access the other layers' services and defines the protocols applications use to exchange data
- Transport - Responsible for providing (TCP) session and (UDP) datagram services for the Application Layer
- Internet - Responsible for host addressing, packaging, and routing functions
- Link - Responsible for placing the TCP/IP packets on the network medium and receiving corresponding packets from the network medium. TCP/IP is designed to work independently of the network access method, frame format, and medium
- With TCP/IP, every application can transfer and exchange data over any network, and it does not matter where the receiver is located
- IP ensure that the data packet reaches its designation, and TCP controls the data transfer and ensure the connection between data stream and application
- The main difference between TCP/IP and OSI is the number of layers, some of which have been combined 
TCP/IP Tasks
- Logical Addressing - Due to many hosts in different networks, there is a need to structure the network topology and logical addressing. Within TCP/IP, IP takes over the logical addressing of networks and nodes. Data packets only reach the network where they are supposed to be. The methods to do so are network classes, subnetting, and CIDR
- Routing - For each data packet, the next node is determined on the way from its sender to the receiver. This way, a data packet is routed to its receiver, even if it's location is unknown to the sender
- Error & Control Flow - The sender and receiver are frequently in touch with each other via a virtual connection. Therefore control messages are sent continuously to check if the connection is still established
- Application Support - TCP and UDP ports form a software abstraction to distinguish specific applications and their communication links
- Name Resolution - DNS provides name resolution through Fully Qualified Domain Names (FQDN) in IP Addresses, enabling us to reach the desired host with specified name on the internet

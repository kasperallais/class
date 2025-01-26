# Networking Primer - Layers 1-4
- This section serves as a quick refresher on networking and how some standard protocols we can see while performing captures work
- These concepts are at the core of capturing and dissecting traffic
- Without a fundamental understanding of typical network flow and what ports and protocols are used, we cannot accurately analyze any traffic we capture

# MAC-Addressing
- Each logical or physical interface attached to a host has a MAC address
- This address is a 48-bit six octet address presented in hexadecimal format
- MAC-addressing is used in layer two communications between hosts
- The works through host-to-host communication within a broadcast domain
- If layer two traffic needs to cross a layer 3 interface, that PDU is sent to the layer three egress interface, and the router will take the layer three address into account when determining where to send it next
- Once it makes a choice, it strips the encapsulation at layer two and replaces it with new information that indicates the next physical address in route

# IP Addressing
- The Internet Protocol (IP) was developed to deliver data form one host to another across network boundaries. IP is responsible for routing packets, the encapsulation of data, and fragmentation and reassembly of datagrams when they reach the destination host
- By nature, IP is a connectionless protocol that provides no assurances that data will reach it's intended recipient
- For reliability and validation of data delivery, IP relies on upper-layer protocols such as TCP. Currently, there exists two main versions of IP. IPv4, which is the current dominant standard, and IPv6, which is intended to be the successor of IPv4

# IPv4
- The most common addressing mechanism most are familiar with is the Internet Protocol address version 4 (IPv4). IPv4 addressing is the core method of routing packets across networks to hosts located outside our immediate vicinity
- An IPv4 address is made up of a 32-bit four octet number represented in decimal format/
- Each octet of an IP address can be represented by a number ranging from 0 to 255
- When examining a PDU, we will find IP addresses in layer three (network) of the OSI model and layer two (internet) of the TCP-IP model

# IPv6
- After a little over a decade of utilizing IPv4, it was determined that we had quickly exhausted the pool of usable IP addresses. With such large chunks sectioned off for special use or private addressing, the world had quickly used up the available space
- To help this issue, two things were done
- The first was implementing variable-length subnet masks (VLSM) and Classless Inter-Domain Routing (CIDR)
- This allowed us to redefine the useable IP addresses in the v4 format changing how addresses were assigned to users
- The second was the creation and continued development of IPv6 as a successor to IPv4
- IPv6 provides us a much larger address space that can be utilized for networked purposes
- IPv6 is a 128-bit address 16 octets represented in hex format
- Along with a much larger address space, IPv6 provides
    - Better support for Multicasting
    - Global addressing per device 
    - Security within the protocol in the for of IPSec 
    - Simplified Packet headers allow for easier processing and move from connection to connection without being re-assigned an address

# IPv6 Addressing Types
- Unicast - Addresses for a single interface
- Anycast - Addresses for multiple interfaces, where only one of them receives the packet
- Multicast - Addresses for multiple interfaces, where all of them receive the same packet
- Broadcast - Does not exist and is realized with multicast address

# TCP / UDP, Transport Mechanisms
- The Transport Layer has several mechanisms to help ensure the seamless delivery of data to from the source to destination
- Think about the Transport Layer as a control hub
- Application data from the higher layers have to traverse down the stack to the Transport Layer
- This layer directs how the traffic will be encapsulated and thrown to the lower layer protocols
- Once this data reaches its intended recipient, the Transport Layer, working with the Network / Internet layer protocols, is responsible for reassembling the encapsulated data back in the correct order
- The two mechanisms used to accomplish this task are TCP and UDP

# TCP Three-way Handshake
- One of the ways TCP ensures the delivery of data from server to client is the utilization of sessions
- These sessions are established through what is called a three-way handshake
- To make this happen, TCP utilizes an option in the TCP header called flags
- The common flags to see in a three way handshake are SYN and ACK
    - The client sends a packet with the SYN flag set to on along with other negotiable options in the TCP header
        - This is a synchronization packet. It swill only be set in the first packet from host and server and enables establishing a session by allowing both end to agree on a sequence number to start communicating with
        - This is crucial for the tracking of packets. Along with the sequence number sync, many other options are negotiated in this phase to include window size, maximum segments size, and selective acknowledgments
    - The server will respond with a TCP packet that includes a SYN flag set for the sequence number negotiation and an ACK flag set to acknowledge the previous SYN packet sent by the host
         - The server will also include any changes to the TCP options it requires set in the options fields of the TCP header
    - The client will respond with a TCP packet with an ACK flag set agreeing to the negotiation
        - This packet is the end of the three-way handshake and establishes the connection between client and server

# TCP Three-way Handshake
- Another flag we will see with TCP is the FIN flag
- It is used for signaling that the data transfer is finished and the sender is requesting termination of the connection
- The client acknowledges the receipt of the data and then sends a FIN and ACK to being session termination
- The server responds with an acknowledgement of the FIN and sends back it's own FIN

# HTTP
- Hypertext Transfer Protocol (HTTP) is a stateless Application Layer protocol that has been in use since 1990
- HTTP enables the transfer of data in a clear text between a client and a server over TCP
- The client would send an HTTP request to the server, asking for a resource
- A session is established, and the server responds with the requested media (HTML, images, hyperlinks, video)
- HTTP utilizes ports 80 or 8000 over TCP during normal operations
- In exceptional circumstances, it can be modified to use alternate ports, or even at times, UDP

# HTTP Methods
- To perform operations such as fetching webpages, requesting items for download, or posting your most recent tweet all require the use of specific methods
    - HEAD - (required) Head is a safe method that request a response from the server similar to Get request except hat the message body is not included. It is a great way to acquire more information about the server and it's operational status
    - GET - (required) Get is most common method used. It requests information and content from the server. For example GET http://10.1.1.1/Webserver/index.html requests the index.html page from the sever based on our supplied URI
    - POST - (optional) Post is a way to submit information to a sever based on the fields in the request. For example, submitting a message to a Facebook post or website forum is a POST action. The actual action taken can vary based on the server, and we should pay attention to the response codes send back to validate the action
    - PUT - (optional) - Put will take the data appended to the message and place it under the requested URI. If an item does not exist there already, it will create one with the supplied data. If an object already exists, the new PUT will be considered the most up-to-date, and the object will be modified to match. The easiest way to visualize the differences between PUT and POST is to think of it like this; Put will create or update an object and the URI supplied, while POST will create child entities at the provided URI. The action take can be compared with the difference between creating a new file vs. Writing comments about that file on the same page
    - DELETE - (optional) Delete does as the name implies. It will remove the object at the given URI
    - TRACE - (optional) Allows for remote server diagnosis. The remote server will echo the same request that was sent it its response if the TRACE method is enabled
    - OPTIONS - (optional) The Options method can gather information on the supported HTTP methods the server recognizes. This way, we can determine the requirements for interacting with a specific resource or server without actually requesting data or objects from it.
    - CONNECT - (optional) Connect is reserved for use with Proxies and other security devices like firewalls. Connect allows for tunneling over HTTP
- As a requirement by the standard, GET and HEAD must always work and exist with standard HTTP implementations
- This is only true for them

# HTTPS
- HTTP Secure (HTTPS) is a modification of the HTTP protocol designed to utilize Transport Layer Security (TLS) and Secure Sockets Layer (SSL) with older applications for data security
- TLS is utilized as an encryption mechanism to secure the communications between a client and a server
- TLS can wrap regular HTTP traffic within TLS, which means that we can encrypt our entire conversation, not just the data sent or requested
- Before the TLS mechanism was in place, we were vulnerable to Man-in-the-middle attacks and other types or reconnaissance or hijacking, meaning anyone in the same LAN as the client or server could view the web traffic if they were listening on the wire
- Even though it is HTTP at it's base, HTTPS utilizes ports 443 and 8443 instead of the standard port 80
- This is a simple way for the client to signal the server that it wishes to establish a secure connection
- HTTPS Handshake:
    - Client and server exchange hello messages to agree on connection parameters
    - Client and server exchange necessary cryptographic parameters to establish a premaster secret
    - Client and server will exchange x.509 certificates and cryptographic information allowing for authentication within the session
    - Generate a master secret from the premaster secret and exchanged random values
    - Client and server issue negotiated security parameters to the record layer portion of the TLS protocol
    - Client and server verify that their peer has calculated the same security parameters and that the handshake occurred without tampering by an attacker

# FTP
- File transfer protocol is an Application Layer protocol that enables quick data transfer between computing devices
- FTP can be utilized from the command-line, web browser, or through a graphical FTP client such as FileZilla
- FTP itself is established as an insecure protocol, and most users have moved to utilize tools such as SFTP to transfer files through secure channels
- When we think about communication between hosts, we typically think about a client and a server talking over a single socket
- Through this socket, both the client and server send commands and data over the same link
- In this aspect, FTP is unique since it utilizes multiple ports at the same time
- FTP uses ports 20 and 21 over TCP
- Port 20 is used for data transfer, while port 21 is utilized for issuing commands controlling the FTP session
- In regards to authentication, FTP supports user authentication as well as allowing anonymous access if configured
- FTP is capable of running in two different modes, active or passive
- Active is the default operational method utilized by FTP, meaning that the server listens for a control command PORT from the client, stating what port to use for data transfer
- Passive mode enables us to access FTP servers located behind firewalls or NAT-enabled link that makes direct TCP connections impossible
- In this instance, the client would send the PASV command and wait for a response from the server informing the client what IP and port to utilize for the data transfer channel connection
- Common FTP Commands
    - USER - specifies the user to log in
    - PASS - sends the password for the user attempting to log in
    - PORT - when in active mode, this will change the data port used
    - PASV - switches the connection to the server from active mode to passive mode
    - LIST - displays a list of the files in the current directory
    - CWD - will change the current working directory to one specified
    - PWD - prints out the directory you are currently working in
    - SIZE - will return the size of a file specified
    - QUIT - ends the session

# SMB
- Server Message Block (SMB) is a protocol most widely seen in Windows Enterprise Environments that enables sharing resources between hosts over common networking architecture
- SMB is a connection-oriented protocol that requires user authentication from the host to the resource to ensure the user has current permission to use that resource or perform actions
- In the past, SMB used NetBIOS as its transport mechanism over UDP ports 137 and 138
- Since modern changes, SMB now supports direct TCP transport over port 445, NetBIOS over TCP port 139, and even QUIC protocol



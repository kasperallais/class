TCP/UDP Connections
- TCP and UDP are both protocols used in information and data transmission on the Internet
- Typically, TCP connections transmit important data, such as web pages and emails.
- In contrast, UDP connections transmit real-time data such as streaming video or online gambling
- TCP is a connection-oriented protocol that ensures that all data sent from one computer to another is received
- It is like a telephone conversation where both parties remain connected until the call is terminated
- If an error occurs while sending data, the receiver sends a message back so the sender can resent the missing data
- This makes TCP reliable and slower than UDP because more time is required for transmission and error recovery
- UDP, on the other hand, is a connectionless protocol
- It is used when speed is more important than reliability, such as for video streaming or online gambling
- With UDP, there is no verification that the received data is complete or error-free
- If an error occurs while sending data, the receiver will not receive the missing data, and no message will be sent back to resend it
- Some data may be lost with UDP, but the overall transmission is faster
IP Packet
- An IP packet is the data area used by the network layer of the Open Systems Intercommunication (OSI) model to transmit data from one computer to another
- It consists of a header and the payload, the actual payload data
IP Header
- The IP header of an IP packet contains several fields that have important information:
	- Version - Indicates which version of the IP protocol is being used
	- Internet Header Length - Indicates the size of the header in 32-bit words
	- Class of Service - Means how important the transmission of data is
	- Total Length - Specifies the total length of the packet in bytes
    - Identification (ID) - Is used to identify fragments of the packet when fragmented into smaller parts
	- Flags - Used to indicate fragmentation
	- Fragment Offset - Indicates where the current fragment is placed in the packet
	- Time to Live - Specifies how long the packet may remain on the network
	- Protocol - Specifies which protocol is used to transmit the data, such as TCP or UDP
    - Checksum - Is used to detect errors in the header
    - Source/Destination - Indicate where the packet was sent from and where it is being sent to
    - Options - Contains optional information for routing
    - Padding - Pads the packet to a full word length
IP Record-Route Field
- The Record-Route field in the IP header also records the route to a destination device
- When the destination device sends back the ICMP Echo Reply packet, the IP addresses of all devices that pass through the packet are listed in the Record-Route field of the IP header.
TCP
- TCP packets, also known as segments, are divided into several sections called headers and payloads
- The TCP segments are wrapped in the sent IP packet
- The header contains several fields that contain important information
- The source port indicates the computer from which the packet was sent
- The destination port indicates to which computer the packet is sent
- The sequence number indicates the order in which the data was sent
- The confirmation number is used to confirm that all data was received successfully
- The control flags indicate whether the packet marks the end of a message, whether it is an acknowledgment that data has been received, or whether it contains a request to repeat data
- The window size indicates how much data the receiver can receive
- The checksum is used to detect errors in the header and payload
- The Urgent Pointer alerts the receiver that important data is in the payload
UDP
- UDP transfers datagrams between two hosts
- It is a connectionless protocols, meaning it does not need to establish a connection between the sender and the receiver before sending data
- Instead, the data is sent directly to the target host without any prior connection
Blind Spoofing
- Blind Spoofing, is a method of data manipulation attack in which an attacker sends false information on a network without seeing the actual responses sent back by the target devices
- It involves manipulating the IP header field to indicate false source and destination address

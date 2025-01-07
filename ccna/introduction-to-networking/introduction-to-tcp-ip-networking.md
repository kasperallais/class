Introduction to TCP/IP Networking
- Networks work correctly because the various devices and software follows the rules
- Those rules come in the form of standards and protocols, which are agreements of a particular part of how a network should work
- Networking models define a structure and different categories of standards and protocols
- As new standards and protocols emerge over time, networkers can think of those new details in the context of a working model
- Today, TCP/IP rules as the most pervasive model in use
- You can find support for TCP/IP on practically every computer operating system (OS) in existence, from mobile phones to mainframe computers
- Every network built using Cisco products today support TCP/IP
Perspectives on Networking
- In networking diagrams, a cloud represents a part of a network whose details are not important to the purpose of the diagram
TCP/IP Networking Model
- A networking model, sometimes also called either a networking architecture or networking blueprint, refers to a comprehensive set of documents
- Individually, each document describes one small function required for a network; collectively, these documents define everything that should happen for a computer network to work
- Some documents define a protocol, which is a set of logical rules that devices must follow to communicate
- Other documents define some physical requirements for networking
History Leading to TCP/IP
- Today, the world of computer networking uses one networking model: TCP/IP
- However, the world has not always been so simple
- The world used to be comprised of vendor-defined proprietary networking models
- Although vendor-defined proprietary networking models often worked well, having an open, vendor-neutral networking model would aid competition and reduce complexity
- The International Organization for Standardization (ISO) took on the task to create such a model, starting as early as the late 1970s, beginning work on what would become known as the Open Systems Interconnection (OSI) networking model
- ISO had a noble goal for the OSI model: to standardize data networking protocols to allow communication among all computers across the entire planet
- A second less-formal effort to create an open, vendor-neutral, public networking model sprouted forth from a U.S. Department of Defense contract
- Researchers at various universities volunteered to help further develop the protocols surrounding the original DoD work
- These efforts resulted in a competing open networking model called TCP/IP
Overview of the TCP/IP Networking Model
- The TCP/IP model both defines and references a large collection of protocols that allow computers to communicate 
- To define a protocol, TCP/IP uses documents called Requests For Comment (RFC)
- The TCP/IP model also avoids repeating work already done by some other standards body or vendor consortium by simply referring to standards or protocols created by those groups
- For example, the IEEE defines Ethernet LANs; the TCP/IP model does not define Ethernet in RFCs, but refers to the IEEE Ethernet as an option
- The TCP/IP model creates a set of rules that allows us all to take a computer out of the box, plug in all the right cables, turn it on, and connect to use the network
- The TCP/IP model shows the more common terms and layers used when people talk about TCP/IP today
- The bottom layer focuses on how to transmit bits over each individual link
- The data-link layer focuses on sending data over one type of physical link
- The network layer focuses on delivering data over the entire path from the original sending computer to the final destination computer
- The top two layers focus more on the applications that need to send a receive data
TCP/IP Application Layer
- TCP/IP application layer protocols provide services to the application software running on a computer
- The application layer does not define the application itself, but it defines services that applications need
- Arguably, the most popular TCP/IP application today is the web browser
- Many major software vendors either have already changed or are changing their application software to support access from a web browser
HTTP Protocol Mechanisms
- To make the request for web page and return the contents of a web page, the applications use the Hypertext Transfer Protocol (HTTP)
TCP/IP Transport Layer
- The most commonly used transport layer protocols are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP)
-  Transport layer protocols provide services to the application layer protocols that reside one layer higher in the TCP/IP model
Same-Layer and Adjacent-Layer Interactions
- Same-layer interaction of different computers - The two computers use a protocol to communicate with the same layer on another computer. The protocol defines a header that communicates what each computer wants to do
- Adjacent-layer interaction on the same computer - On a single computer, one lower layer provides a service to the layer just above. The software or hardware that implements the higher layer requests that the next lower layer perform the needed function
TCP/IP Network Layer
- The TCP/IP network layer includes a small number of protocols, but only one major protocol: the Internet Protocol (IP)
- IP provides several features, most importantly, addressing and routing
Internet Protocol and Postal Service
IP Routing Basics
- The TCP/IP network layer, using the IP protocol, provides a service of forwarding IP packets form one device to another
- Any device with an IP address can connect to the TCP/IP network and send packets
- The term IP host refers to any device, regardless of size or power, that has an IP address and connects to any TCP/IP network
TCP/IP Data-Link and Physical Layers
- The TCP/IP model's data-link and physical layers define the protocols and hardware required to deliver data across some physical network
- The physical layer defines the cabling and energy that flow over the cables 
- Focusing on the data-link layer for a moment, just like every layer in any networking model, the TCP/IP data-link layer provides services to the layer above it in the model
- When a host's or router's IP process chooses to send an IP packet to another router or host, that host or router then uses link-layer details to send that packet to the next host/router
Larry Using Ethernet to Forward an IP Packet to Router R1
- Larry encapsulates the IP packet between an Ethernet header and Ethernet trailer, creating an Ethernet frame
- Larry physically transmits the bits of this Ethernet frame, using electricity flowing over the Ethernet cabling
- Router R1 physically receives the electrical signal over a cable and re-creates the same bits by interpreting the meaning of the electrical signals
- Router R1 de-encapsulates the IP packet from the Ethernet frame by removing and discarding the Ethernet header and trailer
- Protocols define both header and trailers for the same general reason, but headers exist at the beginning of the message and trailers exist at the end
- The data-link and physical layers include a large number of protocols and standards
- For example, the link layer includes all variations of Ethernet protocols and wireless LAN protocols discussed throughout the course
- In short, the TCP/IP physical and data-link layers include two distinct functions, respectively: functions related to the physical transmission of the data, plus the protocols and rules that control the use of the physical media
Data Encapsulation Terminology
- Each layer adds its own header (and for data-link protocols, also a trailer) to the data supplied by the higher layers
- The term encapsulation refers to the process of putting headers (and sometimes trailers) around data
- The process by which a TCP/IP host sends data can be viewed as five-step process
- The first four steps relate to the encapsulation performed by the four TCP/IP layers, and the last step is the actual physical transmission of the data by the host
- The steps are summarized in the following list:
    - Create an encapsulate the application data with any required application layer headers. For example, the HTTP OK message can be returned in an HTTP header, followed by part of the contents of a web page
    - Encapsulate the data supplied by the application layer inside a transport layer header. For end-user applications, a TCP or UDP header is typically used
    - Encapsulate the data supplied by the transport layer inside a network layer (IP) header. IP defines the IP address that uniquely identifies each computer
    - Encapsulate the data supplied by the network layer inside a data-link layer header and trailer. This layer uses both a header and trailer
    - Transmit the bits. The physical layer encodes a signal onto the medium to transmit the frame
Names of TCP/IP Messages
- One reason this chapter takes the time to show the encapsulation steps in detail has to do with terminology
- When talking and writing about networking, people use segment, and frame to refer to the messages in TCP/IP
- Each term has a specific meaning, referring to the headers (and possibly trailers) defined by a particular layer and the data encapsulated following that header
- Each term, however, refers to a different layer, segment for the transport layer, packet for the network layer, and frame for the link layer
- When focusing on the work done by a particular layer, the encapsulated data typically is unimportant
- For example an IP packet can indeed have a TCP header after the IP header, an HTTP header after the TCP header, and the data for a web page after the HTTP header
- However, when discussing IP, you probably just care about the IP header, so everything after the IP header is just called data
- So when drawing IP packets, everything after the IP header is typically shown simply as data
OSI Networking Model and Terminology 
- At one point in the history of the OSI model, many people though that OSI would win the battle of the networking models discussed earlier
- During those years in which many people thought the OSI model would become commonplace in the world of networking, many vendors and protocol documents started using terminology from the OSI model
- So, while you will never need to work with a computer that uses OSI, to understand modern networking terminology, you need to understand something about OSI
Comparing OSI and TCP/IP Layer Names and Numbers
- The OSI model has many similarities to the TCP/IP model from a basic conceptual perspective
- It has layers, and each layer defines a set of typical networking functions
- As with TCP/IP; the OSI layers each refer to multiple protocols and standards that implement the functions specified by each layer
- In other cases, just as for TCP/IP, the OSI committees did not create new protocols or standards, but instead referred other protocols that were already defined
- For example, the IEEE defines Ethernet standards, so the OSI committees did not waste time specifying a new type of Ethernet, it simply referred to the IEEE Ethernet standards
- Even though the world uses TCP/IP today rather than OSI, we tend to use the numbering from the OSI layer
- For instance, when referring to an application layer protocol in a TCP/IP network, the world still refers to the protocol as a "Layer 7 protocol"
- Also, while TCP/IP includes more functions at its application layer, OSI breaks those into session, presentation, and application layers
- Most of the time, no one cares much about the distinction, so you will see references like "Layer 5-7 protocol", again using the OSI numbering
OSI Data Encapsulation Terminology
- Like TCP/IP, each OSI layer ask for services from the next lower layer
- To provide the services, each layer makes use of a header and possibly a trailer
- The lower layer encapsulates the higher layer's data behind a header
- OSI uses a more generic term to refer to messages, rather than frame, packet, and segment, OSI uses the term protocol data unit (PDU)
- A PDU represents the bits that include the headers and trailers for that layer, as well as the encapsulated data
- For example, an IP packet, using OSI terminology, is a PDU, more specifically a Layer 3 PDU because IP is a Layer 3 protocol
- OSI simply refers to the Layer X PDU (LxPDU), with x referring to the number of the layer being discussed

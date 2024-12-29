The OSI Model
- The goal in defining the ISO/OSI standard was to create a reference model that enables the communication of different technical systems via various devices and technologies and provides compatibility
OSI Layers
- Application - Controls the input and output of data and provides the application functions
- Presentation - Transfer the system-dependent presentation of data into a form independent of the application
- Session - Controls the logical connection between two systems and prevents, connection breakdown or other problems
- Transport - End-to-end control of the transferred data. The Transport Layer can detect and avoid congestion situations and segment data streams
- Network - Connections are established in circuit-switched networks, and data packets are forwarded in packet-switched networks. Data is transmitted over the entire network from the sender to the receiver
- Data Link - Enable reliable and error-free transmissions on the respective medium. For this purpose, the bitstream from layer 1 are divided into blocks or frames
- Physical - The transmission techniques used are, for example, electrical signals, optical signals, or electromagnetic waves. Through layer 1, the transmission takes place on wired or wireless transmission lines
OSI Model Characteristics
- The layers 2-4 are transport oriented, and the layers 5-7 are application oriented layers
- If two systems communicate, all seven layers of the OSI model are run through at least twice, since both the sender and the receiver must take the layer model into account

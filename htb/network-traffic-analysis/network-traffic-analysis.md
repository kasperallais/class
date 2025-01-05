Network Traffic Analysis
- Network Traffic Analysis (NTA) can be described as the act of examining network traffic to characterize common ports and protocols utilized, establish a baseline for our environment, monitor and respond to threats, and ensure the greatest possible insight into our organization's network
- This process helps security specialists determine anomalies, including security threats in the network, early and effectively pinpoint threats
- Network Traffic Analysis can also facilitate the process of meeting security guidelines
- Attackers update their tactics frequently to avoid detection and leverage legitimate credentials with tools that most companies allow in their networks, making detection and subsequently, response challenging for defenders
- Everyday use cases of NTA include:
    - Collecting real-time traffic within the network to analyze upcoming threats
    - Setting a baseline for day-to-day network communications
    - Identifying and analyzing traffic from non-standard ports, suspicious hosts, and issues with networking protocols such as HTTP errors, problems with TCP, or other networking misconfiguration
    - Detecting malware on the wire, such as ransom ware, exploits, and non-standard interactions
    - NTA is also useful when investigating past incidents and during threat hunting
Required Skills and Knowledge
- TCP/IP Stack & OSI Model
- Basic Networking Concepts
- Common Ports and Protocols
- Concepts of IP Packets and the Sub layers
- Protocol Transport Encapsulation
Environment and Equipment
- tcpdump - tcpdump is a command-line utility that, with the aid of LibPcap, captures and interprets network traffic from a network interface or capture file
- Tshark - TShark is a network packet analyzer much like TCPDump. It will capture packets from a live network or read and decode from a file. It is the command-line variant of Wireshark
- Wireshark - Wireshark is a graphical network traffic analyzer. It captures and decodes frames off the wire and allows for an in-depth look into the environment. It can run many different dissectors against the traffic to characterize the protocols and applications and provide insight into what is happening
- NGrep - NGrep is a pattern-matching tool built to serve a similar function as grep for Linux distributions. The big difference is that it works with network traffic packets. NGrep understands how to read live traffic from a PCAP file and utilize regex expression and BPF syntax. This tool shines best when used to debug traffic from protocols like HTTP and FTP
- tcpick - tcpick is command-line packet sniffer that specializes in tracking and reassembling TCP streams
- Network Taps - Taps are devices capable of taking copies of network traffic and sending them to another place for analysis. These can be in-line or out of band. They can actively capture and analyze the traffic directly or passively by putting the original packet back on the wire as if nothing had changed
- Networking Span Ports - Span Ports are a way to copy frames from layer two or three networking devices during egress or ingress processing and send them to a collection point. Often a port is mirrored to send those copies to a log server
- Elastic Stack - The Elastic Stack is a culmination of tools that can take data from many sources, ingest the data, and visualize it, to enable searching and analysis of it
- SIEMS - SIEMS are a central point in which data is analyzed and visualized. Altering, forensic analysis, and day-to-day checks against the traffic are all use cases for a SIEM
BPF Syntax
- Many of the tools mentioned above have their syntax and commands to utilize, but one that is shared among them is Berkeley Packet Filter (BPF) syntax
- This syntax is the primary method we will use
- In essence, BPF is a technology that enables a raw interface to read and write from the Data-Link layer
- With all this in mind, we care for BPF because of the filtering and decoding abilities it provides us
- We will be utilizing BPF syntax through the module, so a basic understanding of how a BPF filter is set up can be helpful


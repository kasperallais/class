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
Performing Network Traffic Analysis
- Performing analysis can be as simple as watching live traffic roll in our console or as complex as capturing data with a tap, sending it back to a SIEM for ingestion, and analyzing the pcap data and alerts related to common tactics and techniques
- At a minimum, to listen passively, we need to be connected to the network segment we wish to listen on 
- This is especially true in a switched environment where VLANS and switch ports will not forward traffic outside their broadcast domain
- With that in mind, if we wish to capture traffic from a specific VLAN, our capture device should be connected to the same network
- Devices like network taps, switch or router configurations like span ports, and port mirroring can allow us to get a copy of all traffic traversing a specific link, regardless of what network segment or destination it belongs to
NTA Workflow
- Traffic Analysis is not an exact science. NTA can be a very dynamic process and is not a direct loop
- It is greatly influence by what we are looking for and where we have visibility into our network
- Perming traffic analysis can be distilled down to a few basic tenants
    - Ingest traffic - Once we have decided our placement, begin capturing traffic. Utilize capture filters if we already have an idea of what we are looking for
    - Reduce Noise by Filtering - Capturing traffic of a link, especially one in a production environment, can be extremely noisy. Once we complete the initial capture, an attempt to filter out unnecessary traffic from our view can make analysis easier
    - Analyze and Explore - Now is the time to start carving out data pertinent to the issue we are chasing down. Look at specific hosts, protocols, even things as specific as flags set in the TCP header. The following questions will help us:
        - Is the traffic encrypted or plain text? Should it be?
        - Can we see users attempting to access resources which they should not have access?
        - Are different hosts talking to each other that typically do not?
    - Detect and Alert - Are we seeing any errors? Is a device not responding that should be? Use our analysis to decide if what we see is benign or potentially malicious. Other tolls like IDS and IPS can come in handy at this point. They can run heuristics and signatures against the traffic to determine if anything within is potentially malicious

# Filtering and Advanced Syntax Options
- By reducing the amount of info we capture and write to disk, we can help reduce the space needed to write the file and help the buffer process data quicker
- Filters can be handy when paired with standard tcpdump syntax options

# Helpful TCPDump Filters
- host - host will filter visible traffic to show anything involving the designated host. Bi-directional
- src / dest - src and dest are modifiers. We can use them to designate a source or destination host or port.
- net - net will show us any traffic sourcing from or destined to the network designated. It uses / notation.
- proto - will filter for a specific protocol type. (ether, TCP, UDP, and ICMP as examples)
- port - port is bi-directional. It will show any traffic with the specified port as the source or destination.
- portrange - portrange allows us to specify a range of ports. (0-1024)
- less / greater "< >" - less and greater can be used to look for a packet or protocol option of a specific size.
- and / && - and && can be used to concatenate two different filters together. for example, src host AND port.
- or - or allows for a match on either of two conditions. It does not have to meet both. It can be tricky.

# Host Filter

    sudo tcpdump -i eth0 host 192.168.1.128

- This filter is often used when we want to examine only a specific host or server

# Source/Destination Filter

    sudo tcpdump -i eth0 src host 172.16.142.2

- Source and destination allow us to work within the directions of communications

# Utilizing Source With Port as a Filter

    sudo tcpdump -i eth0 tcp src port 80

# Using Destination in Combination with the Net Filter

    sudo tcpdump -i eth0 dest net 172.16.146.0/24

- Used in this manner, net will grab anything matching the / notation for network

# Protocol Filter - Common Name

    sudo tcpdump -i eth0 udp

- This filter can utilize the common protocol name or protocol number for an IP, IPv6, or Ethernet protocol

# Protocol Filter - Number

- Using the port filter, we should keep in mind what we are looking for and how that protocol functions

# Port Range Filter

    sudo tcpdump -i eth0 portrange 0-1024

# Less / Greater Filter

    sudo tcpdump -i eth0 less 64

# And Filter

    sudo tcpdump -i eth0 host 192.168.0.1 and port 23

# Pre-Capture Filters vs. Post-Capture Filters

- When utilizing filters, we can apply them directly to the capture or apply them when reading a capture file

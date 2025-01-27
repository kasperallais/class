# Tcpdump Fundamentals
- Tcpdump is a command-line packet sniffer that can directly capture and interpret data frames from a file or network interface
- It does not require a GUI and can be used through any terminal or remote connection such as SSH
- To capture network traffic from "off the wire", it uses the libraries pcap and libpcap, paired with an interface in promiscuous mode to listen for data

# Listing Available Interfaces
    
    sudo tcpdump -D

# Choosing an Interface to Capture From

    sudo tcpdump -i wlan0

# Disable Name Resolution

    sudo tcpdump -i wlan0 -nn

# Include ASCII and Hex Output

    sudo tcpdump -i wlan0 -X

# Display Ethernet Header

    sudo tcpdump -i wlan0 -e

# File Input/Output with Tcpdump
- Using -w will write our capture to a file
- We can save our PCAP Output to a File with:

    sudo tcpdump -i eth0 -w ~/output.pcap

- To read output from a file use:

    sudo tcpdump -r ~/output.pcap

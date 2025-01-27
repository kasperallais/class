# Analysis with Wireshark
- Wireshark is a free and open-source network traffic analyzer much like tcpdump but with a GUI
- Wireshark is multi platform and capable of capturing live data off many different interface types

# TShark vs. Wireshark
- Both options have their merits
- TShark is a purpose built terminal tool based on Wireshark
- TShark shared many of the same features that are included with Wireshark and even shares syntax and options
- Wireshark is the feature rich GUI option for traffic capture and analysis

# TShark Basic Usage
- TShark can use filters for protocols, common items like hosts and ports, and even the ability to dig deeper into the packets and dissect individual fields from the packet

    tshark -i 1 -w /tmp/test.pcap

- With the basic string in the command line, we utilize TShark to capture on en0, specified with the -i flag and the -w options to save the capture to a speficied output file
- Using TShark is very similar to using TCPDump in the filters and switches we use
- To read the capture, tshark can be passed the -r switch just like in TCPDump
- Or we can pass the -P switch to have tshark print the packet summaries while writing out to a file

# Selecting an Interface & Writing to a File

    sudo tshark -i eth0 -w /tmp/test.pcap

# Applying Filters

    sudo tshark -i eth0 -f "host 172.16.146.2"

# Termshark
- Termshark is a Text-based User Interface (TUI) application that provides the user with a Wireshark-like interface right in your terminal window

# Wireshark
- Wireshark's toolbar is a central point to manage the many features that Wireshark includes

# Pre-capture and Post-Capture Processing and Filtering
- While capturing traffic with Wireshark, we have several options regarding how and when we filter out traffic
- This is accomplished utilizing Capture and Display filters
- The Former initiated before the capture starts and the latter during or after the capture is complete
- The more packets captured, the longer it will take Wireshark to run the display or analysis filter against it

# Capture Filters
- Capture Filters are entered before the capture is started
- These use BPF syntax like host 214.15.2.30 much in the same fashion as TCPDump

# Display Filters
- Display filters are used while the capture is running and after the capture has stopped
- Display filters are proprietary to Wireshark
- When using capture and display filters, keep in mind that what we specify is taken in a literal sense



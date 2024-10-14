Firewall
- Provide security mechanism for controlling and monitoring network traffic between different network segments
Iptables
- Provides a flexible set of rules for filtering network traffic based on various criteria such as source and destination IP addresses, port numbers, protocols, and more
Nftables
- Nftables provides a more modern syntax and improved performance over iptables
Component and Description list
- Tables -> Tables are used to organize and categorize firewall rules
- Chains -> Chains are used to group a set of firewall rules applied to specific type of network traffic
- Rules -> Rules define the criteria for filtering network traffic and the actions to take for packets that match the criteria
- Matches -> Matches are used to match specific criteria for filtering network traffic, such as source or destination IP addresses, ports, protocols and more
- Targets -> Targets specify the action for packets that match a specific rule
Tables
- filter -> Used to filter network traffic based on IP addresses, ports, and protocols
- nat -> used to modify the source or destination IP addresses of network packet
- mangle -> used to modify the header fields of network packets
Chains
- Organize rules that define how network traffic should be filtered or modified
    - Built-in chains
    - User-defined chains
- Built-in chains are pre-defined and automatically created when a table is created
- User-defined chains can simplify rule management by grouping firewall rules based on specific criteria, such as source IP address, destination port, or protocol.
Rules and Targets
- Used to define the criteria for filtering network traffic and the actions to take for packets that meat the criteria
- Rules are added to chains using the -A option followed by the chain name
Common Targets
- ACCEPT -> Allows the packet to pass through the firewall land continue to its destination
- DROP -> Drops the packet
- REJECT -> Drops the packet and sends an error message back to the source address
- LOG -> Logs the packet information to the system log
- SNAT -> Modifies the source IP address of the packet
- DNAT -> Modifies the destination IP address
- MASQUERADE -> Similar to NAT but used when the source IP address is not fixed
- REDIRECT -> Redirects packets to another port or IP address
- MARK -> Adds or modifies the Netfilter mark value of the packet
Matches
- Used to specify the criteria that determine whether a firewall rules should be applied to a particular packet or connection
-p or --protocol 	Specifies the protocol to match (e.g. tcp, udp, icmp)
--dport 	Specifies the destination port to match
--sport 	Specifies the source port to match
-s or --source 	Specifies the source IP address to match
-d or --destination 	Specifies the destination IP address to match
-m state 	Matches the state of a connection (e.g. NEW, ESTABLISHED, RELATED)
-m multiport 	Matches multiple ports or port ranges
-m tcp 	Matches TCP packets and includes additional TCP-specific options
-m udp 	Matches UDP packets and includes additional UDP-specific options
-m string 	Matches packets that contain a specific string
-m limit 	Matches packets at a specified rate limit
-m conntrack 	Matches packets based on their connection tracking information
-m mark 	Matches packets based on their Netfilter mark value
-m mac 	Matches packets based on their MAC address
-m iprange 	Matches packets based on a range of IP addresses 


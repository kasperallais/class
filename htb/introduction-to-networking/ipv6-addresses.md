IPv6 Addresses
- IPv6 is the successor of IPv4
- In contrast to IPv4, the IPv6 address is 128 bits long
- The prefix identifies the host and network parts
- IANA is responsible for assigning IPv4 and IPv6 addresses and their associated network portions
- In the long term, IPv6 is expected to completely replace IPv4, which is still predominantly used on the internet
- IPv6 consistently follows the end-to-end principle and provides publicly accessible IP addresses for any end devices without need for NAT
- An interface can have multiple IPv6 addresses, and there are special IPv6 addresses to which multiple interfaces are assigned
- IPv6 is a protocol with many features, which also has many other advantages over IPv4
    - Larger address space
    - Address self-configuration (SLAAC)
    - Multiple IPv6 addresses per interface
    - Faster routing 
    - End-to-end encryption (IPSec)
    - Data packages up to 4 GByte
Types of IPv6 Addresses
- Unicast - Addresses for a single interface
- Anycast - Addresses for multiple interfaces, where only one of them receives the packet
- Multicast - Addresses for multiple interfaces, where all receive the same packet
- Broadcast - Do not exist and is realized with multicast address
Hexadecimal System
- The hexadecimal system is used to make the binary representation more readable and understandable
- We can only show 10 statues with the decimal system and 2 with the binary system by using a single character
- In contrast to the binary and decimal system, we can use the hexadecimal system to show 16 states with a single character
IPv6 Addresses
- An IPv6 address consists of two parts:
    - Network Prefix
    - Interface Identifier also called the Suffix
- The Network Prefix identifies the network, subnet, or address range
- The Interface Identifier is formed from the 48-bit MAC address of the interface and is converted to a 64-bit address in the process
- The default prefix length is /64


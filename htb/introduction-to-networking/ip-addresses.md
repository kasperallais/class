IP Addresses
- Each host in the network located can be identified by the so-called Media Access Control address (MAC)
- This would allow data exchange within this one network
- If the remote host is located in another network, knowledge of the MAC address is not enough to establish a connection
- Addressing on the Internet is done via the IPv4 and/or IPv6 address, which is made of the network address and the host address
- It does not matter whether it is a smaller network, such as a home computer network, or the entire Internet. The IP address ensures the delivery of data to the correct receiver
- We can imagine the representation of MAC and IPv4/IPv6 addresses as follows:
    - IPv4/IPv6 - describes the unique postal address and district of the receiver's building
    - MAC - describes the exact floor and apartment of the receiver
- It is possible for a single IP address to address multiple receivers or for a device to respond to multiple IP addresses
- However, it must be ensured that each IP address is assigned only once within the network
IPv4 Structure
- The most common method of assigning IP addresses is IPv4, which consists of a 32-bit binary number combined into 4 bytes consisting of 8-bit groups ranging from 0-255
- These are converted into more easily readable decimal numbers, separated by dots and represented as dotted-decimal notation
- Each network interface is assigned a unique IP address
- The IPv4 format allows 4,294,967,296 unique addresses
- The IP address is divided into a host part and a network park
- The router assigns the host part of the IP address at home or by an administrator
- The respective network administrator assigns the network part
- On the Internet, this is IANA, which allocates and manages the unique IPs 
Subnet Mask
- A further separation of these classes into small networks is done with the help of subnetting
- This separation is done using the net masks, which is as long as an IPv4 address
- As with classes, it describes which bit positions within the IP address act as the network part or host part
Network and Gateway Addresses
- The two additional IPs added in the IPs column are reserved for the so-called network address and the broadcast address
- Another important role plays the default gateway, which is the name for the IPv4 address of the router that couples networks and systems with different protocols and manages addresses and transmission methods
- It is common for the default gateway to be assigned the first or last assignable IPv4 address in a subnet
Broadcast Address
- The broadcast IP address's task is to connect all devices in a network with each other
- Broadcast in a network is a message that is transmitted to all participants of a network and does not require any response
- In this way, a host sends a data packet to all other participants of the network simultaneously and, in doing so, communicated its IP address, which the receivers can use to contact it
- The last IPv4 address is used for the broadcast
Binary System
- The binary system is a number system that uses only two different states that are represented into two numbers opposite to the decimal system
- An IPv4 address is divided into 4 octets, as we have already seen
-Each octet consists of 8 bits
- Each position of a bit in an octet has a specific decimal value
CIDR
- Classless Inter-Domain Routing is a method of representation and replaces the fixed assignment between IPv4 address and network classes
- The division is based on the subnet mask or the so-called CIDR suffix, which allows the bitwise division of the IPv4 address space and thus into subnets of any size
- The CIDR suffix indicates how many bits from the beginning of the IPv4 address belong to the network

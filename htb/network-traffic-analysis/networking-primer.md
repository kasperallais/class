Networking Primer - Layers 1-4
- This section serves as a quick refresher on networking and how some standard protocols we can see while performing captures work
- These concepts are at the core of capturing and dissecting traffic
- Without a fundemental understanding of typical network flow and what ports and protocols are used, we cannot accurately analyze any traffic we catpure
MAC-Addressing
- Each logical or physical interface attached to a host has a MAC address
- This address is a 48-bit six octet address presented in hexademcimal format
- MAC-addressing is used in layer two communications between hosts
- The works through host-to-host communication within a broadcast domain
- If layer two traffic needs to cross a layer 3 interface, that PDU is sent to the layer three egress interface, and the router wil ltake the layer three address into account when determining where to send it next
- Once it makes a choice, it strips the encapsulation at layer two and replaces it with new information that indicates the next physical address in route
IP Addressing
- The Internet Protocol (IP) was developed to deliver data form one host to another across network boundaries. IP is responsible for routing packets, the encapsulation of data, and fragmentation and reassembly of datagrams when they reach the destination host
- By nature, IP is a connectionless protocol that provides no assurances that data will reach it's intended recipient
- For reliability and validation of data delivery, IP relies on upper-layer protocols such as TCP. Currently, there exists two main versions of IP. IPv4, which is the current dominant standard, and IPv6, which is intended to be the successor of IPv4
IPv4
- The most common addressing mechanism most are familiar with is the Internet Protocol address version 4 (IPv4). IPv4 addressing is the core method of routing packets across networks to hosts located outside our immediate vicinity
- An IPv4 address is made up of a 32-bit four octet number represented in decimal format
- Each octet of an IP address can be represented by a number ranging from 0 to 255
- When examining a PDU, we will find IP addresses in layer three (network) of the OSI model and layer two (internet) of the TCP-IP model
IPv6
- After a little over a decade of utilizing IPv4, it was determined that we had quickly exhausted the pool of usable IP addresses. With such large chunks secitoned off for special use or private addressing, the world had quickly used up the available space
- To help this issue, two things were done
- The first was implementing variable-length subnet masks (VLSM) and Classless Inter-Domain Routing (CIDR)
- This allowed us to redefine the useable IP addresses in the v4 format changing how addresses were assigned to users
- The second was the creation and continued development of IPv6 as a successor to IPv4

Subnetting
- The division of an address range of IPv4 addresses into several smaller address ranges is called subnetting
- A subnet is a logical segment of a network that uses IP addresses with the same network address
- In subnetting, we use the subnet mask as a template for the IPv4 address
- From the 1-bits in the subnet-mask, we know which bits in the IPv4 address cannot be changed
- These are fixed and therefore determine the "main network" in which the subnet is located
Host Part
- The bits in the host part can be changed to the first and the last address. The first address is the network address, and the last address is the broadcast address for the respective subnet
- The network address is vital for the delivery of a data packet
- If the network address is the same for the source and the destination address, the data packet is delivered within the same subnet
- If the network addresses are different, the packet must be router to another subnet using the default gateway
Network Address
- If we set all bits to 0 in the host part of the IPv4 address, we get the respective subnet's network address
Broadcast Address
- If we set all bits in the host part of the IPv4 address to 1, we get the broadcast address

Mental Subnet
- Number of hosts: 32
- Subnet: 10.200.20.0/27
- Required Subnets: 4

- Expanded Subnet: 10.200.20.0/29
- Host range for each subnet = 8

1 - 10.200.20.0 - 10.200.20.7
2 - 10.200.20.8 - 10.200.20.15
3 - 10.200.20.16

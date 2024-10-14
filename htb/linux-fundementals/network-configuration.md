NAC 
- Discretionary Access Control
- Mandatory Access Control
- Role-based Access Control
Network Monitoring
- Tools such as syslog, rsyslog, ss, lsof, and the ELK stack
Configuring Network interfaces
- Configure local network interfaces with ifconfig or ip
- ifconfig is deprecated in newer versions of Linux and replaced by the ip command
Activate Network Interface
- 'sudo ifconfig eth0 up' or 'sudo ip link set eth0 up'
Assign an IP Address to an Interface
- 'sudo ifconfig <interface> <address>'
Assign a Netmask to an Interface
- 'sudo ifconfig <interface> netmask <netmask>'
Assign a Route to an Interface
- 'sudo route add default gw 192.168.1.1 eth0'
DNS
- Domain Name Server
- DNS's translate domain names into IP addresses
- 'sudo vim /etc/resolv.conf'
- Then edit the /etc/network/interfaces file
Restart network service
- 'sudo systemctl restart networking'
ping
- 'ping <remote_host>' 
traceroute
- traces the route packets take to reach a remote host
- sends packets with increasing TTL and displays IP addresses of the devices that the packets pass through
netstat
- used to display active network connections and their associated ports
- used to identify network traffic and troubleshoot connectivity issues
- 'netstat -a' -> detailed information about each connection
- protocol used, number of bytes received and sent, IP addresses, port numbers of local and remote devices, and current connection state
Hardening
- SELinux, App Armor, and TCP
SELinux
- MAC system that is built into the Linux kernel
- Enforcing a policy that defines the access controls for each process and file on the sytem
AppArmor
- MAC system that provides a similar level of control over sytem resources and applications
TCP Wrappers
- Host-based network access control mechanism that can be used to restrict accessto network services based on the IP address of the client system.

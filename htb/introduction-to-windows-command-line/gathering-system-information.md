What types of information can we gather from the system?
- The goal of host enumeration is to provide an overall picture of the target host, its environment, and how it interacts with other systems across the network
Types of Information we are looking for
- General System Information - Contains information about the overall target system. Includes hostname, OS-specific details and installed hotfixes/patches for the system
- Networking Information - Contains networking and connection information for the target system and system(s) to which the target is connected over the network. Host IP address, available network interfaces, accessible subnets, DNS server(s), known hosts, and network resources
- Basic Domain Information - Contains Active Directory information regarding the domain to which the target system is connected
- User Information - Contains information regarding local users and groups on the target system. This can typically be expanded to contain anything accessible to these account, such as environment variables, currently running tasks, scheduled tasks, and known services
Why do we need this information?
- It can be easy to write off a system as being completely patched and not vulnerable to any CVEs or the latest vulnerabilities. However, if you only focus on that aspect, it is easy to miss out on the many human configuration errors that could exist in the environment
How do we get this information?
- Casting a Wide Net
    - CMD provides a one-stop shop for information via the 'systeminfo' command. 
- Examining the system
    - If we need basic information such as hostname or OS version, we can use the hostname and ver utilities built into the command prompt
    - 'hostname' follows namesake and 'ver' prints out the system version
- Scoping the network
    - To gather this information quickly, 'ipconfig' displays all current TCP/IP network configurations for the machine
    - If we need additional information or want to dig further into the specific settings applied to each adapter, we can use the following command: 'ipconfig /all'
    - If we need to quickly see what hosts our target has come into contact with, look not further than the arp command
Understanding our current user
- 'whoami' allows us to display the user, group, and privilege information for the user that is currently logged in
- 'whoami /priv' shows us current user's security privileges
Investigating groups
- 'whoami /groups'
Investigating other users/groups
- 'net user' allows us to display a list of all users on a host, information about a specific user, and to create or delete users
Net Group / LocalGroup
- 'net group' and 'net localgroup' to display any groups that exist on the host from which we issued the command, create or delete groups, and add or remove users from the groups
Net Share
- 'net share' allows us to display info about shared resources on the host and to create new shared resources as well
Net View
- 'net view' will display to us any shared resources the host you are issuing the command against knows of
Piecing 

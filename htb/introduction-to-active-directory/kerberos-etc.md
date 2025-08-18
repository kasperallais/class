## Kerberos, DNS, LDAP, MSRPC
- While Windows operating systems use a variety of protocols to communicate, AD specifically requires LDAP, DNS for authentication and communication, and MSRPC which is Microsoft's implementation to Remote Procedure Call

# Kerberos
- Kerberos has been the default authentication protocol for domain accounts since Windows 2000
- Open standard and allows for interoperability with other systems using the same standard
- When a user logs into their PC, Kerberos is used to authenticate them via manual authentication, or both the user and the server verify their identity
- Kerberos is a stateless authentication protocol based on tickets instead of transmitting user passwords over the network
- As part of AD DS, Domain Controllers have a Kerberos Key Distribution Center (KDC) that issues tickets
- When a user initiates a login request to the system, the client they are using to authenticate requests a ticket from the KDC, encrypting the request with the user's password
- If the KDC can decrypt the request using their password, it will create a Ticket Granting Ticket and transmit it to the user
- The user then presents its TGT to a Domain Controller to request a Ticket Granting Service ticket, encrypted with the associated service's NTLM password hash
- Finally, the client requests access to the required service by presenting the TGS to the application or service, which decrypts it with its password hash

# DNS
- AD DS uses DNS to allow clients to locate Domain Controllers and for Domain Controllers that host the directory service to communicate amongst themselves
- Private internal networks use Active Directory DNS name 

# DNS Lookups
- Forward DNS Lookup
    - nslookup [domain-name]
- Reverse DNS Lookup
    - nslookup [ip-addr]

# LDAP
- AD supports LDAP for directory lookups
- LDAP is an open-source and cross-platform protocol used for authentication against various directory services
- AD stores user account information such as passwords and facilitates sharing this information with other devices on the network
- LDAP is the language that applications use to communicate with other servers that provide directory services
- An LDAP session begins by first connecting to an LDAP server, also known as a Directory System Agent
- The Domain Controller in AD actively listens for LDAP requests, such as security authentication requests

# AD LDAP Authentication
- LDAP is set up to authenticate credentials against AD using a "BIND" operation to set the authentication state for an LDAP session
- There are two types of LDAP authentication
    - Simple Authentication
        - Includes anonymous authentication, unauthenticated authentication, and username/password authentication
    - SASL Authentication:
        - Simple Authentication and Security Layer
        - Uses other services, such as Kerberos, to bind to the LDAP server and then uses this authentication service to authenticate LDAP

# MSRPC
- Four key RPC interfaces
    - lsarpc
    - netlogon
    - samr
    - drsuapi


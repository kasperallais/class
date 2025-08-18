## NTLM Authentication
- Aside from Kerberos and LDAP, AD uses several other authentication methods which can be used by applications and services in AD
- These include LM, NTLM, NTLMv1, NTLMv2, LM and NTLM 

# LM 
- LAN Manager hashes are the oldest password storage mechanism used by the Windows Operating System

# NTHash
- NT LAN Manager hashes are used on modern Windows systems
- It is a challenge-response authentication protocol and uses three messages to authenticate: a client first sends a NEGOTIATE_MESSAGE to the server, whose response in a CHALLENGE_MESSAGE to verify the client's identity
- Lastly, the client responds with an AUTHENTICATE_MESSAGE
- These hashes are stored locally in the SAM database or the NTDS.DIT database file on a Domain Controller
- The protocol has two hashed password values to choose from to perform authentication: the LM hash and the NT hash, which is the MD4 hash of the little-endian UTF-16 value of the password

# NTLMv1
- The NTLM protocol performs a challenge/response between a server and client using the NT hash. NTLMv1 uses both the NT and the LM hash, which can make it easier to crack offline after capturing a hash using a tool such as Responder or via an NTLM relay attack
- The protocol is used for network authentication, and the NTLMv1 hash itself is created from a challenge/response algorithm

# NTLMv2
- Successor to NTLMv1 introduced on Windows NT 4.0 SP4

# Domain Cache Credentials
- In an AD environment, the authentication methods mentioned above require the host we are trying to access to communicate with the "brains" of the network, the domain controller.
- MSCache2 was made for authentication without the Domain Controller

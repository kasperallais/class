## User and Machine Accounts
- User accounts are created on both local systems and in AD to give a person or program the ability to logon on to the computer and access resources based on their rights
- When a user logs in, the system verifies their password and creates an access token
- This token describes the security content of a process or thread and includes the user's security identity and group membership
- User accounts present an immense attack surface and are usually a key focus for gaining foothold during a penetration test

# Local Accounts
- Local accounts are stored locally on a particular server or workstations
- Any rights assigned can only be granted to that specific host and will not work across the domain
- There are several default local user accounts that are created on a Windows system:
    - Administrator
        - This account has the SID S-1-5-domain-500 and is the first account created with a new Windows installation
    - Guest
        - This account is disabled by default
        - The purpose of this account is to allow users without an account on the computer to log in temporarily with limited access rights
    - SYSTEM
        - The SYSTEM account on a Windows host is the default account installed and used by the operating system to perform many internal functions
        - A SYSTEM account is the highest permission level one can achieve on a windows host
    - Network Service
        - Predefined local account used by the Service Control Manager
        - When a service runs in the context of this particular account, it will present credentials to remote services
    - Local Service
        - This is another predefined local account used by the SCM

# Domain Users
- Domain users differ from local users in that they are granted rights from the domain to access resources such as file servers, printers, intranet hosts, and other objects based on their permissions
- One account to keep in mind is the KRBTGT account
    - Acts as a service account for the Key Distribution service providing authentication

# Domain-joined vs. Non-Domain-joined Machines
- Domain Joined
    - Hosts joined to a domain have greater ease of information sharing within the enterprise and a central management point to gather resources, policies, and updates from
    - A host joined to a domain will acquire any configurations or changes necessary through the domain's Group Policy
- Non-Domain Joined
    - Non-domain joined computers or computers in a workgroup are not manged by domain policy

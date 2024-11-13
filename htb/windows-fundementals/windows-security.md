Windows Security
- Security is a critical topic in Windows operating systems
- Windows systems can be easily misconfigured
Security Identifier (SID)
- Each of the security principals on the system has unique security identifier (SID)
- The system automatically generates SIDs
- SIDs are string values with different lengths, which are stored in the security database
- A SID consists of the Identifier Authority and the Relative ID (RID)
- In an AD domain, the SID also includes the domain SID
- Broken down into this pattern:
    - (SID)-(revision level)-(identifier-authority)-(subauthority1)-(subauthority2)-(etc)
Security Accounts Manager (SAM) and Access Control Entries (ACE)
- SAM grants rights to a network to execute specific processes
- The access rights themselves are manged by Access Control Entries (ACE) in Access Control Lists (ACL)
- The ACLs contain ACEs that define which users, groups, or processes have access to a file or to execute a process
- The permissions to access a securable object are given by the security descriptor, classified into two types of ACLs: the Discretionary Access Control List (DACL) or System Access Control List (SACL)
- Every thread and process started or initiated by a user goes through an authorization process 
- An integral part of this process is access tokens, validated by the Local Security Authority (LSA) 
User Account Control (UAC)
- Security feature in Windows to prevent malware from running or manipulating processes that could damage the computer or its contents
- There is the Admin Approval Mode in UAC, which is designed to prevent unwanted software from being installed without the administrator's knowledge or to prevent system wide changes from being made
- Consent prompt interrupt the execution of scripts and binaries that malware or attackers try to execute until the user enters the password or confirms execution
Registry
- Hierarchical database in Windows critical for the operating system
- Stores low-level settings for the Windows operating system and applications that choose to use it
- Divided into computer-specific and user-specific data
- We can open the registry by typing regedit from the command line or Windows search bar
Run and RunOnce Registry Keys
- Also called registry hives, which contain a logical group of keys, subkeys and values to support software and files loaded into memory when the operating system is started or a user logs in
Application Whitelisting
- List of approved software applications or executables allowed to be present and run on a system
- Protect the environment from harmful malware and unapproved software that does not align with the specific business needs of an organization
AppLocker
- Microsoft's application whitelisting solution
- Gives system administrators control over which applications and files users can run
- Allows for creating rules based on file attributes such as the publisher's name, product name, file name, and version
Local Group Policy
- Allows administrators to set, configure, and adjust a variety of settings
- In a domain environment, group policies are pushed down from a Domain Controller onto all domain-joined machines that Group Policy objects (GPOs) are linked to
Windows Defender
- Built-in antivirus that ships for free with Windows operating systems
- Comes with several features such as real-time protection
- When files are submitted to the cloud protection service, they are "locked" to prevent any potential malicious behavior until the analysis is complete
- Another feature is Tamper Protection, which prevents security settings from being changed through the Registry, PowerShell cmdlets, or group policy

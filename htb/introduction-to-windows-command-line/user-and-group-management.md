What are User Accounts?
- User accounts are a way for personnel to access and use a host's resources
- Four different account types
    - Service Accounts
    - Built-in accounts
    - Local users
    - Domain users
Brief Intro to Active Directory
- Active Directory is a directory service for Windows environments that provides a central point of management for users, computers, groups, network devices, file shares, group policies, devices and trusts with other organizations
- Anyone who is part of the domain can access resources freely, while anyone who is not is denied access to those same resources or, at a minimum, stuck waiting in the visitors center
Local vs. Domain Joined Users
- Domain users differ from local users in that they are granted rights from the domain to access resources such as file servers, printers, intranet hosts, and other object based on user and group membership
- Domain user accounts can log in to any host in the domain, while the local user only has permission to access the specific host they were created on
What are User Groups?
- Groups are a way to sort user accounts logically and, in doing so, provide granular permissions and access to resources without having to manage each user manually
Adding/Removing/Editing User Accounts & Groups
- Like most other things in PowerShell, we use the get, new, and set verbs to find, create and modify users and groups
Identifying Local Users
- 'Get-LocalUser' displays users on the host
Creating a New User
- 'New-LocalUser -Name "NAME" -NoPassword'
Modifying a User
- 'Set-LocalUser -Name "NAME" -Password $Password -Description "DESCRIPTION"'
Get Local Groups
- 'Get-LocalGroup' displays groups on the host
Adding a Member to a Group
- 'Add-LocalGroupMember -Group "GROUP" -Member "MEMBER"'
Installing RSAT
- 'Get-WindowsCapability -Name RSAT* -Online | Add-WindowsCapability -Online
Get-ADUser
- 'Get-ADUser -Filter (star)'
- Grabs all users within an Active Directory
Get a Specific User
- 'Get-ADUser -Identity "USER"'
Searching On An Attribute
- 'Get-ADUser -Filter {EmailAddress -like '(star)greenhhorn.corp'}
Creating a new AD user
- 'New-ADUser -Name "MTanaka" -Surname"Tanaka" -GivenName "Mori" -Office "Security" -OtherAttributes @{'title'="Sensei";'mail'="MTanaka@greenhorn.corp"} -Accountpassword (Read-Host -AsSecureString "AccountPassword") -Enabled $true'

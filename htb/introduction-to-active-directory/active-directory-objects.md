## AD Objects

# Users
- These are the users within the organization's AD environment
- Users are considered leaf objects, which means that they account contain any other objects within them
- A user objects is considered a security principal and has a security identifier and a global unique identifier
- User objects have many possible attributes, such as their display name, last login time, date of last password change, email address, account description, manager, address and more

# Contacts
- A contact object is usually used to represent an external user and contains informational attributes such as first name, last name, email address, telephone number, etc
- They are leaf objects and are NOT security principals, so they don't have a SID, only a GUID

# Printers
- A printer object points to a printer accessible within the AD network

# Computers
- A computer object is any computer joined to the AD network
- Like users, they are prime targets for attackers since full administrative access to a computer grants similar rights to a standard domain user and can be used to perform the majority of the enumeration tasks that a user account can have

# Shared Folders
- A shared folder object points to a shared folder on the specific computer where the folder resides
- Shared folders can have stringent access control applied to them and can be either accessible to everyone, open to only authenticated users, or be locked down to allow certain users/groups access
- Anyone not explicitly allowed access will be denied from listing or reading its contents
- Shared folders are NOT security principals and only have a GUID

# Groups
- A group is considered a contains objects because it can contain other objects, including users, computers, and even other groups
- Groups in AD can have many attributes, the most common being the name, description, membership, and other groups that the group belongs to

# Organizational Units (OUs)
- Container that system administrators can use to store similar objects for ease of administration
- OUs are often used for administrative delegation of tasks without granting a user account full administrative rights

# Domain
- A domain is the structure of an AD network
- Domains contain objects such as users and computers, which are organized into container objects: groups and OUs
- Every domain has its own separate database and sets of policies that can be applied to any and all within the domain

# Domain Controllers
- Domain controllers are essentially the brains of an AD network
- They handle authentication requests, verify users on the network, and control who can access the various resources in the domain
- All access request are validated via the domain controller and privileged access requests are based on predetermined roles assigned to users
- It also enforces security policies and stores information about very other object in the domain

# Sites
- A site in AD is a set of computers across one or more subnets connected using high-speed links
- They are used to make replication across domain controllers run efficiently

# Built-in
- In AD, built-in is a container that holds default groups in an AD domain
- They are predefined when an AD domain is created

# Foreign Security Principals
- A foreign security principal is an object created in AD to represent a security principal that belongs to a trusted external forest


## Active Directory Groups
- Groups are another key target for attackers and penetration tests, as the rights that they confer on their members may not be readily apparent but may grant excessive privileges

# Types of Groups
- Groups in Active Directory have two fundamental characteristics: type and scope.
- The group type defined the group's purpose, while the group scope shows how the group can be used within the domain or forest
- There are two main types
    - Security
    - Distribution
- The Security Groups type is primarily for ease of assigning permissions and rights to a collections of users instead of one at a time
- All users added to a security group will inherit any permissions assigned to the group, making it easier to move users in and out of groups while leaving the group's permissions unchanged
- The distribution group type is used by email applications such as Microsoft exchange to distribute messages to group members

# Group Scopes
- There are three different group scopes that can be assigned when creating a new group
    - Domain Local Group
    - Global Group
    - Universal Group
- Domain Local Group
    - Domain local groups can only be used to manage permissions to domain resources in the domain where it was created
- Global Group
    - Global groups can be used to grant access to resources in another domain
    - A global group can only contain accounts from the domain where it was created
- Universal Group
    - The universal group scope can be used to manage resources distributed across multiple domains and can be given permissions to any object within the same forest
    - They are avilable to all domains within an organization and can contain users from any domain
    - Unlike domain local and global groups, universal groups are stored in the Global Catalog, and adding or removing objects form a universal group triggers forest-wide replication
    - Replication is only triggered at the individual domain level when a user is removed from a global group
- Group scopes can be changed, but there are a few caveats:
    - A Global Group can only be converted to a Universal Group if it is NOT part of another Global Group
    - A Domain Local Group can only be converted to a Universal Group if the Domain Local Group does NOT contain any other Domain Local Groups as members
    - A Universal Group can be converted to a Domain Local Group without any restrictions


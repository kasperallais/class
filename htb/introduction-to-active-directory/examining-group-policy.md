## Examining Group Policy
- Windows feature that provides adminstrators with a wide arroy of advanced settings that can apply to both user and computer accounts in a Windows environment

# GPOs
- A Group Policy Object is a virtual collection of policy settings that can be applied to users or computers
- GPOs include policies such as screen lock timeouts, disabling USB ports, installing software, etc.
- GPOs settings are processed using the hierarchical structure of AD and are applied using the Order of Precedence rule

# GP Refresh Frequency
- When a GPO is created, the settings are not applied right away
- Windows periodically perform a Group Policy update, which is by default every 90 minutes
- Only 5 minutes for Domain Controllers
- We can use the gpupdate /force to kick off the update process


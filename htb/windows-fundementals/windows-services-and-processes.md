Windows Services
- Major component of the Windows operating system
- Allow for the creation and management of long-running processes
- Windows services can be started automatically at system boot without user intervention
- These services can continue to run in the background even after the user logs out of their account on the system
- Applications can be created to install as a service, such as a network monitoring application installed on a server
- Windows services are manged via the Service Control Manager (SCM) system, accessible via the services.msc MMC add-in
- It is also possible to query and manage services via the command line using sc.ex using PowerShell cmdlets such as Get-Service
- Service status can appear as Running, Stopped, or Paused, and they can be set to start manually, automatically, or on a delay at system boot
- Services can also be shown in the state of Starting or Stopping if some action has triggered them to either start or stop
- Windows has three categories of services: Local Services, Network Services, and System Services
- Misconfiguration around service permissions are a common privilege escalation vector on Windows systems
Processes
- Processes run in the background on Windows systems
- Processes associated with installed applications can often be terminated without causing a severe impact on the operating system
Local Security Authority Subsystem Service
- lsass.exe is the process that is responsible for enforcing the security policy on Windows systems.
- When a user attempts to log on to the system, this process verifies their log on attempt and creates access tokens based on the user's permission levels
- LSASS is also responsible for user account password changes
- LSASS is an extremely high-value target as several tools exist to extract both clear text and hashed credentials stored in memory by this process 
Sysinternals Tools
- Set of portable Windows applications that can be used to administer Windows systems
- The tools can be either downloaded from the Microsoft website or by loading them directly from an internet-accessible file share by typing "\\live.sysinternals.com\tools
- The suite includes tools such as Process Explorer, an enhanced version of Task Manager, and Process Monitor, which can be used to monitor file system, registry, and network activity related to any process running on the system.

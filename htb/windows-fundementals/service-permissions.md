Examining Services using services.msc
- Most services run with LocalSystem privileges by default which is the highest level of access allowed on an individual Windows OS
- Not all applications need Local System account-level permissions, so it is beneficial to perform a research on a case-by-case basis when considering installing new applications in a Windows environment
- Notable Built-in service account in Windows:
    - LocalService
    - NetworkService
    - LocalSystem
Examining services using sc
- 'sc qc' command is used to query the service
- If we wanted to query a service on a device over the network, we could specify the hostname or IP address immediately after sc
- We can also use sc to start and stop srevices
- Much more script friendly than services.msc
Examine service permissions using PowerShell
- Using the 'Get-Acl' PowerShell cmdlet, we can examine service permissions by targeting the path of a specific service in the registry

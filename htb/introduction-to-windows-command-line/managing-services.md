Service Controller
- SC is a Windows executable utility that allows us to query, modify, and manage host services locally and over the network
Query Services
- Query All Active Services: 'sc query type= service'
- Querying for Windows Defender: 'sc query windefend'
Stopping Services
- Stopping the Print Spooler Service: 'sc stop Spooler'
Starting Services
- Starting the Print Spooler Service: 'sc start Spooler'
Modifying Services
- Disabling Windows Update Service: 'sc config wuauserv start= disabled'
Using tasklist
- Shows us running tasks on a system, however using the '/svc' parameter we can see all running services
Using Net Start
- 'net start' with no parameters will also show all running services
Using WMIC
- Show all services with wmic: 'wmic service list brief'

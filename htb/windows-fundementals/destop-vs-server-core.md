Windows Server Core
- Released with Windows Server 2008 as a minimalistic Server environment only containing key Server functionality
- Server Core has lower management requirements, a smaller attack surface, and uses less disk space
- In Server Core, all configuration and maintenance tasks are performed via the command-line, PowerShell, or remote management with MMC or Remote Server Administration Tools (RSAT)
- Server Core still supports some graphical programs, such as Registry Editor, Notepad, System Information, etc.
- Initial config is done using Sconfig 
- Certain server applications cannot run on Server Core, including Microsoft Server Virtual Machine Manager 2019 and others
- Server core is lighter weight and less resource-intensive but has a steeper learning curve 

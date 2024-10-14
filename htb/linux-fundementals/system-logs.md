System Logs
- Set of files that contain information about the sytem and the activities taking place on it
- Important for monitoring and troubleshooting the sytem
- Different type of system logs
    - Kernel logs
    - System logs
    - Authentication logs
    - Application logs
    - Security logs
Kernel Logs
- Information about the system's kernel
- /var/log/kern.log
System Logs
- Information about system-level events
- /var/log/syslog
Authentication logs
- Informatoin about authentication attemps, including syccessful and failed attemps
- /var/log/auth.log
Application logs
- Information about the activities of specific applicaoitn running on the system
- /var/log/apache2/error.log
- Important when targeting specific applications, such as web servers or databases
Security Logs
- Often recorded in a variety of log files
- For example, Fail2ban records failed login attemps in the var/log/fail2ban.log

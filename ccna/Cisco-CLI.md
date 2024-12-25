What is a CLI?
- Command-line interface
- The interface you use to configure Cisco devices
- GUI (Graphical User Interface)
How to connect to a Cisco device (Console Port)
- Rollover cable
User EXEC Mode
- 'SYSTEM-NAME>'
- User EXEC mode is very limited
- Users can look at some things, but can't make any changes to the configuration
- Also called 'user mode'
Privileged EXEC Mode
- 'SYSTEM-NAME#'
- Enter using command enable
- Provides complete access to view the device's configuration, restart the device, etc.
- Cannot change the configuration, but can change the time on the device, save the configuration file, etc. 
Cisco IOS CLI Autocompletion
- Type in a character and then press tab
- If there is only one command that it can be it will just go to that
- You can do 'CHAR?' to see what commands end in that
Global Configuration Mode
- 'SYSTEM-NAME(config)#'
- Enter using 'configure terminal'
- Shortest possible command is 'conf t'
enable password
- 'enable password PASSWORD'
- The password odes not display as you type it (for security purposes)
running-config/startup-config
- There are two separate configuration files kept on the device at once
- Running-config = the current, active configuration file on the device. As you enter commands in the CLI, you edit the active configuration
- Startup-config = the configuration file that will be loaded upon the restart of the device 
- Use 'show running-config' to see the running configuration
- Use 'show startup-config' to see startup configuration 
- Three ways to save running configuration file
    - All are executed from Privileged EXEC Mode
    - write
    - write memory
    - copy running-config startup-config
Password Encryption
- Number before command in running-config shows encryption type (5 for MD5 Encryption, 7 for CISCO Proprietary)
- 'service password-encryption' will encrypt the password (Cisco-proprietary Encryption) DON'T USE
- 'enable secret PASSWORD'
- You can use 'do' to execute Privileged EXEC commands from Global Configuration Mode
- If both enable secret and enable password are enabled then enable password will be ignored 
- To delete a command from the running or startup config use 'no COMMAND'

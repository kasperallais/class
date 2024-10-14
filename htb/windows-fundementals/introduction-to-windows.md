The Windows Operating System
- Introduced on November 20th, 1985
- Graphical operating system shell for MS-DOS
- Windows 95 was the first full integration of Windows and DOS and offered built-in Internet support for the first time
- Debuted the Internet Explorer web browser
Windows Server
- Released in 1993
- IIS, networking protocols, Administrative Wizards
Local Access Concepts
- Most common way to access any computer
- Input is likely happening through a keyboard, trackpad &/or mouse
- Output is coming from the display screen
Remote Access Concepts
- Accessing a computer over a network
- Virtual Private Networks
- File Transfer Protocol
- Virtual Network Computing
- Windows Remote Management
- Remote Desktop Protocol
Remote Desktop Protocol (RDP)
- RDP listens by default on logical port 3389
- Once a request has reached a destination computer via its IP address, the request will be directed to an application hosted on the computer based on the port specified in that requets. 
- If we are connecting to a Windows target from aWindows host, we can use the built-in RDP clinet application called mstsc.exe
- For this to work, remote access must already be allowed on the target Windows System
xfreerdp
- From a Linux-based attack host we can use a tool called xfreerdp to remotely access Windows targets
Connecting to the Windows Target
- 'xfreerdp /v:<targetIp> /u:<user> /p:<password>

Server Message Block Protocol (SMB)
- Used in Windows to connect shared resources like files and printers
Share Permissions vs. NTFS Permissions
- Share Permissions
    - Full Control -> Users are permitted to perform all actions given by Change and Read Permissions as well as change permissions for NTFS files and subfolders
    - Change -> Users are permitted to read, edit, delete and add files and subfolders
    - Read -> Users are allowed to view file and subfolder contents
- NTFS Basic Permissions
    - Full Control -> Users are permitted to add, edit, move, delete files and folders as well as change NTFS permissions that apply to all allowed folders
    - Modify -> Users are permitted or denied permissions to view and modify files and folders
    - Read and Execute -> Users are permitted or denied permissions to read the contents of files and execute programs
    - List folder contents -> Users are permitted or denied permissions to view a listing of files and subfolders
    - Read -> Users are permitted or denied permissions to read the contents of files
    - Write -> Users are permitted or denied permissions to write changes to a file and add new files to a folder
    - Special Permissions -> A variety of advanced permissions options
Creating a Network Share
Windows Defender Firewall Considerations
- Since we are connecting from a Linux-based system the firewall has blocked access from any device that is not joined to the same work group.
- When a Windows system is joined to a Windows Domain environment, all netlogon requests are authenticated against Active Directory
- It is very common for firewalls to be left completely deactivated for the sake of convenience or lack of understanding

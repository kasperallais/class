Windows File Systems
- Fat12, Fat16, Fat32, NTFS, and exFat
- Fat12 and Fat16 are no longer used
- Fat32 is widely used across many types of storage devices such as USB memory sticks and SD cards but can also be used to format hard drives
Fat32 Pros and Cons
- Pros:
    - Device compatibility - it can be used on computers, digital cameras, gaming consoles, smartphones, tablets, and more.
    - Operating System Compatibility - It works on all Windows operating system starting from Windows 95 and is also supported by MacOS and Linux
- Cons:
    - Can only be used with files less than 4GB
    - No built-in data protection or files compression
    - Must use third-party tools for encryption
NTFS
- Default Windows file system since Windows NT 3.1
- Better support for metadata and better performance due to improved data structuring.
NTFS Pros and Cons
- Reliable and can restore the consistency of the file in the event of a system failure or power loss
- Provides security by allowing us to set granular permissions on both files and folders
- Supports very large-sized partitions
- Has journaling built-in, meaning that file modifications are logged
Cons of NTFS:
- Most mobile devices do not support NTFS natively
- Older media devices such as TVs and digital cameras do not offer support for NTFS storage devices
Permissions
- Full Control -> Allows reading writing, changing, deleting of files/folders
- Modify -> Allows reading, writing, and deleting of files/folders
- List Folder Contents -> Allows for viewing and listing folders and subfolders as well as executing files. Folders only inherit this permissions
- Read and Execute -> Allows for viewing and listing files and subfolders as well as executing files. Files and folders inherit this permission
- Write -> Allows for adding files to folders and subfolders and writing to file
- Read -> Allows for viewing and listing of folders and subfolders and viewing a file's contents
- Traverse folder -> This allows or denies the ability to move through folders to reach other files or folders
- Files and folders inherit the NTFS permissions of their parents folder for ease of administration
Integrity Control Access Control List
- We can list out the NTFS permissions on a specific directory by running icacls
- The resource access level is listed after each user in the output
- The possible settings are:
    - (CI) -> Container inherit
    - (OI) -> Object inherit
    - (IO) -> Inherit only
    - (NP) -> Do not propagate inherit
    - (I) -> Permission inherited from parent container
- Basic access permissions are as follows:
    - F -> Full Access
    - D -> Delete Access
    - N -> No Access
    - M -> Modify Access
    - RX -> Read and execute access
    - R -> Read-only access
    - W -> Write-only access
- We can add and remove permissions via the command line using icacls
- Using the command 'icacls c:\users /grant joe:f' we cna grand the joe user full control over the directory
- These permissions can be revoked using the command 'icacls c:\users /remove joe'

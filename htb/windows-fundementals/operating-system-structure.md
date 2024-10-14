Operating System Structure
- The root directory is <drive_letter>:\
- The root directory is where the operating system is installed
- Other physical drives are assigned other letters
Directory Structure
- Perlogs -> Performance logs but empty by default
- Program Files -> On 32 bit system, 16-bit and 32-bit programs are installed here. On 64-bit, only 64-bit programs are here.
- Program Files (x86) -> 32-bit and 16-bit programs are installed here on 64-bit editions
- ProgramData -> Hidden folder that contains data that is essential for certain installed programs to run
- Users -> User profiles for each user that logs onto the system
- Default -> Default user profile template for all created users
- Public -> Intended for computers to share files and is accessible to all users by default
- AppData -> Per user application data and settings are stored in a hidden user subfolder. Each of these folders contains three subfolders. The roaming folder contains machine-independent data that should follow the user's profile. The local d- Windows -> Majority of the files required for the Windows operating system are contained here
- System, System32, SysWOW64 -> Contains all DLLs required for the core features of the Windows and the Windows API. The operating system searches these folders any time a program asks to load a DLL without specifying an absolute path
- WinSxS -> Windows component store contains a copy of all Windows components, updates, and service packs
Exploring Directories Using Command Line
- 'dir <drive> <options>' -> List all files in a directory
- 'tree "<folder>"' -> List tree diagram of a folder


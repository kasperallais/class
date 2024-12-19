Why choose PowerShell over CMD.exe
- PowerShell is built for automation
- PowerShell's logging and history capability makes is powerful and will log more of our interactions with the host
- If we need to be more stealthy we should use CMD
Using Get-Help
- Test-Wsman Example: 'Get-Help Test-Wsman'
Using Update-Help
- Updates the Help command with more information
Where are we?
- We can find our current path using the 'Get-Location' cmdlet
List the current directory
- Use the 'Get-ChildItem' cmdlet
Move to a New Directory
- Use the 'Set-Location' cmdlet
- Move example: 'Set-Location .\Documents\'
Display the contents of a file
- 'Get-Content' cmdlet
- Example: 'Get-Content Readme.md'
Find a cmdlet
- 'Get-Command' cmdlet
- Get all cmdlets example: 'Get-Command'
- Get a specific cmdlet (verb): 'Get-Command -verb get'
- Get a specific cmdlet (noun): 'Get-Command -noun windows'
- 'Get-Command' works with wildcards
History
- 'Get-History' cmdlet
Viewing PSReadLine History
- 'get-content C:\Users\DLarusso\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt'
- Automatically tries to sort entries
Clear Screen
- 'Clear-Host' cmdlet
- We can also use clear or cls alternatives
Tab Completion
- Use 'tab' and 'SHIFT+tab' to autocomplete and move through autocomplete options
Aliases
- 'Get-Alias' cmdlet
Using Set-Alias
- 'Set-Alias' cmdlet
- 'Set-Alias -Name gh -Value Get-Help'

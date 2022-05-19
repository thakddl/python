Set WshShell = CreateObject ("WScript.shell")
Dim strArgs
strArgs = "cmd /c + mycrawl.bat"
WshShell.Run strArgs, 0, false
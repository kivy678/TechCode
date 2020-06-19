forfiles /P [path] /M *.dmp /D -5 /C "cmd /c del @file"
psftp.exe -b [path]\setting.txt [host] -P [port] -l [id] -pw [password]

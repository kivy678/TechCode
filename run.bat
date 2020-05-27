@echo off

:: find python version 3
FOR /F "tokens=2" %%v in ('python -V') DO SET var=%%v

if %var:~0,1% == 3 (
	echo Find PYTHON3
	goto INSTALL
) ELSE (
	echo NO PYTHON3
	goto EXIT
)

:: install env
:INSTALL
echo %~dp0

SET ENV_DIR=.env

IF EXIST  %~dp0%ENV_DIR% (
	echo [*] run
	%~dp0%ENV_DIR%\scripts\activate && python %~dp0run.py && deactivate
) ELSE (
	echo [*] Install virutalenv
	virtualenv %~dp0%ENV_DIR%
	%~dp0%ENV_DIR%\scripts\activate && pip install -r %~dp0requirements.txt && deactivate
	goto INSTALL
)

:EXIT
echo stript done
pause

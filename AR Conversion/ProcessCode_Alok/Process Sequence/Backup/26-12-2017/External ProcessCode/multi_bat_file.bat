@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /R "D:\AR Conversion\ProcessCode_Alok\Request\External Process Sql Request" %%c in (cedbba43-d761-40f2-a871-edd4516f8834_Num1-1_Pending.txt) DO (
FOR /F "tokens=*" %%A in ('Type "%%c"') DO (
rem echo %%c
call :check
START /MIN "" "D:\AR Conversion\ProcessCode_Alok\Process Sequence\External ProcessCode\Multi_Open_And_Read_Excel_Omni.py" "%%A"
)
)
call :check1
ENDLOCAL
Exit

:retrywait1
TIMEOUT 5 /nobreak

:check1
FOR /F %%i IN (' "WMIC process get commandline | find /I /C "Multi_Open_And_Read_Excel_Omni.py"" ') DO SET X=%%i
echo !X!
IF !X! GTR 3 GOTO retrywait1

:retrywait
TIMEOUT 5 /nobreak

:check
FOR /F %%i IN (' "WMIC process get commandline | find /I /C "Multi_Open_And_Read_Excel_Omni.py"" ') DO SET X=%%i
echo !X!
IF !X! GTR 10 GOTO retrywait

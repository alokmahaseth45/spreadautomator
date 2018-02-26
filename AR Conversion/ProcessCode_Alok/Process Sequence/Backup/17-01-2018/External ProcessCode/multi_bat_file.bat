@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /R "D:\AR Conversion\ProcessCode_Alok\Request\External Process Sql Request" %%c in (605d8072-048e-445f-bac7-9155cd5dd2ac_Num2-4_Pending.txt) DO (
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

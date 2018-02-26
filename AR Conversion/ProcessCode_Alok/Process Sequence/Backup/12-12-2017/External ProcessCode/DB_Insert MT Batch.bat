TITLE IEC
@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /R "D:\AR Conversion\ProcessCode_Alok\Request\External Process Sql Request" %%c in (5329150317_Num1-4_Converted.txt) DO (
FOR /F "tokens=*" %%A in ('Type "%%c"') DO (
rem echo %%c
call :check
START /MIN "" "D:\AR Conversion\ProcessCode_Alok\Open Excel And Read Data\open_And_Read_Excel_Omni Test.py" "%%A"
)
)
ENDLOCAL
Exit

:retrywait
TIMEOUT 6 /nobreak

:check
FOR /F %%i IN (' "tasklist | find /I /C "python.exe"" ') DO SET X=%%i
echo !X!
IF !X! GTR 20 GOTO retrywait
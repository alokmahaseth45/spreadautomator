call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "066a3989-fa44-4c73-87a8-2cae05bd7f82"
echo SPV_AR_Process_Internal_P2 for RequestId-066a3989-fa44-4c73-87a8-2cae05bd7f82   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 '066a3989-fa44-4c73-87a8-2cae05bd7f82' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2066a3989-fa44-4c73-87a8-2cae05bd7f82@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-066a3989-fa44-4c73-87a8-2cae05bd7f82   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"

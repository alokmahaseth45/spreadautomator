call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "83c69de2-f18d-4517-97f4-01ff1edf24e0"
echo SPV_AR_Process_Internal_P2 for RequestId-83c69de2-f18d-4517-97f4-01ff1edf24e0   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 '83c69de2-f18d-4517-97f4-01ff1edf24e0' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P283c69de2-f18d-4517-97f4-01ff1edf24e0@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-83c69de2-f18d-4517-97f4-01ff1edf24e0   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
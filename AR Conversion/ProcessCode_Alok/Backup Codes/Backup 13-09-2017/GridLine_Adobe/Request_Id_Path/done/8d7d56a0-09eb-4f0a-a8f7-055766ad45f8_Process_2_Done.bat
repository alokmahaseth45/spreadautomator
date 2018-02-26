call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "8d7d56a0-09eb-4f0a-a8f7-055766ad45f8"
echo SPV_AR_Process_2 for RequestId-8d7d56a0-09eb-4f0a-a8f7-055766ad45f8   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '8d7d56a0-09eb-4f0a-a8f7-055766ad45f8' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_18d7d56a0-09eb-4f0a-a8f7-055766ad45f8@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-8d7d56a0-09eb-4f0a-a8f7-055766ad45f8   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

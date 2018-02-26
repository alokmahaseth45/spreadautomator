call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "085dd367-98be-40e0-b912-12130394ab31"
echo SPV_AR_Process_2 for RequestId-085dd367-98be-40e0-b912-12130394ab31   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '085dd367-98be-40e0-b912-12130394ab31' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1085dd367-98be-40e0-b912-12130394ab31@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-085dd367-98be-40e0-b912-12130394ab31   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

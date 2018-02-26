call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "4f97900c-be4a-458b-aabb-7df43590ce43"
echo SPV_AR_Process_2 for RequestId-4f97900c-be4a-458b-aabb-7df43590ce43   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '4f97900c-be4a-458b-aabb-7df43590ce43' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_14f97900c-be4a-458b-aabb-7df43590ce43@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-4f97900c-be4a-458b-aabb-7df43590ce43   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

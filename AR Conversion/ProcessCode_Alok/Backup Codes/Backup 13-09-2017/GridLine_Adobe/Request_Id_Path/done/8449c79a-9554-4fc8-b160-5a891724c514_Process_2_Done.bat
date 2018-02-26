call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "8449c79a-9554-4fc8-b160-5a891724c514"
echo SPV_AR_Process_2 for RequestId-8449c79a-9554-4fc8-b160-5a891724c514   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '8449c79a-9554-4fc8-b160-5a891724c514' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_18449c79a-9554-4fc8-b160-5a891724c514@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-8449c79a-9554-4fc8-b160-5a891724c514   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

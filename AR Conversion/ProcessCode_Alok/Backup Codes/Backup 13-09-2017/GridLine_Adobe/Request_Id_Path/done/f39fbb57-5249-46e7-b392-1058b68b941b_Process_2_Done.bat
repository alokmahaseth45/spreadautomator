call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "f39fbb57-5249-46e7-b392-1058b68b941b"
echo SPV_AR_Process_2 for RequestId-f39fbb57-5249-46e7-b392-1058b68b941b   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'f39fbb57-5249-46e7-b392-1058b68b941b' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1f39fbb57-5249-46e7-b392-1058b68b941b@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-f39fbb57-5249-46e7-b392-1058b68b941b   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "58b4cd85-93e8-4769-947f-b17b626380f3"
echo SPV_AR_Process_2 for RequestId-58b4cd85-93e8-4769-947f-b17b626380f3   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '58b4cd85-93e8-4769-947f-b17b626380f3' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_158b4cd85-93e8-4769-947f-b17b626380f3@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-58b4cd85-93e8-4769-947f-b17b626380f3   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

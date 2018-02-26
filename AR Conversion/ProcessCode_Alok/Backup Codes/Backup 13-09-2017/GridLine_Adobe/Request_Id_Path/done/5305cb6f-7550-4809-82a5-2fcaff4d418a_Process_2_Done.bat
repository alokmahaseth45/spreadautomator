call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "5305cb6f-7550-4809-82a5-2fcaff4d418a"
echo SPV_AR_Process_2 for RequestId-5305cb6f-7550-4809-82a5-2fcaff4d418a   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '5305cb6f-7550-4809-82a5-2fcaff4d418a' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_15305cb6f-7550-4809-82a5-2fcaff4d418a@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-5305cb6f-7550-4809-82a5-2fcaff4d418a   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

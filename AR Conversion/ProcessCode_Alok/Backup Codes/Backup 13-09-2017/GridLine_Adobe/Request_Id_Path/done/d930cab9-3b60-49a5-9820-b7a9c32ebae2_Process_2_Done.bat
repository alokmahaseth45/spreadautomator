call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "d930cab9-3b60-49a5-9820-b7a9c32ebae2"
echo SPV_AR_Process_2 for RequestId-d930cab9-3b60-49a5-9820-b7a9c32ebae2   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'd930cab9-3b60-49a5-9820-b7a9c32ebae2' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1d930cab9-3b60-49a5-9820-b7a9c32ebae2@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-d930cab9-3b60-49a5-9820-b7a9c32ebae2   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

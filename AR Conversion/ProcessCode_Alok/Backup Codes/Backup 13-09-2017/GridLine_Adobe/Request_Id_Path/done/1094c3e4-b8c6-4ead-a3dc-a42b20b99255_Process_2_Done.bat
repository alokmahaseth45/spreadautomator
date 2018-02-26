call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "1094c3e4-b8c6-4ead-a3dc-a42b20b99255"
echo SPV_AR_Process_2 for RequestId-1094c3e4-b8c6-4ead-a3dc-a42b20b99255   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '1094c3e4-b8c6-4ead-a3dc-a42b20b99255' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_11094c3e4-b8c6-4ead-a3dc-a42b20b99255@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-1094c3e4-b8c6-4ead-a3dc-a42b20b99255   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

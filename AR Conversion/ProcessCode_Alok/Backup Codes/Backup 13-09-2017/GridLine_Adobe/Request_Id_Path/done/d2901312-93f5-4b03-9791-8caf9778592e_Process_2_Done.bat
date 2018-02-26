call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "d2901312-93f5-4b03-9791-8caf9778592e"
echo SPV_AR_Process_2 for RequestId-d2901312-93f5-4b03-9791-8caf9778592e   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'd2901312-93f5-4b03-9791-8caf9778592e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1d2901312-93f5-4b03-9791-8caf9778592e@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-d2901312-93f5-4b03-9791-8caf9778592e   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

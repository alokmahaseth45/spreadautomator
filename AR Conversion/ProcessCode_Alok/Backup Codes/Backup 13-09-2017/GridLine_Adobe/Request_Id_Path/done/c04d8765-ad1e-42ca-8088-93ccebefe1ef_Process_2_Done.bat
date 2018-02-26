call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "c04d8765-ad1e-42ca-8088-93ccebefe1ef"
echo SPV_AR_Process_2 for RequestId-c04d8765-ad1e-42ca-8088-93ccebefe1ef   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'c04d8765-ad1e-42ca-8088-93ccebefe1ef' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1c04d8765-ad1e-42ca-8088-93ccebefe1ef@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-c04d8765-ad1e-42ca-8088-93ccebefe1ef   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

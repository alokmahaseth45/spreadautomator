call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "877fab10-123f-4f2b-a5c1-70cf52749246"
echo SPV_AR_Process_2 for RequestId-877fab10-123f-4f2b-a5c1-70cf52749246   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '877fab10-123f-4f2b-a5c1-70cf52749246' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1877fab10-123f-4f2b-a5c1-70cf52749246@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-877fab10-123f-4f2b-a5c1-70cf52749246   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "03fd7e0e-efa0-4183-9821-59eb095cdd5a"
echo SPV_AR_Process_2 for RequestId-03fd7e0e-efa0-4183-9821-59eb095cdd5a   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '03fd7e0e-efa0-4183-9821-59eb095cdd5a' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_103fd7e0e-efa0-4183-9821-59eb095cdd5a@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-03fd7e0e-efa0-4183-9821-59eb095cdd5a   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "d262aa81-218f-46ab-921e-288b09d9bf34"
echo SPV_AR_Process_Internal_P2 for RequestId-d262aa81-218f-46ab-921e-288b09d9bf34   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 'd262aa81-218f-46ab-921e-288b09d9bf34' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2d262aa81-218f-46ab-921e-288b09d9bf34@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-d262aa81-218f-46ab-921e-288b09d9bf34   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"

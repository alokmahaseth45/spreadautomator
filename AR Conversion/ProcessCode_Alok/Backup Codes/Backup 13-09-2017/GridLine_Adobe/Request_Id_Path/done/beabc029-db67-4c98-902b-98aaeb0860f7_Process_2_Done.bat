call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "beabc029-db67-4c98-902b-98aaeb0860f7"
echo SPV_AR_Process_2 for RequestId-beabc029-db67-4c98-902b-98aaeb0860f7   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'beabc029-db67-4c98-902b-98aaeb0860f7' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1beabc029-db67-4c98-902b-98aaeb0860f7@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-beabc029-db67-4c98-902b-98aaeb0860f7   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

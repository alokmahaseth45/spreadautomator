call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "73bd444d-d8ce-4a0c-8c99-8904741f8658"
echo SPV_AR_Process_2 for RequestId-73bd444d-d8ce-4a0c-8c99-8904741f8658   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '73bd444d-d8ce-4a0c-8c99-8904741f8658' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_173bd444d-d8ce-4a0c-8c99-8904741f8658@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-73bd444d-d8ce-4a0c-8c99-8904741f8658   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

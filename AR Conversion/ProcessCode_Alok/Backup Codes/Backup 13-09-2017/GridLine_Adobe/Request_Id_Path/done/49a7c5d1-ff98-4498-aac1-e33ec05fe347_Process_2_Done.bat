call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "49a7c5d1-ff98-4498-aac1-e33ec05fe347"
echo SPV_AR_Process_2 for RequestId-49a7c5d1-ff98-4498-aac1-e33ec05fe347   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '49a7c5d1-ff98-4498-aac1-e33ec05fe347' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_149a7c5d1-ff98-4498-aac1-e33ec05fe347@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-49a7c5d1-ff98-4498-aac1-e33ec05fe347   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

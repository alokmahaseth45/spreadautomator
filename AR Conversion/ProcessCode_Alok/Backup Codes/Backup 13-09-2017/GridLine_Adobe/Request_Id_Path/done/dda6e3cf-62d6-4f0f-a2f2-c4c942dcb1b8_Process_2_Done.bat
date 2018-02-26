call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "dda6e3cf-62d6-4f0f-a2f2-c4c942dcb1b8"
echo SPV_AR_Process_2 for RequestId-dda6e3cf-62d6-4f0f-a2f2-c4c942dcb1b8   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'dda6e3cf-62d6-4f0f-a2f2-c4c942dcb1b8' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1dda6e3cf-62d6-4f0f-a2f2-c4c942dcb1b8@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-dda6e3cf-62d6-4f0f-a2f2-c4c942dcb1b8   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

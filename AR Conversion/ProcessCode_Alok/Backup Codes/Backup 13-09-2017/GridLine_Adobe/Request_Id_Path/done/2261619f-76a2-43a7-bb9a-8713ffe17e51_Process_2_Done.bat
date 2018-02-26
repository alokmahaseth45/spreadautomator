call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "2261619f-76a2-43a7-bb9a-8713ffe17e51"
echo SPV_AR_Process_2 for RequestId-2261619f-76a2-43a7-bb9a-8713ffe17e51   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '2261619f-76a2-43a7-bb9a-8713ffe17e51' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_12261619f-76a2-43a7-bb9a-8713ffe17e51@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-2261619f-76a2-43a7-bb9a-8713ffe17e51   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

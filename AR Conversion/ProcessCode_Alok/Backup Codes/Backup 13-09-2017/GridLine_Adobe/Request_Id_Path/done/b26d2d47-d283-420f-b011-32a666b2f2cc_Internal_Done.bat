call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "b26d2d47-d283-420f-b011-32a666b2f2cc"
echo SPV_AR_Process_Internal_P2 for RequestId-b26d2d47-d283-420f-b011-32a666b2f2cc   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 'b26d2d47-d283-420f-b011-32a666b2f2cc' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2b26d2d47-d283-420f-b011-32a666b2f2cc@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-b26d2d47-d283-420f-b011-32a666b2f2cc   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
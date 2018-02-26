call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "ad446019-632d-45fd-87c9-119ec058de43"
echo SPV_AR_Process_2 for RequestId-ad446019-632d-45fd-87c9-119ec058de43   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'ad446019-632d-45fd-87c9-119ec058de43' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1ad446019-632d-45fd-87c9-119ec058de43@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-ad446019-632d-45fd-87c9-119ec058de43   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

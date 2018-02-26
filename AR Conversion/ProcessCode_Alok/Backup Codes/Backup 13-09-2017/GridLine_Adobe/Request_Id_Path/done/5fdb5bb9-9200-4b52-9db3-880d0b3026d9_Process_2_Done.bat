call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "5fdb5bb9-9200-4b52-9db3-880d0b3026d9"
echo SPV_AR_Process_2 for RequestId-5fdb5bb9-9200-4b52-9db3-880d0b3026d9   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '5fdb5bb9-9200-4b52-9db3-880d0b3026d9' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_15fdb5bb9-9200-4b52-9db3-880d0b3026d9@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-5fdb5bb9-9200-4b52-9db3-880d0b3026d9   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

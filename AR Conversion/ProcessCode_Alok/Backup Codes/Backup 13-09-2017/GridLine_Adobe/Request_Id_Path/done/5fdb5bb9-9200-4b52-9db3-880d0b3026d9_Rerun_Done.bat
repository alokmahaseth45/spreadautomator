echo RerunSPV_AR_Process_Internal_P1 for RequestId-5fdb5bb9-9200-4b52-9db3-880d0b3026d9   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P1 '5fdb5bb9-9200-4b52-9db3-880d0b3026d9' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15fdb5bb9-9200-4b52-9db3-880d0b3026d9@%date:/=-%_%time::=^%.txt"
echo RerunSPV_AR_Process_Internal_P1 for RequestId-5fdb5bb9-9200-4b52-9db3-880d0b3026d9   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"
echo RerunSPV_AR_Process_Internal_P1 for RequestId-17c0d39c-a9d5-46cb-b4ed-18f27811c7e0   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P1 '17c0d39c-a9d5-46cb-b4ed-18f27811c7e0' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P117c0d39c-a9d5-46cb-b4ed-18f27811c7e0@%date:/=-%_%time::=^%.txt"
echo RerunSPV_AR_Process_Internal_P1 for RequestId-17c0d39c-a9d5-46cb-b4ed-18f27811c7e0   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"

echo RerunSPV_AR_Process_Internal_P1 for RequestId-d2901312-93f5-4b03-9791-8caf9778592e   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P1 'd2901312-93f5-4b03-9791-8caf9778592e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1d2901312-93f5-4b03-9791-8caf9778592e@%date:/=-%_%time::=^%.txt"
echo RerunSPV_AR_Process_Internal_P1 for RequestId-d2901312-93f5-4b03-9791-8caf9778592e   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"
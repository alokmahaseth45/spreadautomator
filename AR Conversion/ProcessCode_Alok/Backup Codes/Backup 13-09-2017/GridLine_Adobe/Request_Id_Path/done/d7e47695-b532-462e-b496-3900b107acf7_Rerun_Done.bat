echo RerunSPV_AR_Process_Internal_P1 for RequestId-d7e47695-b532-462e-b496-3900b107acf7   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P1 'd7e47695-b532-462e-b496-3900b107acf7' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1d7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
echo RerunSPV_AR_Process_Internal_P1 for RequestId-d7e47695-b532-462e-b496-3900b107acf7   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"

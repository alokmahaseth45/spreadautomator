echo RerunSPV_AR_Process_Internal_P1 for RequestId-ef9f1b1b-8305-4590-b6bd-ab773a3f7f15   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P1 'ef9f1b1b-8305-4590-b6bd-ab773a3f7f15' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1ef9f1b1b-8305-4590-b6bd-ab773a3f7f15@%date:/=-%_%time::=^%.txt"
echo RerunSPV_AR_Process_Internal_P1 for RequestId-ef9f1b1b-8305-4590-b6bd-ab773a3f7f15   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P1.txt"

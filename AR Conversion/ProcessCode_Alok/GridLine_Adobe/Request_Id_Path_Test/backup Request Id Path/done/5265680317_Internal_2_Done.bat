echo Start Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5265680317_Internal_2.txt"
sqlcmd -E -S localhost -d Pdf_Gridlines -Q "Exec SPV_AR_Process_DeleteGridlineData '5265680317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_DeleteGridlineData5265680317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5265680317','Internal 2 Proc Start' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15265680317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-5265680317   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 '5265680317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P25265680317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-5265680317   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
echo End Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5265680317_Internal_2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5265680317','Complete' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15265680317@%date:/=-%_%time::=^%.txt"

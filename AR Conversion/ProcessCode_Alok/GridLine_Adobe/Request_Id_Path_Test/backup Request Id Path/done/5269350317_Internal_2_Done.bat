echo Start Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5269350317_Internal_2.txt"
sqlcmd -E -S localhost -d Pdf_Gridlines -Q "Exec SPV_AR_Process_DeleteGridlineData '5269350317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_DeleteGridlineData5269350317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5269350317','Internal 2 Proc Start' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15269350317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-5269350317   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 '5269350317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P25269350317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-5269350317   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
echo End Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5269350317_Internal_2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5269350317','Complete' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15269350317@%date:/=-%_%time::=^%.txt"

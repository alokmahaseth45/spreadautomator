call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "5238620317" "Internal_1"
echo Start Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5238620317_Internal_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5238620317','Internal 1 Proc Start' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15238620317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-5238620317   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '5238620317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_15238620317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-5238620317   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
echo End Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5238620317_Internal_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5238620317','Internal 1 Proc End' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15238620317@%date:/=-%_%time::=^%.txt"

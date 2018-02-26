rem call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "5238280317" "Internal_2"
echo Start Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5238280317_Internal_2.txt"
sqlcmd -E -S localhost -d Pdf_Gridlines -Q "Exec SPV_AR_Process_DeleteGridlineData '5238280317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_DeleteGridlineData5238280317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5238280317','Internal 2 Proc Start' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15238280317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-5238280317   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 '5238280317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P25238280317@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-5238280317   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
echo Mapping for RequestId-5238280317   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\Mapping.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_BS '5238280317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_BS5238280317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_PL '5238280317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_PL5238280317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_BS '5238280317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_BS5238280317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_PL '5238280317' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_PL5238280317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched '5238280317','BS' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matched5238280317@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched '5238280317','PL' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matched5238280317@%date:/=-%_%time::=^%.txt"
echo Mapping for RequestId-5238280317   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\Mapping.txt"
echo End Date_Time proc call-->%date% %time%>>"D:\AR Conversion\ProcessCode_Alok\Log\5238280317_Internal_2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SP_Read_Conversion_Log '5238280317','Complete' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunSPV_AR_Process_Internal_P15238280317@%date:/=-%_%time::=^%.txt"

echo RerunMapping for RequestId-2261619f-76a2-43a7-bb9a-8713ffe17e51   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunMapping.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_BS '2261619f-76a2-43a7-bb9a-8713ffe17e51' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_BS2261619f-76a2-43a7-bb9a-8713ffe17e51@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_PL '2261619f-76a2-43a7-bb9a-8713ffe17e51' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_PL2261619f-76a2-43a7-bb9a-8713ffe17e51@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_BS '2261619f-76a2-43a7-bb9a-8713ffe17e51' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_BS2261619f-76a2-43a7-bb9a-8713ffe17e51@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_PL '2261619f-76a2-43a7-bb9a-8713ffe17e51' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_PL2261619f-76a2-43a7-bb9a-8713ffe17e51@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched '2261619f-76a2-43a7-bb9a-8713ffe17e51','BS' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matched2261619f-76a2-43a7-bb9a-8713ffe17e51@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched '2261619f-76a2-43a7-bb9a-8713ffe17e51','PL' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matched2261619f-76a2-43a7-bb9a-8713ffe17e51@%date:/=-%_%time::=^%.txt"
echo RerunMapping for RequestId-2261619f-76a2-43a7-bb9a-8713ffe17e51   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunMapping.txt"
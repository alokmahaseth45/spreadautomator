echo RerunMapping for RequestId-d7e47695-b532-462e-b496-3900b107acf7   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunMapping.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_BS 'd7e47695-b532-462e-b496-3900b107acf7' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_BSd7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_PL 'd7e47695-b532-462e-b496-3900b107acf7' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_PLd7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_BS 'd7e47695-b532-462e-b496-3900b107acf7' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_BSd7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_PL 'd7e47695-b532-462e-b496-3900b107acf7' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_PLd7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched 'd7e47695-b532-462e-b496-3900b107acf7','BS' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matchedd7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched 'd7e47695-b532-462e-b496-3900b107acf7','PL' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matchedd7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
echo RerunMapping for RequestId-d7e47695-b532-462e-b496-3900b107acf7   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\RerunMapping.txt"

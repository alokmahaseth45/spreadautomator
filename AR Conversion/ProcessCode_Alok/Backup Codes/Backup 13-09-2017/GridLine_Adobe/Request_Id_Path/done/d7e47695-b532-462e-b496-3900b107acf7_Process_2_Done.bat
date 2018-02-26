call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "d7e47695-b532-462e-b496-3900b107acf7"
echo SPV_AR_Process_2 for RequestId-d7e47695-b532-462e-b496-3900b107acf7   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'd7e47695-b532-462e-b496-3900b107acf7' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1d7e47695-b532-462e-b496-3900b107acf7@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-d7e47695-b532-462e-b496-3900b107acf7   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "31d747aa-8dc0-4f20-9e3c-18d6cd106ce3"
echo SPV_AR_Process_Internal_P2 for RequestId-31d747aa-8dc0-4f20-9e3c-18d6cd106ce3   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P231d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-31d747aa-8dc0-4f20-9e3c-18d6cd106ce3   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
echo Mapping for RequestId-31d747aa-8dc0-4f20-9e3c-18d6cd106ce3   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\Mapping.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_BS '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_BS31d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_PL '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_PL31d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_BS '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_BS31d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_PL '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_PL31d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3','BS' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matched31d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3','PL' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matched31d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
echo Mapping for RequestId-31d747aa-8dc0-4f20-9e3c-18d6cd106ce3   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\Mapping.txt"

call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "fe896085-5f70-4a0a-bcea-0e27cbfa540e"
echo SPV_AR_Process_Internal_P2 for RequestId-fe896085-5f70-4a0a-bcea-0e27cbfa540e   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 'fe896085-5f70-4a0a-bcea-0e27cbfa540e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2fe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-fe896085-5f70-4a0a-bcea-0e27cbfa540e   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
echo Mapping for RequestId-fe896085-5f70-4a0a-bcea-0e27cbfa540e   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\Mapping.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_BS 'fe896085-5f70-4a0a-bcea-0e27cbfa540e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_BSfe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Rerun_Mapping_PL 'fe896085-5f70-4a0a-bcea-0e27cbfa540e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Rerun_Mapping_PLfe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_BS 'fe896085-5f70-4a0a-bcea-0e27cbfa540e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_BSfe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Parent_PL 'fe896085-5f70-4a0a-bcea-0e27cbfa540e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Parent_PLfe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched 'fe896085-5f70-4a0a-bcea-0e27cbfa540e','BS' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matchedfe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_Update_Total_Matched 'fe896085-5f70-4a0a-bcea-0e27cbfa540e','PL' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_Update_Total_Matchedfe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
echo Mapping for RequestId-fe896085-5f70-4a0a-bcea-0e27cbfa540e   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\Mapping.txt"

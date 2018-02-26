call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "fe896085-5f70-4a0a-bcea-0e27cbfa540e"
echo SPV_AR_Process_2 for RequestId-fe896085-5f70-4a0a-bcea-0e27cbfa540e   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 'fe896085-5f70-4a0a-bcea-0e27cbfa540e' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1fe896085-5f70-4a0a-bcea-0e27cbfa540e@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-fe896085-5f70-4a0a-bcea-0e27cbfa540e   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

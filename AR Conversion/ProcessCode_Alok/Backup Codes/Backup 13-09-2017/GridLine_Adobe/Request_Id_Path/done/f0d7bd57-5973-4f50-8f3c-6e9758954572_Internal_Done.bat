call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "f0d7bd57-5973-4f50-8f3c-6e9758954572"
echo SPV_AR_Process_Internal_P2 for RequestId-f0d7bd57-5973-4f50-8f3c-6e9758954572   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 'f0d7bd57-5973-4f50-8f3c-6e9758954572' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2f0d7bd57-5973-4f50-8f3c-6e9758954572@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-f0d7bd57-5973-4f50-8f3c-6e9758954572   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
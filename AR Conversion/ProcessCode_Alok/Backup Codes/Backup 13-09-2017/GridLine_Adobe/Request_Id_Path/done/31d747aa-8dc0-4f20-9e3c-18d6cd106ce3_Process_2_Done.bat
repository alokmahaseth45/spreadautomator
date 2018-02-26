call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "31d747aa-8dc0-4f20-9e3c-18d6cd106ce3"
echo SPV_AR_Process_2 for RequestId-31d747aa-8dc0-4f20-9e3c-18d6cd106ce3   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '31d747aa-8dc0-4f20-9e3c-18d6cd106ce3' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_131d747aa-8dc0-4f20-9e3c-18d6cd106ce3@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-31d747aa-8dc0-4f20-9e3c-18d6cd106ce3   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

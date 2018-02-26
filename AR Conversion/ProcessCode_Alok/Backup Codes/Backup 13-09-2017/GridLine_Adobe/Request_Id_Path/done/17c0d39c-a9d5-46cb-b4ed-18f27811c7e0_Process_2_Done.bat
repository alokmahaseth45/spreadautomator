call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "17c0d39c-a9d5-46cb-b4ed-18f27811c7e0"
echo SPV_AR_Process_2 for RequestId-17c0d39c-a9d5-46cb-b4ed-18f27811c7e0   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_2 '17c0d39c-a9d5-46cb-b4ed-18f27811c7e0' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_117c0d39c-a9d5-46cb-b4ed-18f27811c7e0@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_2 for RequestId-17c0d39c-a9d5-46cb-b4ed-18f27811c7e0   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_1.txt"

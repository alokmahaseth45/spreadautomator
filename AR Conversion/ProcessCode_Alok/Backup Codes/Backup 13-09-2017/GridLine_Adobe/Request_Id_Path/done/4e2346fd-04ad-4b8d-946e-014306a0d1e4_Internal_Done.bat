call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "4e2346fd-04ad-4b8d-946e-014306a0d1e4"
echo SPV_AR_Process_Internal_P2 for RequestId-4e2346fd-04ad-4b8d-946e-014306a0d1e4   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 '4e2346fd-04ad-4b8d-946e-014306a0d1e4' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P24e2346fd-04ad-4b8d-946e-014306a0d1e4@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-4e2346fd-04ad-4b8d-946e-014306a0d1e4   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"

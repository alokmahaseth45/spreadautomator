call "D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Abode_Gridline_To_Pdf.py" "a9522d78-1846-4d0c-a954-44fcea8ab686"
pause
echo SPV_AR_Process_Internal_P2 for RequestId-a9522d78-1846-4d0c-a954-44fcea8ab686   Start %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"
sqlcmd -E -S localhost -d Annual_Reports -Q "Exec SPV_AR_Process_Internal_P2 'a9522d78-1846-4d0c-a954-44fcea8ab686' ">>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2a9522d78-1846-4d0c-a954-44fcea8ab686@%date:/=-%_%time::=^%.txt"
echo SPV_AR_Process_Internal_P2 for RequestId-a9522d78-1846-4d0c-a954-44fcea8ab686   End %date% %time%>>"D:\AR Conversion\ProcessCode_Alok\GridLine_Adobe\Request_Id_Path\log\SPV_AR_Process_Internal_P2.txt"

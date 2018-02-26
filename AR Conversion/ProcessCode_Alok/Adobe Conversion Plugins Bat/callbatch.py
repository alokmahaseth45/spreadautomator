import os

def Function_bat_run(bat):
	print bat
	bat = '""'+bat+'""'
	# print bat
	os.system(bat)
	# pdb.set_trace()
	return


call_bat2 = "D:\AR Conversion\ProcessCode_Alok\Open Excel And Read Data\CallBatch2.bat"

Function_bat_run(call_bat2)
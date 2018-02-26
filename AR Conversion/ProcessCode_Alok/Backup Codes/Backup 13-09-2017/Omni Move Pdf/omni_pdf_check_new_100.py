import psutil
import pdb
import os
import time
import datetime
import shutil
import glob
# import subprocess

mypath = r'D:\BSE India Annual Report\ProcessCode 100\OmniWatch100'
move_counter = 0
while 1==1:
    job_flag = 0
    for proc in psutil.process_iter():
        if "JobRunner.exe" in proc.name():
            job_flag = 1
            pid = proc.pid
            print pid
            pid = int(pid)
            ct = datetime.datetime.fromtimestamp(proc.create_time())
            print "Proc Create time",ct
            print "--------------------------------"
            if pid>0:
                print("process uptime according to psutil:--> {}".format(
                (datetime.datetime.now() - ct).total_seconds()))
                # (datetime.datetime.now() - ct)))

                process_update = (datetime.datetime.now() - ct).total_seconds()
                print "Process time is : ",process_update

                print "--------------------------------"

                if int(process_update) > 1500:
                    print('Process found. Terminating it.')
                    proc.terminate()
            break
    pdf_flag = 0
    pdf_files = glob.glob(mypath +'/'+"*.pdf")
    if len(pdf_files) > 0:
        pdf_flag = 1

    if job_flag == 0 and pdf_flag == 1:
        move_counter = move_counter + 1
        print "move_counter",move_counter
    else:
        print "process rerun"
        move_counter = 0

    if move_counter > 5:
        print "moving files"
        pdf_files = glob.glob(mypath +'/'+"*.pdf")
        print pdf_files
        omni_pdf_move = [x.replace('D:\BSE India Annual Report\ProcessCode 100\OmniWatch100','D:\BSE India Annual Report\ProcessCode 100\Omni Move Pdf') for x in pdf_files]
        print "----------------",omni_pdf_move

        for x in pdf_files:
            print ">>>>>>>>>>>>>>>>>>>>>>>",x
            shutil.move(x,'D:\BSE India Annual Report\ProcessCode 100\Omni Move Pdf/')
        time.sleep(20)
        for y in omni_pdf_move:
            shutil.move(y,'D:\BSE India Annual Report\ProcessCode 100\OmniWatch100/')
        print "Pdf Files Moved"
        move_counter = 0
        # break
    time.sleep(10)

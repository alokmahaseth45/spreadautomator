import psutil
import pdb
import os
import time
import datetime
import shutil
# import subprocess






mypath = r'D:\OmniWatch'
for proc in psutil.process_iter():
    flag= 1
    while flag == 1
    pdf_files = glob.glob(mypath +'/'+"*.pdf")

    for x in pdf_files:
        if ".pdf" in x and "JobRunner.exe" in proc.name()

    if "JobRunner.exe" in proc.name():
        print proc.ppid()
        pid = proc.pid
        print pid
        print proc.name()
        print proc.username()
        print proc.cpu_percent()
        print "Waiting for JobRunner Stop"
       

    else:
        time.sleep(20)
        import glob
        mypath = r'D:\OmniWatch'
        pdf_files = glob.glob(mypath +'/'+"*.pdf")
        print pdf_files
        omni_pdf_move = [x.replace('D:\\OmniWatch','D:\Omni Move Pdf') for x in pdf_files]
        print "----------------",omni_pdf_move

        for x in pdf_files:
            print ">>>>>>>>>>>>>>>>>>>>>>>",x
            shutil.move(x,'D:\Omni Move Pdf/')
        time.sleep(20)
        for y in omni_pdf_move:
            shutil.move(y,'D:\OmniWatch/')

        # for 
        pdb.set_trace()




       





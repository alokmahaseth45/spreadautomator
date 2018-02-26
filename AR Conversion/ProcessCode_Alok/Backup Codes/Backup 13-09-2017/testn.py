import os
import pdb

# import requests
# url = 'http://nclt.c2k.in/OtherNCLT/Publication/principal_bench/2017/397_398/VikramakshivsconnaughtPlazaRestaurantsLtd.pdf'

# page = requests.get(url)

# print page.status_code

# with open('xyzzzzzzz.pdf','wb') as f:
# 	f.write(page.content)


# bat = 'E:\Merge Videos\FFMPEG\FFMPEG\\ffmpeg convert1.bat'
# print bat
# bat = '""'+bat+'""'
# print bat
# # pdb.set_trace()

# os.system(bat)
# pdb.set_trace()


# path = r'E:\XBRL Read\Instance_Lama.xml'
# with open(path) as f:
# 	inputr = f.read()

# print inputr


# bat = r'E:\Merge Videos\FFMPEG\FFMPEG\ffmpeg join_new.bat'

# print bat
# bat = '""'+bat+'""'
# print bat

# os.system(bat)

# 'E:\XBRL\XBRL XML FIles\L15140MH1986PLC038536\6\Form-AOC-4(XBRL)-18112016-signed~18_11_2016\FY[2015-2016] L15140MH1986PLC038536 Standalone_BalanceSheet 11-11-2016.xml'

# file = r'E:\XBRL\XBRL XML FIles\L15140MH1986PLC038536\6'

# if not os.path.exists(file):
# 	os.makedirs(file)
# import pdftops
# import pdftrick
# import pdf2pdf

# pdf2ps "xxxyyy.pdf" "output.ps"
# ps2pdf output.ps output.pdf
# import reportlab

# c = reportlab.pdfgen.canvas.Canvas("C:\Users\john\Desktop\xxxyyy.pdf")
# # draw some stuff on c
# c.showPage()
# print c.showPage()
# exit()
# c.setPageSize((700, 500)) #some page size, given as a tuple in points
# # draw some more stuff on c
# c.showPage()
# c.save()

# import pypdf
# import pypdf2
from pyPdf import PdfFileWriter, PdfFileReader
# from pypdf2 import PdfFileWriter, PdfFileReader
listfile = 'D:\AR Conversion\Annual Reports\\admin\Pdf_Single_Files\\14db0fba-2827-4e96-a269-692be4c6a365_Attach P P OIL PRIVATE LIMITED 2016_1.pdf'

input1 = PdfFileReader(file(listfile, "rb"))
# print the title of document1.pdf
# print "title = %s" % (input1.getDocumentInfo().title)
# print input1.getPage(0).mediaBox
input1.getPage(0).mediaBox

# print type(input1.getPage(0).bleedBox) 
# print list(input1.getPage(0).mediaBox)
pxcel_files  = list(input1.getPage(0).mediaBox)
print type(pxcel_files[2])
if int(pxcel_files[2])>2015 or int(pxcel_files[3])>2015:
	# print int(pxcel_files[3])
	x =  float(1000/float(pxcel_files[3]))
	print x
	print "file is greater"
	# print input1.getPage(0).scale(0.5, 0.5)
	print input1.getPage(0).scaleBy(.35)
	# print type(input1.getPage(0).scale(0.5, 0.5))x
	# output = PdfFileWriter()
	# print input1.getPage(0).mediaBox
	# scaned_folder = r'C:\Users\john\Desktop\scaned file folder'
	# scaned_filesave = listfile.replace('New folder (2)','scaned file folder')
	# output.addPage(input1.getPage(0))
	# outDoc = open(scaned_filesave, 'wb')
	# output.write(outDoc)
	# outDoc.close()




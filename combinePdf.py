# Combine two PDF files

import PyPDF2, sys

pdf1File = open(sys.argv[1], 'rb')
pdf2File = open(sys.argv[2], 'rb')
pdf1Reader = PyPDF2.PdfReader(pdf1File)
pdf2Reader = PyPDF2.PdfReader(pdf2File)

pdfWriter = PyPDF2.PdfWriter()

for pageNum in range(len(pdf1Reader.pages)):
    pageObj = pdf1Reader.pages[pageNum]
    pdfWriter.add_page(pageObj)
    
for pageNum in range(len(pdf2Reader.pages)):
    pageObj = pdf2Reader.pages[pageNum]
    pdfWriter.add_page(pageObj)
    
pdfOutputFile = open('combinedmintues.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
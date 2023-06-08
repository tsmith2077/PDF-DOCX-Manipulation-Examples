# Overlay on Pdf
# Input file name to modify, then file name to overlay.
# 3rd enter page number of file to be modified.
# ex: python3 overlay.pdf fileToModify.pdf fileToOverlay.pdf 0

import PyPDF2, sys

fileToModify = open(sys.argv[1], 'rb')
fileToOverlay = open(sys.argv[2], 'rb')
pageNum = int(sys.argv[3])

pdfReader = PyPDF2.PdfReader(fileToModify)
pageToModify = pdfReader.pages[pageNum]
pdfWatermarkReader = PyPDF2.PdfReader(fileToOverlay, 'rb')
pageToModify.merge_page(pdfWatermarkReader.pages[0])
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(pageToModify)

for pageNum in range(1, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)
    
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
fileToModify.close()
fileToOverlay.close()
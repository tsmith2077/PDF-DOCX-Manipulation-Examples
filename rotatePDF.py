# Rotates PDF file image
# Enter file, then page number to be rotated 2nd

import PyPDF2, sys

fileInput = sys.argv[1]
pageToBeRotated = int(sys.argv[2])

pdfFile = open(fileInput, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)
page = pdfReader.pages[pageToBeRotated]
page.rotate(90)

pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
pdfFile.close()


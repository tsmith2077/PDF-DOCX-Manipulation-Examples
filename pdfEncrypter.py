# Find all pdf's in a given path without a 
# password, encrypt them, and delete the old pdf.

import os, PyPDF2

def encryptPdfs(path, password):
    path =  os.path.abspath(path)
    # Add all pdf files from given path to pdfFiles list.
    for path, foldername, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(path, filename)
            if filename.endswith('.pdf'):
                pdfReader = PyPDF2.PdfReader(open(filePath, 'rb'))
                if pdfReader.is_encrypted == False:
                    pdfWriter = PyPDF2.PdfWriter()
                    for pageNum in range(1, len(pdfReader.pages)):
                        pdfWriter.add_page(pdfReader.pages[pageNum])
                
                    # Encrypt file and save as filename_encrypted.pdf
                    pdfWriter.encrypt(password)    
                    fileBasename = os.path.splitext(filename)[0]
                    newFileName = f'{fileBasename}_encrypted.pdf'
                    newFilePath = os.path.join(path, newFileName)
                    pdfOutput = open(newFilePath, 'wb')
                    pdfWriter.write(pdfOutput)
                    pdfOutput.close()
                
                    # Confirm password works before deleting old file.
                    newPdfReader = PyPDF2.PdfReader(open(newFilePath, 'rb'))
                    if newPdfReader.decrypt(password) == 2:
                        print(f"Encryption complete for {filename}.")
                        os.unlink(filePath)
                    else:
                        print(f'Error when encrypting {filename}.')

        
        
    
encryptPdfs('/Users/genesmith/Documents/VS Code Projects/Automate Boring Stuff/Chapter15/pdfFolder/',
            'helloworld')
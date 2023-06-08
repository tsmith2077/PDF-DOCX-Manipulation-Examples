# Find all encoded pdf's, remove the password
# and delete the old encrypted pdf.

import os, PyPDF2, re

def decryptPdfs(path, password):
    path =  os.path.abspath(path)
    # Add all pdf files from given path to pdfFiles list.
    for path, foldername, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(path, filename)
            if filename.endswith('.pdf'):
                pdfReader = PyPDF2.PdfReader(open(filePath, 'rb'))
                if pdfReader.is_encrypted:
                    pdfReader.decrypt(password)
                    pdfWriter = PyPDF2.PdfWriter()
                    for pageNum in range(1, len(pdfReader.pages)):
                        pdfWriter.add_page(pdfReader.pages[pageNum])
                
                    encryptedFileNameRegex = re.compile('''
                    (\w+)
                    (_encrypted)
                    (\.pdf)                               
                    ''', re.VERBOSE)
                    fileBasename = os.path.splitext(filename)[0]
                    mo = encryptedFileNameRegex.search(filename)
                    
                    if mo == None:
                        newFileName = f'{fileBasename}.pdf'
                    else:
                        beforeEncryptedText = mo.group(1)
                        extension = mo.group(3)
                        newFileName = f'{beforeEncryptedText}{extension}'
                        
                    newFilePath = os.path.join(path, newFileName)
                    pdfOutput = open(newFilePath, 'wb')
                    pdfWriter.write(pdfOutput)
                    pdfOutput.close()
                
                    # # Delete old encrypted file.
                    os.unlink(filePath)
                    print(f'Pdf {filename} decrypted and replaced with {newFileName}.')

        
        
    
decryptPdfs('/Users/genesmith/Documents/VS Code Projects/Automate Boring Stuff/Chapter15/pdfFolder/',
            'helloworld')
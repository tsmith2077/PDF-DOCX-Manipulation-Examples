# Runs through dictionary.txt file to match 
# password set for pdf decryption.
# Entry example:
# python3 bruteForcePw.py encryptedPdf.pdf

import os, PyPDF2, sys


def decryptPassword():
    pdfFile = sys.argv[1]
    pdfReader = PyPDF2.PdfReader(open(pdfFile, 'rb'))
    dictionaryDoc = open(os.path.abspath('dictionary.txt'))
    dictionaryList = []
    for word in dictionaryDoc.readlines():
        dictionaryList.append(word.strip('\n').lower())
        dictionaryList.append(word.strip('\n').upper())
    if pdfReader.is_encrypted:
        for password in dictionaryList:
            if pdfReader.decrypt(password) == 2:
                return print(f'The password is {password}.')
    return print(f'The pdf file {pdfFile} is not encrypted.')
decryptPassword()

import PyPDF2

rb = open('old.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(rb)
pdfReader.decrypt('BIBH1969')
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOut = open('new.pdf','wb')
pdfWriter.write(pdfOut)
pdfOut.close()
rb.close()
print('Done')
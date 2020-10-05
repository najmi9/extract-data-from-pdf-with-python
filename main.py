import PyPDF2 as p2


pdf = p2.PdfFileReader(open('data.pdf','rb'))

pages = pdf.getNumPages()



for p in range(pages):
	page = pdf.getPage(p)
	content = page.extractText()
	print(content)
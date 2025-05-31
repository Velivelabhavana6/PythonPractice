import PyPDF2

with open('file.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    # print(len(pdf_reader.pages))  # Total pages

    page_one = pdf_reader.pages[1]  # Second page (index starts at 0)
    page_one_text = page_one.extract_text()
    # print(page_one_text)
    
f=open('file.pdf','rb')
pdf_reader=PyPDF2.PdfReader(f)
first_page=pdf_reader.pages[0]
pdf_writer=PyPDF2.PdfWriter()
print(type(first_page))
pdf_writer.add_page(first_page)
pdf_output=open('Some_BrandNew_Doc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

f=open('file.pdf', 'rb')
pdf_text=[]
pdf_reader=PyPDF2.PdfReader(f)
for num in range(len(pdf_reader.pages)):
    page=pdf_reader.pages[2] 
    pdf_text.append(page.extract_text())

print(pdf_text)
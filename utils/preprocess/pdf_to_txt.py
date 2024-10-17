from pypdf import PdfReader

reader = PdfReader('Doc1-1.pdf')

print(f"There are {len(reader.pages)} Pages")


for i in range(len(reader.pages)):
  page = reader.pages[i]
  print(page.extract_text())

import pdfplumber

with pdfplumber.open('Doc1-1.pdf') as pdf:
    for page in pdf.pages:
        print(page, pdf)
        text = page.extract_tables()
        print(text)




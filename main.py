import pdfplumber

url_pdf = 'C://Users//王连兴//Desktop//机器学习第二次作业.pdf'

with pdfplumber.open(url_pdf) as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
# pip install pdfplumber -q
# https://eu.jotform.com/pdf-editor/

# Импортируйте свой модуль.
import pdfplumber
 
path = "invoice.pdf"

# Эта функция откроет файл с именем '' pdf ': 
with pdfplumber.open(path) as pdf:
    # Выбрать страницу, на которой хотите извлечь искомую информацию
    # page = pdf.pages[0]

    pages = pdf.pages
 
    for page in pages:
        with open('invoice.txt', 'a') as f:
            # Теперь нужно извлечь из нее текст:
            t = page.extract_text()
            print(t)
            f.write(t)
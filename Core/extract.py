from Objects.pdf import PDF
from Objects.extract_thread import Extract_thread
from PyPDF2 import PdfFileReader

files = []
pdf_files = []

def extract_text(id):
    pdf_files.append(PDF(files[id]))

    open_file = open(files[id], "rb")
    open_pdf_file = PdfFileReader(open_file)

    pages = open_pdf_file.getNumPages()
    pdf_files[-1].pages = pages

    for page in range(pages):
        content = open_pdf_file.getPage(page)
        pdf_files[-1].text += content.extractText()


def open_files(files_):
    threads = []
    files = files_

    for i in range(len(files)):
        threads.append(Extract_thread(i))




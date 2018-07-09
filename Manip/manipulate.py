import os
from PyPDF2 import PdfFileReader
from Objects.pdf import *


files = []  # files holds the pdf files found in path
pdf_files = []  # store pdf objects
keywords = []
results = []

dbg_path = ''  # debugging path
user_path = None
path = None


def find_pdf(path, name):
    """
    find a specific file (name) in a specific dir (path)
    if found append in the files list
    :param path: path to search for pdf files
    :param name: name of the file to find
    :return: None
    """
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            flag = re.search(name, file)
            if flag:
                files.append(file)
    if files:
        print('Found file in ' + os.getcwd())
    else:
        print('Could not files in ' + os.getcwd())


def find_pdf_all(path):
    """
    mostly used
    enter a path and append all pdf files in the files list
    :param path: path to find pdf files
    :return: None
    """
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            files.append(file)

    if files:
        print('Found files in ' + path)
    else:
        print('Could not find pdf files in ' + path)


def find_every_file():
    """
    search every directory in the linux's home folder
    append all files found in the files list
    :return: None
    """
    status = False
    for file in os.listdir('/home/'):
        if file.endswith('.pdf '):
            files.append(file)
            status = True

    if status:
        print('Found pdf files in ' + os.getcwd())
    else:
        print('Could not found pdf files in ' + os.getcwd())


def print_results(verbose=False):
    """
    prints results from the search
    :param verbose: if True print files with some extra info
    :return: None
    """
    for i in files:
        print(i)

    if verbose:
        print('Name\tPages')
        for file in pdf_files:
            print(file.name + '\t' + file.pages)


def return_result(result_index, verbose=False):

    return results[result_index]


def open_pdfs():

    if not files:
        return

    for i in range(files.__len__()):
        print(files[i])
        pdf_files.append(PDF(files[i]))

        open_file = open(os.path.abspath(files[i]), 'rb')
        pdf_open_file = PdfFileReader(open_file)

        for page in range(pdf_open_file.pages):
            content = pdf_open_file.getPage(page)
            pdf_files[i].text += content.extractText()

        open_file.close()


def match_keywords():
    for pdf in pdf_files:
        for word in keywords:
            found = re.match(word, pdf.text)
            if found:
                pass

def get_path():
    new = input('Select path: /home/')
    if new.endswith('/'):
        final_new = '/home/' + new
    else:
        final_new = '/home/' + new + '/'

    return final_new


def extract_s_text(content, field, chapter = 0):
    """
    extract specific text from a text content
    used for scientific papers
    can be used to extract abstract or a specific chapter
    :param content: the entire text to search, in this caase the pdf content
    :param field: the field of the file to search like abstract or keywords
    :param chapter: a numbered chapter of the file (default 0)
    :return:None
    """

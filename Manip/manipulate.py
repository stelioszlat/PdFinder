import os
from PyPDF2 import PdfFileReader
import pdf_extractor
from Objects.pdf import *
from Objects.keyword import *
from Manip.statistics import prioritise


files = [
    [],  # files as str
    [],  # files as objects
]
keywords = [
    Keyword('word'),
    Keyword('keyword'),
]  # list of Keyword Objects

results = []  # result files from word matching

dbg_path = '$HOME/Downloads'  # debugging path
user_path = None
path = ''


def find_pdf(fpath, find_all=False, dbg=True):
    """
    mostly used
    enter a path and append all pdf files in the files list
    :param path: path to find pdf files
    :return: None
    """
    if find_all:
        os.chdir('$HOME')
        for file in os.listdir(os.walk(os.curdir)):
            if file.endswith('.pdf'):
                files[0].append(file)
    else:
        for file in os.listdir(fpath):
            if file.endswith('.pdf'):
                files[0].append(file)

    if dbg:
        if files[0]:
            print('Found files in ' + fpath)
        else:
            print('Could not find pdf files in ' + fpath)


def print_results(verbose=False):
    """
    prints results from the search
    :param verbose: if True print files with some extra info
    :return: None
    """
    for i in files:
        print(i)

    if verbose:
        for file in files[1]:
            print('|=====================================|')
            print('File:' + file.name)
            print('Pages:' + str(file.pages))
            print('Keywords: ' + str(file.keywords))


def open_pdfs():

    if not files:
        return False

    # for i in range(files.__len__()):
    #     print(files[i])
    #     pdf_files.append(PDF(files[i]))
    #
    #     open_file = open(path + files[i], 'rb')
    #     pdf_open_file = PdfFileReader(open_file, strict=False)
    #
    #     for page in range(pdf_open_file.getNumPages()):
    #         content = pdf_open_file.getPage(page)
    #         pdf_files[i].text += content.extractText()
    #
    #     open_file.close()

    for file in files[0]:
        try:
            print(file)
            files[1].append(PDF(file))

            pdf_extractor

            open_file = open(path+file, 'rb')
            pdf_open_file = PdfFileReader(open_file)
            pages = pdf_open_file.getNumPages()
            files[1][-1].pages = pages

            for page in range(pages):
                content = pdf_open_file.getPage(page)
                files[1][-1].text += content.extractText()

            open_file.close()
        except IOError:
            print('I/O Error occurred')
        except EOFError:
            print('EOF Error occurred')


def match_keywords():

    # for pdf in files[1]:
    #     for word in keywords:
    #         found = re.findall(word.name, pdf.text)
    #         if found:
    #             print(found)
    #             word.file_appeared[pdf.title] = found.__len__()
    #             print(word.file_appeared)
    #             print(files[0])
    #     results.append(files[0])
    # print(results)

    for i in range(files[1].__len__()):
        for word in keywords:
            found = re.findall(word.name, files[1][i].text)
            if found:
                print('Found times' + str(found.__len__()))
                word.file_appeared[files[0][i]] = found.__len__()
                print(word.file_appeared)
            else:
                return False
        results.append(files[0][i])
    # print(results)


def return_result(result_index, verbose=False):

    return results[result_index]


def get_path():
    new = input('Select path: ~/')
    if new.endswith('/'):
        final_new = '$HOME/' + new
    else:
        final_new = '$HOME' + new + '/'

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


if __name__ == '__main__':
    path = '/home/zlat/Documents/'
    find_pdf(path)
    open_pdfs()
    match_keywords()
    prioritise(files)
    print_results()

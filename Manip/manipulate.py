#! /usr/bin/python3
import os
from PyPDF2 import PdfFileReader, utils
from Objects.pdf import *
from Objects.keyword import *
from Manip.statistics import prioritise


files = [
    [],  # files as str
    [],  # files as objects
    [],  # directory of the file
]
keywords = [
    Keyword('word'),
    Keyword('keyword'),
]  # list of Keyword Objects

results = []  # result files from word matching

dbg_path = os.environ['HOME'] + '/Downloads'  # debugging path
user_path = None
path = ''


def find_pdf(fpath, find_all, dbg=True):
    """
    mostly used
    enter a path and append all pdf files in the files list
    :param path: path to find pdf files
    :return: None
    """

    os.chdir(fpath)

    if find_all:
        os.chdir(os.environ['HOME'])

    for r, d, f in os.walk(os.curdir):
        for file in f:
            if file.endswith('.pdf'):
                print('Found file')
                files[0].append(file)
                print(os.path)
                files[2].append(os.path.join(r, file))
    print('SUCCESS!')
    print(files[2])


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

    for i in range(files[0].__len__()):
        try:
            print(files[0][i])
            files[1].append(PDF(files[0][i]))

            open_file = open(files[2][i], 'rb')
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
        except TypeError:
            print('Type Error occured')
        except utils.PdfReadError:
            print('Could not read malformed PDF file')

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
    """
    get path from user manually
    not really usable
    :return : the new path
    """
    new = input('Select path: ~/')

    final_new = os.environ['HOME'] + new
    if not new.endswith('/'):
        final_new += '/'

    print(final_new)
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
    path = os.environ['HOME'] + '/Downloads'
    find_pdf(path)
    open_pdfs()
    match_keywords()
    prioritise(files)
    print_results()

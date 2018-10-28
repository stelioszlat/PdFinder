# Stelios Zlatintsis 5/7/2017 - 7/7/2017
# changes until 13/7/2017
# PDF project
# pdfinder v-0.1
import PyPDF2
import os
import re
import tkinter as tk
from tkinter import filedialog


class Keyword:
    ignore = False
    file_name = []
    appearance = []
    percentage = []

    def __init__(self, name,):
        self.name = name

    # sort every list by the appearance
    def sort(self):
        for pass_num in range(len(self.appearance) - 1, 0, -1):
            for e in range(pass_num):
                if self.appearance[e] < self.appearance[e+1]:
                    temp = self.appearance[e]
                    self.appearance[e] = self.appearance[e+1]
                    self.appearance[e+1] = temp
                    temp = self.percentage[e]
                    self.percentage[e] = self.percentage[e+1]
                    self.percentage[e+1] = temp
                    temp = self.file_name[e]
                    self.file_name[e] = self.file_name[e+1]
                    self.file_name[e+1] = temp

    # calculate the percentage value by words
    def calculate_percentage(self, position, words,):
        self.percentage[position] = self.appearance[position] * 100 / words

    # calculates the appearance of the keyword in a specific file
    def appeared(self, position):
        if not self.ignore:
            self.appearance[position] += 1


# print results
def print_results(num):
    printed_files = 0
    # print results only once
    for res in range(num):
        flag = False
        for r in range(res - 1, 0):
            if result_files[res] == result_files[r]:
                flag = True
        if not flag:
            print(result_files[res])
            printed_files += 1
        if num == printed_files:
            break


# check characters length
# 1: all words are below 3 letters so the program will terminate
# 2: only one word is below three letters (return the position of this words in the list)
# 3: more than one words are below three letters ...
# 4: all except 1 are below 3 words (return the position of the exception)
def check_words_length(array):
    new_array = []
    code = 0
    count = 0
    flag = False
    for s in range(len(array)):
        new_array.append(0)
        if len(array[s].name) <= 3:
            new_array[s] = 1
            flag = True

    if flag:
        for n in new_array:
            if n == 1:
                count += 1

        if count == len(array):
            # all words are <= 3
            code = 1
        elif count == 1:
            # there is only one <= 3 letters words
            code = 2
        elif 1 < count < len(array):
            # more than one <= 3 letters words
            code = 3
        elif count == len(array) - 1:
            # all except one <= 3 letters words
            code = 4

        return code
    else:
        # every word is > 3
        return


# list of pdf files in given directory
pdf_files = []
keywords = [Keyword("")]
break_choices = ("No", "no", "0", "NO", "o", "O", "n", "N",)

# use tkinter to get path
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

# get first keyword
first_keyword = input("Enter a keyword: ")
keywords[0] = Keyword(first_keyword)

# get multiple keywords
while True:
    choice = input("Do you want to add another keyword? ")
    if choice in break_choices:
        break
    word = input("Enter another keyword: ")
    keywords.append(Keyword(word.lower()))

# get the status of the keywords length
check = check_words_length(keywords)

# if all keywords are invalid exit the program
if check == 1:
    print("all keywords all invalid...the program will terminate")
    exit(0)

# ignore keywords
for key in keywords:
    if check == 2:
        if len(key.name) <= 3:
            # ignore this keyword
            key.ignore = True
            break
    elif check == 3 or check == 4:
        if len(key.name) <= 3:
            # ignore keywords found
            key.ignore = True

# ======================================================================================================================
# find all pdf files in the given directory
for file in os.listdir(path):
    if file.endswith(".pdf"):
        pdf_files.append(file)

# cutting the absolute path and keep only the name of the pdf
for i in pdf_files:
    cut_point = re.match('\'', i)  # use re.match to find the point to cut the path
    sub = list(i)
    var = sub[:cut_point]
    var = ''.join(var)
    item = var

print(str(len(pdf_files))+" items found")
# time.sleep(3) #optional
# print(pdf_files)

found = 0
count_words = 0

# loop
# for every file found in directory
for i in range(len(pdf_files)):
    file = path+"/"+pdf_files[i]
    keywords[0].file_name.append(pdf_files[i])
    keywords[0].appearance.append(0)
    keywords[0].percentage.append(0)

# demo file
# file = "C:\\Users\\User\\Desktop\\Pdf Project\\example1.pdf"

# open pdf file and search for the keyword
    pdf_object = open(file, "rb")
    pdf = PyPDF2.PdfFileReader(pdf_object)
    pdf_info = pdf.getDocumentInfo()
    appearance = 0
    # search keyword in every page of the file
    for page in range(pdf.getNumPages()):
        content = pdf.getPage(page)
        text = content.extractText()
        text.split()
        for w in text.lower():
            count_words += 1
        # loop for every keyword in the list
        for keys in range(len(keywords)):
            if keywords[keys].name in text:
                keywords[keys].appeared(i)
                appearance += 1

    # calculate percentage values
    for keys in keywords:
        for k in range(len(keys.file_name)):
            keys.sort()
            # print(count_words)
            # print(appearance)
            keys.calculate_percentage(k, count_words,)

    count_words = 0
# =======================================================================================================================

# find the results of the search
result_files = []
results_num = input("Enter number of results: ")
for j in range(len(keywords)):  # for every keyword in keywords list
    for i in range(len(keywords[j].file_name)):  # for every file in every keyword
        # if the value is positive
        if keywords[j].percentage[i] > 0.0:
            # append the file's name to the final list
            result_files.append(keywords[j].file_name[i])

# if the results are less than the expected results print the number of available files
if int(results_num) > len(result_files) > 0:
    print("There are only " + str(len(result_files)) + " files that match")
    print_results(results_num)
elif len(result_files) == 0:  # if there are no results
    print("There are no matches")
elif int(results_num) < 0:
    print("Wrong number")
elif int(results_num) == 0:
    print("You selected not to print the results")
else:
    print_results(int(results_num))

# end of script

#! /usr/bin/python3
# pdfinder v-0.2
from sys import exit, argv
import argparse
import Manip.manipulate as m
from Objects.pdf import *
from GUI.gui import Root
from PyQt5.QtWidgets import QApplication
import os


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--all', help='search all directories (in $HOME)')
    parser.add_argument('-d', '--debug', help='use debugging path', action='store_true')
    parser.add_argument('-g', '--graphical', help='show graphical environment', action='store_true')
    keyword_group = parser.add_argument_group('keyword_group')
    keyword_group.add_argument('-k', help="keyword to seek", nargs='+')
    parser.add_argument('-s', '--statistics', help='print statistics of the search', action='store_true')
    parser.add_argument('-p', '--path', help='option to enter path or search the current directory', action='store_true')
    results_group = parser.add_argument_group('results_group')
    results_group.add_argument('-r', '--results', help='option to select number of results to display', action='store_true')
    results_group.add_argument('-R', help='number of results', type=int)
    parser.add_argument('-v', '--verbose', help="print results with more details", action="store_true")
    args = parser.parse_args()

    # if args.keyword:
    #     key = Keyword(args.keyword)

    m.path = os.environ['HOME']
    all = False

    if args.all:
        print('Searching all sub-directories in home')
        all = True

    if args.debug:
        try:
            m.path = os.environ['HOME'] + '/examples'
        except FileNotFoundError:
            print('Couldn\'t find examples directory')

    if args.graphical:
        app = QApplication(argv)
        r = Root()
        exit(app.exec_())

    if args.statistics:
        print('statistics: ')

    if args.path:
        path = m.get_path()

    if args.results:
        results_num = args.R

    m.find_pdf(m.path, all)
    m.open_pdfs()
    m.match_keywords()
    m.prioritise(m.files)

    if not m.files[0]:
        print('No Results')
    elif args.verbose:
        m.print_results(True)
    else:
        m.print_results()

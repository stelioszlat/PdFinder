from sys import exit, argv
import argparse
from Manip.manipulate import *
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
    keyword_group.add_argument('-keyword', help="keyword to seek", type=str)
    keyword_group.add_argument('-K', '--keywords', help="enter multiple keywords as arguments", action="store_true")
    parser.add_argument('-s', '--statistics', help='print statistics of the search', action='store_true')
    parser.add_argument('-p', '--path', help='option to enter path or search the current directory', action='store_true')
    results_group = parser.add_argument_group('results_group')
    results_group.add_argument('-r', '--results', help='option to select number of results to display', action='store_true')
    results_group.add_argument('-R', help='number of results', type=int)
    parser.add_argument('-v', '--verbose', help="print results with more details", action="store_true")
    args = parser.parse_args()

    # if args.keyword:
    #     key = Keyword(args.keyword)
    if args.graphical:
        app = QApplication(argv)
        r = Root()
        exit(app.exec_())

    path = os.getcwd()  # by default the searching directory is the current directory
    print(path)
    if args.debug:
        try:
            path = '$HOME/examples'
        except FileNotFoundError:
            print('Couldn\'t find examples directory')

    if not files[0]:
        print('No Results')
    elif args.verbose:
        print_results(True)
    else:
        print_results()
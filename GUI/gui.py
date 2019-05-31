from PyQt5 import QtWidgets
# from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from Core.manipulate import *


class Root(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('PdFinder')
        self.setGeometry(300, 100, 500, 400)
        self.setFixedSize(500, 400)
        icon = QIcon('icon.png')
        self.setWindowIcon(icon)
        menuBar = self.menuBar()

        settingsMenu = menuBar.addMenu('Settings')
        helpMenu = menuBar.addMenu('Help')

        settingsMenu.addAction('Open Settings')
        helpMenu.addAction('Help')
        helpMenu.addAction('About')

        keywordlabel = QtWidgets.QLabel(self)
        keywordlabel.setText('Enter keyword')
        keywordlabel.setGeometry(20, 40, 200, 20)
        self.wordtext = QtWidgets.QLineEdit(self, )
        self.wordtext.setGeometry(120, 40, 100, 30)
        self.addbutton = QtWidgets.QPushButton(self)
        self.addbutton.setText('Add')
        self.addbutton.setGeometry(240, 40, 100, 30)
        self.deletebutton = QtWidgets.QPushButton(self)
        self.deletebutton.setText('Delete')
        self.deletebutton.setGeometry(240, 40, 100, 30)
        self.deletebutton.setVisible(False)

        self.words = QListWidget(self)
        self.words.setGeometry(360, 40, 100, 70)
        pathlabel = QtWidgets.QLabel(self)
        pathlabel.setText('Select Folder')
        pathlabel.setGeometry(20, 80, 200, 20)
        pathbutton = QtWidgets.QPushButton(self)
        pathbutton.setText('Folder...')
        pathbutton.setGeometry(120, 80, 100, 30)
        findbutton = QtWidgets.QPushButton(self)
        findbutton.setText('Find')
        findbutton.setGeometry(240, 80, 100, 30)

        l2 = QtWidgets.QLabel(self)
        l2.setText('Results')
        l2.setGeometry(5, 120, 200, 20)
        self.results = QtWidgets.QListWidget(self)
        self.results.setGeometry(5, 160, 480, 220)

        self.path = '/home/zlat/Downloads'

        self.model = QFileSystemModel()
        self.model.setRootPath('/home')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setWindowTitle('Select folder')
        # self.progressbar = QProgressBar(self)
        # self.progressbar.setGeometry()
        # self.progressbar.setValue(10)
        # self.progressbar.setVisible(False)

        self.addbutton.clicked.connect(self.add_button_clicked)
        pathbutton.clicked.connect(self.path_button_clicked)
        findbutton.clicked.connect(self.find_button_clicked)
        self.words.itemClicked.connect(self.item_to_delete)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Enter:
            self.add_button_clicked()

    def add_button_clicked(self):
        if self.wordtext.text():
            word = self.wordtext.text()
            self.words.addItem(word)
            keywords.append(Keyword(word))
            self.wordtext.setText("")
        print(keywords)

    def path_button_clicked(self):
        self.path = QFileDialog.getExistingDirectory(self, 'Open Folder')
        print(path)

    def find_button_clicked(self):

        # start the searching proccess

        find_pdf(self.path)  # find all pdf files in the path

        open_pdfs()

        match_keywords()

        for i in range(3):
            self.results.addItem(results[i])

        # when finished show results
        pass

    def item_to_delete(self):
        self.deletebutton.setVisible(True)
        self.addbutton.setVisible(False)

        # delete from list widget and keywords list
        to_be_deleted = self.words.selectedItems()
        for item in to_be_deleted:
            self.words.removeItemWidget(item)

        self.addbutton.setVisible(True)
        self.deletebutton.setVisible(False)

    def closeEvent(self, event):
        # reply = QMessageBox.question(self, 'Warning!', 'Are you sure you want to quit?',
        #                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #
        # if reply == QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()
        pass

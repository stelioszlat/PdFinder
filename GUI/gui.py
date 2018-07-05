from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class Root(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initui()
        self.model = None
        self.tree = None

    def initui(self):
        self.setWindowTitle('PdFinder')
        self.setGeometry(300, 100, 500, 400)
        keywordlabel = QtWidgets.QLabel(self)
        keywordlabel.setText('Enter keyword')
        keywordlabel.setGeometry(20, 40, 200, 20)
        t1 = QtWidgets.QTextEdit(self)
        t1.setGeometry(120, 40, 100, 30)
        addbutton = QtWidgets.QPushButton(self)
        addbutton.setText('Add')
        addbutton.setGeometry(240, 40, 100, 30)

        t2 = QtWidgets.QTextEdit(self)
        t2.setGeometry(360, 40, 100, 70)
        pathlabel = QtWidgets.QLabel(self)
        pathlabel.setText('Select Path')
        pathlabel.setGeometry(20, 80, 200, 20)
        pathbutton = QtWidgets.QPushButton(self)
        pathbutton.setText('Path...')
        pathbutton.setGeometry(120, 80, 100, 30)
        b4 = QtWidgets.QPushButton(self)
        b4.setText('Find')
        b4.setGeometry(240, 80, 100, 30)

        l2 = QtWidgets.QLabel(self)
        l2.setText('Results')
        l2.setGeometry(5, 120, 200, 20)
        results = QtWidgets.QScrollArea(self)
        results.setGeometry(5, 160, 480, 220)

        self.model = QFileSystemModel()
        self.model.setRootPath('/home/')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setWindowTitle('Select folder')

        # addbutton.clicked.connect(self.add_button_clicked())
        # pathbutton.clicked.connect(self.pathButtonClicked)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Enter:
            self.addButtonClicked()

    def add_button_clicked(self):
        pass


    def path_button_clicked(self):
        pass

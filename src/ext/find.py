from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QRadioButton, QTextEdit, QLabel, QCheckBox, QGridLayout, QWidget, QDialog, QPushButton

import re


class Find(QDialog):
    def __init__(self, parent=None):

        QDialog.__init__(self, parent)

        self.parent = parent

        self.lastMatch = None

        self.init_ui()

    def init_ui(self):

        find_button = QPushButton("Find", self)
        find_button.clicked.connect(self.find)

        replace_button = QPushButton("Replace", self)
        replace_button.clicked.connect(self.replace)

        allButton = QPushButton("Replace all", self)
        allButton.clicked.connect(self.replace_all)

        self.normal_radio = QRadioButton("Normal", self)
        self.normal_radio.toggled.connect(self.normal_mode)

        self.regex_radio = QRadioButton("RegEx", self)
        self.regex_radio.toggled.connect(self.regex_mode)

        self.find_field = QTextEdit(self)
        self.find_field.resize(250, 50)

        self.replace_field = QTextEdit(self)
        self.replace_field.resize(250, 50)

        options_label = QLabel("Options: ", self)

        self.case_sens = QCheckBox("Case sensitive", self)

        self.whole_words = QCheckBox("Whole words", self)

        layout = QGridLayout()

        layout.addWidget(self.find_field, 1, 0, 1, 4)
        layout.addWidget(self.normal_radio, 2, 2)
        layout.addWidget(self.regex_radio, 2, 3)
        layout.addWidget(find_button, 2, 0, 1, 2)

        layout.addWidget(self.replace_field, 3, 0, 1, 4)
        layout.addWidget(replace_button, 4, 0, 1, 2)
        layout.addWidget(allButton, 4, 2, 1, 2)

        spacer = QWidget(self)

        spacer.setFixedSize(0, 10)

        layout.addWidget(spacer, 5, 0)

        layout.addWidget(options_label, 6, 0)
        layout.addWidget(self.case_sens, 6, 1)
        layout.addWidget(self.whole_words, 6, 2)

        self.setGeometry(300, 300, 360, 250)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

        self.normal_radio.setChecked(True)

    def find(self):

        text = self.parent.text.toPlainText()

        query = self.find_field.toPlainText()

        if self.whole_words.isChecked():
            query = r'\W' + query + r'\W'

        flags = 0 if self.case_sens.isChecked() else re.I

        pattern = re.compile(query, flags)

        start = self.lastMatch.start() + 1 if self.lastMatch else 0

        self.lastMatch = pattern.search(text, start)

        if self.lastMatch:

            start = self.lastMatch.start()
            end = self.lastMatch.end()

            if self.whole_words.isChecked():
                start += 1
                end -= 1

            self.move_cursor(start, end)

        else:

            self.parent.text.moveCursor(QTextCursor.End)

    def replace(self):

        cursor = self.parent.text.textCursor()

        if self.lastMatch and cursor.hasSelection():
            cursor.insertText(self.replace_field.toPlainText())

            self.parent.text.setTextCursor(cursor)

    def replace_all(self):

        self.lastMatch = None

        self.find()

        while self.lastMatch:
            self.replace()
            self.find()

    def regex_mode(self):

        self.case_sens.setChecked(False)
        self.whole_words.setChecked(False)

        self.case_sens.setEnabled(False)
        self.whole_words.setEnabled(False)

    def normal_mode(self):

        self.case_sens.setEnabled(True)
        self.whole_words.setEnabled(True)

    def move_cursor(self, start, end):

        cursor = self.parent.text.textCursor()

        cursor.setPosition(start)

        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end - start)

        self.parent.text.setTextCursor(cursor)

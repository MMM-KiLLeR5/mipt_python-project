import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit


class Main(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)

        self.init_tool_bar()
        self.initFormatbar()
        self.init_menu_bar()

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # x and y coordinates on the screen, width, height
        self.setGeometry(100, 100, 1030, 800)

        self.setWindowTitle("Writer")

    def init_tool_bar(self):
        self.toolbar = self.addToolBar("Options")

        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatbar(self):
        self.formatbar = self.addToolBar("Format")

    def init_menu_bar(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")


def main():
    app = QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

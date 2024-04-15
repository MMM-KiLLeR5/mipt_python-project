import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1030, 800)

        self.setWindowTitle("Writer")


def main():
    app = QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

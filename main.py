import sys
from src.TextEditor import TextEditor
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    obj = TextEditor()
    obj.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

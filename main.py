import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrintDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QFileDialog, QDialog


class Main(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.filename = ""

        self.init_ui()

    def init_ui(self):
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)

        self.init_tool_bar()
        self.init_format_bar()
        self.init_menu_bar()

        self.statusbar = self.statusBar()

        self.setGeometry(100, 100, 1030, 800)

        self.setWindowTitle("Writer")

    def init_tool_bar(self):
        self.new_action = QAction(QIcon("icons/new.png"), "New", self)
        self.new_action.setStatusTip("Create a new document from scratch.")
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.new)

        self.open_action = QAction(QIcon("icons/open.png"), "Open file", self)
        self.open_action.setStatusTip("Open existing document")
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open)

        self.save_action = QAction(QIcon("icons/save.png"), "Save", self)
        self.save_action.setStatusTip("Save document")
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.save)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.open_action)
        self.toolbar.addAction(self.save_action)

        self.toolbar.addSeparator()

        self.addToolBarBreak()
        self.print_action = QAction(QIcon("icons/print.png"), "Print document", self)
        self.print_action.setStatusTip("Print document")
        self.print_action.setShortcut("Ctrl+P")
        self.print_action.triggered.connect(self.print)

        self.preview_action = QAction(QIcon("icons/preview.png"), "Page view", self)
        self.preview_action.setStatusTip("Preview page before printing")
        self.preview_action.setShortcut("Ctrl+Shift+P")
        self.preview_action.triggered.connect(self.preview)
        self.toolbar.addAction(self.print_action)
        self.toolbar.addAction(self.preview_action)

        self.toolbar.addSeparator()

    def init_format_bar(self):
        self.formatbar = self.addToolBar("Format")

    def init_menu_bar(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        file.addAction(self.new_action)
        file.addAction(self.open_action)
        file.addAction(self.save_action)
        file.addAction(self.print_action)
        file.addAction(self.preview_action)

    def new(self):
        spawn = Main(self)
        spawn.show()

    def open(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.writer)")

        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())

    def save(self):

        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self, 'Save File')

        if not self.filename.endswith(".writer"):
            self.filename += ".writer"

        with open(self.filename, "wt") as file:
            file.write(self.text.toHtml())

    def preview(self):

        # Open preview dialog
        preview = QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def print(self):

        # Open printing dialog
        dialog = QPrintDialog()

        if dialog.exec_() == QDialog.Accepted:
            self.text.document().print_(dialog.printer())




def main():
    app = QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

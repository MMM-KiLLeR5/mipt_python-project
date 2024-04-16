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

        self.addToolBarBreak()
        self.print_action = QAction(QIcon("icons/print.png"), "Print document", self)
        self.print_action.setStatusTip("Print document")
        self.print_action.setShortcut("Ctrl+P")
        self.print_action.triggered.connect(self.print)

        self.preview_action = QAction(QIcon("icons/preview.png"), "Page view", self)
        self.preview_action.setStatusTip("Preview page before printing")
        self.preview_action.setShortcut("Ctrl+Shift+P")
        self.preview_action.triggered.connect(self.preview)

        self.cut_action = QAction(QIcon("icons/cut.png"), "Cut to clipboard", self)
        self.cut_action.setStatusTip("Delete and copy text to clipboard")
        self.cut_action.setShortcut("Ctrl+X")
        self.cut_action.triggered.connect(self.text.cut)

        self.copy_action = QAction(QIcon("icons/copy.png"), "Copy to clipboard", self)
        self.copy_action.setStatusTip("Copy text to clipboard")
        self.copy_action.setShortcut("Ctrl+C")
        self.copy_action.triggered.connect(self.text.copy)

        self.paste_action = QAction(QIcon("icons/paste.png"), "Paste from clipboard", self)
        self.paste_action.setStatusTip("Paste text from clipboard")
        self.paste_action.setShortcut("Ctrl+V")
        self.paste_action.triggered.connect(self.text.paste)

        self.undo_action = QAction(QIcon("icons/undo.png"), "Undo last action", self)
        self.undo_action.setStatusTip("Undo last action")
        self.undo_action.setShortcut("Ctrl+Z")
        self.undo_action.triggered.connect(self.text.undo)

        self.redo_action = QAction(QIcon("icons/redo.png"), "Redo last undone thing", self)
        self.redo_action.setStatusTip("Redo last undone thing")
        self.redo_action.setShortcut("Ctrl+Y")
        self.redo_action.triggered.connect(self.text.redo)


        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.print_action)
        self.toolbar.addAction(self.preview_action)
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.open_action)
        self.toolbar.addAction(self.save_action)
        self.toolbar.addAction(self.cut_action)
        self.toolbar.addAction(self.copy_action)
        self.toolbar.addAction(self.paste_action)
        self.toolbar.addAction(self.undo_action)
        self.toolbar.addAction(self.redo_action)

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
        edit.addAction(self.undo_action)
        edit.addAction(self.redo_action)
        edit.addAction(self.cut_action)
        edit.addAction(self.copy_action)
        edit.addAction(self.paste_action)

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

        preview = QPrintPreviewDialog()

        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def print(self):

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

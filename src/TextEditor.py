from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QTextListFormat, QTextCharFormat, QFont, QTextCursor, QImage, QContextMenuEvent
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrintDialog
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QDialog, QFontComboBox, \
    QComboBox, QColorDialog, QMessageBox, QMenu, QSpinBox
from src.ext import *


class TextEditor(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.filename = ""

        self.changesSaved = True

        self.init_ui()

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

        bullet_action = QAction(QIcon("icons/bullet.png"), "Insert bullet List", self)
        bullet_action.setStatusTip("Insert bullet list")
        bullet_action.setShortcut("Ctrl+Shift+B")
        bullet_action.triggered.connect(self.bullet_list)

        numbered_action = QAction(QIcon("icons/number.png"), "Insert numbered List", self)
        numbered_action.setStatusTip("Insert numbered list")
        numbered_action.setShortcut("Ctrl+Shift+L")
        numbered_action.triggered.connect(self.number_list)

        self.find_action = QAction(QIcon("icons/find.png"), "Find and replace", self)
        self.find_action.setStatusTip("Find and replace words in your document")
        self.find_action.setShortcut("Ctrl+F")
        self.find_action.triggered.connect(find.Find(self).show)

        image_action = QAction(QIcon("icons/image.png"), "Insert image", self)
        image_action.setStatusTip("Insert image")
        image_action.setShortcut("Ctrl+Shift+I")
        image_action.triggered.connect(self.insert_image)

        word_count_action = QAction(QIcon("icons/count.png"), "See word/symbol count", self)
        word_count_action.setStatusTip("See word/symbol count")
        word_count_action.setShortcut("Ctrl+W")
        word_count_action.triggered.connect(self.word_count)

        date_time_action = QAction(QIcon("icons/calender.png"), "Insert current date/time", self)
        date_time_action.setStatusTip("Insert current date/time")
        date_time_action.setShortcut("Ctrl+D")
        date_time_action.triggered.connect(datetime.DateTime(self).show)

        table_action = QAction(QIcon("icons/table.png"), "Insert table", self)
        table_action.setStatusTip("Insert table")
        table_action.setShortcut("Ctrl+T")
        table_action.triggered.connect(table.Table(self).show)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.open_action)
        self.toolbar.addAction(self.save_action)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.print_action)
        self.toolbar.addAction(self.preview_action)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cut_action)
        self.toolbar.addAction(self.copy_action)
        self.toolbar.addAction(self.paste_action)
        self.toolbar.addAction(self.undo_action)
        self.toolbar.addAction(self.redo_action)

        self.toolbar.addSeparator()

        self.toolbar.addAction(word_count_action)
        self.toolbar.addAction(image_action)
        self.toolbar.addAction(self.find_action)

        self.toolbar.addSeparator()

        self.toolbar.addAction(bullet_action)
        self.toolbar.addAction(numbered_action)

        self.toolbar.addAction(date_time_action)

        self.toolbar.addAction(table_action)

        self.addToolBarBreak()

    def init_format_bar(self):
        font_box = QFontComboBox(self)
        font_box.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))

        font_size = QSpinBox(self)

        font_size.setSuffix(" pt")

        font_size.valueChanged.connect(lambda size: self.text.setFontPointSize(size))

        font_size.setValue(14)

        font_color = QAction(QIcon("icons/font-color.png"), "Change font color", self)
        font_color.triggered.connect(self.font_color)

        bold_action = QAction(QIcon("icons/bold.png"), "Bold", self)
        bold_action.triggered.connect(self.bold)

        italic_action = QAction(QIcon("icons/italic.png"), "Italic", self)
        italic_action.triggered.connect(self.italic)

        underl_action = QAction(QIcon("icons/underline.png"), "Underline", self)
        underl_action.triggered.connect(self.underline)

        strike_action = QAction(QIcon("icons/strike.png"), "Strike-out", self)
        strike_action.triggered.connect(self.strike)

        super_action = QAction(QIcon("icons/superscript.png"), "Superscript", self)
        super_action.triggered.connect(self.super_script)

        sub_action = QAction(QIcon("icons/subscript.png"), "Subscript", self)
        sub_action.triggered.connect(self.sub_script)

        align_left = QAction(QIcon("icons/align-left.png"), "Align left", self)
        align_left.triggered.connect(self.align_left)

        align_center = QAction(QIcon("icons/align-center.png"), "Align center", self)
        align_center.triggered.connect(self.align_center)

        align_right = QAction(QIcon("icons/align-right.png"), "Align right", self)
        align_right.triggered.connect(self.align_right)

        align_justify = QAction(QIcon("icons/align-justify.png"), "Align justify", self)
        align_justify.triggered.connect(self.align_justify)

        indent_action = QAction(QIcon("icons/indent.png"), "Indent Area", self)
        indent_action.setShortcut("Ctrl+Tab")
        indent_action.triggered.connect(self.indent)

        dedent_action = QAction(QIcon("icons/dedent.png"), "Dedent Area", self)
        dedent_action.setShortcut("Shift+Tab")
        dedent_action.triggered.connect(self.dedent)

        back_color = QAction(QIcon("icons/highlight.png"), "Change background color", self)
        back_color.triggered.connect(self.highlight)

        self.formatbar = self.addToolBar("Format")

        self.formatbar.addWidget(font_box)
        self.formatbar.addWidget(font_size)

        self.formatbar.addSeparator()

        self.formatbar.addAction(font_color)
        self.formatbar.addAction(back_color)

        self.formatbar.addSeparator()

        self.formatbar.addAction(bold_action)
        self.formatbar.addAction(italic_action)
        self.formatbar.addAction(underl_action)
        self.formatbar.addAction(strike_action)
        self.formatbar.addAction(super_action)
        self.formatbar.addAction(sub_action)

        self.formatbar.addSeparator()

        self.formatbar.addAction(align_left)
        self.formatbar.addAction(align_center)
        self.formatbar.addAction(align_right)
        self.formatbar.addAction(align_justify)

        self.formatbar.addSeparator()

        self.formatbar.addAction(indent_action)
        self.formatbar.addAction(dedent_action)

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

        edit.addAction(self.find_action)

        toolbar_action = QAction("Toggle Toolbar", self)
        toolbar_action.triggered.connect(self.toggle_toolbar)

        formatbar_action = QAction("Toggle Formatbar", self)
        formatbar_action.triggered.connect(self.toggle_formatbar)

        statusbar_action = QAction("Toggle Statusbar", self)
        statusbar_action.triggered.connect(self.toggle_statusbar)

        view.addAction(toolbar_action)
        view.addAction(formatbar_action)
        view.addAction(statusbar_action)

    def init_ui(self):
        self.text = QTextEdit(self)

        self.text.setTabStopWidth(33)

        self.init_tool_bar()
        self.init_format_bar()
        self.init_menu_bar()

        self.setCentralWidget(self.text)

        self.statusbar = self.statusBar()

        self.text.cursorPositionChanged.connect(self.cursor_position)

        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)

        self.text.textChanged.connect(self.changed)

        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Writer")
        self.setWindowIcon(QIcon("icons/icon.png"))

    def font_family(self, font):
        self.text.setCurrentFont(font)

    def font_size(self, font_size):
        self.text.setFontPointSize(int(font_size))

    def font_color(self):

        color = QColorDialog.getColor()

        self.text.setTextColor(color)

    def highlight(self):

        color = QColorDialog.getColor()

        self.text.setTextBackgroundColor(color)

    def bold(self):

        if self.text.fontWeight() == QFont.Bold:

            self.text.setFontWeight(QFont.Normal)

        else:

            self.text.setFontWeight(QFont.Bold)

    def italic(self):

        state = self.text.fontItalic()

        self.text.setFontItalic(not state)

    def underline(self):

        state = self.text.fontUnderline()

        self.text.setFontUnderline(not state)

    def strike(self):

        fmt = self.text.currentCharFormat()

        fmt.setFontStrikeOut(not fmt.fontStrikeOut())

        self.text.setCurrentCharFormat(fmt)

    def super_script(self):

        fmt = self.text.currentCharFormat()

        align = fmt.verticalAlignment()

        if align == QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)

        else:

            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

    def sub_script(self):

        fmt = self.text.currentCharFormat()

        align = fmt.verticalAlignment()

        if align == QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QTextCharFormat.AlignSubScript)

        else:

            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

    def align_left(self):
        self.text.setAlignment(Qt.AlignLeft)

    def align_right(self):
        self.text.setAlignment(Qt.AlignRight)

    def align_center(self):
        self.text.setAlignment(Qt.AlignCenter)

    def align_justify(self):
        self.text.setAlignment(Qt.AlignJustify)

    @staticmethod
    def new():
        spawn = TextEditor()
        spawn.show()

    def open(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.writer)")[0]

        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())

    def save(self):

        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self, 'Save File')[0]

        if self.filename:

            if not self.filename.endswith(".writer"):
                self.filename += ".writer"

            with open(self.filename, "wt") as file:
                file.write(self.text.toHtml())

            self.changesSaved = True

    def preview(self):

        preview = QPrintPreviewDialog()

        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def print(self):

        dialog = QPrintDialog()

        if dialog.exec_() == QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def bullet_list(self):

        cursor = self.text.textCursor()

        cursor.insertList(QTextListFormat.ListDisc)

    def number_list(self):

        cursor = self.text.textCursor()

        cursor.insertList(QTextListFormat.ListDecimal)

    def cursor_position(self):

        cursor = self.text.textCursor()

        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line, col))

    def indent(self):

        cursor = self.text.textCursor()

        if cursor.hasSelection():

            temp = cursor.blockNumber()

            cursor.setPosition(cursor.selectionEnd())

            diff = cursor.blockNumber() - temp

            for n in range(diff + 1):
                cursor.movePosition(QTextCursor.StartOfLine)

                cursor.insertText("\t")

                cursor.movePosition(QTextCursor.Up)

        else:

            cursor.insertText("\t")

    def dedent(self):

        cursor = self.text.textCursor()

        if cursor.hasSelection():

            temp = cursor.blockNumber()

            cursor.setPosition(cursor.selectionEnd())

            diff = cursor.blockNumber() - temp

            for n in range(diff + 1):
                self.handle_dedent(cursor)

                cursor.movePosition(QTextCursor.Up)

        else:
            self.handle_dedent(cursor)

    @staticmethod
    def handle_dedent(cursor):

        cursor.movePosition(QTextCursor.StartOfLine)

        line = cursor.block().text()

        if line.startswith("\t"):

            cursor.deleteChar()

        else:
            for char in line[:8]:

                if char != " ":
                    break

                cursor.deleteChar()

    def toggle_toolbar(self):

        state = self.toolbar.isVisible()

        self.toolbar.setVisible(not state)

    def toggle_formatbar(self):

        state = self.formatbar.isVisible()

        self.formatbar.setVisible(not state)

    def toggle_statusbar(self):

        state = self.statusbar.isVisible()

        self.statusbar.setVisible(not state)

    def insert_image(self):

        filename, _ = QFileDialog.getOpenFileName(self, 'Insert image', ".",
                                                  "Images (*.png *.xpm *.jpg *.bmp *.gif)")

        image = QImage(filename)

        if image.isNull():

            popup = QMessageBox(QMessageBox.Critical,
                                "Image load error",
                                "Could not load image file!",
                                QMessageBox.Ok,
                                self)
            popup.show()

        else:

            cursor = self.text.textCursor()

            cursor.insertImage(image, filename)

    def word_count(self):

        wc = wordcount.WordCount(self)

        wc.get_text()

        wc.show()

    def context(self, pos):

        cursor = self.text.textCursor()

        table = cursor.currentTable()
        if table:

            menu = QMenu(self)

            append_row_action = QAction("Append row", self)
            append_row_action.triggered.connect(lambda: table.appendRows(1))

            append_col_action = QAction("Append column", self)
            append_col_action.triggered.connect(lambda: table.appendColumns(1))

            remove_row_action = QAction("Remove row", self)
            remove_row_action.triggered.connect(self.remove_row)

            remove_col_action = QAction("Remove column", self)
            remove_col_action.triggered.connect(self.remove_col)

            insert_row_action = QAction("Insert row", self)
            insert_row_action.triggered.connect(self.insert_row)

            insert_col_action = QAction("Insert column", self)
            insert_col_action.triggered.connect(self.insert_col)

            merge_action = QAction("Merge cells", self)
            merge_action.triggered.connect(lambda: table.mergeCells(cursor))

            if not cursor.hasSelection():
                merge_action.setEnabled(False)

            split_action = QAction("Split cells", self)

            cell = table.cellAt(cursor)
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                split_action.triggered.connect(lambda: table.splitCell(cell.row(), cell.column(), 1, 1))

            else:
                split_action.setEnabled(False)

            menu.addAction(append_row_action)
            menu.addAction(append_col_action)

            menu.addSeparator()

            menu.addAction(remove_row_action)
            menu.addAction(remove_col_action)

            menu.addSeparator()

            menu.addAction(insert_row_action)
            menu.addAction(insert_col_action)

            menu.addSeparator()

            menu.addAction(merge_action)
            menu.addAction(split_action)

            pos = self.mapToGlobal(pos)
            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)

            menu.move(pos)

            menu.show()

        else:

            event = QContextMenuEvent(QContextMenuEvent.Mouse, QPoint())

            self.text.contextMenuEvent(event)

    def remove_row(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.remove_rows(cell.row(), 1)

    def remove_col(self):

        cursor = self.text.textCursor()
        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.remove_columns(cell.column(), 1)

    def insert_row(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.insert_rows(cell.row(), 1)

    def insert_col(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.insert_columns(cell.column(), 1)

    def changed(self):
        self.changesSaved = False

    def closeEvent(self, event):

        if self.changesSaved:
            event.accept()
        else:
            popup = QMessageBox(self)
            popup.setIcon(QMessageBox.Warning)
            popup.setText("The document has been modified")
            popup.setInformativeText("Do you want to save your changes?")
            popup.setStandardButtons(QMessageBox.Save |
                                     QMessageBox.Cancel |
                                     QMessageBox.Discard)
            popup.setDefaultButton(QMessageBox.Save)
            answer = popup.exec_()
            if answer == QMessageBox.Save:
                self.save()
                event.accept()
            elif answer == QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()




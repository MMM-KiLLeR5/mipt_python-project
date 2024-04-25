from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from src.ext import *


class ToolBar:
    @staticmethod
    def init_tool_bar(parent):
        parent.new_action = QAction(QIcon("icons/new.png"), "New", parent)
        parent.new_action.setStatusTip("Create a new document from scratch.")
        parent.new_action.setShortcut("Ctrl+N")
        parent.new_action.triggered.connect(parent.new)

        parent.open_action = QAction(QIcon("icons/open.png"), "Open file", parent)
        parent.open_action.setStatusTip("Open existing document")
        parent.open_action.setShortcut("Ctrl+O")
        parent.open_action.triggered.connect(parent.open)

        parent.save_action = QAction(QIcon("icons/save.png"), "Save", parent)
        parent.save_action.setStatusTip("Save document")
        parent.save_action.setShortcut("Ctrl+S")
        parent.save_action.triggered.connect(parent.save)

        parent.print_action = QAction(QIcon("icons/print.png"), "Print document", parent)
        parent.print_action.setStatusTip("Print document")
        parent.print_action.setShortcut("Ctrl+P")
        parent.print_action.triggered.connect(parent.print)

        parent.preview_action = QAction(QIcon("icons/preview.png"), "Page view", parent)
        parent.preview_action.setStatusTip("Preview page before printing")
        parent.preview_action.setShortcut("Ctrl+Shift+P")
        parent.preview_action.triggered.connect(parent.preview)

        parent.cut_action = QAction(QIcon("icons/cut.png"), "Cut to clipboard", parent)
        parent.cut_action.setStatusTip("Delete and copy text to clipboard")
        parent.cut_action.setShortcut("Ctrl+X")
        parent.cut_action.triggered.connect(parent.text.cut)

        parent.copy_action = QAction(QIcon("icons/copy.png"), "Copy to clipboard", parent)
        parent.copy_action.setStatusTip("Copy text to clipboard")
        parent.copy_action.setShortcut("Ctrl+C")
        parent.copy_action.triggered.connect(parent.text.copy)

        parent.paste_action = QAction(QIcon("icons/paste.png"), "Paste from clipboard", parent)
        parent.paste_action.setStatusTip("Paste text from clipboard")
        parent.paste_action.setShortcut("Ctrl+V")
        parent.paste_action.triggered.connect(parent.text.paste)

        parent.undo_action = QAction(QIcon("icons/undo.png"), "Undo last action", parent)
        parent.undo_action.setStatusTip("Undo last action")
        parent.undo_action.setShortcut("Ctrl+Z")
        parent.undo_action.triggered.connect(parent.text.undo)

        parent.redo_action = QAction(QIcon("icons/redo.png"), "Redo last undone thing", parent)
        parent.redo_action.setStatusTip("Redo last undone thing")
        parent.redo_action.setShortcut("Ctrl+Y")
        parent.redo_action.triggered.connect(parent.text.redo)

        bullet_action = QAction(QIcon("icons/bullet.png"), "Insert bullet List", parent)
        bullet_action.setStatusTip("Insert bullet list")
        bullet_action.setShortcut("Ctrl+Shift+B")
        bullet_action.triggered.connect(parent.bullet_list)

        numbered_action = QAction(QIcon("icons/number.png"), "Insert numbered List", parent)
        numbered_action.setStatusTip("Insert numbered list")
        numbered_action.setShortcut("Ctrl+Shift+L")
        numbered_action.triggered.connect(parent.number_list)

        parent.find_action = QAction(QIcon("icons/find.png"), "Find and replace", parent)
        parent.find_action.setStatusTip("Find and replace words in your document")
        parent.find_action.setShortcut("Ctrl+F")
        parent.find_action.triggered.connect(find.Find(parent).show)

        image_action = QAction(QIcon("icons/image.png"), "Insert image", parent)
        image_action.setStatusTip("Insert image")
        image_action.setShortcut("Ctrl+Shift+I")
        image_action.triggered.connect(parent.insert_image)

        word_count_action = QAction(QIcon("icons/count.png"), "See word/symbol count", parent)
        word_count_action.setStatusTip("See word/symbol count")
        word_count_action.setShortcut("Ctrl+W")
        word_count_action.triggered.connect(parent.word_count)

        date_time_action = QAction(QIcon("icons/calender.png"), "Insert current date/time", parent)
        date_time_action.setStatusTip("Insert current date/time")
        date_time_action.setShortcut("Ctrl+D")
        date_time_action.triggered.connect(datetime.DateTime(parent).show)

        table_action = QAction(QIcon("icons/table.png"), "Insert table", parent)
        table_action.setStatusTip("Insert table")
        table_action.setShortcut("Ctrl+T")
        table_action.triggered.connect(table.Table(parent).show)

        parent.toolbar = parent.addToolBar("Options")

        parent.toolbar.addAction(parent.new_action)
        parent.toolbar.addAction(parent.open_action)
        parent.toolbar.addAction(parent.save_action)

        parent.toolbar.addSeparator()

        parent.toolbar.addAction(parent.print_action)
        parent.toolbar.addAction(parent.preview_action)

        parent.toolbar.addSeparator()

        parent.toolbar.addAction(parent.cut_action)
        parent.toolbar.addAction(parent.copy_action)
        parent.toolbar.addAction(parent.paste_action)
        parent.toolbar.addAction(parent.undo_action)
        parent.toolbar.addAction(parent.redo_action)

        parent.toolbar.addSeparator()

        parent.toolbar.addAction(word_count_action)
        parent.toolbar.addAction(image_action)
        parent.toolbar.addAction(parent.find_action)

        parent.toolbar.addSeparator()

        parent.toolbar.addAction(bullet_action)
        parent.toolbar.addAction(numbered_action)

        parent.toolbar.addAction(date_time_action)

        parent.toolbar.addAction(table_action)

        parent.addToolBarBreak()

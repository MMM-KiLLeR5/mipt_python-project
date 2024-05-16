from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QFont
from PyQt5.QtWidgets import QFontComboBox, QSpinBox, QAction, QMainWindow, QColorDialog
from PyQt5.QtCore import Qt


class Lexic:

    @staticmethod
    def init_format_bar(var):
        font_box = QFontComboBox(var)
        font_box.currentFontChanged.connect(lambda font: var.text.setCurrentFont(font))

        font_size = QSpinBox(var)

        font_size.setSuffix(" pt")

        font_size.valueChanged.connect(lambda size: var.text.setFontPointSize(size))

        font_size.setValue(14)

        font_color = QAction(QIcon("icons/font-color.png"), "Change font color", var)
        font_color.triggered.connect(lambda: Lexic.font_color(var))

        bold_action = QAction(QIcon("icons/bold.png"), "Bold", var)
        bold_action.triggered.connect(lambda: Lexic.bold(var))

        italic_action = QAction(QIcon("icons/italic.png"), "Italic", var)
        italic_action.triggered.connect(lambda: Lexic.italic(var))

        underl_action = QAction(QIcon("icons/underline.png"), "Underline", var)
        underl_action.triggered.connect(lambda: Lexic.underline(var))

        strike_action = QAction(QIcon("icons/strike.png"), "Strike-out", var)
        strike_action.triggered.connect(lambda: Lexic.strike(var))

        super_action = QAction(QIcon("icons/superscript.png"), "Superscript", var)
        super_action.triggered.connect(lambda: Lexic.super_script(var))

        sub_action = QAction(QIcon("icons/subscript.png"), "Subscript", var)
        sub_action.triggered.connect(lambda: Lexic.sub_script(var))

        align_left = QAction(QIcon("icons/align-left.png"), "Align left", var)
        align_left.triggered.connect(lambda: Lexic.align_left(var))

        align_center = QAction(QIcon("icons/align-center.png"), "Align center", var)
        align_center.triggered.connect(lambda: Lexic.align_center(var))

        align_right = QAction(QIcon("icons/align-right.png"), "Align right", var)
        align_right.triggered.connect(lambda: Lexic.align_right(var))

        align_justify = QAction(QIcon("icons/align-justify.png"), "Align justify", var)
        align_justify.triggered.connect(lambda: Lexic.align_justify(var))

        indent_action = QAction(QIcon("icons/indent.png"), "Indent Area", var)
        indent_action.setShortcut("Ctrl+Tab")
        indent_action.triggered.connect(lambda: Lexic.indent(var))

        dedent_action = QAction(QIcon("icons/dedent.png"), "Dedent Area", var)
        dedent_action.setShortcut("Shift+Tab")
        dedent_action.triggered.connect(lambda: Lexic.dedent(var))

        back_color = QAction(QIcon("icons/highlight.png"), "Change background color", var)
        back_color.triggered.connect(lambda: Lexic.highlight(var))

        var.formatbar = var.addToolBar("Format")

        var.formatbar.addWidget(font_box)
        var.formatbar.addWidget(font_size)

        var.formatbar.addSeparator()

        var.formatbar.addAction(font_color)
        var.formatbar.addAction(back_color)

        var.formatbar.addSeparator()

        var.formatbar.addAction(bold_action)
        var.formatbar.addAction(italic_action)
        var.formatbar.addAction(underl_action)
        var.formatbar.addAction(strike_action)
        var.formatbar.addAction(super_action)
        var.formatbar.addAction(sub_action)

        var.formatbar.addSeparator()

        var.formatbar.addAction(align_left)
        var.formatbar.addAction(align_center)
        var.formatbar.addAction(align_right)
        var.formatbar.addAction(align_justify)

        var.formatbar.addSeparator()

        var.formatbar.addAction(indent_action)
        var.formatbar.addAction(dedent_action)

    def dedent(var):

        cursor = var.text.textCursor()

        if cursor.hasSelection():

            temp = cursor.blockNumber()

            cursor.setPosition(cursor.selectionEnd())

            diff = cursor.blockNumber() - temp

            for n in range(diff + 1):
                Lexic.handle_dedent(cursor)

                cursor.movePosition(QTextCursor.Up)

        else:
            Lexic.handle_dedent(cursor)

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

    @staticmethod
    def toggle_formatbar(var):

        state = var.formatbar.isVisible()

        var.formatbar.setVisible(not state)

    @staticmethod
    def font_color(var):

        color = QColorDialog.getColor()

        var.text.setTextColor(color)

    @staticmethod
    def highlight(var):

        color = QColorDialog.getColor()

        var.text.setTextBackgroundColor(color)

    @staticmethod
    def bold(var):
        if var.text.fontWeight() == QFont.Bold:

            var.text.setFontWeight(QFont.Normal)

        else:

            var.text.setFontWeight(QFont.Bold)

    @staticmethod
    def italic(var):

        state = var.text.fontItalic()

        var.text.setFontItalic(not state)

    @staticmethod
    def underline(var):

        state = var.text.fontUnderline()

        var.text.setFontUnderline(not state)

    @staticmethod
    def strike(var):

        fmt = var.text.currentCharFormat()

        fmt.setFontStrikeOut(not fmt.fontStrikeOut())

        var.text.setCurrentCharFormat(fmt)

    @staticmethod
    def super_script(var):

        fmt = var.text.currentCharFormat()

        align = fmt.verticalAlignment()

        if align == QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)

        else:

            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        var.text.setCurrentCharFormat(fmt)

    @staticmethod
    def sub_script(var):

        fmt = var.text.currentCharFormat()

        align = fmt.verticalAlignment()

        if align == QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QTextCharFormat.AlignSubScript)

        else:

            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        var.text.setCurrentCharFormat(fmt)

    @staticmethod
    def align_left(var):
        var.text.setAlignment(Qt.AlignLeft)

    @staticmethod
    def align_right(var):
        var.text.setAlignment(Qt.AlignRight)

    @staticmethod
    def align_center(var):
        var.text.setAlignment(Qt.AlignCenter)

    @staticmethod
    def align_justify(var):
        var.text.setAlignment(Qt.AlignJustify)

    @staticmethod
    def indent(var):

        cursor = var.text.textCursor()

        if cursor.hasSelection():
            temp = cursor.blockNumber()

            cursor.setPosition(cursor.anchor())

            diff = cursor.blockNumber() - temp

            direction = QTextCursor.Up if diff > 0 else QTextCursor.Down

            for n in range(abs(diff) + 1):
                cursor.movePosition(QTextCursor.StartOfLine)

                cursor.insertText("\t")

                cursor.movePosition(direction)

        else:

            cursor.insertText("\t")

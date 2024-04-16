from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QDialog


class WordCount(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.parent = parent

        self.init_ui()

    def init_ui(self):
        current_label = QLabel("Current selection", self)
        current_label.setStyleSheet("font-weight:bold; font-size: 15px;")

        current_words_label = QLabel("Words: ", self)
        current_symbols_label = QLabel("Symbols: ", self)

        self.current_words = QLabel(self)
        self.current_symbols = QLabel(self)

        total_label = QLabel("Total", self)
        total_label.setStyleSheet("font-weight:bold; font-size: 15px;")

        total_words_label = QLabel("Words: ", self)
        total_symbols_label = QLabel("Symbols: ", self)

        self.total_words = QLabel(self)
        self.total_symbols = QLabel(self)


        layout = QGridLayout(self)

        layout.addWidget(current_label, 0, 0)

        layout.addWidget(current_words_label, 1, 0)
        layout.addWidget(self.current_words, 1, 1)

        layout.addWidget(current_symbols_label, 2, 0)
        layout.addWidget(self.current_symbols, 2, 1)

        spacer = QWidget()
        spacer.setFixedSize(0, 5)

        layout.addWidget(spacer, 3, 0)

        layout.addWidget(total_label, 4, 0)

        layout.addWidget(total_words_label, 5, 0)
        layout.addWidget(self.total_words, 5, 1)

        layout.addWidget(total_symbols_label, 6, 0)
        layout.addWidget(self.total_symbols, 6, 1)

        self.setWindowTitle("Word count")
        self.setGeometry(300, 300, 200, 200)
        self.setLayout(layout)

    def get_text(self):
        text = self.parent.text.textCursor().selectedText()

        words = str(len(text.split()))

        symbols = str(len(text))

        self.current_words.setText(words)
        self.current_symbols.setText(symbols)

        text = self.parent.text.toPlainText()

        words = str(len(text.split()))
        symbols = str(len(text))

        self.total_words.setText(words)
        self.total_symbols.setText(symbols)

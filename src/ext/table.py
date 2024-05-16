from PyQt5.QtGui import QTextTableFormat
from PyQt5.QtWidgets import QDialog, QLabel, QSpinBox, QMessageBox, QPushButton, QGridLayout


class Table(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.parent = parent

        self.init_ui()

    def init_ui(self):

        rows_label = QLabel("Rows: ", self)

        self.rows = QSpinBox(self)

        cols_label = QLabel("Columns", self)

        self.cols = QSpinBox(self)

        space_label = QLabel("Cell spacing", self)

        self.space = QSpinBox(self)

        pad_label = QLabel("Cell padding", self)

        self.pad = QSpinBox(self)

        self.pad.setValue(10)

        insert_button = QPushButton("Insert", self)
        insert_button.clicked.connect(self.insert)

        layout = QGridLayout()

        layout.addWidget(rows_label, 0, 0)
        layout.addWidget(self.rows, 0, 1)

        layout.addWidget(cols_label, 1, 0)
        layout.addWidget(self.cols, 1, 1)

        layout.addWidget(pad_label, 2, 0)
        layout.addWidget(self.pad, 2, 1)

        layout.addWidget(space_label, 3, 0)
        layout.addWidget(self.space, 3, 1)

        layout.addWidget(insert_button, 4, 0, 1, 2)

        self.setWindowTitle("Insert Table")
        self.setGeometry(300, 300, 200, 100)
        self.setLayout(layout)

    def insert(self):

        cursor = self.parent.text.textCursor()

        rows = self.rows.value()

        cols = self.cols.value()

        if not rows or not cols:

            popup = QMessageBox(QMessageBox.Warning,
                                "Parameter error",
                                "Row and column numbers may not be zero!",
                                QMessageBox.Ok,
                                self)
            popup.show()

        else:

            padding = self.pad.value()

            space = self.space.value()

            fmt = QTextTableFormat()

            fmt.setCellPadding(padding)

            fmt.setCellSpacing(space)

            cursor.insertTable(rows, cols, fmt)

            self.close()

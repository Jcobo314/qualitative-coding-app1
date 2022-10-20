import sys
from PySide6 import QtWidgets, QtCore, QtGui


class TableApplication(QtWidgets.QWidget):
    def __init__(self):
        """Instantiates a table, add row button, and a layout"""
        super().__init__()

        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(4)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.addRowButton = QtWidgets.QPushButton("Add Row")
        self.addRowButton.setGeometry(QtCore.QRect(200,150,93,28))
        self.addRowButton.clicked.connect(self.addrow)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.addRowButton)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def addrow(self):
        """Add Row Button Logic"""
        self.table.setRowCount(self.table.rowCount() + 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ex = TableApplication()
    ex.show()
    sys.exit(app.exec())

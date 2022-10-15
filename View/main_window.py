from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """MainWindow is the main window of the application."""

    def __init__(self):
        """
        Constructor - Initializes the properties of the main window and all
        containing GUI elements.
        """
        super().__init__()

        self.setWindowTitle("Qualitative Coding Desktop App")
        self.setWindowState(Qt.WindowMaximized)

        self.create_menu_bar()

    def create_menu_bar(self):
        """
        Creates the main menu-bar for the application window and populates it with a
        File sub-menu.
        """
        file_menu = self.menuBar().addMenu("File")

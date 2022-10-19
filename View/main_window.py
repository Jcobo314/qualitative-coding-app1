from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QStyle

import resources

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
        #accesses image from the resource qrc file
        open_icon = QIcon.fromTheme(":/icons/export.png")  # need an icon image (TODO)!

        #adds a load video button with an action
        self.open_action = QAction(open_icon, "Load video file", self)
        file_menu.addAction(self.open_action)

    """ Make function to add slot to whatever, as parameter given a slot function to access the function
    in the controller """
    def connect_action_to_slot(self, slot):
        """
        Parameters:
            slot: the handler function that is called when the signal is clicked

        In this case this function checks whether the load video button is pressed
        then calls the slot specific slot function in the controller
        """
        self.open_action.triggered.connect(slot)

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QStyle


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
        # Accesses image from the resource qrc file.
        file_dialog_icon = self.style().standardIcon(QStyle.SP_FileDialogStart)

        # Adds a load video button with an action.
        self.open_action = QAction(file_dialog_icon, "Load video file", self)
        file_menu.addAction(self.open_action)

    def connect_load_video_to_slot(self, slot):
        """
        Summary:
            In this case this function checks whether the load video button is pressed
            then calls the slot specific slot function in the controller.

        Parameters:
            slot: The handler function that is called when the signal is clicked.
        """
        self.open_action.triggered.connect(slot)

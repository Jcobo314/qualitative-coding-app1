from PySide6.QtCore import Slot
from PySide6.QtMultimedia import QMediaFormat
from PySide6.QtWidgets import QFileDialog, QDialog


def get_supported_mime_types():
    """
    This returns a list of supported mime types for the specific OS.
    It is used to set a filter on files so only media files can be played.
    """
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result

class Controller:
    """
    The Controller responds to input events from the View. The Controller
    interacts with the application Manager or with the Qt framework in order to
    perform the appropriate response.
    """

    def __init__(self, window):
        """
        Constructor - Initializes the Controller instance.

        Parameters:
            window (MainWindow): the main Window of the application
        """
        self.window = window

        #this calls the function in main_window (view section)
        window.connect_action_to_slot(self.load_video_handler)

    @Slot()
    def load_video_handler(self):
        """
        slot function that will act as a handler whenever the load video
        button is clicked
        """

        #opens the file browser, doesn't need any arguments as the window calls this
        file_dialog = QFileDialog()

        #print(get_supported_mime_types())
        #this gets the mime_types for the specific system and sets a filter
        mime_types = get_supported_mime_types()
        file_dialog.setMimeTypeFilters(mime_types)

        #this checks if a file to play has been selected
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._player.setSource(url)
            self._player.play()



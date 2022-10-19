import sys

from PySide6.QtCore import Slot
from PySide6.QtMultimedia import QMediaFormat, QMediaPlayer
from PySide6.QtWidgets import QFileDialog, QDialog


AVI = "video/x-msvideo"  # AVI


MP4 = 'video/mp4'  # MP4


def get_supported_mime_types():
    """
    Summary:
        get_supported_mime_types() - This returns a list of supported
        mime types for the specific OS. It is used to set a filter on files so
        only media files can be played.
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
        self.media_player = QMediaPlayer()

        window.connect_load_video_to_slot(self.open_file_dialog)

    @Slot()
    def open_file_dialog(self):
        """
        Summary:
            load_video_handler() - Slot function that will act as a handler whenever the
            load video button is clicked.
        """

        # Opens the file browser, doesn't need any arguments as the window calls this.
        file_dialog = QFileDialog()

        # This gets the mime_types for the specific system and sets a filter.
        is_windows = sys.platform == 'win32'
        mime_types = get_supported_mime_types()

        # Adds AVI and MP4 if they were not supported
        if is_windows and AVI not in mime_types:
            mime_types.append(AVI)
        elif MP4 not in mime_types:
            mime_types.append(MP4)
        file_dialog.setMimeTypeFilters(mime_types)

        # This checks if a file to play has been selected.
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self.media_player.setSource(url)

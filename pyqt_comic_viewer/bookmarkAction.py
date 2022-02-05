from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QAction


class BookmarkAction(QAction):
    clicked = pyqtSignal(QAction)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.triggered.connect(self.__sendClicked)

    def __sendClicked(self):
        self.clicked.emit(self)
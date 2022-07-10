import os

from PyQt5.QtWidgets import QApplication
from pyqt_comic_viewer.comicBookViewer import ComicBookViewer

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class ComicBookViewerApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = ComicBookViewer()
        StyleSetter.setWindowStyle(mainWindow)
        icon_filename = os.path.join(os.path.dirname(__file__), 'ico/book.svg')
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBarWindow(mainWindow, icon_filename=icon_filename)
        self.__titleBarWindow.show()
import os, sys, inspect

from PyQt5.QtWidgets import QApplication, QPushButton
from pyqt_custom_titlebar_window import CustomTitlebarWindow
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_comic_viewer.comicBookViewer import ComicBookViewer

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class ComicBookViewerApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = ComicBookViewer()
        StyleSetter.setWindowStyle(mainWindow)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/book.svg')
        self.__titleBarWindow.show()
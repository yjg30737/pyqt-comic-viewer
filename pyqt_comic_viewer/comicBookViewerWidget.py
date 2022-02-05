from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QMenu, QAction, QColorDialog
from PyQt5.QtCore import Qt, pyqtSignal, QPoint, QRect
from pyqt_resource_helper import PyQtResourceHelper

from python_open_filepath_and_select.openFilePathAndSelect import *
from pyqt_viewer_widget import ViewerWidget


class ComicBookViewerWidget(ViewerWidget):
    photoClicked = pyqtSignal(QPoint)
    rectChanged = pyqtSignal(QRect)
    backgroundColorSignal = pyqtSignal(QColor)
    invertColor = pyqtSignal()
    addBookmark = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__invert_flag = False
        self.__initUi()

    def __initUi(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__prepare_menu)
        PyQtResourceHelper.setStyleSheet([self], ['style/text_button.css'])

    def __prepare_menu(self, pos):
        menu = QMenu(self)

        openPathAction = QAction('Show In Explorer', self)
        openPathAction.triggered.connect(self.__openPath)

        backgroundColorSettingsAction = QAction('Set Background Color Settings', self)
        backgroundColorSettingsAction.triggered.connect(self.__sendBackgroundColorSignal)

        self.__invertColorAction = QAction('Invert Color', self)
        self.__invertColorAction.setCheckable(True)
        self.__invertColorAction.setChecked(self.__invert_flag)
        self.__invertColorAction.toggled.connect(self.__invertColor)

        self.__addBookmarkAction = QAction('Add To Bookmark', self)
        self.__addBookmarkAction.triggered.connect(self.__addBookmark)

        menu.addAction(openPathAction)
        menu.addAction(backgroundColorSettingsAction)
        menu.addSeparator()
        menu.addAction(self.__invertColorAction)
        menu.addAction(self.__addBookmarkAction)
        menu.exec(self.mapToGlobal(pos))

    def __sendBackgroundColorSignal(self):
        color = QColorDialog.getColor()
        self.backgroundColorSignal.emit(color)

    def __openPath(self):
        open_file_path_and_select(self.getCurrentFilename())

    def __invertColor(self, f):
        self.__invert_flag = f
        self.__invertColorAction.setChecked(f)
        self.__setImage()

    def _prev(self):
        n = super()._prev()
        if n == 0:
            self.__setImage()
        elif n == -1:
            print('no prev')

    def _next(self):
        n = super()._next()
        if n == 0:
            self.__setImage()
        elif n == -1:
            print('no next')

    def __setImage(self):
        filename = self.getCurrentFilename()
        if self.__invert_flag:
            p = QPixmap(filename)
            img = p.toImage()
            img.invertPixels()
            p.convertFromImage(img)
            self._graphicsView.setPixmap(p)
        else:
            self._graphicsView.setFile(filename)

    def __addBookmark(self):
        self.addBookmark.emit()
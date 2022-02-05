
import sys, os
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, \
    QFileDialog, QColorDialog, QSplitter, QGridLayout, QWidget, QVBoxLayout

from pyqt_comic_viewer.recentFileWidget import RecentFileWidget
from pyqt_comic_viewer.bookmarkAction import BookmarkAction
from pyqt_comic_viewer.comicBookViewerWidget import ComicBookViewerWidget
import zipfile
from zipfile import ZipFile

from pyqt_resource_helper.pyqtResourceHelper import PyQtResourceHelper


class ComicBookViewer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        title = 'Comic Viewer'

        self.setWindowTitle(title)

        self.__comicBookViewerWidget = ComicBookViewerWidget()
        self.__comicBookViewerWidget.addBookmark.connect(self.__addBookmark)

        self.__leftWidget = RecentFileWidget()
        self.__leftWidget.openRecentFile.connect(self.__loadImage)

        lay = QVBoxLayout()
        lay.addWidget(self.__comicBookViewerWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        
        rightWidget = QWidget()
        rightWidget.setLayout(lay)

        mainSplitter = QSplitter()
        mainSplitter.addWidget(self.__leftWidget)
        mainSplitter.addWidget(rightWidget)
        mainSplitter.setSizes([200, 800])

        mainSplitter.setChildrenCollapsible(False)

        lay = QGridLayout()
        lay.addWidget(mainSplitter)
        lay.setContentsMargins(0, 0, 0, 0)
        
        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

        self.__setMenuBar()

        self.__comicBookViewerWidget.setBottomWidgetVisible(False)

        PyQtResourceHelper.setStyleSheet([self], ['style/dark_gray_theme.css'])

    def __backgroundColorSettings(self):
        color = QColorDialog.getColor()
        self.__comicBookViewerWidget.setStyleSheet("QGraphicsView { background: "+color.name() + "}")

    def __mainBackgroundSettings(self):
        filename = QFileDialog.getOpenFileName(self, 'Set the main background', '', 'Image File (*.jpg *.png *.bmp)')
        if filename[0]:
            filename = filename[0]
            print(filename)

    def __setMenuBar(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        homeAction = QAction('&Home', self)
        homeAction.triggered.connect(self.__goHome)

        openFileAction = QAction('&Open File', self)
        openFileAction.triggered.connect(self.__loadFile)

        openZipFileAction = QAction('&Open Compressed File', self)
        openZipFileAction.triggered.connect(self.__loadZipFile)

        openDirAction = QAction('&Open Directory', self)
        openDirAction.setShortcut('Ctrl+O')
        openDirAction.triggered.connect(self.__loadDir)

        fileMenu.addAction(homeAction)
        fileMenu.addSeparator()
        fileMenu.addAction(openFileAction)
        fileMenu.addAction(openZipFileAction)
        fileMenu.addAction(openDirAction)

        viewMenu = menubar.addMenu('&Show')

        self.__bottomWidgetToggledAction = QAction('Show Prev/Next Buttons', self)
        self.__bottomWidgetToggledAction.setCheckable(True)
        self.__bottomWidgetToggledAction.setChecked(False)
        self.__bottomWidgetToggledAction.toggled.connect(self.__bottomWidgetToggled)
        
        self.__recentFileToggleAction = QAction('Show Recent Window', self)
        self.__recentFileToggleAction.setCheckable(True)
        self.__recentFileToggleAction.setChecked(True)
        self.__recentFileToggleAction.triggered.connect(self.__recentFileToggled)

        self.__leftWidget.closeSignal.connect(self.__recentFileToggleAction.setChecked)

        self.__showFullScreenAction = QAction('Show As Full Screen', self)
        self.__showFullScreenAction.setShortcut('F11')
        self.__showFullScreenAction.setCheckable(True)
        self.__showFullScreenAction.setChecked(False)
        self.__showFullScreenAction.toggled.connect(self.__showFullScreenToggled)
        
        viewMenu.addAction(self.__bottomWidgetToggledAction)
        viewMenu.addAction(self.__recentFileToggleAction)
        viewMenu.addAction(self.__showFullScreenAction)

        settingsMenu = menubar.addMenu('Settings')

        backgroundColorSettingsAction = QAction('Set Background Color Settings', self)
        backgroundColorSettingsAction.triggered.connect(self.__backgroundColorSettings)

        mainBackgroundSettingsAction = QAction('Main Background Settings', self)
        mainBackgroundSettingsAction.triggered.connect(self.__mainBackgroundSettings)

        settingsMenu.addAction(backgroundColorSettingsAction)
        settingsMenu.addAction(mainBackgroundSettingsAction)

        self.__bookmarkMenu = menubar.addMenu('&Bookmark')
        self.__initBookmarkMenu()

    def __goHome(self):
        print('home')

    def __loadImage(self, filename):
        dirname = filename if os.path.isdir(filename) else os.path.dirname(filename)
        filenames = os.listdir(dirname)
        if filenames:
            filenames = [os.path.join(dirname, filename) for filename in filenames]
            self.__comicBookViewerWidget.setFilenames(filenames=filenames)
            self.__comicBookViewerWidget.setFocus()

    def __loadFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Image File (*.jpg *.bmp *.png)')
        if filename[0]:
            filename = filename[0]
            filename = os.path.dirname(filename) + '\\' + os.path.basename(filename)
            self.__loadImage(filename)

    def __loadZipFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open Compressed File', '', 'Compressed file (*.zip)')
        if filename[0]:
            if zipfile.is_zipfile(filename[0]):
                zip_file = ZipFile(filename[0])
                filenames = []
                filenames_img_dict = {}
                for file in zip_file.infolist():
                    filename = file.filename
                    filenames.append(filename)
                    p = zip_file.open(file).read()
                    img = QImage()
                    img.loadFromData(p)
                    filenames_img_dict[filename] = QPixmap.fromImage(img)
                self.__comicBookViewerWidget.setFilenames(filenames)

    def __loadDir(self):
        dirname = QFileDialog.getExistingDirectory(None, 'Open Directory', '', QFileDialog.ShowDirsOnly)
        if dirname:
            self.__loadImage(dirname)
            
    def __bottomWidgetToggled(self, flag: bool):
        self.__comicBookViewerWidget.setBottomWidgetVisible(flag)

    def __recentFileToggled(self, flag: bool):
        if flag:
            self.__leftWidget.show()
        else:
            self.__leftWidget.hide()

    def __initBookmarkMenu(self):
        addBookmarkAction = QAction('Add Bookmark', self)
        addBookmarkAction.triggered.connect(self.__addBookmark)

        bookmarkEmpty = QAction('Nothing To Show', self)
        bookmarkEmpty.setEnabled(False)

        self.__bookmarkMenu.addAction(addBookmarkAction)
        self.__bookmarkMenu.addSeparator()
        self.__bookmarkMenu.addAction(bookmarkEmpty)
            
    def __addBookmark(self):
        filename = self.__comicBookViewerWidget.getCurrentFilename()
        actions = [action for action in self.__bookmarkMenu.actions()]
        # check the 'empty action' exists
        bookmarkEmpty = [action for action in actions if action.text() == 'Nothing To Show']
        if bookmarkEmpty:
            self.__bookmarkMenu.removeAction(bookmarkEmpty[0])
            action = BookmarkAction(filename, self)
            action.clicked.connect(self.__showBookmarkFile)
            self.__bookmarkMenu.addAction(action)

            # check the 'remove action' exists
            removeAll = [action for action in actions if action.text() == 'Remove All']
            if removeAll:
                pass
            else:
                removeAllBookmarksAction = QAction('Remove All', self)
                removeAllBookmarksAction.triggered.connect(self.__removeAll)
                sep = self.__bookmarkMenu.addSeparator()
                sep.setObjectName('removeAllBookmarksActionSeparator')
                self.__bookmarkMenu.addAction(removeAllBookmarksAction)
        else:
            action = BookmarkAction(filename, self)
            action.clicked.connect(self.__showBookmarkFile)
            self.__bookmarkMenu.insertAction(actions[2], action)

    def __showBookmarkFile(self, action):
        filename = action.text()
        self.__loadImage(filename)
        self.__bookmarkMenu.removeAction(action)

        actions = [action for action in self.__bookmarkMenu.actions()]
        if len(actions) <= 4:

            removeAll = [action for action in actions if action.text() == 'Remove All'][0]
            removeAllSeparator = [action for action in actions if
                                  action.objectName() == 'removeAllBookmarksActionSeparator'][0]
            if removeAll:
                self.__bookmarkMenu.removeAction(removeAll)
                self.__bookmarkMenu.removeAction(removeAllSeparator)

            bookmarkEmpty = QAction('Nothing To Show', self)
            bookmarkEmpty.setEnabled(False)

            self.__bookmarkMenu.addAction(bookmarkEmpty)

    def __removeAll(self):
        self.__bookmarkMenu.clear()
        self.__initBookmarkMenu()

    def __showFullScreenToggled(self, f):
        if f:
            self.showFullScreen()
        else:
            self.showNormal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    comicBookViewer = ComicBookViewer()
    comicBookViewer.show()
    app.exec_()

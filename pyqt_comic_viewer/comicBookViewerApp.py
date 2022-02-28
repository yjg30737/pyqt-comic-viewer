from PyQt5.QtWidgets import QApplication, QPushButton
from pyqt_comic_viewer.comicBookViewer import ComicBookViewer
from pyqt_custom_titlebar_window import CustomTitlebarWindow
from pyqt_dark_gray_theme.darkGrayTheme import getThemeStyle, getIconButtonStyle, getIconTextButtonStyle, \
    getMenuBarStyle


class ComicBookViewerApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ex = ComicBookViewer()
        ex.setStyleSheet(getThemeStyle())  # theme
        btns = ex.findChildren(QPushButton)  # buttons
        for btn in btns:
            # check if text exists
            if btn.text().strip() == '':
                btn.setStyleSheet(getIconButtonStyle())  # no text - icon button style
            else:
                btn.setStyleSheet(getIconTextButtonStyle())  # text - icon-text button style
        menu_bar = ex.menuBar()  # menu bar
        menu_bar_style = getMenuBarStyle(menu_bar)
        menu_bar.setStyleSheet(menu_bar_style)
        self.__window = CustomTitlebarWindow(ex)
        self.__window.setTopTitleBar()
        self.__window.setButtons()
        self.__window.show()

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QListWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout

from pyqt_svg_icon_pushbutton.svgIconPushButton import SvgIconPushButton


class RecentFileWidget(QWidget):
    closeSignal = pyqtSignal(bool)
    openRecentFile = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi(parent)

    def __initUi(self, parent=None):
        if parent: self.setStyleSheet(parent.styleSheet())

        self.__saveWidget = QListWidget()
        self.__saveWidget.itemDoubleClicked.connect(self.__openRecentFile)
        self.__saveWidget.setStyleSheet('QListWidget { border: none; }')

        self.__closeBtn = SvgIconPushButton(self)
        self.__closeBtn.clicked.connect(self.close)
        self.__closeBtn.setToolTip('Close the file list')
        self.__closeBtn.setIcon('ico/close.svg')

        lbl = QLabel('Recent')
        lbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        lbl.setStyleSheet('QLabel { padding: 1px; }')

        lay = QHBoxLayout()
        lay.addWidget(lbl)
        lay.addWidget(self.__closeBtn)
        lay.setContentsMargins(1, 1, 1, 1)

        topWidget = QWidget()
        topWidget.setLayout(lay)
        topWidget.setObjectName('topWidget')

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(self.__saveWidget)
        lay.setContentsMargins(1, 1, 1, 1)
        lay.setSpacing(0)

        self.setLayout(lay)

        self.setStyleSheet('QWidget#topWidget { background-color: #222; padding: 5; border-bottom: 1px solid #555; }')

    def close(self):
        self.closeSignal.emit(False)
        return super().close()

    def __openRecentFile(self, item):
        pass


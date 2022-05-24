from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QListWidget, QHBoxLayout, QLabel, QVBoxLayout

from pyqt_svg_button import SvgButton
from pyqt_resource_helper.pyqtResourceHelper import PyQtResourceHelper


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
        self.__saveWidget.setObjectName('topWidgetListWidget')

        self.__closeBtn = SvgButton(self)
        self.__closeBtn.clicked.connect(self.close)
        self.__closeBtn.setToolTip('Close the file list')
        self.__closeBtn.setIcon('ico/close.svg')
        self.__closeBtn.setFixedSize(self.__closeBtn.sizeHint())

        lbl = QLabel('Recent')
        lbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        lbl.setObjectName('topWidgetLabel')

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

        PyQtResourceHelper.setStyleSheet([self], ['style/recent_file_widget.css'])

    def close(self):
        self.closeSignal.emit(False)
        return super().close()

    def __openRecentFile(self, item):
        pass


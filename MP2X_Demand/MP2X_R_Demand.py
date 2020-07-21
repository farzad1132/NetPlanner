from PySide2.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem, QFileDialog, QMdiSubWindow, QWidget, QLabel, QAbstractItemView, QListWidgetItem, QMenu, QFontComboBox,
                                QStyledItemDelegate, QGridLayout, QTabWidget, QGroupBox, QSpacerItem, QSizePolicy, QCheckBox, QRadioButton,
                                QPushButton, QComboBox, QHBoxLayout, QSplitter, QFrame, QListWidget, QFormLayout, QDialog, QLineEdit)

from PySide2.QtCore import (Signal, QObject, Slot, QRunnable, QThreadPool, SIGNAL, Qt, QSize, QUrl, QModelIndex, QRect, QCoreApplication,
                            QMetaObject)

from PySide2.QtGui import QPixmap, QBrush, QColor, QFont, QPalette, QStandardItemModel, QLinearGradient, QGradient, QCursor, QIcon

import sys
import os

from data import *
from MP2X_Demand import MP2X_R_SOURCE
from MP2X_Demand import Border_R


class MP2X_R_Demand(QWidget):

    def __init__(self, Panel_ID, nodename, Destination, DualPanelsId):
        super(MP2X_R_Demand, self).__init__()

        self.resize(118, 633)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)
        self.DualPanelsId = DualPanelsId

        grid=QGridLayout(self)
        widget=QWidget(self)
        widget.setStyleSheet("border-image:url(:/Border_R_SOURCE/Border_R.png); ")
        grid.setMargin(0)
        grid.addWidget(widget)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MP2X_R_D = QLabel(self)
        self.MP2X_R_D.setStyleSheet("QLabel{ image: url(:/MP2X_R_SOURCE/MP2X_R.png); }")
        self.MP2X_R_D.setText("")
        self.MP2X_R_D.setObjectName("MP2X_R_D")
        self.horizontalLayout.addWidget(self.MP2X_R_D)
        grid.addLayout(self.horizontalLayout,0,0)


if __name__ == "__main__":

    app = QApplication([])
    window = MP2X_R_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

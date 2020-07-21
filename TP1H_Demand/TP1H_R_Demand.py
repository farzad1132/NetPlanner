from PySide2.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem, QFileDialog, QMdiSubWindow, QWidget, QLabel, QAbstractItemView, QListWidgetItem, QMenu, QFontComboBox,
                                QStyledItemDelegate, QGridLayout, QTabWidget, QGroupBox, QSpacerItem, QSizePolicy, QCheckBox, QRadioButton,
                                QPushButton, QComboBox, QHBoxLayout, QSplitter, QFrame, QListWidget, QFormLayout, QDialog, QLineEdit)

from PySide2.QtCore import (Signal, QObject, Slot, QRunnable, QThreadPool, SIGNAL, Qt, QSize, QUrl, QModelIndex, QRect, QCoreApplication,
                            QMetaObject)

from PySide2.QtGui import QPixmap, QBrush, QColor, QFont, QPalette, QStandardItemModel, QLinearGradient, QGradient, QCursor, QIcon

import sys
import os

from data import *
from TP1H_Demand import Client
from TP1H_Demand import Line
from TP1H_Demand import Socket_bottom
from TP1H_Demand import Socket
from TP1H_Demand import TP1H_R
from TP1H_Demand import title
from TP1H_Demand import Border_R

class TP1H_R_Demand(QWidget):

    def __init__(self, Panel_ID, nodename, Destination, DualPanelsId):
        super(TP1H_R_Demand, self).__init__()

        self.resize(94, 511)

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
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TP1H_R = QLabel(self)
        self.TP1H_R.setMinimumSize(QSize(0, 113))
        self.TP1H_R.setMaximumSize(QSize(16777215, 16777215))
        self.TP1H_R.setStyleSheet("QLabel{ image: url(:/TP1H_R/TP1H_R.png); }")
        self.TP1H_R.setText("")
        self.TP1H_R.setObjectName("TP1H_R")
        self.gridLayout.addWidget(self.TP1H_R, 0, 0, 1, 1)
        grid.addLayout(self.gridLayout,0,0)

if __name__ == "__main__":
    
    app = QApplication([])
    window = TP1H_R_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

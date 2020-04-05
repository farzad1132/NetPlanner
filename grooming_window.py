from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SignalInstance, Slot, )
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtWidgets,QtCore, QtGui

from data import Data


class Grooming_Window(object):
    def setupUi(self, grooming_window):
        grooming_window.setObjectName("grooming_window")
        grooming_window.resize(603, 235)
        self.widget = QtWidgets.QWidget(grooming_window)
        self.widget.setGeometry(QtCore.QRect(20, 20, 185, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MP1HThreshold_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.MP1HThreshold_label.setFont(font)
        self.MP1HThreshold_label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.MP1HThreshold_label.setObjectName("MP1HThreshold_label")
        self.horizontalLayout_2.addWidget(self.MP1HThreshold_label)
        self.MP1H_Threshold_combobox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setBold(True)
        font.setWeight(75)
        self.MP1H_Threshold_combobox.setFont(font)
        self.MP1H_Threshold_combobox.setEditable(True)
        self.MP1H_Threshold_combobox.setObjectName("MP1H_Threshold_combobox")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.MP1H_Threshold_combobox.addItem("")
        self.horizontalLayout_2.addWidget(self.MP1H_Threshold_combobox)
        self.widget1 = QtWidgets.QWidget(grooming_window)
        self.widget1.setGeometry(QtCore.QRect(196, 191, 390, 35))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Start_Grooming_button = QtWidgets.QPushButton(self.widget1)
        self.Start_Grooming_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Start_Grooming_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: lightgreen;\n"
"    min-width: 80px;\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:open { /* when the button has its menu open */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: url(menu_indicator.png);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {\n"
"    position: relative;\n"
"    top: 2px; left: 2px; /* shift the arrow by 2 px */\n"
"}")
        self.Start_Grooming_button.setObjectName("Start_Grooming_button")
        self.gridLayout.addWidget(self.Start_Grooming_button, 0, 0, 1, 1)
        self.Cancel_button = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel_button.sizePolicy().hasHeightForWidth())
        self.Cancel_button.setSizePolicy(sizePolicy)
        self.Cancel_button.setMinimumSize(QtCore.QSize(186, 0))
        self.Cancel_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Cancel_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: lightgreen;\n"
"    min-width: 80px;\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:open { /* when the button has its menu open */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: url(menu_indicator.png);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {\n"
"    position: relative;\n"
"    top: 2px; left: 2px; /* shift the arrow by 2 px */\n"
"}")
        self.Cancel_button.setObjectName("Cancel_button")
        self.gridLayout.addWidget(self.Cancel_button, 0, 1, 1, 1)

        self.retranslateUi(grooming_window)
        self.MP1H_Threshold_combobox.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(grooming_window)

        # NOTE: added 
        self.Cancel_button.clicked.connect(grooming_window.close)
        self.Start_Grooming_button.clicked.connect(self.start_grooming_fun)

    def retranslateUi(self, grooming_window):
        _translate = QtCore.QCoreApplication.translate
        grooming_window.setWindowTitle(_translate("grooming_window", "Grooming Window"))
        self.MP1HThreshold_label.setText(_translate("grooming_window", "MP1H Threshold"))
        self.MP1H_Threshold_combobox.setCurrentText(_translate("grooming_window", "70"))
        self.MP1H_Threshold_combobox.setItemText(0, _translate("grooming_window", "10"))
        self.MP1H_Threshold_combobox.setItemText(1, _translate("grooming_window", "20"))
        self.MP1H_Threshold_combobox.setItemText(2, _translate("grooming_window", "30"))
        self.MP1H_Threshold_combobox.setItemText(3, _translate("grooming_window", "40"))
        self.MP1H_Threshold_combobox.setItemText(4, _translate("grooming_window", "50"))
        self.MP1H_Threshold_combobox.setItemText(5, _translate("grooming_window", "60"))
        self.MP1H_Threshold_combobox.setItemText(6, _translate("grooming_window", "70"))
        self.MP1H_Threshold_combobox.setItemText(7, _translate("grooming_window", "80"))
        self.MP1H_Threshold_combobox.setItemText(8, _translate("grooming_window", "90"))
        self.MP1H_Threshold_combobox.setItemText(9, _translate("grooming_window", "100"))
        self.Start_Grooming_button.setText(_translate("grooming_window", "Start Grooming Algorithm"))
        self.Cancel_button.setText(_translate("grooming_window", "Cancel"))

    def start_grooming_fun(self):
        MP1H_Threshold = str(self.MP1H_Threshold_combobox.currentText())
        
        Data["ui"].grooming_procedure(MP1H_Threshold)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    grooming_window = QtWidgets.QWidget()
    ui = Grooming_Window()
    ui.setupUi(grooming_window)
    grooming_window.show()
    sys.exit(app.exec_())

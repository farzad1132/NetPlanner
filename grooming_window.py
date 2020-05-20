from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SignalInstance, Slot, )
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtWidgets,QtCore, QtGui

from data import Data

from Ui_files.new_ui import iconresources
bus = {}


class Ui_grooming_window(object):
    def setupUi(self, grooming_window):
        
        # NOTE: added
        bus["grooming_window"] = grooming_window
        grooming_window.setObjectName("grooming_window")
        grooming_window.resize(603, 235)
        self.layoutWidget = QtWidgets.QWidget(grooming_window)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 251, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MP1HThreshold_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.MP1HThreshold_label.setFont(font)
        self.MP1HThreshold_label.setStyleSheet("   QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.MP1HThreshold_label.setObjectName("MP1HThreshold_label")
        self.horizontalLayout_2.addWidget(self.MP1HThreshold_label)
        self.MP1H_Threshold_combobox = QtWidgets.QComboBox(self.layoutWidget)
        self.MP1H_Threshold_combobox.setMinimumSize(QtCore.QSize(121, 0))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setBold(True)
        font.setWeight(75)
        self.MP1H_Threshold_combobox.setFont(font)
        self.MP1H_Threshold_combobox.setStyleSheet("QComboBox {\n"
"    \n"
"    border-radius: 0px;\n"
"    padding: 1px 18px 1px 5px;\n"
"    min-width: 6em; \n"
"    \n"
"    border:1px solid rgb(0, 139, 208);\n"
"    \n"
"   \n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    \n"
"    \n"
"    border-left-width: 2px;\n"
"    border-left-color: darkblue;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 0px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"   \n"
"    image: url(:/newPrefix/dropdown.png); \n"
"    \n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    \n"
"    \n"
"    image: url(:/newPrefix/dropup.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border-color:2px solid blue;\n"
"   \n"
"}")
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
        self.MP1H_Threshold_combobox.addItem("")
        self.horizontalLayout_2.addWidget(self.MP1H_Threshold_combobox)
        self.layoutWidget1 = QtWidgets.QWidget(grooming_window)
        self.layoutWidget1.setGeometry(QtCore.QRect(195, 185, 391, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Start_Grooming_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.Start_Grooming_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Start_Grooming_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"     \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.Start_Grooming_button.setObjectName("Start_Grooming_button")
        self.gridLayout.addWidget(self.Start_Grooming_button, 0, 0, 1, 1)
        self.Cancel_button = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel_button.sizePolicy().hasHeightForWidth())
        self.Cancel_button.setSizePolicy(sizePolicy)
        self.Cancel_button.setMinimumSize(QtCore.QSize(84, 0))
        self.Cancel_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Cancel_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"     \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c0c0c0; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.Cancel_button.setObjectName("Cancel_button")
        self.gridLayout.addWidget(self.Cancel_button, 0, 1, 1, 1)

        self.retranslateUi(grooming_window)
        self.MP1H_Threshold_combobox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(grooming_window)

        # NOTE: added 
        self.Cancel_button.clicked.connect(grooming_window.close)
        self.Start_Grooming_button.clicked.connect(self.start_grooming_fun)

    def retranslateUi(self, grooming_window):
        _translate = QtCore.QCoreApplication.translate
        grooming_window.setWindowTitle(_translate("grooming_window", "Grooming Window"))
        self.MP1HThreshold_label.setText(_translate("grooming_window", "MP1H Threshold"))
        self.MP1H_Threshold_combobox.setCurrentText(_translate("grooming_window", "0"))
        self.MP1H_Threshold_combobox.setItemText(0, _translate("grooming_window", "0"))
        self.MP1H_Threshold_combobox.setItemText(1, _translate("grooming_window", "10"))
        self.MP1H_Threshold_combobox.setItemText(2, _translate("grooming_window", "20"))
        self.MP1H_Threshold_combobox.setItemText(3, _translate("grooming_window", "30"))
        self.MP1H_Threshold_combobox.setItemText(4, _translate("grooming_window", "40"))
        self.MP1H_Threshold_combobox.setItemText(5, _translate("grooming_window", "50"))
        self.MP1H_Threshold_combobox.setItemText(6, _translate("grooming_window", "60"))
        self.MP1H_Threshold_combobox.setItemText(7, _translate("grooming_window", "70"))
        self.MP1H_Threshold_combobox.setItemText(8, _translate("grooming_window", "80"))
        self.MP1H_Threshold_combobox.setItemText(9, _translate("grooming_window", "90"))
        self.MP1H_Threshold_combobox.setItemText(10, _translate("grooming_window", "100"))
        self.Start_Grooming_button.setText(_translate("grooming_window", "Start Grooming Algorithm"))
        self.Cancel_button.setText(_translate("grooming_window", "Cancel"))

    def start_grooming_fun(self):
            MP1H_Threshold = str(self.MP1H_Threshold_combobox.currentText())
            
            Data["ui"].grooming_procedure(MP1H_Threshold)
            bus["grooming_window"].close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    grooming_window = QtWidgets.QWidget()
    ui = Ui_grooming_window()
    ui.setupUi(grooming_window)
    grooming_window.show()
    sys.exit(app.exec_())

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from data import Data



class MP2D_panel_R(QWidget):

    def __init__(self,Panel_ID,nodename):

        self.nodename = nodename
        self.id = Panel_ID


        super(MP2D_panel_R, self).__init__()

        self.setFixedSize(109, 810)

        self.label_button1 = QLabel(self)
        self.label_button1.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button1.setFixedSize(15, 12)
        self.label_button1.move(70, 30)

        self.label_ACT = QLabel(self)
        self.label_ACT.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        self.label_ACT.setFixedSize(19, 8)
        self.label_ACT.move(44, 30)

        self.label_button2 = QLabel(self)
        self.label_button2.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button2.setFixedSize(15, 12)
        self.label_button2.move(70, 46)

        self.label_FAIL = QLabel(self)
        self.label_FAIL.setPixmap(QPixmap(os.path.join("MP2D_panel", "FAIL.png")))
        self.label_FAIL.setFixedSize(20, 8)
        self.label_FAIL.move(44, 46)

        self.label_button3 = QLabel(self)
        self.label_button3.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button3.setFixedSize(15, 12)
        self.label_button3.move(70, 62)

        self.label_WP = QLabel(self)
        self.label_WP.setPixmap(QPixmap(os.path.join("MP2D_panel", "wp.png")))
        self.label_WP.setFixedSize(23, 10)
        self.label_WP.move(44, 62)

        self.label_ACT1 = QLabel(self)
        self.label_ACT1.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        self.label_ACT1.setFixedSize(19, 8)
        self.label_ACT1.move(55, 332)

        self.label_button4 = QLabel(self)
        self.label_button4.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button4.setFixedSize(15, 12)
        self.label_button4.move(40, 331)

        self.label_SF1 = QLabel(self)
        self.label_SF1.setPixmap(QPixmap(os.path.join("MP2D_panel", "SF.png")))
        self.label_SF1.setFixedSize(11, 8)
        self.label_SF1.move(55, 348)

        self.label_button5 = QLabel(self)
        self.label_button5.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button5.setFixedSize(15, 12)
        self.label_button5.move(40, 346)

        self.label_ACT2 = QLabel(self)
        self.label_ACT2.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        self.label_ACT2.setFixedSize(19, 8)
        self.label_ACT2.move(55, 397)

        self.label_button6 = QLabel(self)
        self.label_button6.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button6.setFixedSize(15, 12)
        self.label_button6.move(40, 396)

        self.label_SF2 = QLabel(self)
        self.label_SF2.setPixmap(QPixmap(os.path.join("MP2D_panel", "SF.png")))
        self.label_SF2.setFixedSize(11, 8)
        self.label_SF2.move(55, 413)

        self.label_button7 = QLabel(self)
        self.label_button7.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button7.setFixedSize(15, 12)
        self.label_button7.move(40, 411)

        self.label_ACT3 = QLabel(self)
        self.label_ACT3.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        self.label_ACT3.setFixedSize(19, 8)
        self.label_ACT3.move(55, 529)

        self.label_button8 = QLabel(self)
        self.label_button8.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button8.setFixedSize(15, 12)
        self.label_button8.move(40, 528)

        self.label_SF3 = QLabel(self)
        self.label_SF3.setPixmap(QPixmap(os.path.join("MP2D_panel", "SF.png")))
        self.label_SF3.setFixedSize(11, 8)
        self.label_SF3.move(55, 545)

        self.label_button9 = QLabel(self)
        self.label_button9.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        self.label_button9.setFixedSize(15, 12)
        self.label_button9.move(40, 543)

        self.label_CH = QLabel(self)
        self.label_CH.setPixmap(QPixmap(os.path.join("MP2D_panel", "CH.png")))
        self.label_CH.setFixedSize(47, 31)
        self.label_CH.move(35, 470)

        self.label_CH_title = QLabel(self)
        self.label_CH_title.setPixmap(QPixmap(os.path.join("MP2D_panel", "CH_title.png")))
        self.label_CH_title.setFixedSize(12, 7)
        self.label_CH_title.move(35, 460)

        self.lcdd()
        self.setAcceptDrops(True)

    def lcdd(self):

        self.useless_label1 = QLabel(self)
        self.useless_label2 = QLabel(self)
        self.useless_label3 = QLabel(self)
        self.useless_label4 = QLabel(self)
        self.useless_label5 = QLabel(self)
        self.useless_label6 = QLabel(self)

        self.lcd = QLCDNumber(3)
        self.lcd.setFixedSize(60, 50)
        self.lcd.display(100)
        self.lcd.setStyleSheet("QLCDNumber { background-color: DarkOliveGreen }")
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        self.xlay = QVBoxLayout()
        self.xlay.addWidget(self.useless_label1)
        self.xlay.addWidget(self.useless_label3)
        self.xlay.addWidget(self.useless_label4)
        self.xlay.addWidget(self.useless_label6)
        self.xlay.addWidget(self.lcd)
        self.xlay.addWidget(self.useless_label5)
        self.xlay.addWidget(self.useless_label2)
        self.xlay.setSpacing(170)
        self.setLayout(self.xlay)



from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from data import Data

class TP2X_panel(QWidget):

    def __init__(self,Panel_ID,nodename):

        super(TP2X_panel, self).__init__()
        self.id = Panel_ID
        self.nodename = nodename
        self.setFixedSize(109, 810)

        self.label_1 = QLabel(self)
        self.label_1.setPixmap(QPixmap(os.path.join("TP2X_panel", "1.png")))
        self.label_1.setFixedSize(37, 62)
        self.label_1.move(3, 3)

        self.label_2 = QLabel(self)
        self.label_2.setPixmap(QPixmap(os.path.join("TP2X_panel", "2.png")))
        self.label_2.setFixedSize(37, 62)
        self.label_2.move(3, 745)

        self.label_title = QLabel(self)
        self.label_title.setPixmap(QPixmap(os.path.join("TP2X_panel", "title.png")))
        self.label_title.setFixedSize(14, 90)
        self.label_title.move(92, 3)

        self.label_button1 = QLabel(self)
        self.label_button1.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button1.setFixedSize(12, 12)
        self.label_button1.move(41, 96)

        self.label_ACT = QLabel(self)
        self.label_ACT.setPixmap(QPixmap(os.path.join("TP2X_panel", "ACT.png")))
        self.label_ACT.setFixedSize(19, 7)
        self.label_ACT.move(57, 99)

        self.label_button2 = QLabel(self)
        self.label_button2.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button2.setFixedSize(12, 12)
        self.label_button2.move(41, 112)

        self.label_FAIL = QLabel(self)
        self.label_FAIL.setPixmap(QPixmap(os.path.join("TP2X_panel", "FAIL.png")))
        self.label_FAIL.setFixedSize(19, 8)
        self.label_FAIL.move(57, 114)

        self.label_button3 = QLabel(self)
        self.label_button3.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button3.setFixedSize(12, 12)
        self.label_button3.move(41, 128)

        self.label_N1 = QLabel(self)
        self.label_N1.setPixmap(QPixmap(os.path.join("TP2X_panel", "N1.png")))
        self.label_N1.setFixedSize(4, 8)
        self.label_N1.move(45, 143)

        self.label_WP = QLabel(self)
        self.label_WP.setPixmap(QPixmap(os.path.join("TP2X_panel", "wp.png")))
        self.label_WP.setFixedSize(21, 10)
        self.label_WP.move(57, 130)

        self.label_button32 = QLabel(self)
        self.label_button32.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button32.setFixedSize(12, 12)
        self.label_button32.move(81, 128)

        self.label_button32 = QLabel(self)
        self.label_button32.setPixmap(QPixmap(os.path.join("TP2X_panel", "N2.png")))
        self.label_button32.setFixedSize(5, 8)
        self.label_button32.move(85, 143)

        self.label_CNS = QLabel(self)
        self.label_CNS.setPixmap(QPixmap(os.path.join("TP2X_panel", "CNS.png")))
        self.label_CNS.setFixedSize(16, 28)
        self.label_CNS.move(16, 106)

        self.label_CNS_title = QLabel(self)
        self.label_CNS_title.setPixmap(QPixmap(os.path.join("TP2X_panel", "CNS_title.png")))
        self.label_CNS_title.setFixedSize(19, 8)
        self.label_CNS_title.move(14, 96)

        self.label_CH1 = QLabel(self)
        self.label_CH1.setPixmap(QPixmap(os.path.join("TP2X_panel", "CH.png")))
        self.label_CH1.setFixedSize(47, 31)
        self.label_CH1.move(6, 173)

        self.label_CH1_title = QLabel(self)
        self.label_CH1_title.setPixmap(QPixmap(os.path.join("TP2X_panel", "CH1.png")))
        self.label_CH1_title.setFixedSize(19, 7)
        self.label_CH1_title.move(6, 163)

        self.label_button41 = QLabel(self)
        self.label_button41.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button41.setFixedSize(12, 12)
        self.label_button41.move(61, 171)

        self.label_button42 = QLabel(self)
        self.label_button42.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button42.setFixedSize(12, 12)
        self.label_button42.move(84, 171)

        self.label_LSF1 = QLabel(self)
        self.label_LSF1.setPixmap(QPixmap(os.path.join("TP2X_panel", "LSF.png")))
        self.label_LSF1.setFixedSize(11, 8)
        self.label_LSF1.move(61, 185)

        self.label_CSF1 = QLabel(self)
        self.label_CSF1.setPixmap(QPixmap(os.path.join("TP2X_panel", "CSF.png")))
        self.label_CSF1.setFixedSize(12, 6)
        self.label_CSF1.move(84, 186)

        self.label_button51 = QLabel(self)
        self.label_button51.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button51.setFixedSize(12, 12)
        self.label_button51.move(61, 195)

        self.label_button52 = QLabel(self)
        self.label_button52.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button52.setFixedSize(12, 12)
        self.label_button52.move(84, 195)

        self.label_SDH1 = QLabel(self)
        self.label_SDH1.setPixmap(QPixmap(os.path.join("TP2X_panel", "SDH.png")))
        self.label_SDH1.setFixedSize(14, 6)
        self.label_SDH1.move(61, 211)

        self.label_GbE1 = QLabel(self)
        self.label_GbE1.setPixmap(QPixmap(os.path.join("TP2X_panel", "GbE.png")))
        self.label_GbE1.setFixedSize(13, 6)
        self.label_GbE1.move(84, 211)

        self.label_line1 = QLabel(self)
        self.label_line1.setPixmap(QPixmap(os.path.join("TP2X_panel", "line.png")))
        self.label_line1.setFixedSize(47, 79)
        self.label_line1.move(16, 234)

        self.label_client1 = QLabel(self)
        self.label_client1.setPixmap(QPixmap(os.path.join("TP2X_panel", "client.png")))
        self.label_client1.setFixedSize(47, 79)
        self.label_client1.move(16, 323)

        self.label_T_line1 = QLabel(self)
        self.label_T_line1.setPixmap(QPixmap(os.path.join("TP2X_panel", "T.png")))
        self.label_T_line1.setFixedSize(5, 7)
        self.label_T_line1.move(6, 249)

        self.label_R_line1 = QLabel(self)
        self.label_R_line1.setPixmap(QPixmap(os.path.join("TP2X_panel", "R.png")))
        self.label_R_line1.setFixedSize(5, 7)
        self.label_R_line1.move(6, 293)

        self.label_T_client1 = QLabel(self)
        self.label_T_client1.setPixmap(QPixmap(os.path.join("TP2X_panel", "T.png")))
        self.label_T_client1.setFixedSize(5, 7)
        self.label_T_client1.move(6, 338)

        self.label_R_client1 = QLabel(self)
        self.label_R_client1.setPixmap(QPixmap(os.path.join("TP2X_panel", "R.png")))
        self.label_R_client1.setFixedSize(5, 7)
        self.label_R_client1.move(6, 382)

        self.label_CH2 = QLabel(self)
        self.label_CH2.setPixmap(QPixmap(os.path.join("TP2X_panel", "CH.png")))
        self.label_CH2.setFixedSize(47, 31)
        self.label_CH2.move(6, 442)

        self.label_CH2_title = QLabel(self)
        self.label_CH2_title.setPixmap(QPixmap(os.path.join("TP2X_panel", "CH2.png")))
        self.label_CH2_title.setFixedSize(18, 7)
        self.label_CH2_title.move(6, 430)

        self.label_button61 = QLabel(self)
        self.label_button61.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button61.setFixedSize(12, 12)
        self.label_button61.move(61, 439)

        self.label_button62 = QLabel(self)
        self.label_button62.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button62.setFixedSize(12, 12)
        self.label_button62.move(84, 439)

        self.label_LSF2 = QLabel(self)
        self.label_LSF2.setPixmap(QPixmap(os.path.join("TP2X_panel", "LSF.png")))
        self.label_LSF2.setFixedSize(11, 8)
        self.label_LSF2.move(61, 453)

        self.label_CSF2 = QLabel(self)
        self.label_CSF2.setPixmap(QPixmap(os.path.join("TP2X_panel", "CSF.png")))
        self.label_CSF2.setFixedSize(12, 6)
        self.label_CSF2.move(84, 454)

        self.label_button51 = QLabel(self)
        self.label_button51.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button51.setFixedSize(12, 12)
        self.label_button51.move(61, 464)

        self.label_button52 = QLabel(self)
        self.label_button52.setPixmap(QPixmap(os.path.join("TP2X_panel", "button.png")))
        self.label_button52.setFixedSize(12, 12)
        self.label_button52.move(84, 464)

        self.label_SDH1 = QLabel(self)
        self.label_SDH1.setPixmap(QPixmap(os.path.join("TP2X_panel", "SDH.png")))
        self.label_SDH1.setFixedSize(14, 6)
        self.label_SDH1.move(61, 480)

        self.label_GbE1 = QLabel(self)
        self.label_GbE1.setPixmap(QPixmap(os.path.join("TP2X_panel", "GbE.png")))
        self.label_GbE1.setFixedSize(13, 6)
        self.label_GbE1.move(84, 480)

        self.label_line2 = QLabel(self)
        self.label_line2.setPixmap(QPixmap(os.path.join("TP2X_panel", "line.png")))
        self.label_line2.setFixedSize(47, 79)
        self.label_line2.move(16, 508)

        self.label_client2 = QLabel(self)
        self.label_client2.setPixmap(QPixmap(os.path.join("TP2X_panel", "client.png")))
        self.label_client2.setFixedSize(47, 79)
        self.label_client2.move(16, 597)

        self.label_T_line2 = QLabel(self)
        self.label_T_line2.setPixmap(QPixmap(os.path.join("TP2X_panel", "T.png")))
        self.label_T_line2.setFixedSize(5, 7)
        self.label_T_line2.move(6, 523)

        self.label_R_line2 = QLabel(self)
        self.label_R_line2.setPixmap(QPixmap(os.path.join("TP2X_panel", "R.png")))
        self.label_R_line2.setFixedSize(5, 7)
        self.label_R_line2.move(6, 567)

        self.label_T_client2 = QLabel(self)
        self.label_T_client2.setPixmap(QPixmap(os.path.join("TP2X_panel", "T.png")))
        self.label_T_client2.setFixedSize(5, 7)
        self.label_T_client2.move(6, 612)

        self.label_R_client2 = QLabel(self)
        self.label_R_client2.setPixmap(QPixmap(os.path.join("TP2X_panel", "R.png")))
        self.label_R_client2.setFixedSize(5, 7)
        self.label_R_client2.move(6, 656)




        self.setAcceptDrops(True)

    def contextMenuEvent(self, event):
        from BLANK_panel.BLANK_panel import BLANK_panel
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            Panel_Data[self.id].setWidget(BLANK_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"].pop(str(self.id))




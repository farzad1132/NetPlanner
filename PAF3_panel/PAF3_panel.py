from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from data import Data


class PAF3_panel(QWidget):

    def __init__(self,Panel_ID,nodename):

        super(PAF3_panel, self).__init__()
        self.id = str(Panel_ID)
        self.nodename = nodename
        self.setMinimumSize(109, 810)
        self.label_PAF3_1 = QLabel(self)
        self.label_PAF3_1.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_1.png")))
        self.label_PAF3_1.setFixedSize(37, 61)
        self.label_PAF3_1.move(3, 3)

        self.label_PAF3_2 = QLabel(self)
        self.label_PAF3_2.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_2.png")))
        self.label_PAF3_2.setFixedSize(37, 60)
        self.label_PAF3_2.move(3, 747)

        self.label_PAF3_title = QLabel(self)
        self.label_PAF3_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_title.png")))
        self.label_PAF3_title.setFixedSize(17, 97)
        self.label_PAF3_title.move(82, 3)

        self.label_PAF3_ACT = QLabel(self)
        self.label_PAF3_ACT.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_ACT.png")))
        self.label_PAF3_ACT.setFixedSize(20, 19)
        self.label_PAF3_ACT.move(60, 127)

        self.label_PAF3_FAIL = QLabel(self)
        self.label_PAF3_FAIL.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_FAIL.png")))
        self.label_PAF3_FAIL.setFixedSize(20, 8)
        self.label_PAF3_FAIL.move(60, 150)

        self.label_PAF3_SF = QLabel(self)
        self.label_PAF3_SF.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_SF.png")))
        self.label_PAF3_SF.setFixedSize(10, 9)
        self.label_PAF3_SF.move(60, 166)

        self.label_PAF3_CNS = QLabel(self)
        self.label_PAF3_CNS.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_CNS.png")))
        self.label_PAF3_CNS.setFixedSize(16, 28)
        self.label_PAF3_CNS.move(20, 140)

        self.label_PAF3_CNS_title = QLabel(self)
        self.label_PAF3_CNS_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_CNS_title.png")))
        self.label_PAF3_CNS_title.setFixedSize(19, 8)
        self.label_PAF3_CNS_title.move(18, 131)

        self.label_PAF3_button1 = QLabel(self)
        self.label_PAF3_button1.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_button.png")))
        self.label_PAF3_button1.setFixedSize(12, 12)
        self.label_PAF3_button1.move(45, 131)

        self.label_PAF3_button2 = QLabel(self)
        self.label_PAF3_button2.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_button.png")))
        self.label_PAF3_button2.setFixedSize(12, 12)
        self.label_PAF3_button2.move(45, 147)

        self.label_PAF3_button3 = QLabel(self)
        self.label_PAF3_button3.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_button.png")))
        self.label_PAF3_button3.setFixedSize(12, 12)
        self.label_PAF3_button3.move(45, 164)

        self.label_LAF3_S_IN_title = QLabel(self)
        self.label_LAF3_S_IN_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_S_IN_title.png")))
        self.label_LAF3_S_IN_title.setFixedSize(19, 8)
        self.label_LAF3_S_IN_title.move(24, 331)

        self.label_PAF3_S_IN1 = QLabel(self)
        self.label_PAF3_S_IN1.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_S_IN.png")))
        self.label_PAF3_S_IN1.setFixedSize(35, 24)
        self.label_PAF3_S_IN1.move(18, 341)

        self.label_PAF3_S_IN2 = QLabel(self)
        self.label_PAF3_S_IN2.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_S_IN.png")))
        self.label_PAF3_S_IN2.setFixedSize(35, 24)
        self.label_PAF3_S_IN2.move(18, 365)

        self.label_PAF3_OSC_OUT_title = QLabel(self)
        self.label_PAF3_OSC_OUT_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_OSC_OUT_title.png")))
        self.label_PAF3_OSC_OUT_title.setFixedSize(48, 10)
        self.label_PAF3_OSC_OUT_title.move(12, 392)

        self.label_PAF3_DCM_OUT_title = QLabel(self)
        self.label_PAF3_DCM_OUT_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_DCM_OUT_title.png")))
        self.label_PAF3_DCM_OUT_title.setFixedSize(48, 8)
        self.label_PAF3_DCM_OUT_title.move(12, 432)

        self.label_LAF3_DCM_OUT = QLabel(self)
        self.label_LAF3_DCM_OUT.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_S_IN.png")))
        self.label_LAF3_DCM_OUT.setFixedSize(35, 24)
        self.label_LAF3_DCM_OUT.move(18, 443)

        self.label_LAF3_DCM_IN = QLabel(self)
        self.label_LAF3_DCM_IN.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_S_IN.png")))
        self.label_LAF3_DCM_IN.setFixedSize(35, 24)
        self.label_LAF3_DCM_IN.move(18, 467)

        self.label_LAF3_DCM_IN_title = QLabel(self)
        self.label_LAF3_DCM_IN_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_DCM_IN_title.png")))
        self.label_LAF3_DCM_IN_title.setFixedSize(37, 8)
        self.label_LAF3_DCM_IN_title.move(17, 495)

        self.label_LAF3_T = QLabel(self)
        self.label_LAF3_T.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_T.png")))
        self.label_LAF3_T.setFixedSize(5, 7)
        self.label_LAF3_T.move(10, 452)

        self.label_LAF3_R = QLabel(self)
        self.label_LAF3_R.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_R.png")))
        self.label_LAF3_R.setFixedSize(5, 7)
        self.label_LAF3_R.move(10, 475)

        self.label_PAF3_MON_title = QLabel(self)
        self.label_PAF3_MON_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_MON_title.png")))
        self.label_PAF3_MON_title.setFixedSize(25, 8)
        self.label_PAF3_MON_title.move(22, 543)

        self.label_PAF3_MON = QLabel(self)
        self.label_PAF3_MON.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_MON.png")))
        self.label_PAF3_MON.setFixedSize(35, 24)
        self.label_PAF3_MON.move(18, 554)

        self.label_PAF3_S_OUT = QLabel(self)
        self.label_PAF3_S_OUT.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_S_OUT.png")))
        self.label_PAF3_S_OUT.setFixedSize(35, 24)
        self.label_PAF3_S_OUT.move(18, 578)

        self.label_PAF3_S_OUT_title = QLabel(self)
        self.label_PAF3_S_OUT_title.setPixmap(QPixmap(os.path.join("PAF3_panel", "PAF3_S_OUT_title.png")))
        self.label_PAF3_S_OUT_title.setFixedSize(30, 8)
        self.label_PAF3_S_OUT_title.move(22, 605)

        self.setAcceptDrops(True)


    def contextMenuEvent(self, event):
        from BLANK_panel.BLANK_panel import BLANK_panel
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            Panel_Data[self.id].setWidget(BLANK_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"].pop(str(self.id))


if __name__ == "__main__":

    app = QApplication([])
    window = PAF3_panel()
    window.show()
    sys.exit(app.exec_())





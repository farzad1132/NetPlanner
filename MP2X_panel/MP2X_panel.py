from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from data import Data

class MP2X_panel(QWidget):

    def __init__(self,Panel_ID,nodename):

        super(MP2X_panel, self).__init__()
        self.id = Panel_ID
        self.nodename = nodename
        # self.setMaximumSize(109, 810)
        # self.setGeometry(100, 100, 109, 810)
        self.setFixedSize(109, 810)

        self.label_1 = QLabel(self)
        self.label_1.setPixmap(QPixmap(os.path.join("MP2X_panel", "1.png")))
        self.label_1.setFixedSize(37, 62)
        self.label_1.move(3, 3)

        self.label_2 = QLabel(self)
        self.label_2.setPixmap(QPixmap(os.path.join("MP2X_panel", "2.png")))
        self.label_2.setFixedSize(37, 62)
        self.label_2.move(3, 745)

        self.label_title = QLabel(self)
        self.label_title.setPixmap(QPixmap(os.path.join("MP2X_panel", "title.png")))
        self.label_title.setFixedSize(20, 91)
        self.label_title.move(45, 3)

        self.label_line_socket_R = QLabel(self)
        self.label_line_socket_R.setPixmap(QPixmap(os.path.join("MP2X_panel", "line_socket_R.png")))
        self.label_line_socket_R.setFixedSize(15, 25)
        self.label_line_socket_R.move(36, 277)

        self.label_line_socket_L = QLabel(self)
        self.label_line_socket_L.setPixmap(QPixmap(os.path.join("MP2X_panel", "line_socket_L.png")))
        self.label_line_socket_L.setFixedSize(15, 25)
        self.label_line_socket_L.move(17, 277)

        self.label_client_socket_2 = QLabel(self)
        self.label_client_socket_2.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_2.setFixedSize(15, 25)
        self.label_client_socket_2.move(36, 313)

        self.label_client_socket_4 = QLabel(self)
        self.label_client_socket_4.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_4.setFixedSize(15, 25)
        self.label_client_socket_4.move(36, 349)

        self.label_client_socket_6 = QLabel(self)
        self.label_client_socket_6.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_6.setFixedSize(15, 25)
        self.label_client_socket_6.move(36, 385)

        self.label_client_socket_8 = QLabel(self)
        self.label_client_socket_8.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_8.setFixedSize(15, 25)
        self.label_client_socket_8.move(36, 421)

        self.label_client_socket_10 = QLabel(self)
        self.label_client_socket_10.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_10.setFixedSize(15, 25)
        self.label_client_socket_10.move(36, 457)

        self.label_client_socket_12 = QLabel(self)
        self.label_client_socket_12.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_12.setFixedSize(15, 25)
        self.label_client_socket_12.move(36, 493)

        self.label_client_socket_14 = QLabel(self)
        self.label_client_socket_14.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_14.setFixedSize(15, 25)
        self.label_client_socket_14.move(36, 529)

        self.label_client_socket_16 = QLabel(self)
        self.label_client_socket_16.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_R.png")))
        self.label_client_socket_16.setFixedSize(15, 25)
        self.label_client_socket_16.move(36, 565)

        self.label_client_socket_1 = QLabel(self)
        self.label_client_socket_1.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_1.setFixedSize(15, 25)
        self.label_client_socket_1.move(17, 313)

        self.label_client_socket_3 = QLabel(self)
        self.label_client_socket_3.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_3.setFixedSize(15, 25)
        self.label_client_socket_3.move(17, 349)

        self.label_client_socket_5 = QLabel(self)
        self.label_client_socket_5.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_5.setFixedSize(15, 25)
        self.label_client_socket_5.move(17, 385)

        self.label_client_socket_7 = QLabel(self)
        self.label_client_socket_7.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_7.setFixedSize(15, 25)
        self.label_client_socket_7.move(17, 421)

        self.label_client_socket_9 = QLabel(self)
        self.label_client_socket_9.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_9.setFixedSize(15, 25)
        self.label_client_socket_9.move(17, 457)

        self.label_client_socket_11 = QLabel(self)
        self.label_client_socket_11.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_11.setFixedSize(15, 25)
        self.label_client_socket_11.move(17, 493)

        self.label_client_socket_13 = QLabel(self)
        self.label_client_socket_13.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_13.setFixedSize(15, 25)
        self.label_client_socket_13.move(17, 529)

        self.label_client_socket_15 = QLabel(self)
        self.label_client_socket_15.setPixmap(QPixmap(os.path.join("MP2X_panel", "client_socket_L.png")))
        self.label_client_socket_15.setFixedSize(15, 25)
        self.label_client_socket_15.move(17, 565)

        self.label_ACT = QLabel(self)
        self.label_ACT.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT.setFixedSize(15, 7)
        self.label_ACT.move(84, 38)

        self.label_button_ACT = QLabel(self)
        self.label_button_ACT.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_ACT.setFixedSize(5, 5)
        self.label_button_ACT.move(77, 38)

        self.label_button_FAIL = QLabel(self)
        self.label_button_FAIL.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_FAIL.setFixedSize(5, 5)
        self.label_button_FAIL.move(77, 55)

        self.label_FAIL = QLabel(self)
        self.label_FAIL.setPixmap(QPixmap(os.path.join("MP2X_panel", "FAIL.png")))
        self.label_FAIL.setFixedSize(15, 6)
        self.label_FAIL.move(84, 55)

        self.label_button_AL1 = QLabel(self)
        self.label_button_AL1.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_AL1.setFixedSize(5, 5)
        self.label_button_AL1.move(74, 277)

        self.label_button_AL2 = QLabel(self)
        self.label_button_AL2.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_AL2.setFixedSize(5, 5)
        self.label_button_AL2.move(87, 277)

        self.label_ACT_L = QLabel(self)
        self.label_ACT_L.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_L.setFixedSize(15, 7)
        self.label_ACT_L.move(94, 275)

        self.label_L1_b = QLabel(self)
        self.label_L1_b.setPixmap(QPixmap(os.path.join("MP2X_panel", "L1.png")))
        self.label_L1_b.setFixedSize(10, 8)
        self.label_L1_b.move(72, 286)

        self.label_L2_b = QLabel(self)
        self.label_L2_b.setPixmap(QPixmap(os.path.join("MP2X_panel", "L2.png")))
        self.label_L2_b.setFixedSize(10, 8)
        self.label_L2_b.move(87, 286)

        self.label_button_SL1 = QLabel(self)
        self.label_button_SL1.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_SL1.setFixedSize(5, 5)
        self.label_button_SL1.move(74, 298)

        self.label_button_SL2 = QLabel(self)
        self.label_button_SL2.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_SL2.setFixedSize(5, 5)
        self.label_button_SL2.move(87, 298)

        self.label_SF_L = QLabel(self)
        self.label_SF_L.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_L.setFixedSize(8, 7)
        self.label_SF_L.move(96, 296)

        ##############################

        self.label_button_A1 = QLabel(self)
        self.label_button_A1.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A1.setFixedSize(5, 5)
        self.label_button_A1.move(74, 313)

        self.label_button_A2 = QLabel(self)
        self.label_button_A2.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A2.setFixedSize(5, 5)
        self.label_button_A2.move(87, 313)

        self.label_ACT_12 = QLabel(self)
        self.label_ACT_12.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_12.setFixedSize(15, 7)
        self.label_ACT_12.move(94, 311)

        self.label_N1 = QLabel(self)
        self.label_N1.setPixmap(QPixmap(os.path.join("MP2X_panel", "N1.png")))
        self.label_N1.setFixedSize(4, 8)
        self.label_N1.move(74, 322)

        self.label_N2 = QLabel(self)
        self.label_N2.setPixmap(QPixmap(os.path.join("MP2X_panel", "N2.png")))
        self.label_N2.setFixedSize(5, 8)
        self.label_N2.move(87, 322)

        self.label_button_S1 = QLabel(self)
        self.label_button_S1.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S1.setFixedSize(5, 5)
        self.label_button_S1.move(74, 334)

        self.label_button_S2 = QLabel(self)
        self.label_button_S2.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S2.setFixedSize(5, 5)
        self.label_button_S2.move(87, 334)

        self.label_SF_12 = QLabel(self)
        self.label_SF_12.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_12.setFixedSize(8, 7)
        self.label_SF_12.move(96, 332)

        ##########################################

        self.label_button_A3 = QLabel(self)
        self.label_button_A3.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A3.setFixedSize(5, 5)
        self.label_button_A3.move(74, 349)

        self.label_button_A4 = QLabel(self)
        self.label_button_A4.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A4.setFixedSize(5, 5)
        self.label_button_A4.move(87, 349)

        self.label_ACT_34 = QLabel(self)
        self.label_ACT_34.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_34.setFixedSize(15, 7)
        self.label_ACT_34.move(94, 347)

        self.label_N3 = QLabel(self)
        self.label_N3.setPixmap(QPixmap(os.path.join("MP2X_panel", "N3.png")))
        self.label_N3.setFixedSize(5, 8)
        self.label_N3.move(74, 356)

        self.label_N4 = QLabel(self)
        self.label_N4.setPixmap(QPixmap(os.path.join("MP2X_panel", "N4.png")))
        self.label_N4.setFixedSize(7, 8)
        self.label_N4.move(87, 356)

        self.label_button_S3 = QLabel(self)
        self.label_button_S3.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S3.setFixedSize(5, 5)
        self.label_button_S3.move(74, 368)

        self.label_button_S4 = QLabel(self)
        self.label_button_S4.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S4.setFixedSize(5, 5)
        self.label_button_S4.move(87, 368)

        self.label_SF_34 = QLabel(self)
        self.label_SF_34.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_34.setFixedSize(8, 7)
        self.label_SF_34.move(96, 366)

        #################################################

        self.label_button_A5 = QLabel(self)
        self.label_button_A5.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A5.setFixedSize(5, 5)
        self.label_button_A5.move(74, 385)

        self.label_button_A6 = QLabel(self)
        self.label_button_A6.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A6.setFixedSize(5, 5)
        self.label_button_A6.move(87, 385)

        self.label_ACT_56 = QLabel(self)
        self.label_ACT_56.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_56.setFixedSize(15, 7)
        self.label_ACT_56.move(94, 383)

        self.label_N5 = QLabel(self)
        self.label_N5.setPixmap(QPixmap(os.path.join("MP2X_panel", "N5.png")))
        self.label_N5.setFixedSize(5, 8)
        self.label_N5.move(74, 392)

        self.label_N6 = QLabel(self)
        self.label_N6.setPixmap(QPixmap(os.path.join("MP2X_panel", "N6.png")))
        self.label_N6.setFixedSize(6, 8)
        self.label_N6.move(87, 392)

        self.label_button_S5 = QLabel(self)
        self.label_button_S5.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S5.setFixedSize(5, 5)
        self.label_button_S5.move(74, 402)

        self.label_button_S6 = QLabel(self)
        self.label_button_S6.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S6.setFixedSize(5, 5)
        self.label_button_S6.move(87, 402)

        self.label_SF_56 = QLabel(self)
        self.label_SF_56.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_56.setFixedSize(8, 7)
        self.label_SF_56.move(96, 400)

        ########################################

        self.label_button_A7 = QLabel(self)
        self.label_button_A7.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A7.setFixedSize(5, 5)
        self.label_button_A7.move(74, 421)

        self.label_button_A8 = QLabel(self)
        self.label_button_A8.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A8.setFixedSize(5, 5)
        self.label_button_A8.move(87, 421)

        self.label_ACT_78 = QLabel(self)
        self.label_ACT_78.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_78.setFixedSize(15, 7)
        self.label_ACT_78.move(94, 419)

        self.label_N7 = QLabel(self)
        self.label_N7.setPixmap(QPixmap(os.path.join("MP2X_panel", "N7.png")))
        self.label_N7.setFixedSize(6, 8)
        self.label_N7.move(74, 428)

        self.label_N8 = QLabel(self)
        self.label_N8.setPixmap(QPixmap(os.path.join("MP2X_panel", "N8.png")))
        self.label_N8.setFixedSize(6, 8)
        self.label_N8.move(87, 428)

        self.label_button_S7 = QLabel(self)
        self.label_button_S7.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S7.setFixedSize(5, 5)
        self.label_button_S7.move(74, 438)

        self.label_button_S8 = QLabel(self)
        self.label_button_S8.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S8.setFixedSize(5, 5)
        self.label_button_S8.move(87, 438)

        self.label_SF_78 = QLabel(self)
        self.label_SF_78.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_78.setFixedSize(8, 7)
        self.label_SF_78.move(96, 436)

        ###########################################

        self.label_button_A9 = QLabel(self)
        self.label_button_A9.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A9.setFixedSize(5, 5)
        self.label_button_A9.move(74, 457)

        self.label_button_A10 = QLabel(self)
        self.label_button_A10.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A10.setFixedSize(5, 5)
        self.label_button_A10.move(87, 457)

        self.label_ACT_910 = QLabel(self)
        self.label_ACT_910.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_910.setFixedSize(15, 7)
        self.label_ACT_910.move(94, 455)

        self.label_N9 = QLabel(self)
        self.label_N9.setPixmap(QPixmap(os.path.join("MP2X_panel", "N9.png")))
        self.label_N9.setFixedSize(5, 8)
        self.label_N9.move(74, 464)

        self.label_N10 = QLabel(self)
        self.label_N10.setPixmap(QPixmap(os.path.join("MP2X_panel", "N10.png")))
        self.label_N10.setFixedSize(12, 8)
        self.label_N10.move(85, 464)

        self.label_button_S9 = QLabel(self)
        self.label_button_S9.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S9.setFixedSize(5, 5)
        self.label_button_S9.move(74, 474)

        self.label_button_S10 = QLabel(self)
        self.label_button_S10.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S10.setFixedSize(5, 5)
        self.label_button_S10.move(87, 474)

        self.label_SF_910 = QLabel(self)
        self.label_SF_910.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_910.setFixedSize(8, 7)
        self.label_SF_910.move(96, 472)

        ########################################

        self.label_button_A11 = QLabel(self)
        self.label_button_A11.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A11.setFixedSize(5, 5)
        self.label_button_A11.move(74, 493)

        self.label_button_A12 = QLabel(self)
        self.label_button_A12.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A12.setFixedSize(5, 5)
        self.label_button_A12.move(87, 493)

        self.label_ACT_1112 = QLabel(self)
        self.label_ACT_1112.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_1112.setFixedSize(15, 7)
        self.label_ACT_1112.move(94, 491)

        self.label_N11 = QLabel(self)
        self.label_N11.setPixmap(QPixmap(os.path.join("MP2X_panel", "N11.png")))
        self.label_N11.setFixedSize(11, 8)
        self.label_N11.move(70, 500)

        self.label_N12 = QLabel(self)
        self.label_N12.setPixmap(QPixmap(os.path.join("MP2X_panel", "N12.png")))
        self.label_N12.setFixedSize(11, 8)
        self.label_N12.move(85, 500)

        self.label_button_S11 = QLabel(self)
        self.label_button_S11.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S11.setFixedSize(5, 5)
        self.label_button_S11.move(74, 510)

        self.label_button_S12 = QLabel(self)
        self.label_button_S12.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S12.setFixedSize(5, 5)
        self.label_button_S12.move(87, 510)

        self.label_SF_1112 = QLabel(self)
        self.label_SF_1112.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_1112.setFixedSize(8, 7)
        self.label_SF_1112.move(96, 508)

#######################################

        self.label_button_A13 = QLabel(self)
        self.label_button_A13.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A13.setFixedSize(5, 5)
        self.label_button_A13.move(74, 529)

        self.label_button_A14 = QLabel(self)
        self.label_button_A14.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A14.setFixedSize(5, 5)
        self.label_button_A14.move(87, 529)

        self.label_ACT_1314 = QLabel(self)
        self.label_ACT_1314.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_1314.setFixedSize(15, 7)
        self.label_ACT_1314.move(94, 527)

        self.label_N13 = QLabel(self)
        self.label_N13.setPixmap(QPixmap(os.path.join("MP2X_panel", "N13.png")))
        self.label_N13.setFixedSize(11, 8)
        self.label_N13.move(70, 536)

        self.label_N14 = QLabel(self)
        self.label_N14.setPixmap(QPixmap(os.path.join("MP2X_panel", "N14.png")))
        self.label_N14.setFixedSize(12, 8)
        self.label_N14.move(85, 536)

        self.label_button_S13 = QLabel(self)
        self.label_button_S13.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S13.setFixedSize(5, 5)
        self.label_button_S13.move(74, 546)

        self.label_button_S14 = QLabel(self)
        self.label_button_S14.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S14.setFixedSize(5, 5)
        self.label_button_S14.move(87, 546)

        self.label_SF_1314 = QLabel(self)
        self.label_SF_1314.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_1314.setFixedSize(8, 7)
        self.label_SF_1314.move(96, 544)

        ################################################

        self.label_button_A15 = QLabel(self)
        self.label_button_A15.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A15.setFixedSize(5, 5)
        self.label_button_A15.move(74, 565)

        self.label_button_A16 = QLabel(self)
        self.label_button_A16.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_A16.setFixedSize(5, 5)
        self.label_button_A16.move(87, 565)

        self.label_ACT_1516 = QLabel(self)
        self.label_ACT_1516.setPixmap(QPixmap(os.path.join("MP2X_panel", "ACT.png")))
        self.label_ACT_1516.setFixedSize(15, 7)
        self.label_ACT_1516.move(94, 563)

        self.label_N15 = QLabel(self)
        self.label_N15.setPixmap(QPixmap(os.path.join("MP2X_panel", "N15.png")))
        self.label_N15.setFixedSize(11, 8)
        self.label_N15.move(70, 572)

        self.label_N16 = QLabel(self)
        self.label_N16.setPixmap(QPixmap(os.path.join("MP2X_panel", "N16.png")))
        self.label_N16.setFixedSize(12, 8)
        self.label_N16.move(85, 572)

        self.label_button_S15 = QLabel(self)
        self.label_button_S15.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S15.setFixedSize(5, 5)
        self.label_button_S15.move(74, 582)

        self.label_button_S16 = QLabel(self)
        self.label_button_S16.setPixmap(QPixmap(os.path.join("MP2X_panel", "button.png")))
        self.label_button_S16.setFixedSize(5, 5)
        self.label_button_S16.move(87, 582)

        self.label_SF_1516 = QLabel(self)
        self.label_SF_1516.setPixmap(QPixmap(os.path.join("MP2X_panel", "SF.png")))
        self.label_SF_1516.setFixedSize(8, 7)
        self.label_SF_1516.move(96, 580)

        #########################################

        self.label_CH2 = QLabel(self)
        self.label_CH2.setPixmap(QPixmap(os.path.join("MP2X_panel", "CH.png")))
        self.label_CH2.setFixedSize(47, 31)
        self.label_CH2.move(59, 776)

        self.label_CH2_title = QLabel(self)
        self.label_CH2_title.setPixmap(QPixmap(os.path.join("MP2X_panel", "CH2.png")))
        self.label_CH2_title.setFixedSize(19, 8)
        self.label_CH2_title.move(61, 766)

        self.label_CH1 = QLabel(self)
        self.label_CH1.setPixmap(QPixmap(os.path.join("MP2X_panel", "CH.png")))
        self.label_CH1.setFixedSize(47, 31)
        self.label_CH1.move(59, 732)

        self.label_CH1_title = QLabel(self)
        self.label_CH1_title.setPixmap(QPixmap(os.path.join("MP2X_panel", "CH1.png")))
        self.label_CH1_title.setFixedSize(19, 8)
        self.label_CH1_title.move(61, 722)

        ########################################

        self.label_RL1 = QLabel(self)
        self.label_RL1.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_RL1.setFixedSize(5, 7)
        self.label_RL1.move(10, 275)

        self.label_L1 = QLabel(self)
        self.label_L1.setPixmap(QPixmap(os.path.join("MP2X_panel", "L1.png")))
        self.label_L1.setFixedSize(10, 8)
        self.label_L1.move(7, 285)

        self.label_TL1 = QLabel(self)
        self.label_TL1.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_TL1.setFixedSize(5, 7)
        self.label_TL1.move(10, 297)

        ##################################

        self.label_R1 = QLabel(self)
        self.label_R1.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R1.setFixedSize(5, 7)
        self.label_R1.move(10, 311)

        self.label_x1 = QLabel(self)
        self.label_x1.setPixmap(QPixmap(os.path.join("MP2X_panel", "N1.png")))
        self.label_x1.setFixedSize(4, 8)
        self.label_x1.move(7, 321)

        self.label_T1 = QLabel(self)
        self.label_T1.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T1.setFixedSize(5, 7)
        self.label_T1.move(10, 334)

        ###################################

        self.label_R3 = QLabel(self)
        self.label_R3.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R3.setFixedSize(5, 7)
        self.label_R3.move(10, 347)

        self.label_x3 = QLabel(self)
        self.label_x3.setPixmap(QPixmap(os.path.join("MP2X_panel", "N3.png")))
        self.label_x3.setFixedSize(5, 8)
        self.label_x3.move(7, 358)

        self.label_T3 = QLabel(self)
        self.label_T3.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T3.setFixedSize(5, 7)
        self.label_T3.move(10, 370)

        ##################################

        self.label_R5 = QLabel(self)
        self.label_R5.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R5.setFixedSize(5, 7)
        self.label_R5.move(10, 383)

        self.label_x5 = QLabel(self)
        self.label_x5.setPixmap(QPixmap(os.path.join("MP2X_panel", "N5.png")))
        self.label_x5.setFixedSize(5, 8)
        self.label_x5.move(7, 394)

        self.label_T5 = QLabel(self)
        self.label_T5.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T5.setFixedSize(5, 7)
        self.label_T5.move(10, 405)

        ###############################

        self.label_R7 = QLabel(self)
        self.label_R7.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R7.setFixedSize(5, 7)
        self.label_R7.move(10, 419)

        self.label_x7 = QLabel(self)
        self.label_x7.setPixmap(QPixmap(os.path.join("MP2X_panel", "N7.png")))
        self.label_x7.setFixedSize(6, 8)
        self.label_x7.move(7, 430)

        self.label_T7 = QLabel(self)
        self.label_T7.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T7.setFixedSize(5, 7)
        self.label_T7.move(10, 441)

        ###############################

        self.label_R9 = QLabel(self)
        self.label_R9.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R9.setFixedSize(5, 7)
        self.label_R9.move(10, 455)

        self.label_x9 = QLabel(self)
        self.label_x9.setPixmap(QPixmap(os.path.join("MP2X_panel", "N9.png")))
        self.label_x9.setFixedSize(5, 8)
        self.label_x9.move(7, 466)

        self.label_T9 = QLabel(self)
        self.label_T9.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T9.setFixedSize(5, 7)
        self.label_T9.move(10, 477)

        ################################

        self.label_R11 = QLabel(self)
        self.label_R11.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R11.setFixedSize(5, 7)
        self.label_R11.move(10, 491)

        self.label_x11 = QLabel(self)
        self.label_x11.setPixmap(QPixmap(os.path.join("MP2X_panel", "N11.png")))
        self.label_x11.setFixedSize(11, 8)
        self.label_x11.move(5, 502)

        self.label_T11 = QLabel(self)
        self.label_T11.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T11.setFixedSize(5, 7)
        self.label_T11.move(10, 513)

        #################################

        self.label_R13 = QLabel(self)
        self.label_R13.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R13.setFixedSize(5, 7)
        self.label_R13.move(10, 527)

        self.label_x13 = QLabel(self)
        self.label_x13.setPixmap(QPixmap(os.path.join("MP2X_panel", "N13.png")))
        self.label_x13.setFixedSize(11, 8)
        self.label_x13.move(5, 538)

        self.label_T13 = QLabel(self)
        self.label_T13.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T13.setFixedSize(5, 7)
        self.label_T13.move(10, 549)

        #################################

        self.label_R15 = QLabel(self)
        self.label_R15.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R15.setFixedSize(5, 7)
        self.label_R15.move(10, 563)

        self.label_x15 = QLabel(self)
        self.label_x15.setPixmap(QPixmap(os.path.join("MP2X_panel", "N15.png")))
        self.label_x15.setFixedSize(11, 8)
        self.label_x15.move(5, 574)

        self.label_T15 = QLabel(self)
        self.label_T15.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T15.setFixedSize(5, 7)
        self.label_T15.move(10, 585)











        self.label_RL2 = QLabel(self)
        self.label_RL2.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_RL2.setFixedSize(5, 7)
        self.label_RL2.move(53, 275)

        self.label_xL2 = QLabel(self)
        self.label_xL2.setPixmap(QPixmap(os.path.join("MP2X_panel", "L2.png")))
        self.label_xL2.setFixedSize(10, 8)
        self.label_xL2.move(54, 285)

        self.label_TL2 = QLabel(self)
        self.label_TL2.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_TL2.setFixedSize(5, 7)
        self.label_TL2.move(53, 297)

        ##################################

        self.label_R2 = QLabel(self)
        self.label_R2.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R2.setFixedSize(5, 7)
        self.label_R2.move(53, 311)

        self.label_x2 = QLabel(self)
        self.label_x2.setPixmap(QPixmap(os.path.join("MP2X_panel", "N2.png")))
        self.label_x2.setFixedSize(5, 8)
        self.label_x2.move(53, 321)

        self.label_T2 = QLabel(self)
        self.label_T2.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T2.setFixedSize(5, 7)
        self.label_T2.move(53, 334)

        ###################################

        self.label_R4 = QLabel(self)
        self.label_R4.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R4.setFixedSize(5, 7)
        self.label_R4.move(53, 347)

        self.label_x4 = QLabel(self)
        self.label_x4.setPixmap(QPixmap(os.path.join("MP2X_panel", "N4.png")))
        self.label_x4.setFixedSize(7, 8)
        self.label_x4.move(53, 358)

        self.label_T4 = QLabel(self)
        self.label_T4.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T4.setFixedSize(5, 7)
        self.label_T4.move(53, 370)

        ##################################

        self.label_R6 = QLabel(self)
        self.label_R6.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R6.setFixedSize(5, 7)
        self.label_R6.move(53, 383)

        self.label_x6 = QLabel(self)
        self.label_x6.setPixmap(QPixmap(os.path.join("MP2X_panel", "N6.png")))
        self.label_x6.setFixedSize(6, 8)
        self.label_x6.move(53, 394)

        self.label_T6 = QLabel(self)
        self.label_T6.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T6.setFixedSize(5, 7)
        self.label_T6.move(53, 405)

        ###############################

        self.label_R8 = QLabel(self)
        self.label_R8.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R8.setFixedSize(5, 7)
        self.label_R8.move(53, 419)

        self.label_x8 = QLabel(self)
        self.label_x8.setPixmap(QPixmap(os.path.join("MP2X_panel", "N8.png")))
        self.label_x8.setFixedSize(6, 8)
        self.label_x8.move(53, 430)

        self.label_T8 = QLabel(self)
        self.label_T8.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T8.setFixedSize(5, 7)
        self.label_T8.move(53, 441)

        ###############################

        self.label_R10 = QLabel(self)
        self.label_R10.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R10.setFixedSize(5, 7)
        self.label_R10.move(53, 455)

        self.label_x10 = QLabel(self)
        self.label_x10.setPixmap(QPixmap(os.path.join("MP2X_panel", "N10.png")))
        self.label_x10.setFixedSize(12, 8)
        self.label_x10.move(53, 466)

        self.label_T10 = QLabel(self)
        self.label_T10.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T10.setFixedSize(5, 7)
        self.label_T10.move(53, 477)

        ################################

        self.label_R12 = QLabel(self)
        self.label_R12.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R12.setFixedSize(5, 7)
        self.label_R12.move(53, 491)

        self.label_x12 = QLabel(self)
        self.label_x12.setPixmap(QPixmap(os.path.join("MP2X_panel", "N12.png")))
        self.label_x12.setFixedSize(11, 8)
        self.label_x12.move(53, 502)

        self.label_T12 = QLabel(self)
        self.label_T12.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T12.setFixedSize(5, 7)
        self.label_T12.move(53, 513)

        ###########################################

        self.label_R14 = QLabel(self)
        self.label_R14.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R14.setFixedSize(5, 7)
        self.label_R14.move(53, 527)

        self.label_x14 = QLabel(self)
        self.label_x14.setPixmap(QPixmap(os.path.join("MP2X_panel", "N14.png")))
        self.label_x14.setFixedSize(12, 8)
        self.label_x14.move(53, 538)

        self.label_T14 = QLabel(self)
        self.label_T14.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T14.setFixedSize(5, 7)
        self.label_T14.move(53, 549)

        #################################

        self.label_R16 = QLabel(self)
        self.label_R16.setPixmap(QPixmap(os.path.join("MP2X_panel", "R.png")))
        self.label_R16.setFixedSize(5, 7)
        self.label_R16.move(53, 563)

        self.label_x16 = QLabel(self)
        self.label_x16.setPixmap(QPixmap(os.path.join("MP2X_panel", "N16.png")))
        self.label_x16.setFixedSize(12, 8)
        self.label_x16.move(53, 574)

        self.label_T16 = QLabel(self)
        self.label_T16.setPixmap(QPixmap(os.path.join("MP2X_panel", "T.png")))
        self.label_T16.setFixedSize(5, 7)
        self.label_T16.move(53, 585)

        ############################################

        self.label_CNS = QLabel(self)
        self.label_CNS.setPixmap(QPixmap(os.path.join("MP2X_panel", "CNS.png")))
        self.label_CNS.setFixedSize(16, 28)
        self.label_CNS.move(5, 714)

        self.label_CNS_title = QLabel(self)
        self.label_CNS_title.setPixmap(QPixmap(os.path.join("MP2X_panel", "CNS_title.png")))
        self.label_CNS_title.setFixedSize(19, 8)
        self.label_CNS_title.move(3, 704)

        self.setAcceptDrops(True)

    def contextMenuEvent(self, event):
        from BLANK_panel.BLANK_panel import BLANK_panel
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            Panel_Data[self.id].setWidget(BLANK_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"].pop(str(self.id))  # this is uncompleted


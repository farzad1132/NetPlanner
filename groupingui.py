# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupingui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(823, 608)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(300, 50, 257, 193))
        self.widget.setObjectName("widget")
        self.GroupingLayout = QtWidgets.QGridLayout(self.widget)
        self.GroupingLayout.setContentsMargins(0, 0, 0, 0)
        self.GroupingLayout.setObjectName("GroupingLayout")
        self.SetGatewayNode_button = QtWidgets.QPushButton(self.widget)
        self.SetGatewayNode_button.setObjectName("SetGatewayNode_button")
        self.GroupingLayout.addWidget(self.SetGatewayNode_button, 0, 0, 1, 4)
        self.GroupName = QtWidgets.QLabel(self.widget)
        self.GroupName.setObjectName("GroupName")
        self.GroupingLayout.addWidget(self.GroupName, 1, 0, 1, 2)
        self.GroupName_edit = QtWidgets.QLineEdit(self.widget)
        self.GroupName_edit.setObjectName("GroupName_edit")
        self.GroupingLayout.addWidget(self.GroupName_edit, 1, 2, 1, 2)
        self.GroupId_edit = QtWidgets.QLineEdit(self.widget)
        self.GroupId_edit.setObjectName("GroupId_edit")
        self.GroupingLayout.addWidget(self.GroupId_edit, 2, 2, 1, 2)
        self.GroupColor = QtWidgets.QLabel(self.widget)
        self.GroupColor.setObjectName("GroupColor")
        self.GroupingLayout.addWidget(self.GroupColor, 3, 0, 1, 2)
        self.SelectColor_button = QtWidgets.QPushButton(self.widget)
        self.SelectColor_button.setObjectName("SelectColor_button")
        self.GroupingLayout.addWidget(self.SelectColor_button, 3, 2, 1, 2)
        self.SelectSubNode_button = QtWidgets.QPushButton(self.widget)
        self.SelectSubNode_button.setObjectName("SelectSubNode_button")
        self.GroupingLayout.addWidget(self.SelectSubNode_button, 4, 0, 1, 2)
        self.SelectSubNode = QtWidgets.QLabel(self.widget)
        self.SelectSubNode.setObjectName("SelectSubNode")
        self.GroupingLayout.addWidget(self.SelectSubNode, 4, 3, 1, 1)
        self.Cancel_button = QtWidgets.QPushButton(self.widget)
        self.Cancel_button.setObjectName("Cancel_button")
        self.GroupingLayout.addWidget(self.Cancel_button, 5, 1, 1, 2)
        self.OK_button = QtWidgets.QPushButton(self.widget)
        self.OK_button.setObjectName("OK_button")
        self.GroupingLayout.addWidget(self.OK_button, 5, 3, 1, 1)
        self.GroupID = QtWidgets.QLabel(self.widget)
        self.GroupID.setObjectName("GroupID")
        self.GroupingLayout.addWidget(self.GroupID, 2, 0, 1, 2)

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SetGatewayNode_button.setText(_translate("Form", "Set Node as Gateway"))
        self.GroupName.setText(_translate("Form", "Group Name:"))
        self.GroupColor.setText(_translate("Form", "Group Color:"))
        self.SelectColor_button.setText(_translate("Form", "Select Color"))
        self.SelectSubNode_button.setText(_translate("Form", "Select Sub Nodes"))
        self.SelectSubNode.setText(_translate("Form", "TextLabel"))
        self.Cancel_button.setText(_translate("Form", "Cancel"))
        self.OK_button.setText(_translate("Form", "Ok"))
        self.GroupID.setText(_translate("Form", "Group ID:"))
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

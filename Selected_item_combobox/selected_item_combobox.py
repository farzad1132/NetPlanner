from PySide2 import QtWidgets,QtGui,QtCore
import sys

# Creating Class to create ComboBox by creating object of ["name" = ComboBox()]

class ComboBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    #list of index want to be Highlighted:
        self.Chosen_index_to_Highlight = [2, 6, 8]

    #list of index want to reset to Unhighlighted:
        self.Chosen_index_to_Reset = [2, 6]

    #list of Item to add in ComboBox:
        self.items = ["--Select--", "Python", "Java", "C++", "C#", "MP1H", "TP1H", "MP2X", "Line", "Client"]
        self.title = "Customized ComboBox"
        self.setWindowTitle(self.title)
        self.resize(400, 300)
        self.combo_init()

    def combo_init(self):
        self.combo = QtWidgets.QComboBox(self)
        self.combo.setGeometry(QtCore.QRect(100, 40, 190, 22))
        self.combo.addItems(self.items)
        self.combo.setCurrentIndex(0)
        self.combo.setEditable(True)

    # Calling method to Highlight chosen index:
        self.Highlight_Index()

    # Calling method to reset the chosen index:
        self.Reset_Highlight_Index()

# method for highlight the chosen index
    def Highlight_Index(self):
        Highlight_Font = QtGui.QFont()
        Highlight_Font.setBold(True)
        for i in range(len(self.Chosen_index_to_Highlight)):
            model = self.combo.model().item(self.Chosen_index_to_Highlight[i])
            model.setBackground(QtGui.QColor(57,255,20))
            model.setFont(Highlight_Font)

# method for reset the chosen index
    def Reset_Highlight_Index(self):
        Reset_Font = QtGui.QFont()
        Reset_Font.setBold(False)
        for i in range(len(self.Chosen_index_to_Reset)):
            model = self.combo.model().item(self.Chosen_index_to_Reset[i])
            model.setBackground(QtGui.QColor('white'))
            model.setFont(Reset_Font)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    combbox = ComboBox()
    combbox.show()
    sys.exit(app.exec_())
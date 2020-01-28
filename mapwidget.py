# ------------------------------------------------- ----- 
# -------------------- mapwidget.py -------------------- 
# -------------------------------------------------- ---- 
from  PySide2.QtWidgets import *
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from  matplotlib.figure  import  Figure

    
class  MapWidget ( QWidget ):
    
    def __init__ ( self ,  parent  =  None ):

        QWidget.__init__( self ,  parent )
        
        self.canvas = FigureCanvas( Figure())
        
        vertical_layout = QVBoxLayout() 
        vertical_layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.canvas.axes = self.canvas.figure.add_subplot(111) 
        self.setLayout(vertical_layout)

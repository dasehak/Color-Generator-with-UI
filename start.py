from PyQt5 import QtWidgets, QtGui, QtCore, QtTest, uic
import sys
import os, binascii
from PIL import Image, ImageDraw, ImageColor
from modules.ui import *

# creating rectangle
img = Image.new('RGBA', (100, 100), 'white')    
idraw = ImageDraw.Draw(img)
 
idraw.rectangle((0, 0, 100, 100), fill=rgb)
 
img.save('modules/images/rectangle.png', 'png')

class generator_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(generator_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
app = QtWidgets.QApplication([])
application = generator_window()
application.show()

sys.exit(app.exec())
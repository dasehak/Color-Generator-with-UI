from PyQt5 import QtWidgets, uic
import sys
from random import randint
from bs4 import BeautifulSoup
import lxml.etree as ET
import shutil
import os, binascii
import colorsys
from PIL import Image, ImageDraw, ImageFont, ImageColor


pendosia = "{:06x}".format(randint(0, 0xFFFFFF))
etm_super = pendosia
gay_porn = f"#{etm_super}"
h = etm_super
rgb = ImageColor.getrgb(f"{gay_porn}")

# Создаем белый квадрат
img = Image.new('RGBA', (100, 100), 'white')    
idraw = ImageDraw.Draw(img)
 
idraw.rectangle((0, 0, 100, 100), fill=rgb)
 
img.save('rectangle.png', 'png')

#adding the encoding when the file is opened and written is needed to avoid a charmap error
with open(r'ui.xml', encoding="utf8") as f:
  tree = ET.parse(f)
  root = tree.getroot()


  for elem in root.getiterator():
    try:
      elem.text = elem.text.replace('AHAHHAHAHAHAHAHAHA', f"#{etm_super}")
      elem.text = elem.text.replace('test', f"{rgb}")
    except AttributeError:
      pass

#tree.write('output.xml', encoding="utf8")
# Adding the xml_declaration and method helped keep the header info at the top of the file.
tree.write(r'ui.xml', encoding="utf8")


app = QtWidgets.QApplication([])
win = uic.loadUi (r"ui.xml") # расположение вашего файла .ui

shutil.copyfile(r'data/ui.xml', r'ui.xml')

win.show()
sys.exit(app.exec())
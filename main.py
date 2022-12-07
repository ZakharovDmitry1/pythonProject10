import sys
from random import choice, randint
from PIL import Image
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'untitled.ui', self)
        self.im = Image.open('mid_289972_221628.jpg')
        self.im.save('new_image.jpg')
        n = QLabel(self)
        self.label.setPixmap(QPixmap('new_image.jpg'))
        self.pixels = self.im.load()
        self.x, self.y = self.im.size
        self.run()

    def run(self):
        self.btn6.clicked.connect(self.lRotated)
        self.btn5.clicked.connect(self.rRotated)
        self.btn1.clicked.connect(self.r)
        self.btn2.clicked.connect(self.g)
        self.btn3.clicked.connect(self.b)
        self.btn4.clicked.connect(self.all)

    def rRotated(self):
        self.im = Image.open('new_image.jpg')
        self.im = self.im.rotate(90)
        self.im.save('new_image.jpg')
        self.im = Image.open('mid_289972_221628.jpg')
        self.im = self.im.rotate(90)
        self.im.save('mid_289972_221628.jpg')
        self.label.setPixmap(QPixmap('new_image.jpg'))

    def lRotated(self):
        self.im = Image.open('new_image.jpg')
        self.im = self.im.rotate(270)
        self.im.save('new_image.jpg')
        self.im = Image.open('mid_289972_221628.jpg')
        self.im = self.im.rotate(270)
        self.im.save('mid_289972_221628.jpg')
        self.label.setPixmap(QPixmap('new_image.jpg'))

    def r(self):
        self.im = Image.open('mid_289972_221628.jpg')
        self.im.save('new_image.jpg')
        self.pixels = self.im.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = r, 0, 0
        self.im.save('new_image.jpg')
        self.label.setPixmap(QPixmap('new_image.jpg'))


    def g(self):
        self.im = Image.open('mid_289972_221628.jpg')
        self.im.save('new_image.jpg')
        self.pixels = self.im.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 0, g, 0
        self.im.save('new_image.jpg')
        self.label.setPixmap(QPixmap('new_image.jpg'))
        self.im = Image.open('mid_289972_221628.jpg')

    def b(self):
        self.im = Image.open('mid_289972_221628.jpg')
        self.im.save('new_image.jpg')
        self.pixels = self.im.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 0, 0, b
        self.im.save('new_image.jpg')
        self.label.setPixmap(QPixmap('new_image.jpg'))
        self.im = Image.open('mid_289972_221628.jpg')

    def all(self):
        self.im = Image.open('mid_289972_221628.jpg')
        self.pixels = self.im.load()
        self.im.save('new_image.jpg')
        self.label.setPixmap(QPixmap('new_image.jpg'))


if __name__ == '__main__':
    im = Image.open('new_image1.jpg')
    im.save('mid_289972_221628.jpg')
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

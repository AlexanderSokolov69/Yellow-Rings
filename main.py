import sys
from random import randint, choice

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

from Ui import Ui_Form

class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.initUi()
        
    def initUi(self):
        self.setupUi(self)
        self.go_draw = False
        self.colors = ['yellow', 'green', 'red', 'blue', 'brown', 'white']
        self.pushButton.clicked.connect(self.make)
        self.w = self.size().width() // 2
        self.h = self.size().height() // 2
        
    def make(self):
        self.go_draw = True
        self.update()
        
    def paintEvent(self, event):
        if self.go_draw:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(choice(self.colors)))
            d = randint(10, min([self.h, self.w]))
            qp.drawEllipse(self.w - d, self.h - d, d * 2, d * 2)
            qp.end()
        
        
if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
        
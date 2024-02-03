from instr import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import (
    QLabel, 
    QWidget, 
    QApplication, 
    QPushButton, 
    QHBoxLayout, 
    QVBoxLayout, 
    QLineEdit
)

Group = {
    'Низкий' : ((15, 999), (16.5, 999), (18, 999), (19.5, 999), (21, 999)),
    'Удовлет' : ((11, 14.9), (12.5, 16.4), (14, 17.9), (15.5, 19.4), (17, 20.9)),
    'Средний' : ((6, 10.9), (7.5, 12.4), (9, 13.9), (10.5, 15.4), (12, 16.9)),
    'Выше среднего' : ((0.5, 5.9), (2, 7.4), (3.5, 8.9), (5, 10.4), (6.5, 11.9)),
    'Высокий' : ((-999, 0.4), (-999, 1.9), (-999, 3.4), (-999, 4.9), (-999, 6.4)),
}

AgeGroup = {
    1 : (15, 999),
    2 : (13, 14),
    3 : (11, 12),
    4 : (9, 10),
    5 : (-999, 8),
}

def Comparer(Age, Index):
    OurAgeGroup = 1
    for i in AgeGroup:
        Checker = AgeGroup[i]
        if Age >= Checker[0] and Age <= Checker[1]:
            OurAgeGroup = i
    for Groups in Group:
        CurrentGroup = Group[Groups][OurAgeGroup-1]
        if Index >= CurrentGroup[0] and Index <= CurrentGroup[1]:
            return Groups

class FinalWin(QWidget):
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index = (4*(self.p1+self.p2+self.p3)-200)/10
        self.indexs_text = QLabel(txt_index+' '+str(self.index))
        self.result_text = QLabel(txt_result+' '+Comparer(self.Age, self.index))
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.indexs_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.result_text, alignment = Qt.AlignCenter)

        self.setLayout(self.layout)
    def __init__(self, Age, p1, p2, p3):
        super().__init__()
        self.Age = Age
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.set_appear()
        self.initUI()
        self.show()
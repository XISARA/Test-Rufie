from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime
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

Time = QTimer()

class SecondWin(QWidget):
    def FinalClick(self):
        self.destroy()
        Age = self.lineage.text()
        Result1 = self.result1.text()
        Result2 = self.result2.text()
        Result3 = self.result3.text()
        self.fw = FinalWin(int(Age), int(Result1), int(Result2), int(Result3))
    def Appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width, win_height)
    def InitializeUI(self):
        self.fullname = QLabel(txt_name)
        self.linename = QLineEdit(txt_hintname)
        self.fullage = QLabel(txt_age)
        self.lineage = QLineEdit(txt_hintage)
        self.test1text = QLabel(txt_test1)
        self.button1test = QPushButton(txt_starttest1)
        self.result1 = QLineEdit(txt_hinttest1)
        self.test2text = QLabel(txt_test2)
        self.button2test = QPushButton(txt_starttest2)
        self.test3text = QLabel(txt_test3)
        self.button3test = QPushButton(txt_starttest3)
        self.result2 = QLineEdit(txt_hinttest2)
        self.result3 = QLineEdit(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.currentTest = 'test1'

        self.Timer = QLabel('<b>00:00:15<b>', self)
        self.Timer.resize(120, 120)
        self.Timer.move(780, 220)
        self.Timer.setFont(QFont('Arial', 20))
        self.Timer.setAlignment(Qt.AlignLeft)
        self.Timer.show()

        self.rLine = QVBoxLayout()
        self.rLine.addWidget(self.fullname, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.linename, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.fullage, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.lineage, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.test1text, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.button1test, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.result1, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.test2text, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.button2test, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.test3text, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.button3test, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.result2, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.result3, alignment = Qt.AlignLeft)
        self.rLine.addWidget(self.sendresults, alignment = Qt.AlignCenter)

        self.setLayout(self.rLine)

    def Connections(self):
        def TimerEvent(self, Timer):
            global CurrentTimer
            global TypeOfString
            global CurrentTest
            CurrentTimer = CurrentTimer.addSecs(-1)
            Timer.setStyleSheet("color: rgb(0, 0, 0);")
            if TypeOfString == 'full':
                Timer.setText(CurrentTimer.toString("<b>hh:mm:ss<b>"))
                if CurrentTest == 'test3':
                    if int(CurrentTimer.toString("ss")) <= 60 and int(CurrentTimer.toString("ss")) >= 45 or int(CurrentTimer.toString("ss")) <= 15 and int(CurrentTimer.toString("ss")) >= 0:
                        Timer.setStyleSheet("color: rgb(0, 255, 0);")
            elif TypeOfString == 'sec':
                Timer.setText(CurrentTimer.toString("<b>ss<b>"))
            if CurrentTimer.toString("hh:mm:ss") == "00:00:00":
                Time.stop()
        def StartTime(self, TimeGiven, Power, StringType, TestType):
            global CurrentTimer
            global TypeOfString
            global CurrentTest
            TypeOfString = StringType
            CurrentTimer = QTime(TimeGiven[0], TimeGiven[1], TimeGiven[2])
            self.Timer.setStyleSheet("color: rgb(0, 0, 0);")
            CurrentTest = TestType
            if StringType == 'full':
                self.Timer.setText(CurrentTimer.toString("<b>hh:mm:ss<b>"))
            else:
                self.Timer.setText(CurrentTimer.toString("<b>ss<b>"))
            Time.start(Power)
        Time.timeout.connect(lambda: TimerEvent(self, self.Timer))
        self.button1test.clicked.connect(lambda: StartTime(self, (0,0,15), 1000, 'full', 'test1'))
        self.button2test.clicked.connect(lambda: StartTime(self, (0,0,30), 1500, 'sec', 'test2'))
        self.button3test.clicked.connect(lambda: StartTime(self, (0,1,0), 1000, 'full', 'test3'))
    def __init__(self):
        super().__init__()
        self.Appear()
        self.InitializeUI()
        self.Connections()
        self.show()
        self.sendresults.clicked.connect(self.FinalClick)
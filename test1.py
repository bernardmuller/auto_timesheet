#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
from PyQt5 import QtGui
from PyQt5.QtCore import *

import time

def main(arg):

    alarmTime = QTime(int(arg[1]), int(arg[2]))
    while (QTime.currentTime() < alarmTime):
        time.sleep(10)

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(200, 350)
    w.move(300, 300)
    w.setWindowTitle('Rishipal Project')



    b = QtGui.QLabel(w)
    b.setText("Reminder")
    #b.setWindowFlags(Qt.SplashScreen)

    font = QtGui.QFont()
    font.setFamily('Lucida')
    font.setBold(True)
    font.setCapitalization(True)
    font.setFixedPitch(True)
    font.setPointSize(30)
    b.setFont(font)
    b.move(10,10)

    pic = QtGui.QLabel(w)
    pic.move(10,100)
    # use full ABSOLUTE path to the image, not relative
    pic.setPixmap(QtGui.QPixmap("larm.png"))

    #pic.show()
    #b.show()
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
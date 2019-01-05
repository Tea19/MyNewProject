# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import *
 
class ExceptionAS:
    def __init__(self):
        super().__init__()
        uic.loadUi('Error.ui', self)
        self.pushButton.clicked.connect(self.close)
 
        self.show()
 
class Check:
    def test_one(self):
        from test import one1
        data_test = {
            '123432234': "Yes",
            'dsfgdfg': "No",
            '34r34': "No",
            '000004545': "yes"
            }
        rez = True
        for key, valye in data_test.items():
            if one1(key) != value:
                rez = False
                break
        if rez:
            print(1)
        else:
            print(0)
 
    def test_two(self):
        from test import one2
        data_test = {'1221': True, 'abcba': True, 'zxc': False}
        rez = True
        for key, value in data_test.items():
            if one2(key) != value:
                rez = False
                break
        return rez
 
    def test_free(self):
        from test import one3
        data_test = {1024: True, 122: False, 12: False}
        rez = True
        for key, value in data_test.items():
            if one3(key) != value:
                rez = False
                break
        return rez
 
'''class Email:
    def send_mag(self, msg):'''
 
class MyWidget(QMainWindow, Check):
    def __init__(self):
        super().__init__()
        uic.loadUi('Contest1.ui', self)
 
        self.pushButton.clicked.connect(self.botton_one)
        self.pushButton_2.clicked.connect(self.botton_two)
        self.pushButton_3.clicked.connect(self.botton_free)
        self.pushButton_4.clicked.connect(self.goBack)
 
        self.show()
 
    def botton_one(self):
        try:
            if Check.test_one(self) == '1':
                self.label_2.setText('ok')
            else:
                self.label_2.setText('no')
        except Exception as E:
            self.label_2.setText('Ошибка')
 
    def botton_two(self):
        if Check.test_two(self):
            a = 'ok'
            self.label_3.setText(a)
        else:
            self.label_3.setText('no')
 
    def botton_free(self):
        if Check.test_free(self):
            self.label_4.setText('ok')
        else:
            self.label_4.setText('no')
 
    def goBack(self):
        self.close()
 
class Back_end:
    def files(self, msg):
        file = open("1.txt", "w")
        file.write(msg)
        file.close()
        '''with open('1.txt', 'a') as F:
            file = F.read()
            F.write(msg)'''
 
'''class SecondWindow:
    def __init__(self):
        super().__init__()
        uic.loadUi('main2.ui',self)'''
 
class MyWidgetMain(QMainWindow, Back_end):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.wr)
        self.pushButton_2.clicked.connect(self.show_window_2)
 
        self.show()

 
    def wr(self):
        password, email = self.lineEdit_3.text(), self.lineEdit_2.text()
        Back_end.files(
            self, 'Твой имэил: "{}"; пароль: "{}" :)'.format(email, password)
                       )
        self.pushButton_3.setText("Sent")
 
    def run(self):
        textboxValue = self.lineEdit.text()
        sl = {
            '1': 'Базовые понятия, ветвления',
            '2': 'Цикл "while"/"for"',
            '3': 'Всерос',
            '4': 'Контест',
            '5': 'Немного математики',
            '6': 'Личный кабинет'
        }
        try:
            if textboxValue in '23456789':
                self.label_2.setText('Данного урока пока нет:((Belca)')
                self.conn = False
            else:
                self.label_2.setText(sl[textboxValue])
        except:
            self.label_2.setText("Belca")
 
    def show_window_2(self):
        try:
            self.w2 = MyWidget()
            self.w2.show()
        except Exception as e:
            print(e)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidgetMain()
    w.show()
    sys.exit(app.exec_())

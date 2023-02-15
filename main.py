from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QGraphicsDropShadowEffect, QCheckBox, QToolButton, QFileDialog, QMessageBox, QSpinBox
from PyQt5.QtGui import QColor
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QPoint
import actions

import sys
import icons


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui.ui', self)
        self.lable = self.findChild(QLabel, 'label')
        self.shadow = QGraphicsDropShadowEffect(blurRadius=25, offset=QPoint(0, 0), color=QColor("black"))
        self.lable.setGraphicsEffect(self.shadow)

        self.checkb = self.findChild(QCheckBox, 'checkBox')
        self.checkb2 = self.findChild(QCheckBox, 'checkBox_2')
        self.btn1 = self.findChild(QToolButton, 'toolButton')
        self.btn2 = self.findChild(QToolButton, 'toolButton_2')
        self.btn3 = self.findChild(QToolButton, 'toolButton_3')
        self.create_btn = self.findChild(QPushButton, 'pushButton')
        self.rename_btn = self.findChild(QPushButton, 'pushButton_2')
        self.counter = self.findChild(QSpinBox, 'spinBox')
        self.checkb.toggled.connect(self.dbPath)
        self.checkb2.toggled.connect(self.lineName)
        self.btn1.clicked.connect(self.accFile)
        self.btn2.clicked.connect(self.maFile)
        self.create_btn.clicked.connect(self.create)
        self.rename_btn.clicked.connect(self.rename)
        self.hd = 0
        self.nm = 0
        global mafiles
        mafiles = ''

        self.show()


    def dbPath(self):
        if self.hd == 0:
            self.show = QtCore.QPropertyAnimation(self.frame, b'pos')
            self.show.setDuration(200)
            self.show.setStartValue(QPoint(340, 155))
            self.show.setEndValue(QPoint(-15, 155))
            self.show.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
            self.show.start()

            self.hd = 1
        else:
            self.hide = QtCore.QPropertyAnimation(self.frame, b'pos')
            self.hide.setDuration(200)
            self.hide.setStartValue(QPoint(-15, 155))
            self.hide.setEndValue(QPoint(340, 155))
            self.hide.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

            self.hide.start()
            
            self.hd = 0

    def lineName(self):
        if self.nm == 0:
            self.show = QtCore.QPropertyAnimation(self.frame_2, b'pos')
            self.show.setDuration(200)
            self.show.setStartValue(QPoint(340, 110))
            self.show.setEndValue(QPoint(-15, 110))
            self.show.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
            self.show.start()

            self.nm = 1
        else:
            self.hide = QtCore.QPropertyAnimation(self.frame_2, b'pos')
            self.hide.setDuration(200)
            self.hide.setStartValue(QPoint(-15, 110))
            self.hide.setEndValue(QPoint(340, 110))
            self.hide.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

            self.hide.start()
            
            self.nm = 0

    def accFile(self):
        global log_pass
        log_pass, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Files(*.json *.txt)')
        self.lineEdit.setText(log_pass)
            
    def maFile(self):
        global mafiles
        mafiles = QFileDialog.getExistingDirectory(self, 'Open file')   
        self.lineEdit_2.setText(mafiles)

    def create(self):
        name = self.lineEdit_3.text()
        count = int(self.counter.text())
        mafiles = self.lineEdit_2.text()
        log_pass = self.lineEdit.text()
        try:
            actions.createFiles(log_pass, name, count, mafiles)
            QMessageBox.information(self, "Configs creatrs", "Аккаунты созданы")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}", QMessageBox.Ok)

    def rename(self):
        path = QFileDialog.getExistingDirectory(self, 'Open file')
        if path != '':
            try:
                actions.renameFiles(path)
                QMessageBox.information(self, "Configs creatrs", "Файлы переименованы")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}", QMessageBox.Ok)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()

    app.exec_()        
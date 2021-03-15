# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Phanmemtheodoikhautrang(object):
    def setupUi(self, Phanmemtheodoikhautrang):
        Phanmemtheodoikhautrang.setObjectName("Phanmemtheodoikhautrang")
        Phanmemtheodoikhautrang.resize(1080, 720)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Phanmemtheodoikhautrang.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/giphy (1).gif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Phanmemtheodoikhautrang.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Phanmemtheodoikhautrang)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1080, 720))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("Photos/bg.png"))
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)
        self.background.setObjectName("background")
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(220, 120, 640, 480))
        self.screen.setText("")
        self.screen.setPixmap(QtGui.QPixmap("Photos/mask.jpg"))
        self.screen.setScaledContents(True)
        self.screen.setObjectName("screen")
        self.pgname = QtWidgets.QLabel(self.centralwidget)
        self.pgname.setGeometry(QtCore.QRect(90, 20, 900, 90))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pgname.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pgname.setFont(font)
        self.pgname.setAutoFillBackground(True)
        self.pgname.setFrameShape(QtWidgets.QFrame.Panel)
        self.pgname.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pgname.setScaledContents(True)
        self.pgname.setAlignment(QtCore.Qt.AlignCenter)
        self.pgname.setObjectName("pgname")
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(30, 540, 181, 151))
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("Photos/source.gif"))
        self.gif.setScaledContents(True)
        self.gif.setObjectName("gif")
        self.poster = QtWidgets.QLabel(self.centralwidget)
        self.poster.setGeometry(QtCore.QRect(860, 120, 211, 481))
        self.poster.setText("")
        self.poster.setPixmap(QtGui.QPixmap("Photos/5k.jpg"))
        self.poster.setScaledContents(True)
        self.poster.setObjectName("poster")
        self.Slogan = QtWidgets.QLabel(self.centralwidget)
        self.Slogan.setGeometry(QtCore.QRect(250, 600, 711, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Slogan.setFont(font)
        self.Slogan.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Slogan.setAlignment(QtCore.Qt.AlignCenter)
        self.Slogan.setObjectName("Slogan")
        self.noti = QtWidgets.QLabel(self.centralwidget)
        self.noti.setGeometry(QtCore.QRect(20, 320, 181, 191))
        self.noti.setAutoFillBackground(True)
        self.noti.setFrameShape(QtWidgets.QFrame.Panel)
        self.noti.setFrameShadow(QtWidgets.QFrame.Plain)
        self.noti.setScaledContents(True)
        self.noti.setObjectName("noti")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(30, 170, 150, 120))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setObjectName("button")
        Phanmemtheodoikhautrang.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Phanmemtheodoikhautrang)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        Phanmemtheodoikhautrang.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Phanmemtheodoikhautrang)
        self.statusbar.setObjectName("statusbar")
        Phanmemtheodoikhautrang.setStatusBar(self.statusbar)

        self.retranslateUi(Phanmemtheodoikhautrang)
        QtCore.QMetaObject.connectSlotsByName(Phanmemtheodoikhautrang)

    def retranslateUi(self, Phanmemtheodoikhautrang):
        _translate = QtCore.QCoreApplication.translate
        Phanmemtheodoikhautrang.setWindowTitle(_translate("Phanmemtheodoikhautrang", "MainWindow"))
        self.pgname.setText(_translate("Phanmemtheodoikhautrang", "<html><head/><body><p align=\"center\"><span style=\" color:#aa0000;\">Phần mềm theo dõi đeo khẩu trang</span></p></body></html>"))
        self.Slogan.setText(_translate("Phanmemtheodoikhautrang", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; color:#ff0000;\">&quot;HÃY GIỮ AN TOÀN CHO BẠN, GIA ĐÌNH VÀ CỘNG ĐỒNG TRƯỚC ĐẠI DỊCH COVID-19&quot;</span></p></body></html>"))
        self.noti.setText(_translate("Phanmemtheodoikhautrang", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Thông báo:</span></p><p align=\"justify\"><br/><span style=\" font-size:9pt;\">Phát hiện:</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Đã đeo khẩu trang:</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Chưa đeo khẩu trang:</span></p></body></html>"))
        self.button.setText(_translate("Phanmemtheodoikhautrang", "Bắt đầu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Phanmemtheodoikhautrang = QtWidgets.QMainWindow()
    ui = Ui_Phanmemtheodoikhautrang()
    ui.setupUi(Phanmemtheodoikhautrang)
    Phanmemtheodoikhautrang.show()
    sys.exit(app.exec_())
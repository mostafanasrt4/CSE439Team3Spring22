# Form implementation generated from reading ui file 'f:\Ain Shams\Spring 2022\Assignments\Assignments - CSE439 - Design of Compilers\CSE439Team3Spring22\ParserGUIOLD.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1033, 915)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 1041, 921))
        self.widget.setStyleSheet("Qwidget#widget{\n"
"background-color: rgb(255, 255, 255);\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.widget.setObjectName("widget")
        self.parseTreeWebEngineView = QtWebEngineWidgets.QWebEngineView(self.widget)
        self.parseTreeWebEngineView.setGeometry(QtCore.QRect(20, 340, 991, 571))
        self.parseTreeWebEngineView.setObjectName("parseTreeWebEngineView")
        self.parseTreeLabel = QtWidgets.QLabel(self.widget)
        self.parseTreeLabel.setGeometry(QtCore.QRect(20, 280, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.parseTreeLabel.setFont(font)
        self.parseTreeLabel.setObjectName("parseTreeLabel")
        self.inputCodeTextEdit = QtWidgets.QTextEdit(self.widget)
        self.inputCodeTextEdit.setGeometry(QtCore.QRect(270, 50, 481, 161))
        self.inputCodeTextEdit.setObjectName("inputCodeTextEdit")
        self.insertCodeLabel = QtWidgets.QLabel(self.widget)
        self.insertCodeLabel.setGeometry(QtCore.QRect(270, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.insertCodeLabel.setFont(font)
        self.insertCodeLabel.setObjectName("insertCodeLabel")
        self.parsePushButton = QtWidgets.QPushButton(self.widget)
        self.parsePushButton.setGeometry(QtCore.QRect(460, 220, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.parsePushButton.setFont(font)
        self.parsePushButton.setObjectName("parsePushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parseTreeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Parse Tree:</span></p></body></html>"))
        self.inputCodeTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Ex:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">x := 0;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if 1 then</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   x := y;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   if 0 then</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      y := 1;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   end</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   y := 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">end</p></body></html>"))
        self.insertCodeLabel.setText(_translate("MainWindow", "Insert your code here:"))
        self.parsePushButton.setText(_translate("MainWindow", "Parse"))
from PyQt6 import QtWebEngineWidgets

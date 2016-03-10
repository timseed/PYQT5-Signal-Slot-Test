# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(488, 362)
        self.N1 = QtWidgets.QTextEdit(Form)
        self.N1.setGeometry(QtCore.QRect(100, 30, 51, 31))
        self.N1.setObjectName("N1")
        self.N2 = QtWidgets.QTextEdit(Form)
        self.N2.setGeometry(QtCore.QRect(200, 30, 41, 31))
        self.N2.setObjectName("N2")
        self.btnCalc = QtWidgets.QPushButton(Form)
        self.btnCalc.setGeometry(QtCore.QRect(250, 30, 114, 32))
        self.btnCalc.setObjectName("btnCalc")
        self.RESULT = QtWidgets.QTextEdit(Form)
        self.RESULT.setGeometry(QtCore.QRect(370, 20, 41, 41))
        self.RESULT.setReadOnly(True)
        self.RESULT.setObjectName("RESULT")
        self.btnProcess = QtWidgets.QPushButton(Form)
        self.btnProcess.setGeometry(QtCore.QRect(300, 90, 114, 32))
        self.btnProcess.setObjectName("btnProcess")
        self.btnSignal = QtWidgets.QPushButton(Form)
        self.btnSignal.setGeometry(QtCore.QRect(300, 130, 114, 32))
        self.btnSignal.setObjectName("btnSignal")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 62, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 62, 16))
        self.label_2.setObjectName("label_2")
        self.lvSignal = QtWidgets.QListWidget(Form)
        self.lvSignal.setGeometry(QtCore.QRect(310, 160, 141, 101))
        self.lvSignal.setObjectName("lvSignal")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnCalc.setText(_translate("Form", "Call Function"))
        self.btnProcess.setText(_translate("Form", "Process"))
        self.btnSignal.setText(_translate("Form", "Signal!!"))
        self.label.setText(_translate("Form", "Number1"))
        self.label_2.setText(_translate("Form", "Number2"))


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
        Form.resize(400, 300)
        self.N1 = QtWidgets.QTextEdit(Form)
        self.N1.setGeometry(QtCore.QRect(50, 40, 104, 79))
        self.N1.setObjectName("N1")
        self.N2 = QtWidgets.QTextEdit(Form)
        self.N2.setGeometry(QtCore.QRect(220, 40, 104, 79))
        self.N2.setObjectName("N2")
        self.btnCalc = QtWidgets.QPushButton(Form)
        self.btnCalc.setGeometry(QtCore.QRect(140, 220, 114, 32))
        self.btnCalc.setObjectName("btnCalc")
        self.RESULT = QtWidgets.QTextEdit(Form)
        self.RESULT.setGeometry(QtCore.QRect(140, 120, 104, 79))
        self.RESULT.setReadOnly(True)
        self.RESULT.setObjectName("RESULT")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnCalc.setText(_translate("Form", "PushButton"))


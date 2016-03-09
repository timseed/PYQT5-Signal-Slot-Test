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
        self.N1 = QtWidgets.QPlainTextEdit(Form)
        self.N1.setGeometry(QtCore.QRect(70, 50, 104, 79))
        self.N1.setObjectName("N1")
        self.N2 = QtWidgets.QTextEdit(Form)
        self.N2.setGeometry(QtCore.QRect(240, 50, 104, 79))
        self.N2.setObjectName("N2")
        self.ANS = QtWidgets.QTextEdit(Form)
        self.ANS.setGeometry(QtCore.QRect(100, 180, 231, 79))
        self.ANS.setReadOnly(True)
        self.ANS.setObjectName("ANS")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(150, 140, 114, 32))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addButton.setText(_translate("Form", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


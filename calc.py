from PyQt5 import QtCore, QtGui, QtWidgets
from calcui import Ui_Form

class calc(Ui_Form):

    def __init__(self,*argv,**argvw):
        junk=1

    def setupUi(self,*argv,**argvw):
        super(calc,self).setupUi(*argv,**argvw)
        self.N1.setText("123")
        self.N2.setText("333")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = calc()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


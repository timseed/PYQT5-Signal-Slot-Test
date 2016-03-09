
from PyQt5 import QtCore, QtGui, QtWidgets
from calcui import Ui_Form 

class calc(Ui_Form):

    def __init__(self,*args,**kwargs):
       super(Ui_Form, self).__init__(*args, **kwargs)
       junk=1 
       self.myinit()

    def myinit(self,*args,**kwargs):
       print("My Init called")
       self.N1.setText("30")
       self.N2.setText("30")

    def add(self):
        x = int(self.N1.text())
        y = int(self.N2.text())
        self.ANS.setText(str(x + y))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = calc()
    ui.setupUi(Form)
    print("Showing the form")
    Form.show()
    sys.exit(app.exec_())

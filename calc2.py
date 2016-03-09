

from PyQt5 import QtCore, QtGui, QtWidgets
import sys # We need sys so that we can pass argv to QApplication
from calcui import Ui_Form 

class calc(Ui_Form):
    def __init__(self, *kargs,**kwargs):
        super(Ui_Form, self).__init__(*kargs,**kwargs)
        #self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = calc()
    form.show()
    app.exec_()

if __name__=="__main__":
   main()

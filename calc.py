from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import *
from calcui import Ui_Form
import threading
import time

class Communicate(QtWidgets.QWidget):
    """
    Small Class based on a Widget
    It's only purpose is to contain a signal object
    """
    sig = QtCore.pyqtSignal()

class calc(Ui_Form):
    """
    MycCalc implementation
    This inherits from the ClassUI which was created in Qt Designer
    """

    def __init__(self,*argv,**argvw):
        """
        Initialize the Calc class, creating a Communicate object
        :param argv:
        :param argvw:
        :return:
        """
        self.c=Communicate()

    def setupUi(self,*argv,**argvw):
        """
        Setup the "wiring" in the GUI
        This should not add new widgets to the UI.
        We connect widgets to functions
        and signals to slots.

        It is important to call the base method also

        :param argv:
        :param argvw:
        :return:
        """
        super(calc,self).setupUi(*argv,**argvw)
        self.N1.setText("123")
        self.N2.setText("333")
        self.btnCalc.clicked.connect(self.chk_fun)
        self.btnProcess.clicked.connect(self.start_worker)
        self.btnSignal.clicked.connect(self.sendSignal)
        self.c.sig.connect(self.hi_slot)

    def chk_fun(self):
        """
        This is called from a Straight Button
        It it connected up via

        self.btnCalc.clicked.connect(self.chk_fun)

        :return:
        """
        a=int(self.N1.toPlainText())
        b=int(self.N2.toPlainText())
        self.RESULT.setText(str(a+b))
        print("chk fun")


    def sendSignal(self):
        """
        This sends the signal !!
        :return:
        """
        self.c.sig.emit()


    def start_worker(self):
        """
        This is called from a Button - the wiring is

        self.btnProcess.clicked.connect(self.start_worker)

        This creates a thread and runs the method worker

        :return:
        """
        print("Process")
        threading.Thread(target=self.worker, name="_proc").start()


    def worker(self):
        """
        This is the code that the worker thread will run

        :return:
        """
        for i in range(10):
            print("Worker %d"%i)
            time.sleep(1)

    def hi_slot(self):
        """
        A Slot which will receive the signal
        the signal is sent from a button -

        This is wired by
        self.c.sig.connect(self.hi_slot)

        :return:
        """
        print("hi signal received")
        item = QListWidgetItem("Hi Slot")
        self.lvSignal.addItem(item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = calc()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from calcui import Ui_Form
import time


class Communicate(QtCore.QObject):
    """
    Small Class based on a Widget
    It's only purpose is to contain a signal object
    Note: Type QObject
    """
    sig = QtCore.pyqtSignal(object)

class qworker(QThread):

    def __init__(self,*argv,**argvw):
        super(qworker, self).__init__(*argv,**argvw)
        print("qworker init")
        self.c=Communicate()


    def run(self):
        for i in range(4):
            print("Worker %d"%i)
            self.c.sig.emit("Worker "+str(i))
            time.sleep(1)
        self.c.sig.emit("Worker Done")
        print("Worker done")

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

        super(self.__class__, self).__init__()
        self.c=Communicate()
        #self.workerthread=QThread()

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
        Needs a Parameter now...
        :return:
        """
        self.c.sig.emit("Button")

    def start_worker(self):
        """
        This is called from a Button - the wiring is
        This creates a qthread and runs the method worker
        The worker has been connected to a slot here - so when the worker emit the main gui is updated
        :return:
        """
        print("Process")
        #Create Class based on QThread
        self.worker=qworker()
        # Next we need to connect the events from that thread to functions we want
        # to be run when those signals get fired
        self.worker.c.sig.connect(self.hi_slot)
        #start links to qworker.run method
        self.worker.start()

    def Non_SIGNAL_worker(self):
        """
        This is the code that the worker thread will run
        However this code can not send SIGNALS - or more accuratly
        SIGNALS sent by this code will not go to a slot

        This code currently not used

        :return:
        """

        workerC=Communicate()
        for i in range(10):
            print("Worker %d"%i)
            time.sleep(1)

    def hi_slot(self,data):
        """
        A Slot which will receive the signal
        the signal is sent from a button -

        This is wired by
        self.c.sig.connect(self.hi_slot)

        :return:
        """
        print("hi signal received")
        item = QListWidgetItem(data)
        self.lvSignal.addItem(item)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = calc()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


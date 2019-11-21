import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtCore import QSize 

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300,200))
        self.setWindowTitle("PyQt Button Example - pythonprogramminglanguage.com")

        pybutton = QPushButton('Show Messagebox', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,64)
        pybutton.move(50,50)

    def clickMethod(self):
        QMessageBox.about(self, "PyQt MessageBox", "Close me!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
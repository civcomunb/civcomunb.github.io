from PyQt4 import QtGui
import sys
from Diagram import viga

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        mainwidget = MainWidget(self)
        self.setCentralWidget(mainwidget)

        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('CivCom Diagram Calculator')

        self.show()


class MainWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)

        self.lb1 = QtGui.QLabel('Carga Aplicada (kN/m)', self)
        self.le1 = QtGui.QLineEdit(self)

        self.lb2 = QtGui.QLabel('Comprimento da Viga (m)', self)
        self.le2 = QtGui.QLineEdit(self)

        self.btn = QtGui.QPushButton('Calcular', self)
        self.btn.clicked.connect(self.calcular)


        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.lb1, 1, 1)
        layout.addWidget(self.le1, 1, 2)
        layout.addWidget(self.lb2, 2, 1)
        layout.addWidget(self.le2, 2, 2)
        layout.addWidget(self.btn, 3, 1, 1, 2)

        self.setLayout(layout)

    def calcular(self):
        q = float(self.le1.text())
        l = float(self.le2.text())
        viga(q, l)

def main():
    app = QtGui.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())

main()
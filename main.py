import matplotlib.pyplot as plt
import func as fn
from PySide2 import QtCore, QtGui, QtWidgets
import sys
from untitled import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.textEdit.setOverwriteMode(True)
ui.textEdit_2.setOverwriteMode(True)
MainWindow.show()

def chek(string):
    num = 0
    for i in string:
        if '0' <= i <= '9':
            num += 1
    if num == len(string):
        return True
    else:
        return False

def draw():
    dice = 0
    sides = 0
    if chek(ui.textEdit.toPlainText()) != True and chek(ui.textEdit_2.toPlainText()) != True:
        ui.textEdit.clear()
        ui.textEdit_2.clear()
    else: 
        dice = int(ui.textEdit.toPlainText())
        sides = int(ui.textEdit_2.toPlainText())
        probs = []
        targets = [i for i in range(dice, dice*sides + 1)]
        for i in range(len(targets)):
            probs.append(fn.probability(dice,sides,targets[i])) 
        plt.figure(1)
        plt.bar(targets,probs)
        plt.show()

ui.pushButton.clicked.connect(draw)
sys.exit(app.exec_())
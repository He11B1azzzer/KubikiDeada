import matplotlib.pyplot as plt
import func as fn
from PySide2 import QtCore, QtGui, QtWidgets
import sys
from untitled import Ui_MainWindow
import os.path

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
        filename = str(dice) + "d" + str(sides) + "s" + ".txt"
        if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), ".\logs",filename)) == False:
            f = open(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), ".\logs",filename), "w")
            for i in range(len(probs)):
                f.write("\n")
                f.write(str(targets[i]))
                f.write("             ")
                f.write(str(probs[i]))
                f.write("\n")
            f.close()
        plt.figure("График для числа кубиков {0} с числом сторон равным {1} каждый".format(dice,sides))
        plt.bar(targets,probs)
        plt.show()


ui.pushButton.clicked.connect(draw)
sys.exit(app.exec_())
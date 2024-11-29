# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QPropertyAnimation, QLine, QPoint

from Tic_Tac_Toe import Tic_Tac_Toe
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, game,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.game = game
        self.btn = [[None for _ in range(game.col)] for _ in range(game.row)]
        self.line = QLine(QPoint(0,0), QPoint(0,0))
        self.anim = QPropertyAnimation(self, b"endLine")

        self.btn[0][0] = self.ui.btn_00
        self.btn[0][1] = self.ui.btn_01
        self.btn[0][2] = self.ui.btn_02
        self.btn[1][0] = self.ui.btn_10
        self.btn[1][1] = self.ui.btn_11
        self.btn[1][2] = self.ui.btn_12
        self.btn[2][0] = self.ui.btn_20
        self.btn[2][1] = self.ui.btn_21
        self.btn[2][2] = self.ui.btn_22
        for i in range(game.row):
            for j in range(game.col):
                self.btn[i][j].clicked.connect(lambda checked, row=i, col=j: self.on_btn_click(row, col))

    def on_btn_click(self, row, col):
        if(game.map[row][col] == 2):
            if game.who == 0:
                self.btn[row][col].setText('O')
            else :
                self.btn[row][col].setText('X')
        result = game.action(row, col)
        if result != None:
            winner = result[0]
            cal = lambda point : ((point + 1) * 100) / 2
            startPoint = QPoint(cal(result[1][0]), cal(result[1][1]))
            endPoint = QPoint(cal(result[2][0]), cal(result[2][1]))

            self.anim.setDuration(1000)
            self.anim.setStartValue(startPoint)
            self.anim.setEndValue(endPoint)
            self.anim.start()
            endMessage = QMessageBox(self)
            text = "player" + str(winner + 1) + " wins"
            endMessage.setText(text)
            endMessage.show()

    def endLine(self, value):
        self.line.setP2(value)
        self.update()
        return self.line.p2()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Tic_Tac_Toe()
    widget = Widget(game)
    widget.show()
    sys.exit(app.exec())

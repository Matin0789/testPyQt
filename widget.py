# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

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
        game.action(row, col)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Tic_Tac_Toe()
    widget = Widget(game)
    widget.show()
    sys.exit(app.exec())

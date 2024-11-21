# This Python file uses the following encoding: utf-8


class Tic_Tac_Toe():
    def __init__(self):
        self.playerCount = 2
        self.col = 3
        self.row = 3
        self.map = [[2 for _ in range(self.col)] for _ in range(self.row)]
        self.who = 0

    def action(self, row, col):
        if not(0 <= row < self.row) or not(0 <= col < self.col):
            raise Exception("row or col is out of range")

        if 0 <= self.who < self.playerCount:
            if(self.map[row][col] == 2):
                self.map[row][col] = self.who
                self.who = (self.who + 1) % 2
        else:
            raise Exception("invalid player")
    def check_end():
        pass

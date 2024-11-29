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
                who = self.who
                self.who = (self.who + 1) % 2
                row1 = (row + 1) % self.row
                row2 = (row + 2) % self.row
                col1 = (col + 1) % self.col
                col2 = (col + 2) % self.col

                if self.map[row][col] == self.map[row1][col] and self.map[row][col] == self.map[row2][col] and self.map[row1][col] == self.map[row2][col]:
                    return [who, (0,col), (2,col)]
                elif self.map[row][col] == self.map[row][col1]  and self.map[row][col] == self.map[row][col2] and self.map[row][col1] == self.map[row][col2]:
                    return [who, (row,0), (row,2)]
                elif self.map[0][0] == self.map[1][1] == self.map[2][2] == who:
                    return [who, (0,0), (2,2)]
                elif self.map[0][2] == self.map[1][1] == self.map[2][0] == who:
                    return [who, (0,2), (2,0)]
                else:
                    return None
        else:
            raise Exception("invalid player")



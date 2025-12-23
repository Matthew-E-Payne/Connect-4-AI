class Board:
    ROWS = 6
    COLS = 7

    def __init__(self):
        # init board state
        self.board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.heights = [0] * self.COLS
        self.lastMove = None

    def isValidMove(self, col):
        return self.heights[col] < self.ROWS

    def getValidMoves(self):
        pass

    def applyMove(self, col, player):
        pass

    def undoMove(self):
        pass

    def checkWinner(self):
        pass

    def is_full(self):
        pass

    def print(self):
        for i in range(self.COLS):
            print("\033[34m", i, " ", sep="", end="")         # Print the header numbers in blue
       
        print("\033[0m")                                      # Reset Color
        for row in self.board:
            beautify_row = []

            for value in row:
                if value == 1:
                    beautify_row.append("\033[31mX\033[0m")   # Red X
                elif value == -1:
                    beautify_row.append("\033[32mO\033[0m")   # Green O
                else:
                    beautify_row.append("-")

            print(" ".join(beautify_row))

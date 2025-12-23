from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 1
        self.over = False
        self.winner = None

    def make_move(self, col):
        pass

    def undo(self):
        pass

    def get_valid_moves(self):
        pass

    def is_over(self):
        pass

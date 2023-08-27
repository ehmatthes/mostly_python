from random import shuffle

class ChessBoard:

    def __init__(self, variant=""):
        self.variant = variant

        if self.variant == "fischer960":
            pieces = ["R", "N", "B", "Q", "K", "B", "N", "R"]
            shuffle(pieces)
            self.position = ''.join(pieces)
        else:
            self.position = "RNBQKBNR"

    def show_position(self):
        print(self.position)

board = ChessBoard(variant="fischer960")
board.show_position()
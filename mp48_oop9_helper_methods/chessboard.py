class ChessBoard:

    def __init__(self):
        self.position = "RNBQKBNR"

    def show_position(self):
        print(self.position)

board = ChessBoard()
board.show_position()
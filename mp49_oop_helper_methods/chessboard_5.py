from random import shuffle

class ChessBoard:

    def __init__(self, variant=""):
        self.variant = variant
        self.position = self._get_starting_position()

    def show_position(self):
        print(self.position)

    def _get_starting_position(self):
        if self.variant == "fischer960":
            return self._get_fischer960_position()
        else:
            return "RNBQKBNR"

    @staticmethod
    def _get_fischer960_position():
        pieces = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        shuffle(pieces)

        # Check that Bishops are on different colors.
        # Find Bishops in the list:
        bishop_indexes = [
            index
            for index, piece in enumerate(pieces)
            if piece == "B"
        ]
        # One Bishop must have an even index, and one
        #   an odd index. The sum of the indexes
        #   must be odd. Otherwise, call this
        #   method again to start over.
        if sum(bishop_indexes) % 2 == 0:
            return ChessBoard._get_fischer960_position()

        # Check that the King is between the Rooks.
        king_index = pieces.index("K")
        rook_indexes = [
            index
            for index, piece in enumerate(pieces)
            if piece == "R"
        ]
        # King can't be before the first Rook
        #   or after the second Rook.
        if ((king_index < rook_indexes[0]) or
                (king_index > rook_indexes[1])):
            return ChessBoard._get_fischer960_position()

        return ''.join(pieces)

board = ChessBoard(variant="fischer960")
board.show_position()
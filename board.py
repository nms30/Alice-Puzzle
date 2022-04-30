import random
from piece import Piece


class Board:
    """Information about the entire board"""
    def __init__(self, size):
        """Initialize Board object"""
        self.size = size
        piece_size = 600 / self.size
        self.spaces = [((300 + piece_size / 2) + piece_size * i, piece_size / 2 + piece_size * j)
                       for j in range(self.size) for i in range(self.size)]
        self.pieces = [0] * (self.size ** 2)

        available_spaces = self.spaces.copy()
        for i in range(self.size ** 2):
            j = random.randint(0, len(available_spaces) - 1)
            p = available_spaces.pop(j)
            self.pieces[i] = Piece(p[0], p[1], i)

    def check_win(self):
        """
        check if all pieces are in the right place
        :return: Boolean
        """
        for i in range(self.size ** 2):
            piece = self.pieces[i]
            space = self.spaces[i]
            if not piece.check_pos(space):
                break
        last_tag = 'piece' + str(self.size ** 2 - 1)
        return piece.check_pos(space) and piece.tag == last_tag

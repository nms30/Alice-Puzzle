import random
from piece import Piece


class Board:
    """Information about the entire board"""
    def __init__(self):
        """initialize board"""
        self.spaces = [(400 + 200 * i, 100 + 200 * j)
                       for j in range(3) for i in range(3)]
        self.pieces = [0] * 9

        available_spaces = self.spaces.copy()
        for i in range(9):
            j = random.randint(0, len(available_spaces) - 1)
            p = available_spaces.pop(j)
            self.pieces[i] = Piece(p[0], p[1], i)

    def check_win(self):
        """
        check if all pieces are in the right place
        :return: Boolean
        """
        for i in range(9):
            piece = self.pieces[i]
            space = self.spaces[i]
            if not piece.check_pos(space):
                break
        return piece.check_pos(space) and piece.tag == 'piece8'

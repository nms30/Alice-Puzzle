from tkinter import *
from board import Board


class Puzzle(Canvas):
    """store the Board and the Piece that is clicked on"""
    def __init__(self, parent, **kwargs):
        """Initialize Puzzle object"""
        super().__init__(parent, **kwargs)
        self.board = Board()
        self.selected_piece = None
        self.bind('<Button-1>', self.select_piece)

    def select_piece(self, e):
        """
        choose piece to move
        :param e: Event
        :return: None
        """
        for i in range(len(self.board.pieces)):
            piece = self.board.pieces[i]
            if abs(piece.x - e.x) < 45 and abs(piece.y - e.y) < 45:
                self.selected_piece = piece
                break
        if self.selected_piece:
            self.tag_raise(self.selected_piece.tag)
            self.tag_bind(self.selected_piece.tag,
                          '<B1-Motion>', self.move_piece)

    def move_piece(self, e):
        """
        move selected piece
        :param e: Event
        :return: None
        """
        x = self.selected_piece.x
        y = self.selected_piece.y
        self.move(self.selected_piece.tag, e.x - x, e.y - y)
        i = self.board.pieces.index(self.selected_piece)
        self.board.pieces[i].move(e.x, e.y)
        self.tag_bind(self.selected_piece.tag,
                      '<B1-ButtonRelease>', self.release_piece)

    def release_piece(self, e):
        """
        move piece to the closest space on board
        :param e: Event
        :return: None
        """
        x, y = e.x, e.y
        for pos in self.board.spaces:
            if abs(pos[0] - e.x) < 45 and abs(pos[1] - e.y) < 45:
                x, y = pos[0], pos[1]
                self.move(self.selected_piece.tag, x - e.x, y - e.y)
                break
        i = self.board.pieces.index(self.selected_piece)
        self.board.pieces[i].move(x, y)
        if self.board.check_win():
            self.win_message()

    def win_message(self):
        """
        show win message
        :return: None
        """
        self.create_text(150, 300, text='You did it!',
                         font=('Helvetica', '40', 'bold'))

class Piece:
    """Location and tag of a puzzle piece"""
    def __init__(self, x, y, num):
        """
        Initialize Piece object.
        :param x: x coordinate of the center of the piece
        :param y: y coordinate of the center of the piece
        :param num: piece number; unique to piece
        """
        self.x = x
        self.y = y
        self.tag = 'piece' + str(num)

    def move(self, x, y):
        """
        change location of piece
        :param x: x coordinate of mouse
        :param y: y coordinate of mouse
        :return: None
        """
        self.x = x
        self.y = y

    def check_pos(self, correct_pos):
        """
        check if piece is in the right place
        :param correct_pos: Tuple
        :return: Boolean
        """
        return self.x == correct_pos[0] and self.y == correct_pos[1]

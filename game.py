from tkinter import *
from PIL import ImageTk, Image
from puzzle import Puzzle


def divided_image(s):
    """
    divide image into nine parts
    :return: list of images
    """
    piece_size = 600 / s
    pictures = []
    img = Image.open('HeartsCastle.png')
    if img.size[0] != img.size[1]:
        size = min(img.size)
        img = img.crop((0, 0, size, size))
    img = img.resize((600, 600), Image.Resampling.LANCZOS)
    for i in range(s):
        for j in range(s):
            piece_img = img.crop((j * piece_size, i * piece_size,
                                  j * piece_size + piece_size, i * piece_size + piece_size))
            piece_img = ImageTk.PhotoImage(piece_img)
            pictures.append(piece_img)
    return pictures


def get_size():
    size = 0
    while size < 2 or size > 5:
        size = int(input("Enter a number from 2 through 5 for the "
                         "dimensions of the square puzzle: "))
    return size


def run_puzzle():
    """
    run the whole puzzle
    :return: None
    """
    size = get_size()
    root = Tk()
    root.geometry('900x600')
    puzzle = Puzzle(size, root, width=900, height=600, bg='light blue')
    puzzle.pack()
    puzzle.create_text(150, 70, text='Drag and drop the pieces into place.\n'
                                      'Use this area for extra space.',
                       font=('Helvetica', '13', 'italic'))

    pictures = divided_image(size)
    for i in range(size ** 2):
        piece = puzzle.board.pieces[i]
        piece_pic = pictures[i]
        puzzle.create_image(piece.x, piece.y, image=piece_pic, tags=piece.tag)

    root.mainloop()

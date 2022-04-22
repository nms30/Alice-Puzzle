from tkinter import *
from PIL import ImageTk, Image
from puzzle import Puzzle


def divided_image():
    """
    divide image into nine parts
    :return: list of images
    """
    pictures = []
    img = Image.open('C:\\Users\\noram\\Pictures\\castle.png')
    if img.size[0] != img.size[1]:
        size = min(img.size)
        img = img.crop((0, 0, size, size))
    img = img.resize((600, 600), Image.Resampling.LANCZOS)
    for i in range(3):
        for j in range(3):
            piece_img = img.crop((j * 200, i * 200, j * 200 + 200, i * 200 + 200))
            piece_img = ImageTk.PhotoImage(piece_img)
            pictures.append(piece_img)
    return pictures


def run_puzzle():
    """
    run the whole puzzle
    :return: None
    """
    root = Tk()
    root.geometry('800x600')
    puzzle = Puzzle(root, width=800, height=600, bg='light blue')
    puzzle.pack()

    pictures = divided_image()
    for i in range(9):
        piece = puzzle.board.pieces[i]
        piece_pic = pictures[i]
        puzzle.create_image(piece.x, piece.y, image=piece_pic, tags=piece.tag)
    root.mainloop()

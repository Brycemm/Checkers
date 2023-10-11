if __name__ == "__main__":
    print("This is not intended to be run as main.")

from numpy import random


# first function
def build_board(size):
    board = random.choice(['empty', 'red', 'black'], size=(size, size))
    return board


# second function
def get_count(board, color):
    return(board == color).sum()

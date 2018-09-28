"""
Defines a state in a game of chess
"""

import GenerateMoves as GM

def parse(initial_state_string):
    """Translates a nice looking string version of the
    # chess board into a 2D array with integers in order to be more functional.
    
    :param initial_state_string: intial state that is viusally pleasing
    :type initial_state_string: string
    :return: more functional board
    :rtype: 2D integer array
    """

    b = [[0, 0, 0, 0, 0, 0, 0, 0] for r in range(8)] #build 2D array
    rs9 = initial_state_string.split("\n")
    rs8 = rs9[1:]  # eliminate the empty first item.
    for iy in range(8):
        rss = rs8[iy].split(' ')
        for jx in range(8):
            b[iy][jx] = BOARD_PIECES_NUMBERS[rss[jx]]
    return b



# ODDS = lowercase letters = Black (Player 1)
BLACK = 1
WHITE = 0
BOARD_PIECES_NUMBERS = {'-':0, 
'p':(GM.PAWN) ,'P':(GM.PAWN + 1), 
'h':(GM.KNIGHT) ,'H':(GM.KNIGHT + 1) ,
'b':(GM.BISHOP), 'B':(GM.BISHOP + 1), 
'r':(GM.ROOK), 'R':(GM.ROOK + 1) , 
'q':(GM.QUEEN), 'Q':(GM.QUEEN + 1), 
'k':(GM.KING), 'K':(GM.KING + 1)}

NUMBER_TO_PIECE = {0:'-', 
(GM.PAWN):'p' ,(GM.PAWN + 1):'P', 
(GM.KNIGHT): 'h' , (GM.KNIGHT + 1): 'H' ,
(GM.BISHOP):'b', (GM.BISHOP + 1): 'B', 
(GM.ROOK):'r', (GM.ROOK + 1):'R' , 
(GM.QUEEN): 'q', (GM.QUEEN + 1):'Q', 
(GM.KING):'k', (GM.KING + 1):'K'}


INITIAL_BOARD = parse (
'''
r h b q k b h r
p p p p p p p p
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
P P P P P P P P
R H B Q K B H R
'''    
)


def who(piece):
    """
    Determines the piece's player or "color"
    :param piece: number of the piece (int)
    :return: the player of the piece (-1 for empty, 0 or 1)
    """
    if piece is not 0:
        return piece % 2
    else:
        return -1




class ChessState:
    def __init__(self, old_board=INITIAL_BOARD, whose_move=WHITE):
        new_board = [r[:] for r in old_board]  # Deeply copy the board.
        self.board = new_board
        self.whose_move = whose_move

    def __repr__(self):  # Produce an ASCII display of the state.
        s = ''
        for r in range(8):
            for c in range(8):
                s += NUMBER_TO_PIECE[self.board[r][c]] + " "
            s += "\n"
        if self.whose_move == WHITE:
            s += "WHITE's move"
        else:
            s += "BLACK's move"
        s += "\n"

        return s

    def __eq__(self, other):
        if not (type(other) == type(self)):
            return False
        if self.whose_move != other.whose_move:
            return False
        try:
            b1 = self.board
            b2 = other.board
            for i in range(8):
                for j in range(8):
                    if b1[i][j] != b2[i][j]:
                        return False
            return True
        except Exception as e:
            return False


def test_starting_board():
    init_state = ChessState(INITIAL_BOARD, WHITE)
    print(init_state)


if __name__ == "__main__":
    test_starting_board()

"""
A Chess playing agent which uses a smart heuristic and Zobrist hashing to determine the next move
Uses information gathered from the game to comment on the game to its opponent
"""

import random
import ChessState as CS
import GenerateMoves as MOVES
import AlphaBeta as AB
import EvaluatePiece as EVAL
PLAYERS_TURN = None


import EvaluatePiece as EP


def initPlayersTurnsVar(curr_state):
    global PLAYERS_TURN

    if curr_state.whose_move == 0:
        PLAYERS_TURN = 0
        print('Setting PLAYERS TURN TO ---- ' ,PLAYERS_TURN)
    else:
        PLAYERS_TURN = 1
        print('Setting PLAYERS TURN TO ---- ' ,PLAYERS_TURN)


def make_move(current_state):
    global PLAYERS_TURN   
    PLAYERS_TURN = current_state.whose_move
    print("EVAL: " + str(EVAL.eval_board(current_state.board, current_state.whose_move)))
    print("Trying to move player " , PLAYERS_TURN)

    MOVES.PLAYERS_TURN = PLAYERS_TURN
    new_state = CS.ChessState(current_state.board)

    new_state.whose_move = 1 - current_state.whose_move
    move_list = MOVES.generate_moves(PLAYERS_TURN, current_state.board)
    

    # [(old_pos, new_pos), new_state] 

    print('Calling ALPHA BETA')

    best_move = AB.runAlphaBeta(PLAYERS_TURN, current_state, 2)
    temp_move = best_move[1]
    best_state = temp_move[1]
    # print("EVAL: " + str(EVAL.eval_board(best_state.board, best_state.whose_move)) + ", " + str(temp_move))

    # print('hey check for correct form')
    # print(best_move[1])

    return best_move[1]

    try:
        print("Generating a move")
        move = random.choice(moves_list)
        move_touple = (move[0], move[1])
        update_board((new_state, move_touple))
        return [move_touple, new_state]
    except:
        print("Movement failed")
        pass


def update_board(new_state, move):
    old_pos = move[0]
    new_pos = move[1]
    piece = new_state.board[old_pos[0]][old_pos[1]]

    new_state.board[old_pos[0]][old_pos[1]] = 0
    new_state.board[old_pos[0]][new_pos[1]] = piece


def prepare():
    pass


def dumb_heuristic(board, player):
    """
    Loops through the board and generates a sum of all the pieces weights
    param board: 2D list of ints representation of board
    return: a board score (int)
    """
    count = 0
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != 0:
                if piece % 2 is not player:
                    count -= (piece - player)
                else:
                    count += (piece - player)
    return count

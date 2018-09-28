"""
Generates all the possible moves for a given state in a game of chess
"""

import ChessState as CS

"""
board accesses --> board[row][col]
a move is defined as a list of a tuple of tuples and a state [((old_pos),(new_pos)), new_state]
"""

# Weights of all the pieces (also used for identification)
# White is EVENS (PLAYER 0) and Black is ODDS (PLAYER 1)
PAWN = 100
ROOK = 500
KNIGHT = 320
BISHOP = 330
QUEEN = 980
KING = 40000

PLAYER = None


def generate_moves(player, board):
    """
    Generates all the moves for a given |board| and current |player|
    :param player: the current player making the move (either 0 or 1)
    :param board: current configuration of the board
    :return: a list of all possible moves
    """
    global PLAYER
    PLAYER = player
    move_list = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if CS.who(board[row][col]) == PLAYER:
                piece_list = find_moves_for_piece((row, col), board)
                move_list += piece_list
    
    return move_list


def find_moves_for_piece(piece_pos, board):
    """
    Finds all the moves possible for a given piece
    :param piece_pos: The position of the piece to be inspected represented by a tuple (row, col)
    :param board: current configuration of the board
    :return: a list of all moves possible by that piece
    """
    return_list = []
    piece = board[piece_pos[0]][piece_pos[1]]
    piece -= (piece % 2)
    if piece == PAWN:
        generate_pawn(piece_pos, board, return_list)
    if piece == ROOK:
        generate_rook(piece_pos, board, return_list)
    if piece == KNIGHT:
        generate_knight(piece_pos, board, return_list)
    if piece == BISHOP:
        generate_bishop(piece_pos, board, return_list)
    if piece == QUEEN:
        generate_queen(piece_pos, board, return_list)
    if piece == KING:
        generate_king(piece_pos, board, return_list)
    
    return return_list


def generate_pawn(pos, board, list):
    """
    Generates all possible moves for a pawn at the given position
    :param pos: position of the pawn represented by a tuple (row, col)
    :param board: current state of the board
    :param list: list of possible moves which will be added to
    :return: none
    """
    """
    Pawns can move one ahead, or two ahead if they are in their initial position
    They can capture by moving to the top left or top right
    We are ignoring the 'En passant' rule
    """
    if PLAYER == 0:
        # Try moving one space forward
        top_pos = (pos[0] + 1, pos[1])
        if legal_move(top_pos):
            top_piece = board[top_pos[0]][top_pos[1]]
            if top_piece == 0:
                move_pos = (pos, top_pos)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)
                
        # If in the starting position and you can move two spaces forward
        if pos[0] == 1:
            top_pos = (pos[0] + 2, pos[1])
            top_piece = board[top_pos[0]][top_pos[1]]
            if top_piece == 0:
                move_pos = (pos, top_pos)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)
        
        # Check all the kill moves for White pawns
        kill_pos1 = (pos[0] + 1, pos[1] + 1)
        kill_pos2 = (pos[0] + 1, pos[1] - 1)
        if legal_move(kill_pos1):
            kill_piece1 = board[kill_pos1[0]][kill_pos1[1]]
            if kill_piece1 % 2 == 1:
                move_pos = (pos, kill_pos1)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)
        if legal_move(kill_pos2):
            kill_piece2 = board[kill_pos2[0]][kill_pos2[1]]
            if kill_piece2 % 2 == 1:
                move_pos = (pos, kill_pos2)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)
                
    if PLAYER == 1:
        # Try moving one space forward
        top_pos = (pos[0] - 1, pos[1])
        if legal_move(top_pos):
            top_piece = board[top_pos[0]][top_pos[1]]
            if top_piece == 0:
                move_pos = (pos, top_pos)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)
                
        # If in the starting position and you can move two spaces forward
        if pos[0] == 6:
            top_pos = (pos[0] - 2, pos[1])
            top_piece = board[top_pos[0]][top_pos[1]]
            if top_piece == 0:
                move_pos = (pos, top_pos)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)
        
        # Check all the kill moves for Black pawns
        kill_pos1 = (pos[0] - 1, pos[1] + 1)
        kill_pos2 = (pos[0] - 1, pos[1] - 1)
        if legal_move(kill_pos1):
            kill_piece1 = board[kill_pos1[0]][kill_pos1[1]]
            if kill_piece1 % 2 == 0 and kill_piece1 is not 0:
                move_pos = (pos, kill_pos1)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)
        if legal_move(kill_pos2):
            kill_piece2 = board[kill_pos2[0]][kill_pos2[1]]
            if kill_piece2 % 2 == 0 and kill_piece2 is not 0:
                move_pos = (pos, kill_pos2)
                move = [move_pos, generate_state(move_pos, board)]
                list.append(move)


def generate_knight(pos, board, list):
    directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
    for direction in directions:
        directional_moves(pos, board, direction, 1, list)


def generate_king(pos, board, list):
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        directional_moves(pos, board, direction, 1, list)


def generate_rook(pos, board, list):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        directional_moves(pos, board, direction, 8, list)


def generate_bishop(pos, board, list):
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for direction in directions:
        directional_moves(pos, board, direction, 8, list)


def generate_queen(pos, board, list):
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        directional_moves(pos, board, direction, 8, list)


def directional_moves(pos, board, direction, step_size,  list):
    """
    Generates moves in a given direction and adds them to the given list
    :param pos: starting position of the piece given as a tuple (row, col)
    :param board: current state of the board given by a 2D array of ints
    :param direction: tuple indicating direction of movement
    :param step_size: max number of steps to take in the given direction
    :param list: list of moves to be appended to
    :return: none
    """
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if not legal_move(new_pos):
        return
    new_piece = board[new_pos[0]][new_pos[1]]
    found_enemy = False
    while legal_move(new_pos) and (new_piece == 0 or new_piece % 2 != PLAYER) and step_size != 0:
        if new_piece % 2 != PLAYER and new_piece != 0:
            found_enemy = True
        move_pos = (pos, new_pos)
        move = [move_pos, generate_state(move_pos, board)]
        list.append(move)
        if found_enemy:
            break
        new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
        if not legal_move(new_pos):
            break
        new_piece = board[new_pos[0]][new_pos[1]]
        step_size -= 1


def legal_move(pos):
    """
    Checks if a given move is within the bounds of the board
    :param pos: position of move as represented by a tuple [row, col]
    :return: True or false
    """
    if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
            return True
    else:
        return False

def generate_state(move, board):
    """
    Applies a move to the given board and returns the resulting state
    param move: tuple of tuples ((old_pos), (new_pos))
    param board: 2D list representation of the board
    return: new ChessState
    """
    old_pos = move[0]
    new_pos = move[1]
    piece_val = board[old_pos[0]][old_pos[1]]
    if PLAYER is 0:
        new_who = 1
    else: 
        new_who = 0
    new_state = CS.ChessState(board, new_who)
    new_state.board[new_pos[0]][new_pos[1]] = piece_val
    new_state.board[old_pos[0]][old_pos[1]] = 0
    return new_state

"""
Used to evaluate the heuristic value of a given board
Call eval_board(board, player) to evaluate your board


HOW EVALUATION WORKS:

Eval_board loops through every piece on the board and assigns it a score depending on how good its position is
There are three factors that affect whether a piece is in a good position or not:
	Weight tables: Each piece has positions on the board that it should generally strive for. 
		On the weight tables each position is assigned a score based on how advantageous it is for the given piece
	Defenders: This checks whether a piece is defended, and encourages pieces to be defended by pieces that are weaker than themselves
		For example, this algorithm would prefer a bishop were defended by a pawn rather than a queen
	Attackers: This checks whether a piece is attacked. This algorithm discourages being attacked by a piece weaker than yourself.
		For example, being attacked by a piece stronger than yourself is mildly discouraged, 
		but being attacked by a piece weaker than yourself is strongly discouraged 
In addition to this, the pieces individual weights are added to the sum (this is not the same as the weight table)
Finally, there are a couple final calculation rules:
	if the Defenders value is smaller than the attackers value, then we highly discourage this situation by 
		multiplying the attacker value by 2 and subtracting it from the overall score
	we gain an extra bonus if we still own two bishops, and an added bonus if the enemy has less than two bishops
"""

import ChessState as CS
import GenerateMoves as MOVES

PLAYER = 0

pawn_weights = (
[[ 0,  0,  0,  0,  0,  0,  0,  0],
 [50, 50, 50, 50, 50, 50, 50, 50],
 [10, 10, 20, 30, 30, 20, 10, 10],
 [ 5,  5, 10, 27, 27, 10,  5,  5],
 [ 0,  0,  0, 25, 25,  0,  0,  0],
 [ 5, -5,-10,  0,  0,-10, -5,  5],
 [ 5, 10, 10,-25,-25, 10, 10,  5],
 [ 0,  0,  0,  0,  0,  0,  0,  0]])

knight_weights = (
[[-50,-40,-30,-30,-30,-30,-40,-50],
 [-40,-20,  0,  0,  0,  0,-20,-40],
 [-30,  0, 10, 15, 15, 10,  0,-30],
 [-30,  5, 15, 20, 20, 15,  5,-30],
 [-30,  0, 15, 20, 20, 15,  0,-30],
 [-30,  5, 10, 15, 15, 10,  5,-30],
 [-40,-20,  0,  5,  5,  0,-20,-40],
 [-50,-40,-20,-30,-30,-20,-40,-50]])

bishop_weights = ( 
[[-20,-10,-10,-10,-10,-10,-10,-20],
 [-10,  0,  0,  0,  0,  0,  0,-10],
 [-10,  0,  5, 10, 10,  5,  0,-10],
 [-10,  5,  5, 10, 10,  5,  5,-10],
 [-10,  0, 10, 10, 10, 10,  0,-10],
 [-10, 10, 10, 10, 10, 10, 10,-10],
 [-10,  5,  0,  0,  0,  0,  5,-10],
 [-20,-10,-40,-10,-10,-40,-10,-20]])

king_table = (
[[-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-30,-40,-40,-50,-50,-40,-40,-30],
 [-20,-30,-30,-40,-40,-30,-30,-20],
 [-10,-20,-20,-20,-20,-20,-20,-10], 
 [ 20, 20,  0,  0,  0,  0, 20, 20],
 [ 20, 30, 10,  0,  0, 10, 30, 20]])


def eval_board(board, player):
	"""
	Produces a heuristic value representing the quality of the board for the given player
	:param board: 2D list of ints representation of the current board
	:param player: integer representation of the player whose position is to be evaluated
	:return: integer representation of board quality
	"""
	global PLAYER
	PLAYER = player

	friend_bishop = 0
	enemy_bishop = 0
	board_count = 0
	enemy_king_pos = None
	friend_king_pos = None

	# For each piece on the board
	for row in range(8):
		for col in range(8):
			piece = board[row][col]
			# If piece is not 0
			if piece != 0:
				piece_player = piece % 2
				piece -= piece_player
				piece_pos = (row, col)

				if piece == MOVES.PAWN:
					piece_val = eval_pawn(piece_pos, board, piece_player)
				elif piece == MOVES.ROOK:
					piece_val = eval_rook(piece_pos, board, piece_player)
				elif piece == MOVES.KNIGHT:
					piece_val = eval_knight(piece_pos, board, piece_player)
				elif piece == MOVES.BISHOP:
					if piece_player is player:
						friend_bishop += 1
					else:
						enemy_bishop += 1
					piece_val = eval_bishop(piece_pos, board, piece_player)
				elif piece == MOVES.QUEEN:
					piece_val = eval_queen(piece_pos, board, piece_player)
				elif piece == MOVES.KING:
					piece_val = eval_king(piece_pos, board, piece_player)

				if piece_player is player:
					board_count += piece_val
				else:
					board_count -= piece_val
	if friend_bishop is 2:
		board_count += 10
	if enemy_bishop is 2:
		board_count -= 10
	board_count += check_king(board, player)
	return board_count


def check_king(board, player):
	for row in range(8):
		for col in range(8):
			piece = board[row][col]
			piece_player = piece % 2
			piece_val = piece - piece_player
			if piece_player is not player and piece_val is MOVES.KING:
				return 50000
	return 0

def eval_pawn(pos, board, player):
	score = MOVES.PAWN
	if player is 0:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += pawn_weights[eval_pos[0]][eval_pos[1]]
	score += eval_piece(pos, board, player)
	return score


def eval_rook(pos, board, player):
	score = MOVES.ROOK
	score += eval_piece(pos, board, player)
	return score


def eval_knight(pos, board, player):
	score = MOVES.KNIGHT
	if player is 0:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += knight_weights[eval_pos[0]][eval_pos[1]]
	score += eval_piece(pos, board, player)
	return score


def eval_bishop(pos, board, player):
	score = MOVES.BISHOP
	if player is 0:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += bishop_weights[eval_pos[0]][eval_pos[1]]
	score += eval_piece(pos, board, player)
	return score


def eval_queen(pos, board, player):
	score = MOVES.QUEEN
	score += eval_piece(pos, board, player)
	return score


def eval_king(pos, board, player):
	score = MOVES.KING
	if player is 0:
		eval_pos = (7 - pos[0], 7 - pos[1])
	else:
		eval_pos = pos
	score += king_table[eval_pos[0]][eval_pos[1]]
	score += eval_piece(pos, board, player)
	return score


def eval_piece(pos, board, player):
	"""
	Calculates a score based on wh, playerether a piece is attacked or defended. 
	Promotes being defended with no attackers.
	param pos: position of piece on board as a tuple of ints
	param board: current board configuration as a 2D array of ints
	return: the score depending on whether the piece is defended or attacked
	"""
	score = 0
	defended_val = is_defended(pos, board, player)
	attacked_val = is_attacked(pos, board, player)
	if defended_val < abs(attacked_val):
		score += 2 * attacked_val
	else:
		score += (defended_val + attacked_val)
	return score


def is_attacked(pos, board, player):
	"""
	Computes whether a piece is attacked by weaker pieces or not
	"""
	attacked_score = 0
	if player is 0:
		enemy = 1
	else:
		enemy = 0

	if player is 0:
		pawn_list = [(1, -1), (1, 1)]
	else:
		pawn_list = [(-1, -1), (-1, 1)]
	attacked_score -= check_defended_list(pawn_list, pos, board, enemy, MOVES.PAWN)

	knight_list = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
	attacked_score -= check_defended_list(knight_list, pos, board, enemy, MOVES.KNIGHT)

	bishop_list = []
	bishop_direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
	for direction in bishop_direction:
		directional_check(pos, board, direction, 8, bishop_list, enemy)
	attacked_score -= check_defended_list(bishop_list, pos, board, enemy, MOVES.BISHOP)

	rook_list = []
	rook_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	for direction in rook_direction:
		directional_check(pos, board, direction, 8, rook_list, enemy)
	attacked_score -= check_defended_list(rook_list, pos, board, enemy, MOVES.ROOK)

	queen_list = rook_list + bishop_list
	attacked_score -= check_defended_list(queen_list, pos, board, enemy, MOVES.QUEEN)

	king_list = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (0, -1)]
	attacked_score -= check_defended_list(king_list, pos, board, enemy, MOVES.KING)

	return attacked_score


def is_defended(pos, board, player):
	"""
	Computes whether a piece is defended by weaker pieces or not
	"""
	defended_score = 0
	if player is 0:
		pawn_list = [(-1, -1), (-1, 1)]
	else:
		pawn_list = [(1, -1), (1, 1)]
	defended_score += check_defended_list(pawn_list, pos, board, player, MOVES.PAWN)

	knight_list = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
	defended_score += check_defended_list(knight_list, pos, board, player, MOVES.KNIGHT)

	bishop_list = []
	bishop_direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
	for direction in bishop_direction:
		directional_check(pos, board, direction, 8, bishop_list, player)
	defended_score += check_defended_list(bishop_list, pos, board, player, MOVES.BISHOP)

	rook_list = []
	rook_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	for direction in rook_direction:
		directional_check(pos, board, direction, 8, rook_list, player)
	defended_score += check_defended_list(rook_list, pos, board, player, MOVES.ROOK)

	queen_list = rook_list + bishop_list
	defended_score += check_defended_list(queen_list, pos, board, player, MOVES.QUEEN)

	king_list = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (0, -1)]
	defended_score += check_defended_list(king_list, pos, board, player, MOVES.KING)

	return defended_score


def check_defended_list(defend_list, pos, board, player, piece):
	"""
	Check if a |piece| exists in the |defend_list| which is defending the piece at the given |pos|
	"""
	score = 0
	for temp_pos in defend_list:
		rel_pos = (pos[0] + temp_pos[0], pos[1] + temp_pos[1])
		if legal_move(rel_pos):
			rel_piece = board[rel_pos[0]][rel_pos[1]]
			if rel_piece is not 0 and rel_piece % 2 is player and rel_piece - (rel_piece % 2) is piece:
				score += compare_weight(pos, rel_pos, board)
	return score


def compare_weight(pos1, pos2, board):
	"""
	Compares the value of a defended piece to that of its defending piece and returns an int
	:param pos1: the position as a tuple of ints (int, int) of the defended piece
	:param pos2: the position as a tuple of ints (int, int) of the defending piece
	"""
	piece1 = board[pos1[0]][pos1[1]]
	piece2 = board[pos2[0]][pos2[1]]
	if piece1 > piece2:
		return 15
	elif piece2 > piece1:
		return 8
	else:
		return 0


def directional_check(pos, board, direction, step_size, list_var, limit_player):
	"""
	Generates a list of positions (tuples) along a set direction until it encounters a piece or the edge of the board
	step_size determines how many spaces in the given direction to look
	"""
	
	new_pos = (pos[0] + direction[0], pos[1] + direction[1])
	if not legal_move(new_pos):
		return
	new_piece = board[new_pos[0]][new_pos[1]]
	
	while legal_move(new_pos) and (new_piece == 0 or new_piece % 2 != limit_player) and step_size != 0:
		if new_piece % 2 == limit_player and new_piece != 0:
			list_var.append(new_pos)
			break
		
		new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
		if not legal_move(new_pos):
			return
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

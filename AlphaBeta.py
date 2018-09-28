import EvaluatePiece as EP
import GenerateMoves as MOVES
import Player01 as PLAYER
NUM_TIMES_PRUNED = 0

# ==================== DOCUMENTATION ====================
# old alpha beta: https://github.com/bwalchen/cse415_finalProject/blob/master/Mei_BC_Player.py


# -------- Summary --------
# EP.eval_board(board, player)
# ( board , 0 or 1)

# (current_state, whos turn it is)


# child_state = generate moves()

# for each child_state evaluate(child_state)



# ==================== CODE ====================

def runAlphaBeta(which_player_turn, curren_state, max_depth):
    """Helper method that kicks off alpha beta pruning and returns best option.
    
    :param which_player_turn: Who's turn is it.
    :type which_player_turn: Int, 0 or 1
    :param current_board: Current board
    :type current_board: [type]
    :param max_depth: How many layers deep into alpha beta do you wanna go?
    :type max_depth: Int
    :return: Returns best move.
    :rtype: tuple - (old position, new position)
    """

    return (alphabeta(curren_state, max_depth, -9999999, 9999999, True, which_player_turn))


# def alphabeta(node, depth_left, A, B, bool_maximizingPlayer):
def alphabeta(currentState, depth_left, A, B, bool_maximizingPlayer, player_number):
    """Finds the next best move to complete.
    
    :param node: oldpos, newpos, killpos
    :param depth_left: levels of depth left
    :type depth_left: int
    :param A: alpha, start with -9999999
    :param B: beta, start with 9999999
    :param bool_maximizingPlayer: is it maximizing turn
    :type bool_maximizingPlayer: boolean
    :return: heuristic, move
    """
    
    # base: no more tree discovering. Return the heuristic score for the given board state
    if (depth_left == 0):
        # return PLAYER.dumb_heuristic(currentState.board, player_number)
        val = EP.eval_board(currentState.board, player_number)
        # print('val = ' + str(val))
        return val, currentState

    # get all children moves from the given node
    children = MOVES.generate_moves(player_number, currentState.board)

    # who's turn it'll be next
    nextTurnPlayerNumber = 0
    if player_number == 0:
        nextTurnPlayerNumber = 1


    if bool_maximizingPlayer:
        v = -999999
        best_child = None
        # produce children of node
        for child in children:
            child_state = child[1]
            child_move = child[0]

            # v = max(v, alphabeta(child, depth_left - 1, A, B, False))
            returnedInformation = alphabeta(child_state, depth_left - 1, A, B, False, nextTurnPlayerNumber)
            old_v = v
            # print('returned Information: ' + str(returnedInformation))
            v = max(v, returnedInformation[0])
            # print(v)
            # check if it was changed. if it was update Node
            if v is not old_v:
                # best_child = returnedInformation[1]
                best_child = child

            A = max(A, v)
            if B <= A:
                updatePruning()
                break # (* B cut-off *):
        # print("BEST_MOVE: " + str(v) + ", " + str(depth_left) + ", " + str(best_child[0]))
        return v, best_child
    # Minimizing player
    else:
        v = 999999
        best_child = None

        for child in children:
            # v = min(v, alphabeta(child, depth_left - 1, A, B, True))

            child_state = child[1]
            child_move = child[0]


            returnedInformation = alphabeta(child_state, depth_left - 1, A, B, True, nextTurnPlayerNumber)
            # alphabeta(working_board, depth_left - 1, A, B, True, nextTurnPlayerNumber)
            old_v = v
            v = min(v, returnedInformation[0])
            # print(v)
            # check if it was changed. if it was update best child
            if v is not old_v:
                # best_child = returnedInformation[1]
                best_child = child

            B = min(B, v)
            if B <= A:
                updatePruning()
                break # (* A cut-off *)
        # print("BEST_MOVE (Minimizing): " + str(v) + ", " + str(depth_left))
        return v, best_child

 


def updatePruning():
    global NUM_TIMES_PRUNED
    NUM_TIMES_PRUNED += 1
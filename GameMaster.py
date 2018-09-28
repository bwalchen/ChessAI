"""
Runs a game of chess between two players
"""
import sys
import time
import ChessState as CS
import GenerateMoves as MOVES

PLAY_AGAINST_MYSELF = False
TIME_PER_MOVE = 10000
TURN_LIMIT = 300

if len(sys.argv) > 1:
    import importlib
    player1 = importlib.import_module(sys.argv[1])
    player2 = importlib.import_module(sys.argv[1])

    print("Player 1 is: " + str(player1))
    print("Player 2 is: " + str(player2))

    if len(sys.argv) > 3:
        TIME_PER_MOVE = float(sys.argv[3])

else:
    print("Using default players")

    import Player01 as player1
    if PLAY_AGAINST_MYSELF:
        import Player01 as player2
    else:
        import Player02 as player2

# not including Validate Moves because we ain't about that cheating life


def win_tester(s):
    possible_win = "No win"
    black_king_detected = False
    white_king_detected = False
    '''Scan the board looking for any king  
    and return a win for one player if the opponent
    has no king.'''
    b = s.board
    for i in range(8):
        for j in range(8):
            if b[i][j] == MOVES.KING + 1:
                black_king_detected = True
            if b[i][j] == MOVES.KING:
                white_king_detected = True
    if white_king_detected and not black_king_detected:
        possible_win = "Win for WHITE"
    if black_king_detected and not white_king_detected:
        possible_win = "Win for BLACK"
    return possible_win


CURRENT_PLAYER = CS.WHITE
FINISHED = False

# ----------------Run Game------------------


def run_game():
    current_state = CS.ChessState()
    print(str(current_state))

    try:
        p1comment = player1.prepare()
    except:
        report = 'Player 1 failed to prepare, and loses by default.'
        print(report)
        report = 'Congratulations to Player 2!'
        print(report)
        return
    try:
        p2comment = player2.prepare()
    except:
        report = 'Player 2 failed to prepare, and loses by default.'
        print(report)
        report = 'Congratulations to Player 1!'
        print(report)
        return

    print('\nThe Game Master says, "Let\'s Play!"\n')
    print('The initial state is...')

    current_remark = "The game is starting."

    WHITEs_turn = True
    global FINISHED
    FINISHED = False
    WINNER = "not yet known"
    turn_count = 1
    print(current_state)
    while not FINISHED:
        who = current_state.whose_move
        if who == CS.WHITE:
            side = 'WHITE'
            other_side = 'BLACK'
        else:
            side = 'BLACK'
            other_side = 'WHITE'
        global CURRENT_PLAYER
        CURRENT_PLAYER = who
        if WHITEs_turn:
            current_state.whose_move = 0
            move_fn = player1.make_move(current_state)
        else:
            current_state.whose_move = 1
            move_fn = player2.make_move(current_state)
        # player_result = timeout(move_fn, args=(current_state, current_remark, TIME_PER_MOVE), kwargs={},
                                # timeout_duration=TIME_PER_MOVE, default=(None, "I give up!"))
        WHITEs_turn = not WHITEs_turn


        if move_fn is None:
            print("No move returned by " + side + ".")
            WINNER = other_side
            FINISHED = True
            break
            

        try:
            move, new_state = move_fn
            startsq, endsq = move
            i, j = startsq
            ii, jj = endsq
        except Exception as e:
            print("move_and_state did not have proper form of [move, new_state] or")
            print("move did not have the proper form of (old_pos, new_pos)")
            WINNER = other_side
            FINISHED = True
            exit()
        print(side + "'s move: the " + CS.NUMBER_TO_PIECE[current_state.board[i][j]] +
              " at (" + str(i) + ", " + str(j) + ")  to (" + str(ii) + ", " + str(jj) + ".")

        move_report = "Turn " + str(turn_count) + ": Move is by " + side
        print(move_report)
        current_state = new_state
        possible_win = win_tester(current_state)
        if possible_win != "No win":
            WINNER = side
            FINISHED = True
            print(current_state)
            print(possible_win)
            break
        print(current_state)
        turn_count += 1

        if turn_count > TURN_LIMIT:
            FINISHED = True
            print("TURN_LIMIT exceeded! (" + str(TURN_LIMIT) + ")")
            break
    print("Game over.")
    if (WINNER == "not yet known") or (WINNER == "DRAW"):
        print("The outcome is a DRAW. Nobody wins.")
    else:
        print("Congratulations to the winner: " + WINNER)


def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    """
    This function will spawn a thread and run the given function using the args, kwargs and
    return the given default value if the timeout_duration is exceeded
    """

    import threading

    class PlayerThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = default

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception as e:
                print("Seems there was an exception during play by " + CURRENT_PLAYER + ":\n" + str(e))
                print(sys.exc_info())
                self.result = default
    pt = PlayerThread()
    pt.start()
    started_at = time.time()
    pt.join(timeout_duration)
    ended_at = time.time()
    diff = ended_at - started_at
    print("Time used in make_move: %0.4f seconds out of " % diff, timeout_duration)
    if pt.isAlive():
        print("Took too long.")
        print("We are now terminating the game.")
        print("Player " + CURRENT_PLAYER + " loses. ")
        exit()
    else:
        return pt.result


run_game()

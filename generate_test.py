import unittest
import GenerateMoves as MOVES


class TestMoves(unittest.TestCase):
	def setUp(self):
		pass

	def test_start_pos(self):
		"""
		pawns aren't being generated
		"""
		test_board = (
		[[  0,321,  0,  0,  0,  0,  0,  0],
		 [101,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,100,  0,  0,  0,  0,  0,  0],
		 [  0,320,  0,  0,  0,  0,  0,  0]]
		)

		actual_list = MOVES.generate_moves(0, test_board)
		expected_list = [[(0, 1), (2, 0)], [(0, 1), (2, 2)]]


	def test_pawn_black(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (1, 0)

		actual_list = []
		MOVES.generate_pawn(test_pos, test_board, actual_list)
		expected_list = [[(1, 0), (2, 0)], [(1, 0), (3, 0)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (2, 0)

		actual_list = []
		MOVES.generate_pawn(test_pos, test_board, actual_list)
		expected_list = [[(2, 0), (3, 0)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_pawn_black_capture(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,101,  0,  0,  0,  0,  0],
		 [  0,100,  0,100,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (3, 2)

		actual_list = []
		MOVES.generate_pawn(test_pos, test_board, actual_list)
		expected_list = [[(3, 2), (4, 2)], [(3, 2), (4, 1)], [(3, 2), (4, 3)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_bishop_black(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,331,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (6, 1)

		actual_list = []
		MOVES.generate_bishop(test_pos, test_board, actual_list)
		expected_list = [[(6, 1), (7, 0)], [(6, 1), (7, 2)], [(6, 1), (5, 0)], [(6, 1), (5, 2)], [(6, 1), (4, 3)], [(6, 1), (3, 5)], [(6, 1), (2, 6)], [(6, 1), (1, 7)]]

	def test_pawn_simple(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [100,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (6, 0)

		actual_list = []
		MOVES.generate_pawn(test_pos, test_board, actual_list)
		expected_list = [[(6, 0), (5, 0)], [(6, 0), (4, 0)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,100,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (4, 1)

		actual_list = []
		MOVES.generate_pawn(test_pos, test_board, actual_list)
		expected_list = [[(4, 1), (3, 1)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_pawn_capture(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,  0,101,  0,  0,  0,  0,  0],
		 [  0,100,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (4, 1)

		actual_list = []
		MOVES.generate_pawn(test_pos, test_board, actual_list)
		expected_list = [[(4, 1), (3, 1)], [(4, 1), (3, 0)], [(4, 1), (3, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_knight_simple(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,320,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (4, 3)

		actual_list = []
		MOVES.generate_knight(test_pos, test_board, actual_list)
		expected_list = [[(4, 3), (6, 2)], [(4, 3), (6, 4)], [(4, 3), (2, 2)], [(4, 3), (2, 4)], 
		[(4, 3), (3, 1)], [(4, 3), (3, 5)], [(4, 3), (5, 1)], [(4, 3), (5, 5)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_knight_capture(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,101,  0,  0,  0,  0,  0,  0],
		 [  0,  0,101,  0,  0,  0,  0,  0],
		 [320,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (7, 0)

		actual_list = []
		MOVES.generate_knight(test_pos, test_board, actual_list)
		expected_list = [[(7, 0), (5, 1)], [(7, 0), (6, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_bishop_simple(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,330,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (6, 3)

		actual_list = []
		MOVES.generate_bishop(test_pos, test_board, actual_list)
		expected_list = [[(6, 3), (5, 2)], [(6, 3), (5, 4)], [(6, 3), (4, 1)], 
		[(6, 3), (4, 5)], [(6, 3), (3, 0)], [(6, 3), (3, 6)], [(6, 3), (2, 7)],
		[(6, 3), (7, 2)], [(6, 3), (7, 4)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_bishop_capture(self):
		test_board = [
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,101,  0,101,  0,  0,  0],
		 [  0,  0,  0,330,  0,  0,  0,  0],
		 [  0,  0,101,  0,101,  0,  0,  0]]
		test_pos = (6, 3)

		actual_list = []
		MOVES.generate_bishop(test_pos, test_board, actual_list)
		expected_list = [[(6, 3), (5, 2)], [(6, 3), (5, 4)], [(6, 3), (7, 2)], [(6, 3), (7, 4)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_rook_simple(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,500,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (6, 1)

		actual_list = []
		MOVES.generate_rook(test_pos, test_board, actual_list)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (6, 3)], [(6, 1), (6, 4)], 
		[(6, 1), (6, 5)], [(6, 1), (6, 6)], [(6, 1), (6, 7)], [(6, 1), (7, 1)], [(6, 1), (5, 1)], 
		[(6, 1), (4, 1)], [(6, 1), (3, 1)], [(6, 1), (2, 1)], [(6, 1), (1, 1)], [(6, 1), (0, 1)]] 

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_rook_capture(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,101,  0,  0,  0,  0,  0,  0],
		 [101,500,101,  0,  0,  0,  0,  0],
		 [  0,101,  0,  0,  0,  0,  0,  0]])
		test_pos = (6, 1)

		actual_list = []
		MOVES.generate_rook(test_pos, test_board, actual_list)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (7, 1)], [(6, 1), (5, 1)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_queen_simple(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,980,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (6, 1)

		actual_list = []
		MOVES.generate_queen(test_pos, test_board, actual_list)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (6, 3)], [(6, 1), (6, 4)], 
		[(6, 1), (6, 5)], [(6, 1), (6, 6)], [(6, 1), (6, 7)], [(6, 1), (7, 1)], [(6, 1), (5, 1)], 
		[(6, 1), (4, 1)], [(6, 1), (3, 1)], [(6, 1), (2, 1)], [(6, 1), (1, 1)], [(6, 1), (0, 1)],
		[(6, 1), (5, 0)], [(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 2)], [(6, 1), (4, 3)],
		[(6, 1), (3, 4)], [(6, 1), (2, 5)], [(6, 1), (1, 6)], [(6, 1), (0, 7)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_queen_capture(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0],
		 [101,980,101,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0]])
		test_pos = (6, 1)

		actual_list = []
		MOVES.generate_queen(test_pos, test_board, actual_list)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (5, 0)], [(6, 1), (5, 1)],
		[(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 1)], [(6, 1), (7, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list


	def test_king_simple(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,40000,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (6, 1)

		actual_list = []
		MOVES.generate_king(test_pos, test_board, actual_list)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (5, 0)], [(6, 1), (5, 1)],
		[(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 1)], [(6, 1), (7, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_king_capture(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0],
		 [101,40000,101,  0,  0,  0,  0,  0],
		 [101,101,101,  0,  0,  0,  0,  0]])
		test_pos = (6, 1)

		actual_list = []
		MOVES.generate_king(test_pos, test_board, actual_list)
		expected_list = [[(6, 1), (6, 0)], [(6, 1), (6, 2)], [(6, 1), (5, 0)], [(6, 1), (5, 1)],
		[(6, 1), (5, 2)], [(6, 1), (7, 0)], [(6, 1), (7, 1)], [(6, 1), (7, 2)]]

		assert len(expected_list) is len(actual_list)

		for move in expected_list:
			assert move in actual_list

	def test_directional(self):
		test_board = (
		[[  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0],
		 [  0,  0,  0,  0,  0,  0,  0,  0]])
		test_pos = (2, 2)
		test_direction = (-1, -1)
		test_step_size = 8
		actual_list = []
		expected_list = [[(2, 2), (1, 1)], [(2, 2), (0, 0)]]

		MOVES.directional_moves(test_pos, test_board, test_direction, test_step_size, actual_list)

		assert len(actual_list) is len(expected_list)

		for move in expected_list:
			assert move in actual_list

	# def test_generate(self):
	# 	test_board = (
	# 	[[  0,  0,  0,  0,  0,  0,  0,  0],
	# 	 [  0,  0,  0,  0,  0,  0,  0,  0],
	# 	 [  0,  0,  0,  0,  0,  0,  0,  0],
	# 	 [  0,  0,  0,  0,  0,  0,  0,  0],
	# 	 [  0,  0,  0,  0,  0,  0,  0,  0],
	# 	 [  0,  0,  0,  0,  0,  0,  0,  0],
	# 	 [  0,  0,  0,  0,  0,  0,  0,  0],
	# 	 [  0,  0,  0,  0,  0,  0,  0,  0]])

	# 	actual_list = MOVES.generate_moves(0, test_board)

	# 	assert len(actual_list) is 0

if __name__ == '__main__':
	unittest.main()

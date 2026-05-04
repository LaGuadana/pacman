import unittest
from server import maze
from server.entities.pacman import Pacman

ORIGINAL_MAZE = list(maze.MAZE)

class TestPacman(unittest.TestCase):
	def setUp(self):
		maze.MAZE[:] = list(ORIGINAL_MAZE)
		self.pacman = Pacman()

	def test_initial_position(self):
		self.assertEqual(self.pacman.col, 14)
		self.assertEqual(self.pacman.row, 29)
		self.assertIsNone(self.pacman.direction)
		self.assertIsNone(self.pacman.next_direction)

	def test_no_movement_without_direction(self):
		col, row = self.pacman.col, self.pacman.row
		self.pacman.move()
		self.assertEqual(self.pacman.col, col)
		self.assertEqual(self.pacman.row, row)

	def test_move_into_open_space(self):
		self.pacman.next_direction = (-1, 0)
		self.pacman.move()
		self.assertEqual(self.pacman.col, 13)
		self.assertEqual(self.pacman.row, 29)

	def test_blocked_by_wall(self):
		self.pacman.next_direction = (0, 1)
		self.pacman.move()
		self.assertEqual(self.pacman.col, 14)
		self.assertEqual(self.pacman.row, 29)

	def test_eats_dot(self):
		self.pacman.next_direction = (-1, 0)
		self.pacman.move()
		self.assertEqual(maze.MAZE[29][13], ' ')

	def test_resets_direction_when_blocked(self):
		self.pacman.direction = (0, 1)
		self.pacman.move()
		self.assertIsNone(self.pacman.direction)

	def test_buffered_direction_consumed(self):
		self.pacman.next_direction = (-1, 0)
		self.pacman.move()
		self.assertIsNone(self.pacman.next_direction)
		self.assertEqual(self.pacman.direction, (-1, 0))

if __name__ == "__main__":
	unittest.main()

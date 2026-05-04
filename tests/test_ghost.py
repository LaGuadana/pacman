import unittest
import random
from server import maze
from server.entities.ghost import Ghost

ORIGINAL_MAZE = list(maze.MAZE)

class TestGhost(unittest.TestCase):
	def setUp(self):
		maze.MAZE[:] = list(ORIGINAL_MAZE)
		self.ghost = Ghost(12, 14, (255, 0, 0))

	def test_initial_state(self):
		self.assertEqual(self.ghost.col, 12)
		self.assertEqual(self.ghost.row, 14)
		self.assertEqual(self.ghost.color, (255, 0, 0))
		self.assertFalse(self.ghost.controlled)
		self.assertIsNone(self.ghost.direction)

	def test_timer_delays_movement(self):
		self.ghost.direction = (1, 0)
		for _ in range(7):
			self.ghost.move()
		self.assertEqual(self.ghost.col, 12)

	def test_moves_after_timer(self):
		self.ghost.direction = (1, 0)
		for _ in range(8):
			self.ghost.move()
		self.assertEqual(self.ghost.col, 13)

	def test_controlled_does_not_random_pick(self):
		self.ghost.controlled = True
		for _ in range(8):
			self.ghost.move()
		self.assertIsNone(self.ghost.direction)

	def test_random_pick_when_not_controlled(self):
		random.seed(0)
		for _ in range(8):
			self.ghost.move()
		self.assertIsNotNone(self.ghost.direction)

	def test_blocked_by_wall(self):
		self.ghost.col = 1
		self.ghost.row = 14
		self.ghost.direction = (-1, 0)
		for _ in range(8):
			self.ghost.move()
		self.assertEqual(self.ghost.col, 1)
		self.assertIsNone(self.ghost.direction)

	def test_next_direction_overrides(self):
		self.ghost.direction = (1, 0)
		self.ghost.next_direction = (-1, 0)
		for _ in range(8):
			self.ghost.move()
		self.assertEqual(self.ghost.direction, (-1, 0))

if __name__ == "__main__":
	unittest.main()

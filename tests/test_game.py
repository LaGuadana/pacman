import unittest
from server import maze
from server.entities.pacman import Pacman
from server.entities.ghost import Ghost
from server import game

ORIGINAL_MAZE = list(maze.MAZE)

class TestGame(unittest.TestCase):
	def setUp(self):
		maze.MAZE[:] = list(ORIGINAL_MAZE)
		self.player = Pacman()
		self.ghosts = [
			Ghost(12, 14, (255, 0, 0)),
			Ghost(13, 14, (255, 184, 255)),
			Ghost(14, 14, (0, 255, 255)),
			Ghost(15, 14, (255, 184, 82)),
		]

	def test_collision_detected(self):
		self.player.col = 12
		self.player.row = 14
		self.assertTrue(game.check_collision(self.player, self.ghosts[0]))

	def test_no_collision(self):
		self.assertFalse(game.check_collision(self.player, self.ghosts[0]))

	def test_reset_positions(self):
		self.player.col = 5
		self.player.row = 5
		self.player.direction = (1, 0)
		for g in self.ghosts:
			g.col = 0
			g.row = 0
			g.controlled = True
		game.reset_positions(self.player, self.ghosts)
		self.assertEqual((self.player.col, self.player.row), (14, 29))
		self.assertIsNone(self.player.direction)
		self.assertEqual((self.ghosts[0].col, self.ghosts[0].row), (12, 14))
		self.assertEqual((self.ghosts[3].col, self.ghosts[3].row), (15, 14))
		for g in self.ghosts:
			self.assertFalse(g.controlled)

	def test_apply_ghost_input(self):
		game.apply_ghost_input(self.ghosts, (2, (1, 0)))
		self.assertTrue(self.ghosts[2].controlled)
		self.assertEqual(self.ghosts[2].next_direction, (1, 0))
		self.assertFalse(self.ghosts[0].controlled)

	def test_apply_ghost_input_switches_control(self):
		game.apply_ghost_input(self.ghosts, (0, (1, 0)))
		game.apply_ghost_input(self.ghosts, (1, (-1, 0)))
		self.assertFalse(self.ghosts[0].controlled)
		self.assertTrue(self.ghosts[1].controlled)

if __name__ == "__main__":
	unittest.main()

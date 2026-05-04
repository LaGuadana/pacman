import unittest
from server import network
from server.entities.pacman import Pacman
from server.entities.ghost import Ghost
from client import network as client_network

class TestServerNetwork(unittest.TestCase):
	def setUp(self):
		network.clear_ghost_input()

	def test_parse_right(self):
		network.parse_command("1RIGHT")
		self.assertEqual(network.get_ghost_input(), (0, (1, 0)))

	def test_parse_left(self):
		network.parse_command("2LEFT")
		self.assertEqual(network.get_ghost_input(), (1, (-1, 0)))

	def test_parse_up(self):
		network.parse_command("3UP")
		self.assertEqual(network.get_ghost_input(), (2, (0, -1)))

	def test_parse_down(self):
		network.parse_command("4DOWN")
		self.assertEqual(network.get_ghost_input(), (3, (0, 1)))

	def test_parse_invalid_short(self):
		network.parse_command("X")
		self.assertIsNone(network.get_ghost_input())

	def test_clear_input(self):
		network.parse_command("1RIGHT")
		network.clear_ghost_input()
		self.assertIsNone(network.get_ghost_input())

	def test_build_state_format(self):
		maze = ["WWW", "W.W", "WWW"]
		player = Pacman()
		player.col = 1
		player.row = 1
		ghosts = [
			Ghost(12, 14, (255, 0, 0)),
			Ghost(13, 14, (255, 184, 255)),
			Ghost(14, 14, (0, 255, 255)),
			Ghost(15, 14, (255, 184, 82)),
		]
		state = network.build_state(maze, player, ghosts, 5)
		self.assertTrue(state.endswith("\n"))
		parts = state.strip().split(";")
		self.assertEqual(parts[0], "WWW|W.W|WWW")
		self.assertEqual(parts[1], "1,1")
		self.assertEqual(parts[6], "5")


class TestClientNetwork(unittest.TestCase):
	def test_parse_state_round_trip(self):
		maze = ["WWW", "W.W", "WWW"]
		player = Pacman()
		player.col = 1
		player.row = 1
		ghosts = [
			Ghost(12, 14, (255, 0, 0)),
			Ghost(13, 14, (255, 184, 255)),
			Ghost(14, 14, (0, 255, 255)),
			Ghost(15, 14, (255, 184, 82)),
		]
		state = network.build_state(maze, player, ghosts, 7)
		parsed_maze, parsed_pacman, parsed_ghosts, parsed_lives = client_network.parse_state(state.strip())
		self.assertEqual(parsed_maze, maze)
		self.assertEqual(parsed_pacman, [1, 1])
		self.assertEqual(parsed_ghosts[0], [12, 14])
		self.assertEqual(parsed_ghosts[3], [15, 14])
		self.assertEqual(parsed_lives, 7)

if __name__ == "__main__":
	unittest.main()

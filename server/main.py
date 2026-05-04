import pygame, sys
from server.maze import MAZE, TILE, ROWS, COLS
from server.entities.pacman import Pacman
from server.entities.ghost import Ghost
from server import network, renderer, game

def main():
	pygame.init()
	screen = pygame.display.set_mode((COLS * TILE, ROWS * TILE))
	clock  = pygame.time.Clock()
	player = Pacman()

	ghosts = [
		Ghost(12, 14, (255,   0,   0)),
		Ghost(13, 14, (255, 184, 255)),
		Ghost(14, 14, (  0, 255, 255)),
		Ghost(15, 14, (255, 184,  82)),
	]

	conn = network.start_server()
	lives = 10

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					player.next_direction = (1, 0)
				elif event.key == pygame.K_LEFT:
					player.next_direction = (-1, 0)
				elif event.key == pygame.K_UP:
					player.next_direction = (0, -1)
				elif event.key == pygame.K_DOWN:
					player.next_direction = (0, 1)

		player.move()

		ghost_input = network.get_ghost_input()
		if ghost_input is not None:
			game.apply_ghost_input(ghosts, ghost_input)
			network.clear_ghost_input()

		for ghost in ghosts:
			ghost.move()

		renderer.draw(screen, player, ghosts)

		for ghost in ghosts:
			if game.check_collision(player, ghost):
				lives -= 1
				game.reset_positions(player, ghosts)

		state = network.build_state(MAZE, player, ghosts, lives)

		try:
			conn.sendall(state.encode())
		except (BrokenPipeError, ConnectionResetError):
		    print("Client disconnected!")
		    pygame.quit()
		    sys.exit()

		if lives <= 0:
			print("Pacman Loses!")
			pygame.quit()
			sys.exit()
		if not any('.' in row for row in MAZE):
			print("Pacman wins!")
			pygame.quit()
			sys.exit()

		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
	main()

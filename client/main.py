import pygame, sys
from client.config import TILE, ROWS, COLS
from client import network, renderer

def main():
	pygame.init()
	screen = pygame.display.set_mode((COLS * TILE, ROWS * TILE))
	clock  = pygame.time.Clock()
	conn = network.connect(sys.argv[1])

	maze   = []
	pacman = [14, 29]
	ghosts = [[12,14],[13,14],[14,14],[15,14]]
	active = 1
	lives  = 3
	buffer = ""

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:    active = 1
				elif event.key == pygame.K_2:  active = 2
				elif event.key == pygame.K_3:  active = 3
				elif event.key == pygame.K_4:  active = 4
				elif event.key == pygame.K_RIGHT: network.send_command(conn, active, "RIGHT")
				elif event.key == pygame.K_LEFT:  network.send_command(conn, active, "LEFT")
				elif event.key == pygame.K_UP:    network.send_command(conn, active, "UP")
				elif event.key == pygame.K_DOWN:  network.send_command(conn, active, "DOWN")
		try:
			buffer += conn.recv(65536).decode()
			while "\n" in buffer:
				line, buffer = buffer.split("\n", 1)
				maze, pacman, ghosts, lives = network.parse_state(line)
				if lives <= 0:
					print("Pacman loses!")
					pygame.quit()
					sys.exit()
				if not any('.' in row for row in maze):
					print("Pacman wins!")
					pygame.quit()
					sys.exit()
		except (BlockingIOError, OSError)::
			pass

		renderer.draw(screen, maze, pacman, ghosts, active)
		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
	main()

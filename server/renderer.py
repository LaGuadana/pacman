import pygame
from server.maze import MAZE, TILE, ROWS, COLS

def draw(screen, player, ghosts):
	screen.fill((0, 0, 0))
	for row in range(ROWS):
		for col in range(COLS):
			x = col * TILE
			y = row * TILE
			if MAZE[row][col] == 'W':
				pygame.draw.rect(screen, (0, 0, 255), (x, y, TILE, TILE))
			elif MAZE[row][col] == '.':
				pygame.draw.circle(screen, (255, 255, 0), (x + TILE//2, y + TILE//2), TILE//6)
	px = player.col * TILE + TILE//2
	py = player.row * TILE + TILE//2
	pygame.draw.circle(screen, (255, 255, 0), (px, py), TILE//2)

	for ghost in ghosts:
		gx = ghost.col * TILE + TILE//2
		gy = ghost.row * TILE + TILE//2
		pygame.draw.circle(screen, ghost.color, (gx, gy), TILE//2)

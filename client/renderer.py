import pygame
from client.config import TILE, ROWS, COLS, GHOST_COLORS

def draw(screen, maze, pacman, ghosts, active):
	screen.fill((0, 0, 0))
	for row in range(ROWS):
		for col in range(COLS):
			x = col * TILE
			y = row * TILE
			if maze and maze[row][col] == 'W':
				pygame.draw.rect(screen, (0, 0, 255), (x, y, TILE, TILE))
			elif maze and maze[row][col] == '.':
				pygame.draw.circle(screen, (255, 255, 0), (x + TILE//2, y + TILE//2), TILE//6)
	px = pacman[0] * TILE + TILE//2
	py = pacman[1] * TILE + TILE//2
	pygame.draw.circle(screen, (255, 255, 0), (px, py), TILE//2)
	for i, g in enumerate(ghosts):
		gx = g[0] * TILE + TILE//2
		gy = g[1] * TILE + TILE//2
		pygame.draw.circle(screen, GHOST_COLORS[i], (gx, gy), TILE//2)
		if i == active - 1:
			pygame.draw.circle(screen, (255,255,255), (gx, gy), TILE//2, 2)

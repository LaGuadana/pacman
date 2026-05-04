import random
from server.maze import MAZE

class Ghost:
	def __init__(self, col, row, color):
		self.col = col
		self.row = row
		self.color = color
		self.direction = None
		self.next_direction = None
		self.timer = 0
		self.controlled = False

	def move(self):
		self.timer += 1
		if self.timer < 8:
			return
		self.timer = 0

		if self.next_direction is not None:
			dx, dy = self.next_direction
			new_col = self.col + dx
			new_row = self.row + dy
			if MAZE[new_row][new_col] != 'W':
				self.direction = self.next_direction
				self.next_direction = None

		if self.direction is None and not self.controlled:
			self.direction = random.choice([(1,0),(-1,0),(0,1),(0,-1)])

		if self.direction is None:
			return

		dx, dy = self.direction
		new_col = self.col + dx
		new_row = self.row + dy
		if MAZE[new_row][new_col] != 'W':
			self.col = new_col
			self.row = new_row
			if new_col == 27 and new_row == 14:
				self.col = 1
			elif new_col == 1 and new_row == 14:
				self.col = 26
		else:
			self.direction = None

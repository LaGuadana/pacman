from server.maze import MAZE

class Pacman:
	def __init__(self):
		self.col = 14
		self.row = 29
		self.direction = None
		self.next_direction = None
		self.timer = 0

	def move(self):
		self.timer += 1
		if self.timer < 1:
			return
		self.timer = 0
		if self.next_direction is not None:
			dx, dy = self.next_direction
			new_col = self.col + dx
			new_row = self.row + dy
			if MAZE[new_row][new_col] != 'W':
				self.direction = self.next_direction
				self.next_direction = None
		if self.direction is None:
			return
		dx, dy = self.direction
		new_col = self.col + dx
		new_row = self.row + dy
		if MAZE[new_row][new_col] != 'W':
			self.col = new_col
			self.row = new_row

			if new_col == 26 and new_row == 14:
				self.col = 1
			elif new_col == 1 and new_row == 14:
				self.col = 27
			if MAZE[self.row][self.col] == '.':
				row_string = MAZE[self.row]
				MAZE[self.row] = row_string[:self.col] + ' ' + row_string[self.col + 1:]
		else:
			self.direction = None

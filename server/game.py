def reset_positions(player, ghosts):
	player.col = 14
	player.row = 29
	player.direction = None
	player.next_direction = None
	ghosts[0].col = 12;  ghosts[0].row = 14
	ghosts[1].col = 13;  ghosts[1].row = 14
	ghosts[2].col = 14;  ghosts[2].row = 14
	ghosts[3].col = 15;  ghosts[3].row = 14
	for g in ghosts:
		g.direction = None
		g.next_direction = None
		g.controlled = False

def check_collision(player, ghost):
	return ghost.col == player.col and ghost.row == player.row

def apply_ghost_input(ghosts, ghost_input):
	idx, direction = ghost_input
	for ghost in ghosts:
		ghost.controlled = False
	ghosts[idx].controlled = True
	ghosts[idx].next_direction = direction

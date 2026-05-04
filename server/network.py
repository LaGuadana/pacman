import socket, threading

ghost_input = None

def parse_command(line):
	global ghost_input
	line = line.strip()
	if len(line) > 1:
		idx = int(line[0]) - 1
		direction = line[1:]
		if direction == "RIGHT":  ghost_input = (idx, (1,  0))
		elif direction == "LEFT":  ghost_input = (idx, (-1, 0))
		elif direction == "UP":    ghost_input = (idx, (0, -1))
		elif direction == "DOWN":  ghost_input = (idx, (0,  1))

def receive_loop(conn):
	buffer = ""
	while True:
		try:
			data = conn.recv(1024).decode()
			if not data:
				break
			buffer += data
			while "\n" in buffer:
				line, buffer = buffer.split("\n", 1)
				parse_command(line)
		except:
			break

def get_ghost_input():
	return ghost_input

def clear_ghost_input():
	global ghost_input
	ghost_input = None

def start_server(port=9876):
	print("Waiting for client to connect...")
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(("", port))
	server.listen(1)
	conn, addr = server.accept()
	print(f"Client connected: {addr}")
	threading.Thread(target=receive_loop, args=(conn,), daemon=True).start()
	return conn

def build_state(maze, player, ghosts, lives):
	maze_str = "|".join(maze)
	ghost_positions = ";".join(f"{g.col},{g.row}" for g in ghosts)
	return f"{maze_str};{player.col},{player.row};{ghost_positions};{lives}\n"

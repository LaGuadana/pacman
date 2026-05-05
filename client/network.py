import socket

def connect(host, port=9876):
	conn = socket.socket()
	try:
		conn.connect((host, port))
		conn.setblocking(False)
		print("Connected!")
		return conn
	except (ConnectionRefusedError, socket.timeout):
		print(f"ERROR: Can't connect to {host}:{port}")
		print("Make sure the server is running first!")
		sys.exit(1) 

def parse_state(line):
	parts  = line.split(";")
	maze   = parts[0].split("|")
	pacman = [int(x) for x in parts[1].split(",")]
	ghosts = [[int(x) for x in parts[i+2].split(",")] for i in range(4)]
	lives  = int(parts[6])
	return maze, pacman, ghosts, lives

def send_command(conn, active, direction):
	conn.sendall(f"{active}{direction}\n".encode())

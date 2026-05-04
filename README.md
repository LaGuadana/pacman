# Pacman Multiplayer

So basically one person plays Pacman and another person controls the ghosts over the network. Pretty fun when you get a friend to hunt you down.

## Installation

You can either install it as a package or just run it directly.

**Option 1: Install as a package (recommended)**

From inside the `pacman_game/` folder:
```bash
pip install .
```

Now you can run the game from anywhere with simple commands:
```bash
pacman-server              # Start the Pacman player
pacman-client 127.0.0.1    # Start the ghost player
```

**Option 2: Run directly without installing**

```bash
pip install -r requirements.txt
python -m server.main              # Server
python -m client.main 127.0.0.1    # Client
```

## How to play

You need **two terminals** (or two computers if you're feeling fancy).

**Terminal 1** — this is the Pacman player:
```bash
pacman-server
# or: python -m server.main
```

It'll just sit there waiting. That's normal.

**Terminal 2** — this is the ghost player:
```bash
pacman-client 127.0.0.1
# or: python -m client.main 127.0.0.1
```

Use `127.0.0.1` if you're running both on the same machine. If your friend is on another computer, put their IP address instead.

Both windows should pop up once they connect.

## Controls

**Server (Pacman):**
- Arrow keys to move
- Eat all the dots before the ghosts get you
- You have 10 lives
- Game ends when you run out of lives or eat all the dots

**Client (Ghosts):**
- Press `1`, `2`, `3`, or `4` to pick which ghost you're controlling
- Arrow keys to steer the selected ghost
- Try to catch Pacman
- The selected ghost has a white outline so you know which one you're driving

## Game mechanics

- Pacman needs to eat all the dots in the maze to win
- Ghosts that aren't being controlled by the client move randomly
- When you switch ghosts (press 1/2/3/4), the previous one goes back to moving randomly
- If a ghost catches Pacman, he loses a life and everyone resets to starting positions
- There are tunnel passages on the sides of the maze (though they might not work perfectly in this version)

## Running tests

If you want to make sure everything works:
```bash
python -m unittest discover tests
```

All 27 tests should pass.

## Project layout

```
pacman_game/
├── server/          # Pacman side (runs the actual game)
│   ├── entities/    # Pacman and Ghost classes
│   ├── main.py      # Game loop
│   ├── maze.py      # Maze layout and constants
│   ├── network.py   # Server socket and state updates
│   ├── renderer.py  # Pygame drawing
│   └── game.py      # Collision detection and game logic
├── client/          # Ghost side (connects to server)
│   ├── main.py      # Client game loop
│   ├── config.py    # Display constants
│   ├── network.py   # Client socket and command sending
│   └── renderer.py  # Client-side drawing
├── tests/           # Unit tests for game logic
├── requirements.txt
├── setup.py
└── README.md
```

The code is split into modules but it's still pretty much the same game logic, just organized better.

## Troubleshooting

**"Connection refused" error:**
Make sure you start the server first before starting the client.

**"Port already in use" error:**
Either wait a minute for the old connection to close, or kill the process using port 9876.

**Game window doesn't appear:**
Wait for both server and client to connect. The server window won't appear until the client connects.

**Uninstalling:**
```bash
pip uninstall pacman-multiplayer
```

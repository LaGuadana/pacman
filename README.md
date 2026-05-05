# Pacman Multiplayer

One person plays as Pacman, the other controls the ghosts over the network. It's pretty fun once you talk a friend into hunting you down.

## Installation

You can install it as a package or just run it straight from the folder.

### Option 1, install as a package

From inside `pacman_game/`:

```bash
pip install .
```

Then you can run it from anywhere:

```bash
pacman-server              # Pacman player
pacman-client 127.0.0.1    # Ghost player
```

### Option 2, run it directly

```bash
pip install -r requirements.txt
python -m server.main              # Server
python -m client.main 127.0.0.1    # Client
```

## How to play

You'll need two terminals (or two computers if you want to play across the network).

In the first terminal, start the Pacman side:

```bash
pacman-server
# or: python -m server.main
```

It will sit there waiting for a connection. That's normal, nothing's broken.

In the second terminal, start the ghost side:

```bash
pacman-client 127.0.0.1
# or: python -m client.main 127.0.0.1
```

Use `127.0.0.1` if both are running on the same machine. Otherwise put in your friend's IP address. Both windows should appear once the client connects.

## Controls

Pacman (server side) uses the arrow keys. Eat all the dots before the ghosts catch you. You start with 10 lives, and the game ends when you run out or clear the maze.

Ghosts (client side), press 1, 2, 3, or 4 to pick which ghost you want to control, then steer it with the arrow keys. The ghost you're currently driving gets a white outline so you can keep track of it. Switching to a different ghost releases the previous one, and it goes back to wandering on its own.

## Game mechanics

Pacman wins by eating every dot in the maze. Any ghost that isn't being controlled by the client moves randomly. If a ghost catches Pacman, he loses a life and everything resets to starting positions. There are tunnel passages on the sides of the maze, though I'll be honest, they're a bit finicky in this version.

## Running the tests

```bash
python -m unittest discover tests
```

All 27 should pass.

## Project layout

```
pacman_game/
├── server/          # Pacman side, runs the actual game
│   ├── entities/    # Pacman and Ghost classes
│   ├── main.py      # Game loop
│   ├── maze.py      # Maze layout and constants
│   ├── network.py   # Server socket and state updates
│   ├── renderer.py  # Pygame drawing
│   └── game.py      # Collision detection and game logic
├── client/          # Ghost side, connects to the server
│   ├── main.py      # Client game loop
│   ├── config.py    # Display constants
│   ├── network.py   # Client socket and command sending
│   └── renderer.py  # Client-side drawing
├── tests/           # Unit tests for game logic
├── requirements.txt
├── setup.py
└── README.md
```

It's split into modules now, but the game logic is the same as before, just organized better.

## Troubleshooting

If you get a "connection refused" error, you probably started the client before the server. Start the server first.

If you get "port already in use", either wait a minute for the old connection to close or kill whatever is still holding port 9876.

If the game window doesn't appear, give it a second. The server window won't show up until the client connects.

To uninstall:

```bash
pip uninstall pacman-multiplayer
```

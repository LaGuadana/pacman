# Pacman Multiplayer

So basically one person plays Pacman and another person controls the ghosts over the network. Pretty fun when you get a friend to hunt you down.

## How to play

First time setup:
```bash
pip install -r requirements.txt
```

You need **two terminals** (or two computers if you're feeling fancy).

**Terminal 1** — this is the Pacman player:
```bash
python -m server.main
```

It'll just sit there waiting. That's normal.

**Terminal 2** — this is the ghost player:
```bash
python -m client.main 127.0.0.1
```

Use `127.0.0.1` if you're running both on the same machine. If your friend is on another computer, put their IP address instead.

Both windows should pop up once they connect.

## Controls

**Server (Pacman):**
- Arrow keys to move
- Eat all the dots before the ghosts get you

**Client (Ghosts):**
- Press `1`, `2`, `3`, or `4` to pick which ghost you're controlling
- Arrow keys to steer it
- Try to catch Pacman

The selected ghost has a white outline so you know which one you're driving.

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
├── client/          # Ghost side (connects to server)
├── tests/           # Unit tests for game logic
└── requirements.txt
```

The code is split into modules but it's still pretty much the same game logic, just organized better. Check the `server/` and `client/` folders if you want to see how it's structured.

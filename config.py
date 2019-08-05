

SAVE_FP = "save.npy"


# HYPER-PARAMETERS

GAME_WIDTH = 20
GAME_HEIGHT = 20
NUM_CREATURES = 2000

SAVE_INTERVAL = 2


# BRAIN CONFIG

HIDDEN_NODES = [6, 6]  # [16,16]
NUM_INPUTS = 8  # 24


NODES = (NUM_INPUTS, *HIDDEN_NODES, 4)

# SNAKE GAME

EMPTY = 0
APPLE = 1
SNAKE = 2
HEAD = 3
WALL = 4

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)



BLOCK_SIZE = 30
GRID_WIDTH = 10 # 10 blocks wide
GRID_HEIGHT = 20 # 20 blocks high

GAME_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
GAME_WIDTH = BLOCK_SIZE * GRID_WIDTH

SCREEN_WIDTH = GAME_WIDTH + 600
SCREEN_HEIGHT = GAME_HEIGHT + 200

# x and y co-ordinates for start of grid
TOP = 100
LEFT = 100

# starting position on grid for the 5 x 5 square that holds each shape
START_X = 3
START_Y = 0
BLOCKS_PER_SHAPE = 4

# time.sleep delay on each loop, which reduces as the levels increase
DELAY = 0.5
MIN_DELAY = 0.1

# colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

SHAPE_COLORS = {
    "red" : (255, 0, 0),
    "green" : (0, 255, 0),
    "blue" : (0, 0, 255),
    "yellow" : (255,255,0),
    "purple" : (240,0,255),
    "orange" : (255,100,10),
    "pink" : (255,100,180),
}

FPS = 60
LINES_PER_LEVEL = 5

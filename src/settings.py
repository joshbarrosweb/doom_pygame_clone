import math

# Screen Resolution
RES = WIDTH, HEIGHT = 1600, 900
# Half Width and Height for easier calculations
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
# Frames per second
FPS = 60

# Initial player position
PLAYER_POS = 1.5, 5
# Initial player angle
PLAYER_ANGLE = 0
# Player speed for movement
PLAYER_SPEED = 0.004
# Player rotation speed
PLAYER_ROT_SPEED = 0.002
# Player size scale factor
PLAYER_SIZE_SCALE = 60
# Player initial maximum health
PLAYER_MAX_HEALTH = 100

# Mouse sensitivity settings for the player rotation
MOUSE_SENSITIVITY = 0.0003
# Maximum relative mouse movement
MOUSE_MAX_REL = 40
# Left border for mouse to trigger screen rotation
MOUSE_BORDER_LEFT = 100
# Right border for mouse to trigger screen rotation
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

# Floor color in (R,G,B) format
FLOOR_COLOR = (30, 30, 30)

# Field of View
FOV = math.pi / 3
# Half of Field of View
HALF_FOV = FOV / 2
# Number of rays casted for Raycasting
NUM_RAYS = WIDTH // 2
# Half of the total number of rays
HALF_NUM_RAYS = NUM_RAYS // 2
# The angle difference between each ray
DELTA_ANGLE = FOV / NUM_RAYS
# Maximum render depth for the rays
MAX_DEPTH = 20

# Screen distance is calculated based on half field of view
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
# Scaling factor
SCALE = WIDTH // NUM_RAYS

# Texture Size for the walls and other objects
TEXTURE_SIZE = 256
# Half of the texture size
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

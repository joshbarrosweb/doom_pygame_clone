import pygame as pg

_ = False

# The representation of the mini map
mini_map = [
  [1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1],
  [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
  [1, _, _, 2, _, 2, _, _, _, _, 4, _, _, _, 1],
  [1, _, _, _, 2, _, _, _, _, 4, 4, 4, _, _, 1],
  [1, _, _, 2, _, 2, _, _, _, _, 1, _, _, _, 1],
  [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
  [1, _, 3, _, _, _, 3, 3, _, _, _, _, 3, _, 1],
  [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
  [1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1],
]

class Map:
  def __init__(self, game):
    self.game = game
    self.mini_map = mini_map
    self.world_map = {}
    self.rows = len(self.mini_map)
    self.cols = len(self.mini_map[0])
    self.get_map()

  def get_map(self):
    # Converts the mini map into the world map dictionary representation.
    for j, row in enumerate(self.mini_map):
      for i, value in enumerate(row):
        if value:
          self.world_map[(i, j)] = value

  def draw(self):
    # Draws the walls of the world map on the screen.
    [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
     for pos in self.world_map]

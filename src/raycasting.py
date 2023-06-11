import pygame as pg
import math
from settings import *

class RayCasting:
  def __init__(self, game):
    self.game = game
    self.ray_casting_result = [] # will store results of raycasting
    self.objects_to_render = []  # will store objects to be rendered
    self.textures = self.game.object_renderer.wall_textures  # stores wall textures

  def get_objects_to_render(self):
    # Resets list of objects to render
    self.objects_to_render = []

    # Goes through the results of raycasting
    for ray, values in enumerate(self.ray_casting_result):
      depth, proj_height, texture, offset = values

      # If the projected height is less than screen height, a slice of wall is created
      if proj_height < HEIGHT:
        wall_column = self.textures[texture].subsurface(
          offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
        )
        wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
        wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
      else:
        # If the projected height is more than the screen height, wall slice covers the entire height
        texture_height = TEXTURE_SIZE * HEIGHT / proj_height
        wall_column = self.textures[texture].subsurface(
          offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
          SCALE, texture_height
        )
        wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))
        wall_pos = (ray * SCALE, 0)

      # Add the object to the render list with its depth, image, and position
      self.objects_to_render.append((depth, wall_column, wall_pos))

  def ray_cast(self):
    # Resets list of ray casting results
    self.ray_casting_result = []
    texture_vert, texture_hor = 1, 1
    ox, oy = self.game.player.pos
    x_map, y_map = self.game.player.map_pos

    ray_angle = self.game.player.angle - HALF_FOV + 0.0001  # Starting angle for the first ray

    for ray in range(NUM_RAYS):
      sin_a = math.sin(ray_angle)
      cos_a = math.cos(ray_angle)

      # Horizontal grid interception calculation
      y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
      depth_hor = (y_hor - oy) / sin_a
      x_hor = ox + depth_hor * cos_a
      delta_depth = dy / sin_a
      dx = delta_depth * cos_a

      # Horizontal wall detection
      for i in range(MAX_DEPTH):
        tile_hor = int(x_hor), int(y_hor)
        if tile_hor in self.game.map.world_map:
          texture_hor = self.game.map.world_map[tile_hor]
          break
        x_hor += dx
        y_hor += dy
        depth_hor += delta_depth

      # Vertical grid interception calculation
      x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
      depth_vert = (x_vert - ox) / cos_a
      y_vert = oy + depth_vert * sin_a
      delta_depth = dx / cos_a
      dy = delta_depth * sin_a

      # Vertical wall detection
      for i in range(MAX_DEPTH):
        tile_vert = int(x_vert), int(y_vert)
        if tile_vert in self.game.map.world_map:
          texture_vert = self.game.map.world_map[tile_vert]
          break
        x_vert += dx
        y_vert += dy
        depth_vert += delta_depth

      # Determines the closer wall and uses it for rendering
      if depth_vert < depth_hor:
        depth, texture = depth_vert, texture_vert
        y_vert %= 1
        offset = y_vert if cos_a > 0 else (1 - y_vert)
      else:
        depth, texture = depth_hor, texture_hor
        x_hor %= 1
        offset = (1 - x_hor) if sin_a > 0 else x_hor

      # Corrects fisheye effect
      depth *= math.cos(self.game.player.angle - ray_angle)

      # Calculates the projected height of the wall slice
      proj_height = SCREEN_DIST / (depth + 0.0001)

      # Adds the result to the list
      self.ray_casting_result.append((depth, proj_height, texture, offset))

      # Changes the ray angle for the next ray
      ray_angle += DELTA_ANGLE

  def update(self):
    # Updates raycasting and the objects to render
    self.ray_cast()
    self.get_objects_to_render()

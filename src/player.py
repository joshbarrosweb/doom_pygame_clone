import pygame as pg
import math
from settings import *

class Player:
  def __init__(self, game):
    self.game = game
    self.x, self.y = PLAYER_POS  # player's position
    self.angle = PLAYER_ANGLE  # player's facing angle
    self.shot = False  # if player has shot
    self.health = PLAYER_MAX_HEALTH  # player's health
    self.rel = 0  # relative mouse movement
    self.health_recovery_delay = 700  # delay for health recovery
    self.time_prev = pg.time.get_ticks()  # previous recorded time
    self.diagonal_move_correction = 1 / math.sqrt(2)  # correction factor for diagonal movement

  def recover_health(self):
    # Recover health if enough time has passed and not at max health
    if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
      self.health += 1

  def check_health_recovery_delay(self):
    # Check if enough time has passed for health to recover
    time_now = pg.time.get_ticks()
    if time_now - self.time_prev > self.health_recovery_delay:
      self.time_prev = time_now
      return True

  def check_game_over(self):
    # Check if player's health is below 1
    if self.health < 1:
      self.game.object_renderer.game_over()  # call game over function
      pg.display.flip()
      pg.time.delay(1500)
      self.game.new_game()  # start a new game

  def get_damage(self, damage):
    # Reduce player's health and check if game is over
    self.health -= damage
    self.game.object_renderer.player_damage()  # play damage effect
    self.game.sound.player_pain.play()  # play pain sound
    self.check_game_over()  # check if game is over

  def single_fire_event(self, event):
    # Respond to a single fire event
    if event.type == pg.MOUSEBUTTONDOWN:
      if event.button == 1 and not self.shot and not self.game.weapon.reloading:
        self.game.sound.shotgun.play()  # play shooting sound
        self.shot = True
        self.game.weapon.reloading = True  # start weapon reloading

  def movement(self):
    # Handle player movement
    sin_a = math.sin(self.angle)
    cos_a = math.cos(self.angle)
    dx, dy = 0, 0
    speed = PLAYER_SPEED * self.game.delta_time
    speed_sin = speed * sin_a
    speed_cos = speed * cos_a

    keys = pg.key.get_pressed()  # get keys currently being pressed
    num_key_pressed = -1
    if keys[pg.K_w]:
      num_key_pressed += 1
      dx += speed_cos
      dy += speed_sin
    if keys[pg.K_s]:
      num_key_pressed += 1
      dx += -speed_cos
      dy += -speed_sin
    if keys[pg.K_a]:
      num_key_pressed += 1
      dx += speed_sin
      dy += -speed_cos
    if keys[pg.K_d]:
      num_key_pressed += 1
      dx += -speed_sin
      dy += speed_cos

    # Diagonal Move Correction
    if num_key_pressed:
      dx *= self.diagonal_move_correction
      dy *= self.diagonal_move_correction

    self.check_wall_collision(dx, dy)

    # Angle rotation handled by mouse, no need for keyboard rotation
    # if keys[pg.K_LEFT]:
    #   self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
    # if keys[pg.K_RIGHT]:
    #   self.angle += PLAYER_ROT_SPEED * self.game.delta_time
    self.angle %= math.tau  # ensure angle is within [0, 2*pi)

  def check_wall(self, x, y):
    # Check if the point (x, y) is not in the wall
    return (x, y) not in self.game.map.world_map

  def check_wall_collision(self, dx, dy):
    # Check for wall collision before updating player's position
    scale = PLAYER_SIZE_SCALE / self.game.delta_time
    if self.check_wall(int(self.x + dx * scale), int(self.y)):
      self.x += dx
    if self.check_wall(int(self.x), int(self.y + dy * scale)):
      self.y += dy

  def draw(self):
    # Draw player's vision direction and position on the screen
    pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y *100),
                (self.x * 100 + WIDTH * math.cos(self.angle),
                 self.y * 100 + WIDTH * math.sin(self.angle)), 2)
    pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

  def mouse_control(self):
    # Handle mouse control for angle rotation
    mx, my = pg.mouse.get_pos()
    if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
      pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
    self.rel = pg.mouse.get_rel()[0]
    self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
    self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

  def update(self):
    # Update player's movement, mouse control, and health recovery
    self.movement()
    self.mouse_control()
    self.recover_health()

  @property
  def pos(self):
    # Return player's position
    return self.x, self.y

  @property
  def map_pos(self):
    # Return player's position on the map
    return int(self.x), int(self.y)

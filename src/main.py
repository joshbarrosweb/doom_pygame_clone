import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
  def __init__(self):
    pg.init()

    # Initialize the game window and settings
    pg.mouse.set_visible(False)
    self.screen = pg.display.set_mode(RES)
    pg.event.set_grab(True)

    # Set up the game clock and delta time
    self.clock = pg.time.Clock()
    self.delta_time = 1

    # Set up the global trigger and event
    self.global_trigger = False
    self.global_event = pg.USEREVENT + 0
    pg.time.set_timer(self.global_event, 40)

    # Start a new game
    self.new_game()

  def new_game(self):
    # Create game objects
    self.map = Map(self)
    self.player = Player(self)
    self.object_renderer = ObjectRenderer(self)
    self.raycasting = RayCasting(self)
    self.object_handler = ObjectHandler(self)
    self.weapon = Weapon(self)
    self.sound = Sound(self)
    self.pathfinding = PathFinding(self)

    # Start playing background music
    pg.mixer.music.play(-1)

  def update(self):
    # Update game objects
    self.player.update()
    self.raycasting.update()
    self.object_handler.update()
    self.weapon.update()

    # Update display
    pg.display.flip()
    self.delta_time = self.clock.tick(FPS)
    pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

  def draw(self):
    # Draw game objects
    self.object_renderer.draw()
    self.weapon.draw()

  def check_events(self):
    self.global_trigger = False

    # Check for events
    for event in pg.event.get():
      if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
        pg.quit()
        sys.exit()
      elif event.type == self.global_event:
        self.global_trigger = True

      # Pass events to the player object
      self.player.single_fire_event(event)

  def run(self):
    while True:
      # Process game loop
      self.check_events()
      self.update()
      self.draw()

if __name__ == '__main__':
  game = Game()
  game.run()

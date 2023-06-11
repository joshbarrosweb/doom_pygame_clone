from sprite_object import *
from npc import *
from random import choices, randrange

class ObjectHandler:
  # Initialize the ObjectHandler with game, sprite list, NPC list, and NPC positions
  def __init__(self, game):
    self.game = game
    self.sprite_list = []
    self.npc_list = []
    self.npc_sprite_path = './resources/sprites/npc/'
    self.static_sprite_path = './resources/sprites/static_sprites/'
    self.anim_sprite_path = './resources/sprites/animated_sprites/'
    add_sprite = self.add_sprite
    add_npc = self.add_npc
    self.npc_positions = {}

    # Define the number of enemies, the types of NPCs, and their weights for random choice
    self.enemies = 20
    self.npc_types = [SoldierNPC, CacodemonNPC, CyberdemonNPC]
    self.weights = [70, 20, 10]
    self.restricted_area = {(i, j) for i in range(8) for j in range(8)}
    self.spawn_npc()  # Spawn NPCs on initialization

    # Add various sprite objects to the game
    add_sprite(SpriteObject(game))
    add_sprite(AnimatedSprite(game))
    add_sprite(AnimatedSprite(game, pos=(11.5, 11.5)))
    add_sprite(AnimatedSprite(game, pos=(11.5, 1.5)))
    add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.5, 11.5)))
    add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.5, 1.5)))

    # Uncomment this to add a NPC on initialization
    # add_npc(NPC(game))

  # Spawn NPCs in the game world with random positions
  def spawn_npc(self):
    for i in range(self.enemies):
      npc = choices(self.npc_types, self.weights)[0]  # Choose a NPC type based on weights
      pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
      while (pos in self.game.map.world_map) or (pos in self.restricted_area):
        pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)  # Find a valid position for the NPC
      self.add_npc(npc(self.game, pos =(x + 0.5, y + 0.5)))

  # Check if the player has won the game, i.e., if there are no NPCs left
  def check_win(self):
    if not len(self.npc_positions):
      self.game.object_renderer.win()  # Display the win image
      pg.display.flip()
      pg.time.delay(1500)
      self.game.new_game()  # Start a new game

  # Update the state of all sprites and NPCs
  def update(self):
    self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
    [sprite.update() for sprite in self.sprite_list]
    [npc.update() for npc in self.npc_list]
    self.check_win()  # Check for win after each update

  # Add a sprite to the sprite list
  def add_sprite(self, sprite):
    self.sprite_list.append(sprite)

  # Add a NPC to the NPC list
  def add_npc(self, npc):
    self.npc_list.append(npc)

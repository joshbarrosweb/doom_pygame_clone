# Import necessary libraries
import pygame as pg

# Sound class is used to manage all sounds in the game
class Sound:
  # The __init__ function initializes the Sound with given game instance and loads all sound files
  def __init__(self, game):
    self.game = game
    pg.mixer.init()
    self.path = './resources/sound/'
    # Load shotgun sound
    self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
    # Load non-player character (NPC) pain sound
    self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
    # Load NPC death sound
    self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
    # Load NPC shot sound
    self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
    # Set volume for NPC shot sound
    self.npc_shot.set_volume(0.2)
    # Load player pain sound
    self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
    # Load theme music
    self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
    # Set volume for theme music
    pg.mixer.music.set_volume(0.4)

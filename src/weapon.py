# Import necessary modules
from sprite_object import *

# Define the Weapon class, which is a kind of AnimatedSprite
class Weapon(AnimatedSprite):
  # Initialize the weapon with certain default parameters
  def __init__(self, game, path='./resources/sprites/weapon/shotgun/0.png', scale=0.4, animation_time=90):
    # Call the super class's initializer
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    # Preload all the images and scale them
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    # Position the weapon on the screen
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    # The weapon is not reloading at start
    self.reloading = False
    # The number of images for animation sequence
    self.num_images = len(self.images)
    # Initialize paths for the images
    self.image_paths = [f'./resources/sprites/weapon/shotgun/{i}.png' for i in range(self.num_images)]
    self.image_paths = deque(self.image_paths)
    # Frame counter for animation sequence
    self.frame_counter = 0
    # The damage that this weapon can inflict
    self.damage = 50

  # Function to animate the weapon while shooting
  def animate_shot(self):
    # If the weapon is reloading
    if self.reloading:
        self.game.player.shot = False
        # If it's time for the next frame of the animation
        if self.animation_trigger:
            # Rotate the deque of images and paths
            self.images.rotate(-1)
            self.image_paths.rotate(-1)
            # Set the current image
            self.image = self.images[0]
            # Increment the frame counter
            self.frame_counter += 1
            # If we've gone through all the frames of the animation
            if self.frame_counter == self.num_images:
                # Stop reloading
                self.reloading = False
                self.frame_counter = 0
                # Rotate deque to position '0.png' at front
                self.images.rotate(-self.frame_counter)
                self.image_paths.rotate(-self.frame_counter)
    # If the weapon is not reloading
    else:
        # Set image to '0.png'
        self.image = self.images[0]

  # Function to draw the weapon on the screen
  def draw(self):
    self.game.screen.blit(self.image, self.weapon_pos)

  # Function to update the weapon status
  def update(self):
    # Check if it's time for the next frame of the animation
    self.check_animation_time()
    # Animate the weapon
    self.animate_shot()

# DOOM-style Game

This project is a DOOM-style game implemented in Python using the Pygame library. It features raycasting, 2D/3D rendering, sprite animations, sound effects, and more.

## Special Thanks

Special thanks to CoderSpace (Stanislav Petrov) for providing the inspiration and resources for this project.

- [Video Tutorial](https://www.youtube.com/watch?v=ECqUrT7IdqQ&t=3s)
- [CoderSpace GitHub](https://github.com/StanislavPetrovV/DOOM-style-Game)

## Project Structure

The project has the following file and folder structure:

### `src`

This folder contains the source code files for the game:

- `main.py`: The main entry point of the game.
- `map.py`: Implements the game map and its rendering.
- `npc.py`: Handles non-player character logic and behavior.
- `object_handler.py`: Manages game objects and their interactions.
- `object_renderer.py`: Renders game objects in the scene.
- `pathfinding.py`: Provides pathfinding algorithms for AI navigation.
- `player.py`: Implements the player character and its controls.
- `raycasting.py`: Performs raycasting calculations for 3D rendering.
- `settings.py`: Contains game settings and constants.
- `sound.py`: Handles sound effects and music.
- `sprite_object.py`: Defines the base class for sprite-based objects.
- `weapon.py`: Manages the player's weapons and their functionality.

### `resources`

This folder contains various resources used in the game:

#### `sound`

This subfolder contains sound files used for sound effects and music.

- `npc_attack.wav`: Sound effect for NPC attacks.
- `npc_death.wav`: Sound effect for NPC deaths.
- `npc_pain.wav`: Sound effect for NPC pain.
- `player_pain.wav`: Sound effect for player pain.
- `shotgun.wav`: Sound effect for shotgun shots.
- `theme.mp3`: Background music theme.

#### `sprites`

This subfolder contains sprite images used for the game's visuals.

##### `animated_sprites`

This subfolder contains animated sprite sequences used for visual effects.

- `green_light`: Animated sprite sequence for green lights.
- `red_light`: Animated sprite sequence for red lights.

##### `npc`

This subfolder contains sprite images for NPC characters and their animations.

- `caco_demon`: Sprite images for the caco demon NPC.
- `cyber_demon`: Sprite images for the cyber demon NPC.
- `soldier`: Sprite images for the soldier NPC.

##### `static_sprites`

This subfolder contains static sprite images used for environment elements.

- `candlebra.png`: Image of a candlebra.

##### `weapon`

This subfolder contains sprite images for weapons and their animations.

- `shotgun`: Sprite images for the shotgun weapon.

#### `textures`

This subfolder contains texture images used for the game's visual elements.

- `1.png`, `2.png`, `3.png`, `4.png`, `5.png`: Texture images.
- `blood_screen.png`: Image for blood splatter screen effect.
- `digits`: Subfolder containing digit images used for score and UI.
- `game_over.png`: Image displayed when the game is over.
- `sky.png`: Image for the sky background.
- `win.png`: Image displayed when the game is won.

## Instructions

To run the project, follow these steps:

1. Install Python 3 if you haven't already.
2. Install the Pygame library by running the command: `pip install pygame`.
3. Navigate to the project's `src` directory.
4. Run the command: `python3 main.py`.

Make

 sure you have the required resources (images, sounds, etc.) in the appropriate directories as shown in the folder structure.

Feel free to modify and explore the game to suit your needs.

Enjoy playing!

---

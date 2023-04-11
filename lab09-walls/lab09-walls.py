""" Sprite Sample Program """

import arcade
import random
import pyglet

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 900


COIN_COUNT = 10


MOVEMENT_SPEED = 5


class Coin(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        # See if we went off-screen
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT

class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        self.sound = pyglet.media.load('monedas.mp3', streaming=False)

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk5.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # --- Manually place walls

        # Manually create and position a box at 40, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 40
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 160, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 160
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 280, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 280
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 400, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 400
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 520, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 520
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 640, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 640
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 760
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 880
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 990
        wall.center_y = 125
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 880
        wall.center_y = 250
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 990
        wall.center_y = 250
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 760
        wall.center_y = 250
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 990
        wall.center_y = 400
        self.wall_list.append(wall)

        # Manually create and position a box at 760, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 990
        wall.center_y = 550
        self.wall_list.append(wall)

        # Manually create and position a box at 40, 150
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
        wall.center_x = 40
        wall.center_y = 550
        self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_single.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 250
            self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(50, 650, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 380
            self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(100, 965, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 690
            self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(100, 1050, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter_rounded.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 820
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list_1 = [[400, 500],
                            [470, 500],
                            [400, 570],
                            [470, 570]]

        # --- Place walls with a list
        coordinate_list_2= [[200, 500],
                           [270, 500],
                           [200, 570],
                           [270, 570]]

        # --- Place walls with a list
        coordinate_list_3 = [[600, 500],
                             [670, 500],
                             [600, 570],
                             [670, 570]]

        # --- Place walls with a list
        coordinate_list_4 = [[800, 500],
                             [870, 500],
                             [800, 570],
                             [870, 570]]

        # --- Place walls with a list
        coordinate_list_5 = [[800, 375],
                             [870, 375],
                             [800, 425],
                             [870, 425]]

        # Loop through coordinates
        for coordinate in coordinate_list_1:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Loop through coordinates
        for coordinate in coordinate_list_2:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Loop through coordinates
        for coordinate in coordinate_list_3:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Loop through coordinates
        for coordinate in coordinate_list_4:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Loop through coordinates
        for coordinate in coordinate_list_5:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)


            # Create the coins
            for i in range(COIN_COUNT):

                # Create the coin instance
                # Coin image from kenney.nl
                coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

                # --- IMPORTANT PART ---

                # Boolean variable if we successfully placed the coin
                coin_placed_successfully = False

                # Keep trying until success
                while not coin_placed_successfully:
                    # Position the coin
                    coin.center_x = random.randrange(SCREEN_WIDTH)
                    coin.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting a wall
                    wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                    # See if the coin is hitting another coin
                    coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                    if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                        # It is!
                        coin_placed_successfully = True

                # Add the coin to the lists
                self.coin_list.append(coin)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()


        if len(self.coin_list) > 0:
            self.coin_list.draw()
            self.player_list.draw()
            self.wall_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        else:
            arcade.draw_text("ENHORABUENA , Lo has conseguido", 20, 500, arcade.color.WHITE, 40)

    def update(self, delta_time):
        self.coin_list.update()
        self.physics_engine.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.sound = pyglet.media.load('monedas.mp3', streaming=False)
            self.sound.play()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
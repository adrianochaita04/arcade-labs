
import random
import arcade
import pyglet

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25
SPRITE_SCALING_ROCK = 0.25
COIN_COUNT = 5
ROCK_COUNT = 10

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 780


class Coin(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        # See if we went off-screen
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT

class Rock(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        # See if we went off-screen
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "El juego de la rana")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.rock_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLUE)
        self.sound = pyglet.media.load('monedas.mp3', streaming=False)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/enemies/frog.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(":resources:images/items/coinBronze.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the rocks
        for i in range(ROCK_COUNT):

            # Create the rock instance
            # Rock image from kenney.nl
            rock = Rock(":resources:images/space_shooter/meteorGrey_big3.png", SPRITE_SCALING_ROCK)

            # Position the rock
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the rock to the lists
            self.rock_list.append(rock)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        if len(self.coin_list) > 0:
            self.coin_list.draw()
            self.rock_list.draw()
            self.player_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        else:
            arcade.draw_text("ENHORABUENA , Lo has conseguido", 20, 500, arcade.color.WHITE, 40)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.rock_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        rocks_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.rock_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.sound = pyglet.media.load('monedas.mp3', streaming=False)
            self.sound.play()
        for rock in rocks_hit_list:
            rock.remove_from_sprite_lists()
            self.score -= 1
            self.sound = pyglet.media.load('jab-jab.mp3', streaming=False)
            self.sound.play()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

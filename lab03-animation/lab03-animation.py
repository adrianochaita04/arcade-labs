"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Draw the grass
def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.BITTER_LIME)
# Draw the ball
def draw_center():
    arcade.draw_circle_filled(400, 300, 80, arcade.color.WHITE)
    arcade.draw_circle_filled(400, 300, 78, arcade.color.BITTER_LIME)
    arcade.draw_circle_filled(400, 300, 10, arcade.color.WHITE)
    arcade.draw_circle_filled(400, 115, 5, arcade.color.WHITE)
    arcade.draw_circle_filled(400, 485, 5, arcade.color.WHITE)
# Draw the lines
def draw_lines():
    arcade.draw_lrtb_rectangle_filled(10, 790, 50, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(10, 790, 550, 550, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(10, 10, 550, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(790, 790, 550, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(10, 790, 300, 300, arcade.color.WHITE)
# Draw the soccer goal 1
def draw_soccer_goal_1():
    arcade.draw_lrtb_rectangle_filled(300, 300, 550, 450, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(500, 500, 550, 450, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 500, 550, 550, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 500, 450, 450, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(350, 350, 550, 500, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(450, 450, 550, 500, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(350, 450, 550, 550, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(350, 450, 500, 500, arcade.color.WHITE)
# Draw the soccer goal 2
def draw_soccer_goal_2():
    arcade.draw_lrtb_rectangle_filled(300, 300, 150, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(500, 500, 150, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 500, 50, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(300, 500, 150, 150, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(350, 350, 100, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(450, 450, 100, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(350, 450, 50, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(350, 450, 100, 100, arcade.color.WHITE)

    # Set the background color
def draw_background():
    arcade.set_background_color(arcade.color.BITTER_LIME)
def main():
    arcade.open_window(800, 600, "Campo de futbol")

    draw_background()
    draw_grass()
    draw_center()
    draw_lines()
    draw_soccer_goal_1()
    draw_soccer_goal_2()


    # --- Finish drawing ---
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

# Get ready to draw
main()
"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Zixin Fan.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    rectangle.attach_to(window)

    dx = rectangle.get_width()
    dy = rectangle.get_height()

    upper_left_x = min(rectangle.corner_1.x, rectangle.corner_2.x)
    upper_left_y = min(rectangle.corner_1.y, rectangle.corner_2.y)
    lower_right_x = max(rectangle.corner_1.x, rectangle.corner_2.x)
    lower_right_y = max(rectangle.corner_1.y, rectangle.corner_2.y)

    for k in range(n - 1):
        upper_left_x = upper_left_x - dx / 2
        lower_right_x = lower_right_x - dx / 2
        upper_left_y = upper_left_y - dy
        lower_right_y = lower_right_y - dy

        x1 = upper_left_x
        y1 = upper_left_y
        x2 = lower_right_x
        y2 = lower_right_y

        for j in range(k + 2):
            new_rectangle = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
            new_rectangle.attach_to(window)

            x1 = x1 + dx
            x2 = x2 + dx


    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

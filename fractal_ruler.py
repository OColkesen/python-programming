
"""
Drawing a fractal ruler

Author: Oğuzhan Çölkesen
"""
import turtle

def draw_ruler(height, width, level):
    """ Draws a fractal ruler of the desired height, width and level.

    Parameters:
        height - the height of the ruler (i.e., the height of the vertical ruler
                 "edge")
        width - the width of the ruler (i.e., the length of the middle tick).
        level - the recursive level of the ruler.

    Returns:
        None.
    """
    if level == 1:
        turtle.right(90)
        turtle.forward(height/2)
        turtle.left(90)
        turtle.forward(width)
        turtle.back(width)
        turtle.right(90)
        turtle.forward(height/2)
        
    else:
        draw_ruler(height/2, width/2, level-1)
        turtle.left(90)
        turtle.forward(width)
        turtle.back(width)
        draw_ruler(height/2, width/2, level-1)

def main():
    """ Tester function. """
    turtle.speed('fastest')
    draw_ruler(256, 128, 3)
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
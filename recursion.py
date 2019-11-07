"""
This program displays functions that implement recursive functions, such
as recursive delete of a certain character from a string, drawing a koch
snowflake, and drawing mondrian boxes.

Author: Oğuzhan Çölkesen
Time Spent: 4.5 hours 
"""

import turtle
from random import randint, choice

def recursive_delete(string_, character):
    """
    This function recursively removes a specified character by the user from
    a string given by the user. It finally returns the string with
    a specific character removed form it.
    
    Parameters:
        string_ - a string, which includes the text from which the user
                  wants to remove a character from.
                  
        character - a string, which should include a single character
                    that will be removed from the text in "string_"
        
    Returns:
        The function returns a string, which is the same version of
        the parameter string except that the parameter character is
        removed from it.
    """
    if len(string_) == 0:
        return ""
    
    first_character = string_[0]
    rest_of_string = string_[1:]
    
    if first_character == character:
        return recursive_delete(rest_of_string, character)
    
    return first_character + recursive_delete(rest_of_string, character)

def double_countdown(number):
    """
    This functions takes a number parameter and counts down from
    that number to zero. Then, it counts up back to the same number
    recursively. In the end, it returns a string, which demonstrates
    this double countdown.
    
    Parameters:
        number - an integer, which is the number that the user wants to start
                 and end the countdown from.

    Returns:
        The function returns a string, which shows the double countdown in
        a string form. For example, if the number parameter is 2, the function
        return "2 1 0 1 2".
    """
    if number == 0:
        return "0"
    
    string_number = str(number)
    return string_number + " " + double_countdown(number-1) + " " + string_number

def draw_koch_snowflake(length, level):
    """
    This function draws a koch snowflake of a specified length and level
    by calling a recursive drawing function for one side and arranging
    the angles of the turtle to draw all the sides. It displays the koch
    snowflake using turtle graphics.
    
    Parameters:
        length - an integer, which specifies the length of one side of the
                 snowflake. It is recommended that the length is a number,
                 which is a multiple of three.
        level - an integer, which specifies the level of the koch snowflake.
                The number of fractal geometry is defined with this parameter.
                1 is the least value and refers to a straight line. 
    
    Returns:
        The function does not return anything. It uses turtle graphics to
        display the koch snowflake.
    """
    draw_one_side_koch_snowflake(length, level)
    turtle.right(120)
    draw_one_side_koch_snowflake(length, level)
    turtle.right(120)
    draw_one_side_koch_snowflake(length, level)

    turtle.done()
    

def draw_one_side_koch_snowflake(length, level):
    """
    This helper function draws one side of a koch snowflake with a specified
    length and level recursively. It displays that one side of the koch
    snowflake using turtle graphics.
    
    Parameters:
        length - an integer, which specifies the length of one side of the
                 snowflake. It is recommended that the length is a number,
                 which is a multiple of three.
        level - an integer, which specifies the level of the koch snowflake.
                The number of fractal geometry is defined with this parameter.
                1 is the least value and refers to a straight line. 
    
    Returns:
        The function does not return anything. It uses turtle graphics to
        display one side of the koch snowflake.
    """
    if level == 1:
        turtle.forward(length)
        #every zero level addition is a straight line with "length".
    
    else:
        draw_one_side_koch_snowflake(length/3, level-1) #1st recursive statement
        turtle.left(60)
        draw_one_side_koch_snowflake(length/3, level-1) #2nd recursive statement
        turtle.left(240)
        draw_one_side_koch_snowflake(length/3, level-1)
        turtle.left(60)
        draw_one_side_koch_snowflake(length/3, level-1)
        
        #The code under the else statement creates recursive statements
        #within recursive statements. The idea is to decrease the level to 1
        #so that a small level 1 snowflake cna be drawn. When one little
        #level 1 snowflake is drawn all process needs to be repeated because
        #the function goes back to the first recursive statement with level 2.
        #After turning 60 degrees, the entire process of creating a level 2
        #snowflake has to be repeated to continue. After level 2 is done for
        #all the recursive statements, the entire process up until that point
        #is repated because the code returns back to the first recursive
        #statement with level 3. The process continues on.

def draw_mondrian(height, width, alignment):
    """
    This function draws a mondrian box with specified height, width, and
    alignment for the first division line. It draws the initial box at first
    and calls a recursive helper function to draw the mondrian boxes
    inside the drawn big box. It displays the mondrian boxes using turtle
    graphics.
    
    Parameters:
        height - an integer, which determines the height of the big box
                 drawn by the function.
        width - an integer, which determines the width in terms of pixels
                of the big box drawn by the function.
        alignment - a boolean variable, which determines whether the first
                    division is going to be horizontal or vertical. True
                    refers to vertical division and False refers to a
                    horizontal division.
    
    Returns:
        The function does not return anything. It uses turtle graphics to
        display the mondrian boxes.
    """
    turtle.speed(10)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    #Draws the main box.
    
    draw_mondrian_boxes(height, width, alignment)
    #Fills inside the main box.
    
    turtle.done()
    
def draw_mondrian_boxes(height, width, alignment):
    """
    This helper function recursively draws mondrian boxes with specified height,
    width, and alternatingly changing aligments for the division. Additionally,
    the function randomly colorizes some boxes with randomly picked colors.
    It displays the mondrian boxes using turtle graphics.
    
    Parameters:
        height - an integer, which determines the height of the box
                 drawn by the function.
        width - an integer, which determines the width in terms of pixels
                of the box drawn by the function.
        alignment - a boolean variable, which determines whether the division
                    of the box is going to be horizontal or vertical. True
                    refers to vertical division and False refers to a
                    horizontal division. The alignment is automatically
                    alternated in each recursion by the function
    
    Returns:
        The function does not return anything. It uses turtle graphics to
        display the mondrian boxes.
    """
    
    if (height > 40 and width > 60) or (height > 60 and width > 40):
        alignments_list = [True, False]
        random_alignment = choice(alignments_list)
        is_filling = randint(0,1)
        colors = ["red", "green", "blue", "violet", "black", "orange", "salmon",
                  "gold", "lime", "lightpink"]
        
        if alignment == True:
            division = randint(0, width)
            
            if (division < 40 and is_filling == 0) or (division < 60 and height < 60
                                                       and is_filling == 0):
                turtle.color("black", choice(colors))
                turtle.begin_fill()
                
            turtle.forward(division)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
            turtle.forward(division)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
            turtle.end_fill()
            
            draw_mondrian_boxes(height, division, False)
            turtle.forward(division)
            draw_mondrian_boxes(height, (width-division), False)
            turtle.back(division)
            
        elif alignment == False:
            division = randint(0, height)
            
            if (division < 40 and is_filling == 0)  or (division < 60 and height < 60
                                                        and is_filling == 0):
                turtle.color("black", choice(colors))
                turtle.begin_fill()
                
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(division)
            turtle.right(90)
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(division)
            turtle.right(90)
            turtle.end_fill()
            
            draw_mondrian_boxes(division, width, True)
            turtle.right(90)
            turtle.forward(division)
            turtle.right(270)
            draw_mondrian_boxes((height-division), width, True)
            turtle.left(90)
            turtle.forward(division)
            turtle.right(90)

"""
This program draws a city skyline, featuring the Empire State, a Pyramid,
Dutch buildings, a cubic building, and Chambers Building at Davidson
College.

Author: Marshall Yang and Oğuzhan Çölkesen
Time Spent: 5 hours
"""

import turtle
from math import sqrt 

def first_building():
    turtle.forward(50)
    
def go_to_start_point():
    turtle.penup()
    turtle.home()
    turtle.back(553)
    turtle.right(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.pendown()

def draw_horizon():
    go_to_start_point()
    turtle.forward(1106)

def draw_empire_state():
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(12)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(6)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(12)
    turtle.right(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(150)
    
def draw_pyramid():
    turtle.left(60)
    turtle.forward(150)
    turtle.right(120)
    turtle.forward(150)
    turtle.right(180)
    for i in range (1,5):
        turtle.forward(30)
        turtle.left(60)
        length = 150-(i*30)
        turtle.forward(length)
        turtle.back(length)
        turtle.right(60)
            
def draw_one_window():
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)

def draw_windows(x, y):
    for i in range (1, x):
        for j in range (1, y):
            turtle.pendown()
            draw_one_window()
            turtle.penup()
            if y > 2:
                if j < 2:
                    turtle.forward(30)
        if y==3:
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(180)
        if y==2:
            turtle.left(90)
            turtle.forward(30)
            turtle.right(90)
        turtle.pendown()

        
def draw_chambers_wing_roof():
    turtle.left(150)
    turtle.forward(76/sqrt(3))
    turtle.left(60)
    turtle.forward(76/sqrt(3))
    turtle.left(150)
    turtle.forward(76)
        
def draw_chambers_wing():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(76)
    draw_chambers_wing_roof()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    draw_windows(4,3)
                
def draw_chambers_dome():
    for i in range (1, 61):
        turtle.forward(1)
        turtle.right(3)

def draw_chambers_main_roof():
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(45)
    turtle.right(90)
    draw_chambers_dome()

def draw_chambers_columns():
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(10)
    for i in range (1,5):
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(9)
        turtle.left(90)
        turtle.forward(90)
        turtle.right(90)
        if i < 4:
            turtle.forward(18)
            turtle.right(90)

def draw_chambers_body():
    turtle.forward(240)
    turtle.penup()
    turtle.back(225)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    draw_windows(4,3)
    turtle.penup()
    turtle.forward(165)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    draw_windows(4,3)
    turtle.back(105)
    turtle.pendown()
    draw_chambers_columns()
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(180)
    draw_chambers_main_roof()
    
def draw_chambers():
    draw_chambers_wing()
    turtle.pendown()
    turtle.forward(60)
    draw_chambers_body()
    go_to_start_point()
    turtle.forward(316+495)
    draw_chambers_wing()
    
def draw_circle_window():
    turtle.pendown()
    for i in range (1, 95):
        turtle.forward(1)
        turtle.right(4)
    
def draw_cube_building():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    draw_circle_window()
    
def draw_one_dutch_building():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(30)
    turtle.forward(35)
    turtle.right(120)
    turtle.forward(35)
    turtle.right(30)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.right(180)
    draw_windows(4,2)
    turtle.back(10)
    turtle.forward(35)

def draw_dutch_buildings():
    for i in range (1,6):
        draw_one_dutch_building()
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)

def draw_pyramid_base_red():
    turtle.forward(120)
    turtle.color("red")
    turtle.forward(150)
    turtle.color("black")
    turtle.forward(637)

def draw_skyline():
    draw_horizon()
    go_to_start_point()
    turtle.forward(50)
    draw_empire_state()
    turtle.left(90)
    turtle.forward(20)
    turtle.color("red")
    draw_pyramid()
    turtle.color("black")
    go_to_start_point()
    turtle.forward(290)
    draw_dutch_buildings()
    go_to_start_point()
    turtle.forward(495)
    draw_chambers()
    go_to_start_point()
    draw_pyramid_base_red()
    draw_cube_building()
    go_to_start_point()
    turtle.done()

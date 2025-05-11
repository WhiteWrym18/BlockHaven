import turtle
from world import World
from Player import Player 
from blocktype import BlockType

def setup_render():               # Set Up Turtle Rendering 
    screen = turtle.Screen()
    screen.title("BlockHaven - A Simple Minecraft Clone")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    return screen

def render_world(world: World):       # Render the world grid using turtle.
    turtle.clear()
    for y, row in enumerate(world.grid):
        for x, block in enumerate(row):
            if block:
                turtle.penup
                turtle.goto(x*20 - 200, 200 - y *20)
                turtle.pendown()
                if block == BlockType.GRASS:
                    turtle.color("green")
                elif block == BlockType.DIRT:
                    turtle.color("brown")
                elif block == BlockType.STONE:
                    turtle.color("gray")
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(20)
                    turtle.right(90)
                turtle.end_fill()
    turtle.update()

def render_player(player: Player):      # Render the player on the grid.
    turtle.penup()
    turtle.goto(player.x*20 - 200, 200 - player.y*20)
    turtle.shape("circle")
    turtle.color("blue")
    turtle.stamp()
    turtle.update()
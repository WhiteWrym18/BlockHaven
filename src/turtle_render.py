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


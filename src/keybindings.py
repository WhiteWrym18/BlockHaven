from turtle import Screen
from player import Player
from blocktype import BlockType

def setup_keybindings(screen: Screen, player: Player):
    screen.listen()
    screen.onkey(lambda: player.move_up(), "Up")
    screen.onkey(lambda: player.move_down(), "Down")
    screen.onkey(lambda: player.move_left(), "Left")
    screen.onkey(lambda: player.move_right(), "Right")
    screen.onkey(lambda: player.place_block(BlockType.STONE), "space")
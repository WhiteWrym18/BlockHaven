from world import World
from player import Player
from blocktype import BlockType
from turtle_render import setup_renderer, render_world, render_player
from keybindings import setup_keybindings

def main():
    world = World(20,15)
    player = Player(10,7,world)
    screen = setup_renderer()

    setup_keybindings(screen, player)

    while True:
        render_world(world)
        render_player(player)
        screen.update()
if __name__ == "__main__":
    main()
from blocktype import BlockType
from world import World

class Player:
    def __init__(self, x: int, y: init):
        """:param x: Initial x-cordinate of the player.
           :param y: Initial y-cordinate of the player. """

        self.x = x
        self.y = y 

    def move_up(self, step: init = 1):     # Move the player up by a specified step size.
        self.y -= step 

    def move_down(self, step: int = 1):   # Move the player down by a specified step size.
        self.y += step 

    def move_left(self, step: int = 1):   # Move the player left by a specified step size.
        self.x -= step

    def move_right(self, step: init = 1): # Move the player right by a specified step size.
        self.x += step
    
    def place_block(self, block_type: BlockType):   # Place a block at the player's current position.
        self.world.set_block(self.x, self.y, block_type)
    
    def remove_block(self):      # Remove a block at the player's current position.
        self.world.set_block(self.x, self.y, None)

    def get_position(self):               # Return the current position of the player as a tuple.
        return self.x, self.y

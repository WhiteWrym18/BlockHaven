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
    
    def get_position(self):               # Return the current position of the player as a tuple.
        return self.x, self.y
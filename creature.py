'''
Author: HARRISON VERRIOS

This class handles storing the properties of the creature and allowing it to
interact with the world. The creature can control its movement and is able to
evolve and reproduce with others.
'''

# Class that handles all properties of the creature
class Creature:

    # The position of the creature in the world
    x: int = 0
    y: int = 0

    # Default constructor for setting up a creature at some location
    def __init__ (self, ecosystem) -> None:

        # Store the ecosystem
        self.ecosystem = ecosystem


    # Updates the simulation at some time
    def update (self, time: float, step: float) -> None:
        pass


    # Sets the creature to a new position
    def set_position (self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    
    # Returns the position of the creature
    def get_position (self) -> tuple:
        return (self.x, self.y)

    
    # Attempts to move in a particular direction and returns if it is true
    def move (self, delta_x: int, delta_y: int) -> bool:

        # Check if able to move
        if not self.ecosystem.can_move(self, delta_x, delta_y):
            return False

        # Add the offset
        self.x += delta_x
        self.y += delta_y

        # Return a success
        return True
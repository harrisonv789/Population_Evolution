'''
Author: HARRISON VERRIOS

This class handles the ecosystem of different species and specifies the environment
that the world can live in. All creatures are able to move around the environment and
can simulate evolution.
'''

# Import relevant classes
import random
from creature import Creature

# The class definition for the ecosystem
class Ecosystem:

    # The list of creatures that currently exist in the ecosystem
    creatures: list = []

    # The size of the ecosystem
    max_x: int = 50
    max_y: int = 50


    # The default constructor for setting up an ecosystem
    def __init__(self) -> None:
        pass

    
    # Creates a series of creatures
    def create (self, num_creatures: int = 0) -> None:

        # Create a list of creatures
        for _ in range (num_creatures):
            creature = Creature(self)
            self.creatures.append(creature)
            self.randomise_position(creature)


    # Updates the simulation at some time
    def update (self, time: float, step: float) -> None:

        # Updates all creatures
        for c in self.creatures:
            c.update(time, step)


    # Randomises the position of some creature in the world
    def randomise_position (self, creature: Creature) -> None:
        
        # Get random values in the ecosystem
        x: int = random.randint(0, self.max_x - 1)
        y: int = random.randint(0, self.max_y - 1)

        # Move the creature
        creature.set_position(x, y)

    
    # Checks if the creature is able to move
    def can_move (self, creature: Creature, delta_x: int, delta_y: int) -> bool:

        # Get the creatures position
        pos: tuple = creature.get_position()

        # Check if able to move in either axis
        able_x: bool = pos[0] + delta_x >= 0 and pos[0] + delta_x < self.max_x
        able_y: bool = pos[1] + delta_y >= 0 and pos[1] + delta_y < self.max_y

        # Retrurn a success if both are true
        return able_x and able_y
        

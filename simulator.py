'''
Author: HARRISON VERRIOS

This class handles simulating the system within the ecosystem and allows all events to
occur and trigger within the creatures. It also ensures that certain events occur at the
right time, such as evolution and can keep track of plotting.
'''

# Import relevant classes
from ecosystem import Ecosystem


# The class definition for the simulator
class Simulator:

    # The list of all ecosystems that can be simulated
    ecosystems: list = []

    # The current time
    time: float = 0.0
    step: float = 1.0
    max_time: float = 10.0

    # The default constructor for setting up an simulator
    def __init__(self) -> None:
        pass


    # Attaches an ecosystem to the simulation
    def attach (self, ecosystem: Ecosystem) -> None:
        self.ecosystems.append(ecosystem)


    # Executes the simulation and starts running the simulation
    def execute (self) -> None:
        print("Beginning simulation...")

        # Define the update loop
        while self.time < self.max_time:
            
            # Increase the time
            self.time += self.step

            # Update the simulation
            self.update(self.time, self.step)

    
    # Updates the simulation at some time
    def update (self, time: float, step: float) -> None:

        # Loops through each ecosystem
        for eco in self.ecosystems:
            eco.update(time, step)
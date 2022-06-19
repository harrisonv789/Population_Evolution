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

    # The default constructor for setting up an simulator
    def __init__(self) -> None:
        pass


    # Attaches an ecosystem to the simulation
    def attach (self, ecosystem: Ecosystem) -> None:
        self.ecosystems.append(ecosystem)


    # Executes the simulation and starts running the simulation
    def execute (self) -> None:
        print("Beginning simulation...")
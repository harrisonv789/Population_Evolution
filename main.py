#!/usr/bin/python3
'''
Author: HARRISON VERRIOS

This is the main execution file that runs when attempting to run the ecosystem
with all evolution. The parameter file sets up the ecosystem properties and then
the creatures are spawned correctly.
'''

# All imports
from ecosystem import Ecosystem
from simulator import Simulator

# This is the main function that starts up the simulation
def main ():
    
    # Creates the ecosystem 
    ecosystem = Ecosystem()
    ecosystem.create(10)

    # Attaches the ecosystem and begins simulation
    simulator = Simulator()
    simulator.attach(ecosystem)
    simulator.execute()


# When executed by the terminal
if __name__ == "__main__":
    main()
# Layout of the simulator

The simulator is composed of `xx` main components:
- the fixed step simulation
- the static map
- the agents
  - pedestrians
  - robots
  - micromobility vehicles
  - cars?
- The visualization

## simulation

The overall simulation is a fixed step simulation. The simulation is composed of a set of agents and a map. The agents are updated at each step of the simulation. The map is static and is not updated during the simulation.

## map

The map is a static map expressed as a json file.

## agents

The agents are the entities that are simulated. The agents are updated at each step of the simulation. The agents are composed of:
- pedestrians
- robots
- micromobility vehicles
- cars?
- ...

## visualization

the visualization will be in python and can be activated and deactivated
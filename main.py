from __builtins__ import *
from BaseCalculator import get_base_materials
from MixedFarm import mixed_farm

########################################################
todoList = [Unlocks.Grass, Unlocks.Grass, Unlocks.Grass]
mode = "mixed"  # Options: "hay", "wood", "mixed"

########################################################

def move_to_next():
    pass  # Implement movement logic here


clear()
# __main__
while True:
    goal = get_base_materials(todoList)
    
    if mode == "hay":
        pass
    eilf mode == "wood":
        pass
    elif mode == "mixed":
        mixed_farm(goal)
from __builtins__ import *

cycled = False

def move_to_next():
    """Moving to just North, and if it cycled, move to East once
    """
    global cycled
    # Check if at the North edge of the field before moving
    if get_pos_y() == get_world_size() - 1:
        cycled = True
    
    # Anyway, it should be moved to the North
    move(North)
    
    # Check if we've cycled through the line of the field
    if cycled:
        move(East)
        cycled = False

def mixed_farm(goal):
    # Calculate the needed Hay and Wood from the goal
    hay_needed = goal.get(Items.Hay, 0)
    wood_needed = goal.get(Items.Wood, 0)
    favorite = None  # No favorite crop initially
    
    # Initialize the field to record favorite crops
    field = []
    for _ in range(get_world_size()):
        field.append([] * get_world_size())
    
    # Initialize the ground type map
    ground = []
    for i in range(get_world_size()):
        ground.append([])
        for j in range(get_world_size()):
            ground[i].append(get_ground_type())
            move_to_next()
    
    # Start planting until both needs are satisfied
    while True:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                # If there is no favorited crop on this cell, plant based on needs
                if field[i][j] is None:
                    if can_harvest():       # Check if can harvest before
                        harvest()           # If can, harvest first
                    if ground[i][j] != Grounds.Grassland:   # Check if not grassland
                        till()                              # If not, till it
                        ground[i][j] = Grounds.Grassland    # Update ground type
                    # Now, plant!
                    if current_hay >= current_wood:
                        plant(Entities.Bush)    # Plant Bush for Wood
                    else:
                        pass                    # There is no need for Grass to be planted
                
                # If there is a favorited crop, plant it
                else:
                    if can_harvest():       # Check if can harvest before
                        harvest()           # If can, harvest first
                    if field[i][j] == Entities.Grass:       # Favorite: Grass
                        if ground[i][j] != Grounds.Grassland:   # Check if not grassland
                            till()                              # If not, till it
                            ground[i][j] = Grounds.Grassland    # Update ground type
                        pass                                    # There is no need for Grass to be planted
                    elif field[i][j] == Entities.Bush:      # Favorite: Bush
                        if ground[i][j] != Grounds.Grassland:   # Check if not grassland
                            till()                              # If not, till it
                            ground[i][j] = Grounds.Grassland    # Update ground type
                        plant(Entities.Bush)                    # Plant Bush for Wood
                    elif field[i][j] == Entities.Tree:      # Favorite: Tree
                        if ground[i][j] != Grounds.Grassland:   # Check if not grassland
                            till()                              # If not, till it
                            ground[i][j] = Grounds.Grassland    # Update ground type
                        plant(Entities.Tree)                    # Plant Tree for Wood
                    elif:                                   # Favorite: Carrot
                        if ground[i][j] != Grounds.Soil:        # Check if not soil
                            till()                              # If not, till it
                            ground[i][j] = Grounds.Soil         # Update ground type
                        plant(Entities.Carrot)                  # Plant Carrot for Carrot
                
                # Common post-planting actions
                use_item(Items.Water)   # Water the planted crop
                
                current_hay = num_items(Items.Hay)      # Update current Hay count
                current_wood = num_items(Items.Wood)    # Update current Wood count
                if hay_needed > current_hay and wood_needed > current_wood: # If both needs are satisfied,
                    break                                                   # break
                
                favorite, (x, y) = get_companion()
                field[x][y] = favorite  # Update the favorite crop in the field map
                move_to_next()          # Move to the next cell
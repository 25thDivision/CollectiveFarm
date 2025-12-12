from __builtins__ import *

# Dictionary mapping items to the entities that produce/plant them
#####################################################################
# This should be filled according to the actual names in the game ###
item_to_entity_map = {
    Items.Carrot: Entities.Carrot,
    Items.Pumpkin: Entities.Pumpkin,
    Items.Cactus: Entities.Cactus,
    # Other items needed should be added here
}
#####################################################################

def get_base_materials(target):
    """Gets the total base materials (Hay and Wood) needed to create the target entity

    Args:
        target (Items): The target entity/item to calculate the cost for

    Returns:
        dict: {Items.Hay: amount, Items.Wood: amount}
    """
    # 1. Get the immediate cost of the current target. (Takes 1 tick)
    immediate_cost = get_cost(target)
    
    # Return an empty dictionary if already max level or no cost
    if immediate_cost is None or len(immediate_cost) == 0:
        return {}

    # Initialize total base cost dictionary
    total_base_cost = {Items.Hay: 0, Items.Wood: 0}

    # 2. Iterate through components and convert them to base resources
    for item, amount in immediate_cost.items():
        
        # Case A: Base resources (Recursion termination condition)
        if item == Items.Hay or item == Items.Wood:
            total_base_cost[item] += amount
            
        # Case B: Intermediate items (Recursive call)
        else:
            # Find the entity corresponding to the item
            entity = item_to_entity_map.get(item)
            
            if entity:
                # Recursively calculate the base cost to create that entity
                sub_cost = get_base_materials(entity)
                
                # Multiply the sub-cost by the required amount and add to total
                for base_res, base_amount in sub_cost.items():
                    if base_res in total_base_cost:
                        total_base_cost[base_res] += base_amount * amount
            else:
                # Log or ignore if there is an unmapped item
                pass

    return total_base_cost
#q1

def find_flower(inventory, name):
    if inventory is None:
        return None
    if inventory.val == name:
        return True
    elif inventory.val < name:
        find_flower(inventory.left, name)
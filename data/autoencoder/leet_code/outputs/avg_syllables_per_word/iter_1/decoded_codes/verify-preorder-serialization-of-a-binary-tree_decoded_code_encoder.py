def is_valid_serialization(preorder: str) -> bool:
    nodes = preorder.split(',')
    slots = 1
    for node in nodes:
        if slots == 0:
            return False
        slots -= 1
        if node != '#':
            slots += 2
    return slots == 0
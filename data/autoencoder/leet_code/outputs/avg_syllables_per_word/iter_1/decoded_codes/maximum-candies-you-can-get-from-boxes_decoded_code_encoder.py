def max_candies(status, candies, keys_list, containedBoxes, initialBoxes):
    boxes = set(initialBoxes)
    keys = set()
    total = 0

    while True:
        progress = False
        for box in list(boxes):
            if status[box] == 1 or box in keys:
                total += candies[box]
                keys.update(keys_list[box])
                boxes.update(containedBoxes[box])
                boxes.remove(box)
                progress = True
        if not progress:
            break

    return total
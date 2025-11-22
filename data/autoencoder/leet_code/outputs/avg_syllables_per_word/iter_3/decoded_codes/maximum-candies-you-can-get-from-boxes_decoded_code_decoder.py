class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        boxes_we_have = set(initialBoxes)
        keys_we_have = set()
        total_candies = 0
        progress_made = True

        while progress_made:
            progress_made = False
            boxes_to_remove = set()
            for box in list(boxes_we_have):
                if status[box] == 1 or box in keys_we_have:
                    total_candies += candies[box]
                    keys_we_have.update(keys[box])
                    boxes_we_have.update(containedBoxes[box])
                    boxes_to_remove.add(box)
                    progress_made = True
            boxes_we_have.difference_update(boxes_to_remove)

        return total_candies
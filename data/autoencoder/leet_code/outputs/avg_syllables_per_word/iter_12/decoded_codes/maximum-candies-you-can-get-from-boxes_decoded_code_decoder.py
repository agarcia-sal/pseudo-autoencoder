from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes_we_have = set(initialBoxes)
        keys_we_have = set()
        total_candies = 0
        progress_made = True

        while progress_made:
            progress_made = False
            # Iterate over a snapshot of boxes_we_have to safely modify the set during iteration
            for box in list(boxes_we_have):
                if status[box] == 1 or box in keys_we_have:
                    total_candies += candies[box]
                    keys_we_have.update(keys[box])
                    boxes_we_have.update(containedBoxes[box])
                    boxes_we_have.remove(box)
                    progress_made = True
        return total_candies
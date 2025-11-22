from typing import List, Set

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        boxes_we_have: Set[int] = set(initialBoxes)
        keys_we_have: Set[int] = set()
        total_candies = 0
        progress_made = True

        while progress_made:
            progress_made = False
            # Iterate over a static list copy to avoid runtime error on modification during iteration
            for box in list(boxes_we_have):
                # Check if box is open (status[box] == 1) or we have a key to it
                if status[box] == 1 or box in keys_we_have:
                    total_candies += candies[box]
                    keys_we_have.update(keys[box])
                    boxes_we_have.update(containedBoxes[box])
                    boxes_we_have.discard(box)
                    progress_made = True

        return total_candies
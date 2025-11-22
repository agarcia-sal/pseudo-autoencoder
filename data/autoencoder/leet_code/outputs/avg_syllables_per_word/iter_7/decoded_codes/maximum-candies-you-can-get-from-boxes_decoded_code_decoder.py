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
            for box in list(boxes_we_have):
                if status[box] == 1 or box in keys_we_have:
                    total_candies += candies[box]
                    for key in keys[box]:
                        keys_we_have.add(key)
                    for b in containedBoxes[box]:
                        boxes_we_have.add(b)
                    boxes_we_have.remove(box)
                    progress_made = True
        return total_candies
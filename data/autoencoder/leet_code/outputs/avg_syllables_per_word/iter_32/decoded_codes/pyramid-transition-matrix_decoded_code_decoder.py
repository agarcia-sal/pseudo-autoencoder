from collections import defaultdict
from typing import List, Dict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # allowed_map[left][right] = list of possible 'top' chars
        allowed_map: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
        for rule in allowed:
            left, right, top = rule[0], rule[1], rule[2]
            allowed_map[left][right].append(top)

        def can_build_pyramid(current_bottom: str, current_top: str) -> bool:
            if len(current_bottom) == 1:
                return True
            if len(current_top) == len(current_bottom) - 1:
                # Completed the current top row, move upwards
                return can_build_pyramid(current_top, "")

            i = len(current_top)  # index for the next base pair to handle
            left, right = current_bottom[i], current_bottom[i + 1]
            if left in allowed_map and right in allowed_map[left]:
                for top_char in allowed_map[left][right]:
                    if can_build_pyramid(current_bottom, current_top + top_char):
                        return True
            return False

        return can_build_pyramid(bottom, "")
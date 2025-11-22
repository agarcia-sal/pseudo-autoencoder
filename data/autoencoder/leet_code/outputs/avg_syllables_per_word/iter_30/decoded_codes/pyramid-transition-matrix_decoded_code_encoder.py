from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map = defaultdict(lambda: defaultdict(list))
        for rule in allowed:
            left, right, top = rule[0], rule[1], rule[2]
            allowed_map[left][right].append(top)

        def can_build_pyramid(current_bottom: str, current_top: str) -> bool:
            if len(current_bottom) == 1:
                return True
            if len(current_top) == len(current_bottom) - 1:
                return can_build_pyramid(current_top, "")
            pos = len(current_top)
            left = current_bottom[pos]
            right = current_bottom[pos + 1]
            if left in allowed_map and right in allowed_map[left]:
                for top_char in allowed_map[left][right]:
                    if can_build_pyramid(current_bottom, current_top + top_char):
                        return True
            return False

        return can_build_pyramid(bottom, "")
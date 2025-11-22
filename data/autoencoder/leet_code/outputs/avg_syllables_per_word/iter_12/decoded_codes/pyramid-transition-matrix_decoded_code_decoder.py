from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        allowed_map = self.initialize_allowed_map()
        for rule in allowed:
            left, right, top = rule[0], rule[1], rule[2]
            allowed_map[left][right].append(top)

        def can_build_pyramid(current_bottom: str, current_top: str) -> bool:
            if len(current_bottom) == 1:
                return True
            if len(current_top) == len(current_bottom) - 1:
                return can_build_pyramid(current_top, "")
            idx = len(current_top)
            left = current_bottom[idx]
            right = current_bottom[idx + 1]
            if left in allowed_map and right in allowed_map[left]:
                for top in allowed_map[left][right]:
                    if can_build_pyramid(current_bottom, current_top + top):
                        return True
            return False

        return can_build_pyramid(bottom, "")

    def initialize_allowed_map(self):
        # default dict of dict of list: allowed_map[left][right] = list of top blocks
        return defaultdict(lambda: defaultdict(list))
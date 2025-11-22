from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        allowed_map = self.construct_allowed_map_with(allowed)

        def can_build_pyramid(current_bottom: str, current_top: str) -> bool:
            if len(current_bottom) == 1:
                return True
            if len(current_top) == len(current_bottom) - 1:
                return can_build_pyramid(current_top, "")

            left = current_bottom[len(current_top)]
            right = current_bottom[len(current_top) + 1]
            if left in allowed_map and right in allowed_map[left]:
                for top_element in allowed_map[left][right]:
                    if can_build_pyramid(current_bottom, current_top + top_element):
                        return True
            return False

        return can_build_pyramid(bottom, "")

    def construct_allowed_map_with(self, allowed: list[str]):
        map = defaultdict(lambda: defaultdict(list))
        for rule in allowed:
            left = rule[0]
            right = rule[1]
            top = rule[2]
            map[left][right].append(top)
        return map
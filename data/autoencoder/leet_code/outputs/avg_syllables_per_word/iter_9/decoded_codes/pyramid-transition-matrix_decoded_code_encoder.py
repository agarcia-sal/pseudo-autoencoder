from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        allowed_map = defaultdict(lambda: defaultdict(list))
        for rule in allowed:
            allowed_map[rule[0]][rule[1]].append(rule[2])

        def can_build_pyramid(current_bottom: str, current_top: list[str]) -> bool:
            if len(current_bottom) == 1:
                return True
            if len(current_top) == len(current_bottom) - 1:
                return can_build_pyramid("".join(current_top), [])
            i = len(current_top)
            left, right = current_bottom[i], current_bottom[i + 1]
            if left in allowed_map and right in allowed_map[left]:
                for top in allowed_map[left][right]:
                    if can_build_pyramid(current_bottom, current_top + [top]):
                        return True
            return False

        return can_build_pyramid(bottom, [])
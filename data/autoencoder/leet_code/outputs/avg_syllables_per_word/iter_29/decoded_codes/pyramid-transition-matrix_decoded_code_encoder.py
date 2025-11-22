from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: [str]) -> bool:
        # allowed_map[left][right] = list of possible tops
        allowed_map = defaultdict(lambda: defaultdict(list))
        for rule in allowed:
            left = rule[0]
            right = rule[1]
            top = rule[2]
            allowed_map[left][right].append(top)

        def can_build_pyramid(current_bottom: str, current_top: str) -> bool:
            if len(current_bottom) == 1:
                return True
            if len(current_top) == len(current_bottom) - 1:
                return can_build_pyramid(current_top, "")

            position = len(current_top)
            left = current_bottom[position]
            right = current_bottom[position + 1]

            if left in allowed_map and right in allowed_map[left]:
                for top in allowed_map[left][right]:
                    new_top = current_top + top
                    if can_build_pyramid(current_bottom, new_top):
                        return True
            return False

        return can_build_pyramid(bottom, "")
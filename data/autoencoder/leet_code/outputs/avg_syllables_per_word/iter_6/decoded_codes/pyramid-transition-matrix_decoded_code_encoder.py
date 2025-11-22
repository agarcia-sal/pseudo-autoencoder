from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        allowed_map = defaultdict(list)
        for rule in allowed:
            left, right, top = rule[0], rule[1], rule[2]
            allowed_map[(left, right)].append(top)

        def can_build_pyramid(current_bottom: str, current_top: str) -> bool:
            if len(current_bottom) == 1:
                return True
            if len(current_top) == len(current_bottom) - 1:
                return can_build_pyramid(current_top, '')
            i = len(current_top)
            pair = (current_bottom[i], current_bottom[i + 1])
            if pair in allowed_map:
                for top_block in allowed_map[pair]:
                    if can_build_pyramid(current_bottom, current_top + top_block):
                        return True
            return False

        return can_build_pyramid(bottom, '')
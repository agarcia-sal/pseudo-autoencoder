from typing import List

class Solution:
    def canCross(self, list_of_stones: List[int]) -> bool:
        if not list_of_stones or len(list_of_stones) < 2:
            return False

        stone_set = set(list_of_stones)
        last_stone = list_of_stones[-1]
        memo = {}

        def can_jump_to(position: int, jump: int) -> bool:
            if position == last_stone:
                return True
            if (position, jump) in memo:
                return memo[(position, jump)]
            for next_jump in (jump - 1, jump, jump + 1):
                if next_jump > 0 and position + next_jump in stone_set:
                    if can_jump_to(position + next_jump, next_jump):
                        memo[(position, jump)] = True
                        return True
            memo[(position, jump)] = False
            return False

        return can_jump_to(list_of_stones[0], 0)
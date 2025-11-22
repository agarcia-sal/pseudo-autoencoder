from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or len(stones) < 2:
            return False

        stone_set = set(stones)
        last_stone = stones[-1]
        memo = {}

        def can_jump_to(position: int, jump: int) -> bool:
            if position == last_stone:
                return True

            if (position, jump) in memo:
                return memo[(position, jump)]

            for next_jump in range(jump - 1, jump + 2):
                if next_jump > 0 and (position + next_jump) in stone_set:
                    if can_jump_to(position + next_jump, next_jump):
                        memo[(position, jump)] = True
                        return True

            memo[(position, jump)] = False
            return False

        return can_jump_to(stones[0], 0)
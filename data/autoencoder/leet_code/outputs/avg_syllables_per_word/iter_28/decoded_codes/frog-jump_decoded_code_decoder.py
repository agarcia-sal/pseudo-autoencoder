from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or len(stones) < 2:
            return False

        stone_set = set(stones)
        memo = {}

        def can_jump_to(position: int, jump: int) -> bool:
            if position == stones[-1]:
                return True
            if (position, jump) in memo:
                return memo[(position, jump)]

            for next_jump in (jump - 1, jump, jump + 1):
                if next_jump > 0 and (position + next_jump) in stone_set:
                    if can_jump_to(position + next_jump, next_jump):
                        memo[(position, jump)] = True
                        return True

            memo[(position, jump)] = False
            return False

        return can_jump_to(stones[1], stones[0])
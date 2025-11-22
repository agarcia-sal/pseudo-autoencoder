from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or len(stones) < 2:
            return False

        stone_set = set(stones)
        memo = {}
        last_stone = stones[-1]

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

        # The first jump must be from stones[0] to stones[1] with a jump size of stones[1] - stones[0]
        # but the pseudocode calls can_jump_to(stones[1], 0), which means starting at stones[1] with jump size 0
        # To align strictly with pseudocode, call can_jump_to with position=stones[1], jump=0
        # This matches exactly the pseudocode behavior.

        return can_jump_to(stones[1], 0)
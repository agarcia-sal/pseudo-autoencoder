class Solution:
    def canCross(self, list_of_stones):
        if not list_of_stones or len(list_of_stones) < 2:
            return False

        stone_set = set(list_of_stones)
        target = list_of_stones[-1]
        memo = {}

        def can_jump_to(position, jump):
            if position == target:
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

        return can_jump_to(list_of_stones[0], 0)
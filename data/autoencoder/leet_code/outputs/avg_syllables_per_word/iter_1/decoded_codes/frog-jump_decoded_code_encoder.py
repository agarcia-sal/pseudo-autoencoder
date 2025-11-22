def canCross(stones):
    if not stones or len(stones) < 2:
        return False
    stone_set = set(stones)
    memo = {}

    def can_jump_to(pos, jump):
        if pos == stones[-1]:
            return True
        if (pos, jump) in memo:
            return memo[(pos, jump)]

        for next_jump in [jump - 1, jump, jump + 1]:
            if next_jump > 0 and (pos + next_jump) in stone_set:
                if can_jump_to(pos + next_jump, next_jump):
                    memo[(pos, jump)] = True
                    return True

        memo[(pos, jump)] = False
        return False

    return can_jump_to(stones[0], 0)
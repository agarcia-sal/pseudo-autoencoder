def makesquare(matchsticks):
    sum_len = sum(matchsticks)
    if sum_len % 4 != 0:
        return False
    side_len = sum_len // 4
    matchsticks.sort(reverse=True)

    def can_form(sides, i):
        if i == len(matchsticks):
            return all(side == side_len for side in sides)
        for j in range(4):
            if sides[j] + matchsticks[i] <= side_len:
                sides[j] += matchsticks[i]
                if can_form(sides, i + 1):
                    return True
                sides[j] -= matchsticks[i]
            if sides[j] == 0:
                break
        return False

    return can_form([0, 0, 0, 0], 0)
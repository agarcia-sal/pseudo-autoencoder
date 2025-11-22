def can_i_win(maxInt, target):
    if sum(range(1, maxInt + 1)) < target:
        return False
    if target <= 0:
        return True

    memo = {}

    def canWin(total, used):
        if (total, used) in memo:
            return memo[(total, used)]
        for n in range(1, maxInt + 1):
            if used & (1 << n) == 0:
                if total + n >= target or not canWin(total + n, used | (1 << n)):
                    memo[(total, used)] = True
                    return True
        memo[(total, used)] = False
        return False

    return canWin(0, 0)
def canWin(state):
    memo = {}
    def can_win(s):
        if s in memo:
            return memo[s]
        for i in range(len(s) - 1):
            if s[i:i+2] == "++":
                new_s = s[:i] + "--" + s[i+2:]
                if not can_win(new_s):
                    memo[s] = True
                    return True
        memo[s] = False
        return False
    return can_win(state)
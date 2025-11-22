def stone_game(stones):
    prefix = [0]
    for stone in stones:
        prefix.append(prefix[-1] + stone)
    dp = prefix[-1]
    for i in range(len(stones) - 2, 0, -1):
        dp = max(dp, prefix[i] - dp)
    return dp
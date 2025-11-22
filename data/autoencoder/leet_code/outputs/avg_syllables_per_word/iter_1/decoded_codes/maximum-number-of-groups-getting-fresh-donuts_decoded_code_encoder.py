def max_happy_groups(batchSize, groups):
    if batchSize == 1:
        return len(groups)

    cnt = [0] * batchSize
    for g in groups:
        cnt[g % batchSize] += 1

    from functools import lru_cache

    @lru_cache(None)
    def dp(rem, counts):
        max_h = 0
        cnt_list = list(counts)
        for i in range(batchSize):
            if cnt_list[i] == 0:
                continue
            cnt_list[i] -= 1
            new_rem = (rem - i) % batchSize
            if rem == 0:
                happy = 1 + dp(new_rem, tuple(cnt_list))
            else:
                happy = dp(new_rem, tuple(cnt_list))
            max_h = max(max_h, happy)
            cnt_list[i] += 1
        return max_h

    return dp(0, tuple(cnt))
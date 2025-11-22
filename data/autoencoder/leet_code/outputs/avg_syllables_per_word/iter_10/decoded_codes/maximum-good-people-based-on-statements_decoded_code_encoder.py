class Solution:
    def maximumGood(self, statements):
        n = len(statements)
        max_good = 0
        for mask in range(1 << n):
            good = [bool(mask & (1 << j)) for j in range(n)]
            valid = True
            for j in range(n):
                if good[j]:
                    for k in range(n):
                        if (statements[j][k] == 0 and good[k]) or (statements[j][k] == 1 and not good[k]):
                            valid = False
                            break
                    if not valid:
                        break
            if valid:
                max_good = max(max_good, sum(good))
        return max_good
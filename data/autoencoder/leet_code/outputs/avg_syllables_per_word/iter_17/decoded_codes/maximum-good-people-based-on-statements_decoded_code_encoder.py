from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0

        for i in range(1 << n):
            good = [False] * n
            bad = [False] * n

            for j in range(n):
                if (i & (1 << j)) != 0:
                    good[j] = True
                else:
                    bad[j] = True

            valid = True
            for j in range(n):
                if good[j]:
                    for k in range(n):
                        if (good[k] and statements[j][k] == 0) or (bad[k] and statements[j][k] == 1):
                            valid = False
                            break
                    if not valid:
                        break

            if valid:
                max_good = max(max_good, sum(good))

        return max_good
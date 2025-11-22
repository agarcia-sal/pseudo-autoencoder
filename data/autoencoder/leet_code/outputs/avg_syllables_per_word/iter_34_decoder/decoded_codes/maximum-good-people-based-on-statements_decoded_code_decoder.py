from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0
        for i in range(1 << n):
            good = [False] * n
            bad = [False] * n
            for j in range(n):
                if (i & (1 << j)) == (1 << j):
                    good[j] = True
                else:
                    bad[j] = True

            valid = True
            for j in range(n):
                if not valid:
                    break
                if good[j]:
                    for k in range(n):
                        if (statements[j][k] == 0 and good[k]) or (statements[j][k] == 1 and bad[k]):
                            valid = False
                            break

            if valid:
                max_good = max(max_good, sum(good))
        return max_good
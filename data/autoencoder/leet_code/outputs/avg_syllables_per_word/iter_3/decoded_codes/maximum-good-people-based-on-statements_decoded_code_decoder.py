from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0
        for i in range(1 << n):
            valid = True
            for j in range(n):
                if (i >> j) & 1:
                    for k in range(n):
                        if statements[j][k] == 0 and ((i >> k) & 1):
                            valid = False
                            break
                        if statements[j][k] == 1 and not ((i >> k) & 1):
                            valid = False
                            break
                    if not valid:
                        break
            if valid:
                max_good = max(max_good, bin(i).count('1'))
        return max_good
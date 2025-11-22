from typing import List

class Solution:
    def findContestMatch(self, n: int) -> str:
        teams: List[str] = [str(i) for i in range(1, n + 1)]
        while n > 1:
            half = n // 2
            for i in range(half):
                teams[i] = "(" + teams[i] + "," + teams[n - 1 - i] + ")"
            n = half
        return teams[0]
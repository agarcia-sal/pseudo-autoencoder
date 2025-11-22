class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i) for i in range(1, n + 1)]
        while n > 1:
            for i in range(n // 2):
                teams[i] = '(' + teams[i] + ',' + teams[n - 1 - i] + ')'
            n //= 2
        return teams[0]
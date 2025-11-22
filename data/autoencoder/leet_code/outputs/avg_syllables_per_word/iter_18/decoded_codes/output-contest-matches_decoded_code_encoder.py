class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i + 1) for i in range(n)]
        while n > 1:
            for i in range(n // 2):
                teams[i] = f"({teams[i]},{teams[n - 1 - i]})"
            n //= 2
        return teams[0]
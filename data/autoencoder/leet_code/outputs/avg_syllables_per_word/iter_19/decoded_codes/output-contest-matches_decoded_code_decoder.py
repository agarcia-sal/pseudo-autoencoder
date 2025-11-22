class Solution:
    def findContestMatch(self, n):
        teams = list(map(str, range(1, n + 1)))
        while n > 1:
            for i in range(n // 2):
                teams[i] = "(" + teams[i] + "," + teams[n - 1 - i] + ")"
            n //= 2
        return teams[0]
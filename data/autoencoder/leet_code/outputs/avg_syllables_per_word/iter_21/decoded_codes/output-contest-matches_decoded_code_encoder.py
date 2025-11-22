class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = self.initialize_teams(n)
        while n > 1:
            teams = self.pair_teams(teams, n)
            n //= 2
        return teams[0]

    def initialize_teams(self, n: int) -> list[str]:
        return [str(i) for i in range(1, n + 1)]

    def pair_teams(self, teams: list[str], n: int) -> list[str]:
        new_teams = []
        half = n // 2
        for i in range(half):
            paired_team = f"({teams[i]},{teams[n - 1 - i]})"
            new_teams.append(paired_team)
        return new_teams
class Solution:
    def findContestMatch(self, number_of_teams: int) -> str:
        # Initialize list of team strings from "1" to str(number_of_teams)
        list_of_teams = [str(i) for i in range(1, number_of_teams + 1)]
        n = number_of_teams
        while n > 1:
            for i in range(n // 2):
                # Pair team i with team n-1-i inside parentheses
                list_of_teams[i] = "(" + list_of_teams[i] + "," + list_of_teams[n - 1 - i] + ")"
            n //= 2
        return list_of_teams[0]
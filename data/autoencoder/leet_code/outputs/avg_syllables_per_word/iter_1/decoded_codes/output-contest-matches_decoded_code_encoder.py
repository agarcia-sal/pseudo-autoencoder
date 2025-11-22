def generate_matchup(n):
    teams = [str(i+1) for i in range(n)]
    while n > 1:
        for i in range(n // 2):
            teams[i] = "(" + teams[i] + "," + teams[n - 1 - i] + ")"
        n = n // 2
    return teams[0]
def longest_course_time(n, relations, time):
    graph = {i: [] for i in range(1, n+1)}
    for prereq, course in relations:
        graph[course].append(prereq)

    memo = [-1] * (n + 1)

    def dfs(c):
        if memo[c] != -1:
            return memo[c]
        max_prev = 0
        if graph[c]:
            max_prev = max(dfs(p) for p in graph[c])
        memo[c] = max_prev + time[c-1]
        return memo[c]

    return max(dfs(c) for c in range(1, n+1))
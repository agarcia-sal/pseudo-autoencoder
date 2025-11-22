def max_profit_assignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
    worker = sorted(worker)
    max_profit = 0
    best_profit = 0
    i = 0
    for ability in worker:
        while i < len(jobs) and jobs[i][0] <= ability:
            best_profit = max(best_profit, jobs[i][1])
            i += 1
        max_profit += best_profit
    return max_profit
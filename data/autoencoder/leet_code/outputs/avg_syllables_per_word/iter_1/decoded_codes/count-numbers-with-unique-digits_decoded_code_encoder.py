def calculate_count(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    count = 10
    available = 9
    choices = 9
    for i in range(2, n + 1):
        choices *= available
        count += choices
        available -= 1
    return count
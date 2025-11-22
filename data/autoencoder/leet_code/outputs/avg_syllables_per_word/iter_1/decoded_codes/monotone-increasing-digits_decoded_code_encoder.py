def process_number(n):
    D = list(str(n))
    marker = len(D)
    for i in range(len(D)-1, 0, -1):
        if D[i] < D[i-1]:
            D[i-1] = str(int(D[i-1]) - 1)
            marker = i
    for i in range(marker, len(D)):
        D[i] = '9'
    return int("".join(D))
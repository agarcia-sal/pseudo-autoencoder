from collections import Counter

def get_hint(secret, guess):
    bulls, cows = 0, 0
    secret_cnt, guess_cnt = Counter(), Counter()

    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            secret_cnt[s] += 1
            guess_cnt[g] += 1

    for d in secret_cnt:
        cows += min(secret_cnt[d], guess_cnt[d])

    return f"{bulls}A{cows}B"
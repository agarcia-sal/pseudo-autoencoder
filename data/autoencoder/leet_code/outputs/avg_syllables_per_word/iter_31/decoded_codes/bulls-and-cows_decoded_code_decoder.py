from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_count = Counter()
        guess_count = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1

        cows = sum(min(secret_count[d], guess_count.get(d, 0)) for d in secret_count)

        return f"{bulls}A{cows}B"
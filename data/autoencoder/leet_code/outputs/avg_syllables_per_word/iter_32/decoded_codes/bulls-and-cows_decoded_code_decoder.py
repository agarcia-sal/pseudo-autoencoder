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

        cows = 0
        for digit in secret_count:
            cows += min(secret_count[digit], guess_count.get(digit, 0))

        return f"{bulls}A{cows}B"
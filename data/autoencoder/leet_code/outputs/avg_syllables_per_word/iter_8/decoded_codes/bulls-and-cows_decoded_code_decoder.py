from collections import defaultdict

class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        secret_count = defaultdict(int)
        guess_count = defaultdict(int)

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1

        for digit in secret_count:
            cows += min(secret_count[digit], guess_count[digit])

        return str(bulls) + "A" + str(cows) + "B"
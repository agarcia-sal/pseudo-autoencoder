class Solution:
    def maximumGood(self, statements):
        n = len(statements)
        max_good = 0

        for i in range(1 << n):
            good = [False] * n
            bad = [False] * n

            for j in range(n):
                if i & (1 << j):
                    good[j] = True
                else:
                    bad[j] = True

            valid = True
            for j in range(n):
                if good[j]:
                    for k in range(n):
                        # If j is good and statement[j][k] is 0 but k is good -> invalid
                        # If j is good and statement[j][k] is 1 but k is bad -> invalid
                        if (statements[j][k] == 0 and good[k]) or (statements[j][k] == 1 and bad[k]):
                            valid = False
                            break
                    if not valid:
                        break

            if valid:
                max_good = max(max_good, sum(good))

        return max_good
from math import inf

class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        n = len(jobs)
        subset_sums = self.initialize_subset_sums(n, jobs)

        def dp(teams: int, mask: int) -> int:
            if teams == 1:
                return subset_sums[mask]
            res = inf
            submask = mask
            while submask:
                candidate = max(dp(teams - 1, mask ^ submask), subset_sums[submask])
                if candidate < res:
                    res = candidate
                submask = (submask - 1) & mask
            return res

        return dp(k, (1 << n) - 1)

    def initialize_subset_sums(self, n: int, jobs: list[int]) -> list[int]:
        subset_sums = [0] * (1 << n)
        for i in range(n):
            for mask in range(1 << i):
                subset_sums[mask | (1 << i)] = subset_sums[mask] + jobs[i]
        return subset_sums
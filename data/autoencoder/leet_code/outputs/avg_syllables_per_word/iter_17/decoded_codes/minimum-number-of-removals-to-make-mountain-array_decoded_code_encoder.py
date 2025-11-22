class Solution:
    def minimumMountainRemovals(self, list_of_numbers):
        n = len(list_of_numbers)
        lis = [1] * n  # Longest Increasing Subsequence length ending at i
        for i in range(n):
            for j in range(i):
                if list_of_numbers[i] > list_of_numbers[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        lds = [1] * n  # Longest Decreasing Subsequence length starting at i
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if list_of_numbers[i] > list_of_numbers[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        max_mountain_len = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)

        return n - max_mountain_len
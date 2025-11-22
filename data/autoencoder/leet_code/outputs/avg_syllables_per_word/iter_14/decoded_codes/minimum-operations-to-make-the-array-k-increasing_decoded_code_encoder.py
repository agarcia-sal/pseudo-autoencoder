from bisect import bisect_right

class Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        def longest_increasing_subsequence(subarr: list[int]) -> int:
            lis = []
            for num in subarr:
                if not lis or num >= lis[-1]:
                    lis.append(num)
                else:
                    # Find position to replace element strictly greater than num
                    pos = bisect_right(lis, num)
                    lis[pos] = num
            return len(lis)

        total_operations = 0
        n = len(arr)

        for start in range(k):
            subarr = [arr[i] for i in range(start, n, k)]
            lis_length = longest_increasing_subsequence(subarr)
            total_operations += len(subarr) - lis_length

        return total_operations
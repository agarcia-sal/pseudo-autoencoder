from bisect import bisect_right

class Solution:
    def kIncreasing(self, arr, k):
        def longest_increasing_subsequence(subarr):
            lis = []
            for number in subarr:
                if not lis or number >= lis[-1]:
                    lis.append(number)
                else:
                    pos = bisect_right(lis, number)
                    lis[pos] = number
            return len(lis)

        total_operations = 0
        n = len(arr)

        for start in range(k):
            subarr = []
            for i in range(start, n, k):
                subarr.append(arr[i])
            lis_length = longest_increasing_subsequence(subarr)
            total_operations += len(subarr) - lis_length

        return total_operations
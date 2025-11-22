import bisect

class Solution:
    def kIncreasing(self, arr, k):
        def longest_increasing_subsequence(subarr):
            lis = []
            for num in subarr:
                if not lis or num >= lis[-1]:
                    lis.append(num)
                else:
                    pos = bisect.bisect_right(lis, num)
                    lis[pos] = num
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
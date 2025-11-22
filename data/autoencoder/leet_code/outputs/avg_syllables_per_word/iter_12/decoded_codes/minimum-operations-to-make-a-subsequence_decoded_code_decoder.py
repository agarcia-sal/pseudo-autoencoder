import bisect

class Solution:
    def minOperations(self, target, arr):
        index_map = {}
        for index in range(len(target)):
            value = target[index]
            index_map[value] = index

        transformed_arr = []
        for value in arr:
            if value in index_map:
                transformed_arr.append(index_map[value])

        lis = []
        for num in transformed_arr:
            pos = bisect.bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        return len(target) - lcs_length
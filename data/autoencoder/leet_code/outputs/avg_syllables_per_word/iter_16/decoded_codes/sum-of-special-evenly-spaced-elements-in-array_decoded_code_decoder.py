class Solution:
    def solve(self, nums, queries):
        MODULO = 10**9 + 7
        count_of_numbers = len(nums)

        if not queries:
            return []

        maximum_step = max(y for _, y in queries)

        prefix_sums = [[0] * count_of_numbers for _ in range(maximum_step + 1)]

        for step in range(1, maximum_step + 1):
            for index in range(count_of_numbers - 1, -1, -1):
                if index + step < count_of_numbers:
                    prefix_sums[step][index] = nums[index] + prefix_sums[step][index + step]
                else:
                    prefix_sums[step][index] = nums[index]

        answer_list = []
        for x, y in queries:
            answer_list.append(prefix_sums[y][x] % MODULO)

        return answer_list
class Solution:
    def solve(self, list_of_numbers, list_of_queries):
        modulo_constant = 10**9 + 1
        number_count = len(list_of_numbers)

        maximum_step_size = max(y for _, y in list_of_queries)
        prefix_sums = [[0] * number_count for _ in range(maximum_step_size + 1)]

        for step_size in range(1, maximum_step_size + 1):
            for index in range(number_count - 1, -1, -1):
                if index + step_size < number_count:
                    prefix_sums[step_size][index] = list_of_numbers[index] + prefix_sums[step_size][index + step_size]
                else:
                    prefix_sums[step_size][index] = list_of_numbers[index]

        answer_list = []
        for x_value, y_value in list_of_queries:
            answer_list.append(prefix_sums[y_value][x_value] % modulo_constant)

        return answer_list
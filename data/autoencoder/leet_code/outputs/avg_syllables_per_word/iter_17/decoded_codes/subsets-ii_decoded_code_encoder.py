class Solution:
    def subsetsWithDup(self, list_of_numbers):
        list_of_numbers.sort()
        result_list = []
        current_subset = []

        def dfs(index):
            if index >= len(list_of_numbers):
                result_list.append(current_subset[:])
                return

            current_subset.append(list_of_numbers[index])
            dfs(index + 1)

            current_subset.pop()
            while index + 1 < len(list_of_numbers) and list_of_numbers[index] == list_of_numbers[index + 1]:
                index += 1
            dfs(index + 1)

        dfs(0)
        return result_list
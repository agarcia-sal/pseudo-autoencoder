class Solution:
    def subsetsWithDup(self, list_of_numbers):
        list_of_numbers.sort()
        result = []
        subset = []

        def dfs(index):
            if index >= len(list_of_numbers):
                result.append(subset.copy())
                return

            subset.append(list_of_numbers[index])
            dfs(index + 1)
            subset.pop()

            while index + 1 < len(list_of_numbers) and list_of_numbers[index] == list_of_numbers[index + 1]:
                index += 1
            dfs(index + 1)

        dfs(0)
        return result
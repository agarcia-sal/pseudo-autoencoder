class Solution:
    def triangleNumber(self, list_of_numbers: list[int]) -> int:
        list_of_numbers.sort()
        count = 0
        n = len(list_of_numbers)

        for index_k in range(n - 1, 1, -1):
            index_i, index_j = 0, index_k - 1
            while index_i < index_j:
                if list_of_numbers[index_i] + list_of_numbers[index_j] > list_of_numbers[index_k]:
                    count += index_j - index_i
                    index_j -= 1
                else:
                    index_i += 1

        return count
class Solution:
    def triangleNumber(self, list_of_numbers):
        list_of_numbers.sort()
        count = 0
        n = len(list_of_numbers)

        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if list_of_numbers[i] + list_of_numbers[j] > list_of_numbers[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
class Solution:
    def findMaxConsecutiveOnes(self, list_of_numbers):
        maximum_count = 0
        current_count = 0
        zero_count = 0
        left = 0

        for right in range(len(list_of_numbers)):
            if list_of_numbers[right] == 1:
                current_count += 1
            elif zero_count < 1:
                zero_count += 1
                current_count += 1
            else:
                maximum_count = max(maximum_count, current_count)
                while zero_count == 1:
                    if list_of_numbers[left] == 0:
                        zero_count -= 1
                    current_count -= 1
                    left += 1
                current_count += 1

        maximum_count = max(maximum_count, current_count)
        return maximum_count
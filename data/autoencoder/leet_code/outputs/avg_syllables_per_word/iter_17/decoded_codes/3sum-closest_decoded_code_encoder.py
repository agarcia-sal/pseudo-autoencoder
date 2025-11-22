class Solution:
    def threeSumClosest(self, list_of_numbers, target_value):
        list_of_numbers.sort()
        closest_sum = float('inf')

        for index in range(len(list_of_numbers) - 2):
            left_pointer = index + 1
            right_pointer = len(list_of_numbers) - 1

            while left_pointer < right_pointer:
                current_sum = (list_of_numbers[index] +
                               list_of_numbers[left_pointer] +
                               list_of_numbers[right_pointer])

                if abs(current_sum - target_value) < abs(closest_sum - target_value):
                    closest_sum = current_sum

                if current_sum < target_value:
                    left_pointer += 1
                elif current_sum > target_value:
                    right_pointer -= 1
                else:
                    return current_sum

        return closest_sum
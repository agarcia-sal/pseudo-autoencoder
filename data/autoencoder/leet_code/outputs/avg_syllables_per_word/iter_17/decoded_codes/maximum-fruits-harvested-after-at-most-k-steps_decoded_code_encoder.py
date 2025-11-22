class Solution:
    def maxTotalFruits(self, list_of_fruits, start_position, maximum_steps):
        maximum_total_fruits = 0
        current_total_fruits = 0
        left_pointer = 0

        for right_pointer in range(len(list_of_fruits)):
            position = list_of_fruits[right_pointer][0]
            amount = list_of_fruits[right_pointer][1]
            current_total_fruits += amount

            while (left_pointer <= right_pointer and not (
                start_position - maximum_steps <= list_of_fruits[left_pointer][0] <= start_position + maximum_steps and
                start_position - maximum_steps <= list_of_fruits[right_pointer][0] <= start_position + maximum_steps and
                min(abs(list_of_fruits[right_pointer][0] - start_position),
                    abs(list_of_fruits[left_pointer][0] - start_position)) +
                list_of_fruits[right_pointer][0] - list_of_fruits[left_pointer][0] <= maximum_steps
            )):
                current_total_fruits -= list_of_fruits[left_pointer][1]
                left_pointer += 1

            maximum_total_fruits = max(maximum_total_fruits, current_total_fruits)

        return maximum_total_fruits
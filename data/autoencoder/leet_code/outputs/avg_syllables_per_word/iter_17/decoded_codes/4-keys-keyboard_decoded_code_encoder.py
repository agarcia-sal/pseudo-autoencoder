class Solution:
    def maxA(self, number_of_key_presses: int) -> int:
        if number_of_key_presses <= 3:
            return number_of_key_presses

        dp_array = self.initialize_dp_array(number_of_key_presses)

        for index in range(1, 4):
            dp_array[index] = index

        for index in range(4, number_of_key_presses + 1):
            for prev in range(index - 3, 0, -1):
                product = dp_array[prev] * (index - prev - 1)
                if product > dp_array[index]:
                    dp_array[index] = product

        return dp_array[number_of_key_presses]

    def initialize_dp_array(self, number_of_elements: int) -> list:
        # Initialize dp array with zeros; one-based indexing convenience by allocating number_of_elements + 1
        return [0] * (number_of_elements + 1)
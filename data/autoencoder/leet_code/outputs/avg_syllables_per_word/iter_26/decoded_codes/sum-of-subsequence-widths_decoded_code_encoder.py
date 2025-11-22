class Solution:
    def sumSubseqWidths(self, list_of_numbers):
        MODULO = 10**9 + 1
        list_of_numbers.sort()
        count_of_numbers = len(list_of_numbers)
        total_sum = 0
        power_list = [1] * count_of_numbers

        for index in range(1, count_of_numbers):
            power_list[index] = (power_list[index - 1] * 2) % MODULO

        for index in range(count_of_numbers):
            total_sum = (total_sum + list_of_numbers[index] * power_list[index] - list_of_numbers[index] * power_list[count_of_numbers - index - 1]) % MODULO

        return total_sum
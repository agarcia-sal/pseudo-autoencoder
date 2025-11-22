class Solution:
    def sumSubseqWidths(self, list_of_numbers):
        MODULO_MODULUS = 10**9 + 7
        list_of_numbers.sort()
        length_of_list = len(list_of_numbers)
        total_sum = 0
        power_list = [1] * length_of_list

        for index in range(1, length_of_list):
            power_list[index] = (power_list[index - 1] * 2) % MODULO_MODULUS

        for index in range(length_of_list):
            total_sum += list_of_numbers[index] * (power_list[index] - power_list[length_of_list - index - 1])
            total_sum %= MODULO_MODULUS

        return total_sum
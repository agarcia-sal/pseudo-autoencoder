class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half = num[:n // 2]

        half_list = self.convert_string_to_list(half)
        k = -1
        l = -1

        for i in range(len(half_list) - 2, -1, -1):
            if half_list[i] < half_list[i + 1]:
                k = i
                break

        if k == -1:
            return ""

        for i in range(len(half_list) - 1, k, -1):
            if half_list[i] > half_list[k]:
                l = i
                break

        self.swap_elements(half_list, k, l)
        half_list = half_list[: k + 1] + sorted(half_list[k + 1 :])

        new_half = self.convert_list_to_string(half_list)

        if n % 2 == 0:
            return new_half + new_half[::-1]
        else:
            return new_half + num[n // 2] + new_half[::-1]

    def convert_string_to_list(self, input_string: str) -> list:
        return list(input_string)

    def convert_list_to_string(self, input_list: list) -> str:
        return "".join(input_list)

    def swap_elements(self, input_list: list, first_index: int, second_index: int) -> None:
        temp = input_list[first_index]
        input_list[first_index] = input_list[second_index]
        input_list[second_index] = temp
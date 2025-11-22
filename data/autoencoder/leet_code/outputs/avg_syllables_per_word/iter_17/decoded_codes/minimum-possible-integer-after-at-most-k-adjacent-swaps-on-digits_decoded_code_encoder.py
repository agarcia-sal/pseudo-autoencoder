class Solution:
    def minInteger(self, num: str, k: int) -> str:
        digit_list = list(num)
        n = len(digit_list)

        while k > 0:
            swapped = False

            for index in range(n - 1):
                if digit_list[index] > digit_list[index + 1]:
                    min_digit = '9'
                    min_index = -1

                    limit = min(index + k + 1, n)
                    for position in range(index, limit):
                        if digit_list[position] < min_digit:
                            min_digit = digit_list[position]
                            min_index = position

                    self.perform_swap(digit_list, index, min_index)

                    k -= min_index - index
                    swapped = True
                    break

            if not swapped:
                break

        return "".join(digit_list)

    def perform_swap(self, digit_list: list, start_index: int, end_index: int):
        prefix_list = digit_list[start_index:end_index]
        moved_element = digit_list[end_index]
        replacement_list = [moved_element] + prefix_list
        digit_list[start_index:end_index + 1] = replacement_list
class Solution:
    def strobogrammaticInRange(self, low_string: str, high_string: str) -> int:
        def generate_strobogrammatic(current_length: int, total_length: int) -> list[str]:
            if current_length == 0:
                return [""]
            if current_length == 1:
                return ["0", "1", "8"]

            middle_strings = generate_strobogrammatic(current_length - 2, total_length)
            result_list = []

            for middle_string in middle_strings:
                if current_length != total_length:
                    result_list.append("0" + middle_string + "0")
                result_list.append("1" + middle_string + "1")
                result_list.append("6" + middle_string + "9")
                result_list.append("8" + middle_string + "8")
                result_list.append("9" + middle_string + "6")

            return result_list

        def count_strobogrammatic(low: str, high: str) -> int:
            total_count = 0
            for length_index in range(len(low), len(high) + 1):
                for number_string in generate_strobogrammatic(length_index, length_index):
                    if (length_index == len(low) and number_string < low) or \
                       (length_index == len(high) and number_string > high):
                        continue
                    if length_index > 1 and number_string[0] == '0':
                        continue  # Leading zeros invalid except for single digit "0"
                    total_count += 1
            return total_count

        return count_strobogrammatic(low_string, high_string)
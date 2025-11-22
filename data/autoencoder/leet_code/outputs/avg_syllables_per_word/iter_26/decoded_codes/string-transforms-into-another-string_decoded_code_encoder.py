class Solution:
    def canConvert(self, input_string_one: str, input_string_two: str) -> bool:
        if input_string_one == input_string_two:
            return True

        conversion_map = {}

        for ch1, ch2 in zip(input_string_one, input_string_two):
            if ch1 in conversion_map:
                if conversion_map[ch1] != ch2:
                    return False
            else:
                conversion_map[ch1] = ch2

        if len(set(input_string_two)) == 26:
            return False

        return True
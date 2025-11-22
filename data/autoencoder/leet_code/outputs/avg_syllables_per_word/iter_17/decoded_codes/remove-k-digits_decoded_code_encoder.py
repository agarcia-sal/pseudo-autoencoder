class Solution:
    def removeKdigits(self, num_string: str, k_integer: int) -> str:
        stack_list = []

        for digit_character in num_string:
            while k_integer > 0 and stack_list and stack_list[-1] > digit_character:
                stack_list.pop()
                k_integer -= 1
            stack_list.append(digit_character)

        if k_integer == 0:
            final_stack_list = stack_list
        else:
            final_stack_list = stack_list[:-k_integer]

        result_string = ''.join(final_stack_list).lstrip('0')

        return result_string if result_string else '0'
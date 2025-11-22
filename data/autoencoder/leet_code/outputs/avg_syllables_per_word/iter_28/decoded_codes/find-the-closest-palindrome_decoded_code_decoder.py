from typing import Set, Optional

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            integer_value = int(n)
            result_value = integer_value - 1
            return str(result_value)

        candidates: Set[int] = set()

        ten_to_length = 10 ** length
        ten_to_length_minus_one = 10 ** (length - 1)
        candidate_value_low = ten_to_length - 1
        candidate_value_high = ten_to_length + 1
        candidates.add(candidate_value_high)
        candidates.add(candidate_value_low)

        prefix_length = (length + 1) // 2
        prefix_string = n[:prefix_length]
        prefix = int(prefix_string)

        for i in (-1, 0, 1):
            new_prefix_value = prefix + i
            if new_prefix_value < 0:
                continue
            new_prefix_string = str(new_prefix_value)
            if len(new_prefix_string) < prefix_length:  # Pad with leading zeros if needed
                new_prefix_string = new_prefix_string.zfill(prefix_length)
            if length % 2 == 0:
                reversed_part = new_prefix_string[::-1]
                candidate_string = new_prefix_string + reversed_part
            else:
                reversed_part = new_prefix_string[:-1][::-1]
                candidate_string = new_prefix_string + reversed_part
            candidate_integer = int(candidate_string)
            candidates.add(candidate_integer)

        original_number = int(n)
        candidates.discard(original_number)

        minimal_difference = float('inf')
        closest_palindrome: Optional[int] = None
        for candidate in candidates:
            difference = abs(candidate - original_number)
            if (
                difference < minimal_difference or
                (difference == minimal_difference and (closest_palindrome is None or candidate < closest_palindrome))
            ):
                minimal_difference = difference
                closest_palindrome = candidate

        return str(closest_palindrome)
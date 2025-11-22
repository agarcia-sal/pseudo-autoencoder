class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            numeric_value = int(n)
            result_value = numeric_value - 1
            return str(result_value)

        candidates = set()

        ten_power_length = 10 ** length
        candidates.add(ten_power_length + 1)

        ten_power_length_minus_one = 10 ** (length - 1)
        candidates.add(ten_power_length_minus_one - 1)

        half_length = (length + 1) // 2
        prefix = int(n[:half_length])

        for i in (-1, 0, 1):
            modified_prefix_value = prefix + i
            modified_prefix_string = str(modified_prefix_value)

            if length % 2 == 0:
                reversed_part = modified_prefix_string[::-1]
                candidate_string = modified_prefix_string + reversed_part
            else:
                reversed_part = modified_prefix_string[:-1][::-1]  # exclude last char, reverse the rest
                candidate_string = modified_prefix_string + reversed_part

            candidate_numeric = int(candidate_string)
            candidates.add(candidate_numeric)

        original_number = int(n)
        candidates.discard(original_number)

        minimum_difference = float('inf')
        closest_palindrome = None

        for candidate in candidates:
            absolute_difference = abs(candidate - original_number)
            if (absolute_difference < minimum_difference or
                (absolute_difference == minimum_difference and (closest_palindrome is None or candidate < closest_palindrome))):
                minimum_difference = absolute_difference
                closest_palindrome = candidate

        return str(closest_palindrome)
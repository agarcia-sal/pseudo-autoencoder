class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            numeric_value = int(n)
            return str(numeric_value - 1)

        candidates = set()

        power_length = 10 ** length
        power_length_minus_one = 10 ** (length - 1)

        candidates.add(power_length + 1)
        candidates.add(power_length_minus_one - 1)

        prefix = int(n[: (length + 1) // 2])

        for i in (-1, 0, 1):
            new_prefix_numeric = prefix + i
            new_prefix = str(new_prefix_numeric)
            if length % 2 == 0:
                reversed_part = new_prefix[::-1]
                candidate_string = new_prefix + reversed_part
            else:
                substring_reversed = new_prefix[:-1][::-1]
                candidate_string = new_prefix + substring_reversed
            candidate_numeric = int(candidate_string)
            candidates.add(candidate_numeric)

        original_number = int(n)
        candidates.discard(original_number)

        closest = None
        smallest_distance = float('inf')
        for number in candidates:
            current_distance = abs(number - original_number)
            if (
                current_distance < smallest_distance or
                (current_distance == smallest_distance and (closest is None or number < closest))
            ):
                closest = number
                smallest_distance = current_distance

        return str(closest)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            integer_value = int(n)
            result = integer_value - 1
            return str(result)

        candidates = set()

        ten_power_length = 10 ** length
        candidates.add(ten_power_length + 1)

        ten_power_length_minus_one = 10 ** (length - 1)
        candidates.add(ten_power_length_minus_one - 1)

        half_length = (length + 1) // 2
        prefix = int(n[:half_length])

        for i in range(-1, 2):
            new_prefix_value = prefix + i
            new_prefix_string = str(new_prefix_value)
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

        def distance_key(x):
            return (abs(x - original_number), x)

        closest = min(candidates, key=distance_key)
        return str(closest)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            result_number = int(n) - 1
            return str(result_number)

        candidates = set()

        ten_power_length_plus_one = 10 ** (length + 1)
        candidates.add(ten_power_length_plus_one)

        ten_power_length_minus_one = 10 ** (length - 1) - 1
        candidates.add(ten_power_length_minus_one)

        prefix_length = (length + 1) // 2
        prefix = int(n[:prefix_length])

        for i in (-1, 0, 1):
            new_prefix_number = prefix + i
            new_prefix = str(new_prefix_number)

            if length % 2 == 0:
                reversed_part = new_prefix[::-1]
                candidate_string = new_prefix + reversed_part
            else:
                reversed_part = new_prefix[:-1][::-1]
                candidate_string = new_prefix + reversed_part

            # Avoid candidates with length different than original n 
            # due to prefix increment/decrement removing leading digit(s)
            if len(candidate_string) == length:
                candidate_int = int(candidate_string)
                candidates.add(candidate_int)
            else:
                # Candidate length differs from original; still add to set as int
                candidates.add(int(candidate_string))

        original_number = int(n)
        candidates.discard(original_number)

        closest = min(candidates, key=lambda x: (abs(x - original_number), x))

        return str(closest)
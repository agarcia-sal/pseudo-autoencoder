class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            numeric_value = int(n)
            result_numeric = numeric_value - 1
            return str(result_numeric)

        candidates = set()

        candidate_one = 10 ** (length + 1)
        candidate_two = 10 ** (length - 1) - 1
        candidates.add(candidate_one)
        candidates.add(candidate_two)

        prefix = int(n[: (length + 1) // 2])
        for i in range(-1, 2):
            new_prefix_numeric = prefix + i
            new_prefix = str(new_prefix_numeric)
            if length % 2 == 0:
                reversed_part = new_prefix[::-1]
                candidate_string = new_prefix + reversed_part
            else:
                substring_for_reverse = new_prefix[:-1][::-1]
                candidate_string = new_prefix + substring_for_reverse

            candidate_numeric = int(candidate_string)
            candidates.add(candidate_numeric)

        original_number = int(n)
        candidates.discard(original_number)

        closest = min(candidates, key=lambda x: (abs(x - original_number), x))
        return str(closest)
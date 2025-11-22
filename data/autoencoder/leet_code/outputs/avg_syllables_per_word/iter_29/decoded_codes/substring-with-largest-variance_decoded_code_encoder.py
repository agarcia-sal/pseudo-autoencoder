from itertools import permutations

class Solution:
    def largestVariance(self, s: str) -> int:
        def calculate_variance(substring: str, character_a: str, character_b: str) -> int:
            maximum_variance = 0
            count_character_a = 0
            count_character_b = 0
            has_character_b_occurred = False
            first_character_b_flag = False

            for char in substring:
                if char == character_a:
                    count_character_a += 1
                elif char == character_b:
                    count_character_b += 1
                    has_character_b_occurred = True

                if count_character_b > 0:
                    maximum_variance = max(maximum_variance, count_character_a - count_character_b)
                elif count_character_b == 0 and first_character_b_flag:
                    maximum_variance = max(maximum_variance, count_character_a - 1)

                if count_character_b > count_character_a:
                    count_character_a = 0
                    count_character_b = 0
                    first_character_b_flag = has_character_b_occurred

            return maximum_variance

        maximum_variance_overall = 0
        unique_characters = set(s)

        for character_a, character_b in permutations(unique_characters, 2):
            if character_a == character_b:
                continue
            maximum_variance_overall = max(maximum_variance_overall, calculate_variance(s, character_a, character_b))

        return maximum_variance_overall
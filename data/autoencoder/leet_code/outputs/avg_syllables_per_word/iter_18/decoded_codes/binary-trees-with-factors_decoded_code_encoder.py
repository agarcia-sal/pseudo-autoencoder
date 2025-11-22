from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MODULO_DIVISOR = 10**9 + 7
        arr.sort()
        dynamic_mapping = {}
        for number in arr:
            dynamic_mapping[number] = 1
        for i in range(len(arr)):
            number = arr[i]
            for j in range(i):
                factor_candidate = arr[j]
                if number % factor_candidate == 0:
                    complementary_factor = number // factor_candidate
                    if complementary_factor in dynamic_mapping:
                        dynamic_mapping[number] = (dynamic_mapping[number] + dynamic_mapping[factor_candidate] * dynamic_mapping[complementary_factor]) % MODULO_DIVISOR
        total_count = sum(dynamic_mapping.values()) % MODULO_DIVISOR
        return total_count
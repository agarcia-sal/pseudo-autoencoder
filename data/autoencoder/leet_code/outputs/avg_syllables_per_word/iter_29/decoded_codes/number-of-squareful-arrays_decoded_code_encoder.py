from collections import Counter
from math import isqrt
from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(number: int) -> bool:
            root = isqrt(number)
            return root * root == number

        count = Counter(nums)
        length = len(nums)

        def backtrack(path: List[int], current_count: Counter) -> int:
            if len(path) == length:
                return 1
            answer = 0
            for num in current_count:
                if current_count[num] > 0 and (not path or is_square(path[-1] + num)):
                    current_count[num] -= 1
                    answer += backtrack(path + [num], current_count)
                    current_count[num] += 1
            return answer

        return backtrack([], count)
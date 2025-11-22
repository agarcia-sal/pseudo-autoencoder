from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result = [i + 1 for i in range(len(s) + 1)]
        start = 0
        for end in range(len(s) + 1):
            if end == len(s) or s[end] == 'I':
                result[start:end + 1] = reversed(result[start:end + 1])
                start = end + 1
        return result
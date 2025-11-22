from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # Initialize result as a list of numbers from 1 to len(s)+1
        result = [i + 1 for i in range(len(s) + 1)]

        start = 0
        for end in range(len(s) + 1):
            # When at the end or current char is 'I'
            if end == len(s) or s[end] == 'I':
                # Reverse the segment from start to end inclusive in result
                segment = result[start:end+1]
                reversed_segment = segment[::-1]
                for offset, val in enumerate(reversed_segment):
                    result[start + offset] = val
                start = end + 1

        return result
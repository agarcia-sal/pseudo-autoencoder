class Solution:
    def findPermutation(self, s: str) -> list[int]:
        result = [i + 1 for i in range(len(s) + 1)]
        start = 0
        for end_index in range(len(s) + 1):
            if end_index == len(s) or s[end_index] == 'I':
                segment_length = end_index - start + 1
                # Reverse the segment in result from start to end_index inclusive
                reversed_segment = [result[start + segment_length - 1 - pos] for pos in range(segment_length)]
                for pos in range(segment_length):
                    result[start + pos] = reversed_segment[pos]
                start = end_index + 1
        return result
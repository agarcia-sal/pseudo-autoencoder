class Solution:
    def findPermutation(self, string_s: str) -> list[int]:
        result = self.InitializeResultArray(string_s)
        start = 0
        n = len(string_s)
        for end in range(n + 1):
            if end == n or string_s[end] == 'I':
                self.ReverseSegment(result, start, end)
                start = end + 1
        return result

    def InitializeResultArray(self, string_s: str) -> list[int]:
        n = len(string_s)
        return [i + 1 for i in range(n + 1)]

    def ReverseSegment(self, list_values: list[int], start_index: int, end_index: int) -> None:
        segment_length = end_index - start_index + 1
        # Reverse the segment within list_values in place
        for i in range(segment_length // 2):
            list_values[start_index + i], list_values[end_index - i] = list_values[end_index - i], list_values[start_index + i]
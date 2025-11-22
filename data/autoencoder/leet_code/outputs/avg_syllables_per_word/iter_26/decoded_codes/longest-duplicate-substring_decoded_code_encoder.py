class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(length: int) -> str:
            seen = set()
            for i in range(len(s) - length + 1):
                substring = s[i:i+length]
                if substring in seen:
                    return substring
                seen.add(substring)
            return ""

        left_pointer, right_pointer = 1, len(s) - 1
        longest_substring = ""

        while left_pointer <= right_pointer:
            middle_value = (left_pointer + right_pointer) // 2
            candidate_substring = search(middle_value)
            if candidate_substring != "":
                longest_substring = candidate_substring
                left_pointer = middle_value + 1
            else:
                right_pointer = middle_value - 1

        return longest_substring
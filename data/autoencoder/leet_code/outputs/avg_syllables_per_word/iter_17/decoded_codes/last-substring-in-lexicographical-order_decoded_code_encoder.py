class Solution:
    def lastSubstring(self, s: str) -> str:
        length_n = len(s)
        maximum_character = max(s)
        maximum_indices = self.getIndicesOfMaxChar(s, maximum_character, length_n)
        maximum_substring = ""
        for start_position in maximum_indices:
            current_substring = s[start_position:]
            if current_substring > maximum_substring:
                maximum_substring = current_substring
        return maximum_substring

    def getIndicesOfMaxChar(self, s: str, max_character: str, length_n: int) -> list[int]:
        list_of_indices = []
        for index in range(length_n):
            if s[index] == max_character:
                list_of_indices.append(index)
        return list_of_indices
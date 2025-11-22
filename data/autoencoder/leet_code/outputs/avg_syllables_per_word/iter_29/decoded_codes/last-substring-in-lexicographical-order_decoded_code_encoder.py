class Solution:
    def lastSubstring(self, string_s: str) -> str:
        length_n = len(string_s)
        maximum_character = max(string_s)
        collection_of_maximum_indices = [i for i, ch in enumerate(string_s) if ch == maximum_character]

        maximum_substring = ""
        for start_index in collection_of_maximum_indices:
            current_substring = string_s[start_index:]
            if current_substring > maximum_substring:
                maximum_substring = current_substring

        return maximum_substring
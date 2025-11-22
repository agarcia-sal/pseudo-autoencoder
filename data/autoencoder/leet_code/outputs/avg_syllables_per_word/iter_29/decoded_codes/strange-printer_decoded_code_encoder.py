class Solution:
    def strangePrinter(self, string_of_characters: str) -> int:
        def dp(start_index: int, end_index: int, memo_dictionary: dict) -> int:
            if start_index > end_index:
                return 0
            if (start_index, end_index) in memo_dictionary:
                return memo_dictionary[(start_index, end_index)]
            result = dp(start_index, end_index - 1, memo_dictionary) + 1
            for index_k in range(start_index, end_index):
                if string_of_characters[index_k] == string_of_characters[end_index]:
                    candidate_value = dp(start_index, index_k, memo_dictionary) + dp(index_k + 1, end_index - 1, memo_dictionary)
                    if candidate_value < result:
                        result = candidate_value
            memo_dictionary[(start_index, end_index)] = result
            return result

        return dp(0, len(string_of_characters) - 1, {})
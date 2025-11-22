class Solution:
    def wordBreak(self, input_string: str, list_of_words: list[str]) -> list[str]:
        wordSet = set(list_of_words)
        memo = {}

        def backtrack(current_start: int) -> list[str]:
            if current_start in memo:
                return memo[current_start]
            if current_start == len(input_string):
                return [""]

            result_list = []

            for end_position in range(current_start + 1, len(input_string) + 1):
                word_substring = input_string[current_start:end_position]
                if word_substring in wordSet:
                    for sentence in backtrack(end_position):
                        if sentence == "":
                            result_list.append(word_substring)
                        else:
                            result_list.append(word_substring + " " + sentence)

            memo[current_start] = result_list
            return result_list

        return backtrack(0)
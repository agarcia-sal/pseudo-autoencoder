class Solution:
    def letterCasePermutation(self, string_input: str) -> list[str]:
        def dfs(index_position: int) -> None:
            if index_position >= len(temporary_list):
                answer_list.append("".join(temporary_list))
                return
            dfs(index_position + 1)
            char = temporary_list[index_position]
            if char.isalpha():
                # Toggle case using bitwise XOR with 32
                temporary_list[index_position] = chr(ord(char) ^ 32)
                dfs(index_position + 1)
                temporary_list[index_position] = char  # revert to original

        temporary_list = list(string_input)
        answer_list = []
        dfs(0)
        return answer_list
class Solution:
    def letterCasePermutation(self, input_string: str) -> list[str]:
        def dfs(index: int):
            if index >= len(temporary_list):
                result_list.append("".join(temporary_list))
                return
            dfs(index + 1)
            if temporary_list[index].isalpha():
                temporary_list[index] = chr(ord(temporary_list[index]) ^ 32)
                dfs(index + 1)
                temporary_list[index] = chr(ord(temporary_list[index]) ^ 32)  # revert the change

        temporary_list = list(input_string)
        result_list = []
        dfs(0)
        return result_list
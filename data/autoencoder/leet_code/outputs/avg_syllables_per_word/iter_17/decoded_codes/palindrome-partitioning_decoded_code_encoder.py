class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, path: list[str]) -> None:
            if start == len(s):
                result.append(path)
                return
            for end_index in range(start + 1, len(s) + 1):
                substr = s[start:end_index]
                if is_palindrome(substr):
                    backtrack(end_index, path + [substr])

        result = []
        backtrack(0, [])
        return result
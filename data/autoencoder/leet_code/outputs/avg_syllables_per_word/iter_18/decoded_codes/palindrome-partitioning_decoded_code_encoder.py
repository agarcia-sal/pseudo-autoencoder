class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, path: list[str]) -> None:
            if start == len(s):
                result.append(path)
                return
            for end_position in range(start + 1, len(s) + 1):
                substring = s[start:end_position]
                if is_palindrome(substring):
                    backtrack(end_position, path + [substring])

        result = []
        backtrack(0, [])
        return result
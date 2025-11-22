class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, path: list[str]) -> None:
            if start == len(s):
                result.append(path)
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result: list[list[str]] = []
        backtrack(0, [])
        return result
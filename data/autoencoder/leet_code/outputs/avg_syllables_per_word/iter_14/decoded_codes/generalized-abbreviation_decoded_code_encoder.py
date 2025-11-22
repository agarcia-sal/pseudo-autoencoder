class Solution:
    def generateAbbreviations(self, word: str) -> list[str]:
        def backtrack(index: int, path: list[str], count: int) -> None:
            if index == len(word):
                if count > 0:
                    path.append(str(count))
                result.append(''.join(path))
                if count > 0:
                    path.pop()
                return
            # Option 1: Abbreviate current character (increment count)
            backtrack(index + 1, path, count + 1)
            # Option 2: Keep current character
            if count > 0:
                path.append(str(count))
            path.append(word[index])
            backtrack(index + 1, path, 0)
            path.pop()
            if count > 0:
                path.pop()

        result = []
        backtrack(0, [], 0)
        return result
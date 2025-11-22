from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def backtrack(index: int, path: List[str], count: int) -> None:
            if index == len(word):
                if count > 0:
                    path.append(str(count))
                result.append(''.join(path))
                if count > 0:
                    path.pop()
                return
            # Abbreviate current character (increase count)
            backtrack(index + 1, path, count + 1)
            # Keep current character (append count if > 0, then char)
            if count > 0:
                path.append(str(count))
            path.append(word[index])
            backtrack(index + 1, path, 0)
            path.pop()
            if count > 0:
                path.pop()

        result: List[str] = []
        backtrack(0, [], 0)
        return result
from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def backtrack(index: int, path: List[str], count: int) -> None:
            if index == len(word):
                if count > 0:
                    path.append(str(count))
                result.append("".join(path))
                if count > 0:
                    path.pop()
                return

            if count > 0:
                path.append(str(count))
                path.append(word[index])
                backtrack(index + 1, path, 0)
                path.pop()
                path.pop()
            else:
                path.append(word[index])
                backtrack(index + 1, path, 0)
                path.pop()

            backtrack(index + 1, path, count + 1)

        result = []
        backtrack(0, [], 0)
        return result
from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def backtrack(index: int, path: List[str], count: int) -> None:
            if index == len(word):
                # If count > 0, append it before joining to path result
                if count > 0:
                    path.append(str(count))
                result.append(''.join(path))
                # Backtrack path to original state before returning
                if count > 0:
                    path.pop()
                return

            # Option 1: abbreviate the current character, increment count
            backtrack(index + 1, path, count + 1)

            # Option 2: keep the current character
            if count > 0:
                path.append(str(count))
            path.append(word[index])
            backtrack(index + 1, path, 0)
            # Backtrack path to original state after recursive call
            path.pop()
            if count > 0:
                path.pop()

        result: List[str] = []
        backtrack(0, [], 0)
        return result
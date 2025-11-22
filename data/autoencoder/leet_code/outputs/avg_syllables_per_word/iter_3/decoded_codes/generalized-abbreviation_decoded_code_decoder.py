class Solution:
    def generateAbbreviations(self, word: str) -> list[str]:
        def backtrack(index: int, path: list[str], count: int):
            if index == len(word):
                if count > 0:
                    path.append(str(count))
                result.append("".join(path))
                if count > 0:
                    path.pop()
                return
            if count > 0:
                backtrack(index + 1, path + [str(count), word[index]], 0)
            else:
                backtrack(index + 1, path + [word[index]], 0)
            backtrack(index + 1, path, count + 1)

        result = []
        backtrack(0, [], 0)
        return result
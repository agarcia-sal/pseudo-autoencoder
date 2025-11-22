class Solution:
    def generateAbbreviations(self, word):
        def backtrack(index, path, count):
            if index == len(word):
                if count > 0:
                    path.append(str(count))
                result.append(''.join(path))
                if count > 0:
                    path.pop()
                return
            # Abbreviate current character
            backtrack(index + 1, path, count + 1)
            # Keep current character
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
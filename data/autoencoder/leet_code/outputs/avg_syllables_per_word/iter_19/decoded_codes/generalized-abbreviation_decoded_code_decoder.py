class Solution:
    def generateAbbreviations(self, word):
        def backtrack(index, path, count):
            if index == len(word):
                if count > 0:
                    path.append(str(count))
                result.append("".join(path))
                if count > 0:
                    path.pop()
                return
            # If count > 0, append count before adding current char
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
            # Abbreviate current character by incrementing count
            backtrack(index + 1, path, count + 1)

        result = []
        backtrack(0, [], 0)
        return result
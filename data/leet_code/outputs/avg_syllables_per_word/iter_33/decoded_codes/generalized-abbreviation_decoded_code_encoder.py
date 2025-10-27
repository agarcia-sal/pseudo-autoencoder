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
            if count > 0:
                # Append count before the current char
                backtrack(index + 1, path + [str(count), word[index]], 0)
            else:
                # Append the current char
                backtrack(index + 1, path + [word[index]], 0)
            # Increase the count (abbreviate this char)
            backtrack(index + 1, path, count + 1)

        result = []
        backtrack(0, [], 0)
        return result
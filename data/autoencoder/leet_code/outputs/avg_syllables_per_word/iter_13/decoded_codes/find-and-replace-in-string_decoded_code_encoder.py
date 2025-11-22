class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0

        for index, source, target in replacements:
            result.append(s[prev_end:index])
            if s[index:index+len(source)] == source:
                result.append(target)
                prev_end = index + len(source)
            else:
                result.append(s[index:index+len(source)])
                prev_end = index + len(source)

        result.append(s[prev_end:])
        return ''.join(result)
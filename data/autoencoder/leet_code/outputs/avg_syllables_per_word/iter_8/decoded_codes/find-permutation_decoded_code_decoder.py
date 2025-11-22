class Solution:
    def findPermutation(self, s):
        result = list(range(1, len(s) + 2))
        start = 0
        for end in range(len(s) + 1):
            if end == len(s) or s[end] == 'I':
                result[start:end+1] = result[start:end+1][::-1]
                start = end + 1
        return result
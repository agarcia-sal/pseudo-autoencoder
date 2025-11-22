class Solution:
    def splitIntoFibonacci(self, num):
        def backtrack(start, path):
            if start == len(num) and len(path) >= 3:
                return path
            for end in range(start + 1, len(num) + 1):
                if num[start] == '0' and end > start + 1:
                    continue
                next_num = int(num[start:end])
                if next_num >= 2**31:
                    break
                if len(path) < 2 or next_num == path[-1] + path[-2]:
                    result = backtrack(end, path + [next_num])
                    if result:
                        return result
            return []
        return backtrack(0, [])
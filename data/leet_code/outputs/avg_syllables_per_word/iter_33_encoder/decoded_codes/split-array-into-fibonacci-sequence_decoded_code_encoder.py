class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        LIMIT = 2 ** 31

        def backtrack(start: int, path: list[int]) -> list[int]:
            if start == len(num) and len(path) >= 3:
                return path
            for end in range(start + 1, len(num) + 1):
                # Skip numbers with leading zeroes
                if num[start] == '0' and end > start + 1:
                    continue
                next_num = int(num[start:end])
                if next_num >= LIMIT:
                    break
                if len(path) < 2 or next_num == path[-1] + path[-2]:
                    result = backtrack(end, path + [next_num])
                    if result:
                        return result
            return []

        return backtrack(0, [])
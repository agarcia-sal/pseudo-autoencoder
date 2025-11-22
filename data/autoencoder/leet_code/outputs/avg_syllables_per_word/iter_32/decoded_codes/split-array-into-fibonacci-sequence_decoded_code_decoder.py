from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        MAX_INT = 2 ** 31

        def backtrack(start: int, path: List[int]) -> List[int]:
            if start == len(num) and len(path) >= 3:
                return path

            for end in range(start + 1, len(num) + 1):
                # Leading zero check: if current number has leading zero and length > 1, skip
                if num[start] == '0' and end > start + 1:
                    continue

                next_num = int(num[start:end])
                if next_num >= MAX_INT:
                    break  # No need to consider longer numbers if this exceeded limit

                # If path has less than 2 numbers, no sum check required
                if len(path) < 2 or next_num == path[-1] + path[-2]:
                    result = backtrack(end, path + [next_num])
                    if result:
                        return result

            return []

        return backtrack(0, [])
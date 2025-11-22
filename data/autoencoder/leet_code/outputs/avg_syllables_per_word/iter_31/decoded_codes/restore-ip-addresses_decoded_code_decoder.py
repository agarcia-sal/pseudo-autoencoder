from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool:
            if len(segment) == 1:
                return True
            if segment[0] != '0' and int(segment) <= 255:
                return True
            return False

        def backtrack(start: int, path: List[str]) -> None:
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])

        result = []
        backtrack(0, [])
        return result
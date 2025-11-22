from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool:
            # segment is valid if:
            # length == 1, or
            # length > 1 and segment does not start with '0' and int(segment) <= 255
            return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

        def backtrack(start: int, path: List[str]):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start+length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])

        result: List[str] = []
        backtrack(0, [])
        return result
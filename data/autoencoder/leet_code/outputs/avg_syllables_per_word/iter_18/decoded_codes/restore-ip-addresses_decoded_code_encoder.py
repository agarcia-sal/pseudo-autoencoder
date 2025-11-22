class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def is_valid(segment: str) -> bool:
            # Valid if length is 1 (single digit) or no leading zero and <= 255
            return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

        def backtrack(start: int, path: list[str]) -> None:
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])

        result: list[str] = []
        backtrack(0, [])
        return result
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def is_valid(segment: str) -> bool:
            # Segment is valid if its length is 1 (single digit)
            # or if it does not start with '0' and integer value <= 255
            if len(segment) == 1:
                return True
            elif segment[0] != '0' and int(segment) <= 255:
                return True
            else:
                return False

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

        result = []
        backtrack(0, [])
        return result
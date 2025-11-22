class Solution:
    def restoreIpAddresses(self, string_s: str) -> list[str]:
        def is_valid(segment: str) -> bool:
            return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

        def backtrack(integer_start: int, list_path: list[str]) -> None:
            if len(list_path) == 4:
                if integer_start == len(string_s):
                    result.append('.'.join(list_path))
                return
            for integer_length in range(1, 4):
                if integer_start + integer_length <= len(string_s):
                    string_segment = string_s[integer_start:integer_start + integer_length]
                    if is_valid(string_segment):
                        backtrack(integer_start + integer_length, list_path + [string_segment])

        result = []
        backtrack(0, [])
        return result
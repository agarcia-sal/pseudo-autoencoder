class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def split_string_by_dot(version: str) -> list[str]:
            return version.split('.')

        def convert_string_to_integer(s: str) -> int:
            return int(s)

        v1_revisions = split_string_by_dot(version1)
        v2_revisions = split_string_by_dot(version2)
        max_length = max(len(v1_revisions), len(v2_revisions))

        for index in range(max_length):
            v1 = convert_string_to_integer(v1_revisions[index]) if index < len(v1_revisions) else 0
            v2 = convert_string_to_integer(v2_revisions[index]) if index < len(v2_revisions) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
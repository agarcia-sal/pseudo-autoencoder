from typing import List

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')
        max_length = max(len(v1_revisions), len(v2_revisions))

        for i in range(max_length):
            v1 = int(v1_revisions[i]) if i < len(v1_revisions) else 0
            v2 = int(v2_revisions[i]) if i < len(v2_revisions) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
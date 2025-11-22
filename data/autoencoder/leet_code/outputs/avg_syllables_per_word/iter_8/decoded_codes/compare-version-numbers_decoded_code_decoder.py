class Solution:
    def compareVersion(self, version1, version2):
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')

        max_length = max(len(v1_revisions), len(v2_revisions))

        for i in range(max_length):
            if i < len(v1_revisions):
                v1 = int(v1_revisions[i])
            else:
                v1 = 0
            if i < len(v2_revisions):
                v2 = int(v2_revisions[i])
            else:
                v2 = 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0
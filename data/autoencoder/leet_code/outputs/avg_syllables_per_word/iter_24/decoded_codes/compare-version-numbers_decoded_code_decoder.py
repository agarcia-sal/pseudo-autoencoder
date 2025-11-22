class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list_of_parts_one = version1.split('.')
        list_of_parts_two = version2.split('.')
        maximum_length = max(len(list_of_parts_one), len(list_of_parts_two))
        for index in range(maximum_length):
            revision_one = int(list_of_parts_one[index]) if index < len(list_of_parts_one) else 0
            revision_two = int(list_of_parts_two[index]) if index < len(list_of_parts_two) else 0
            if revision_one < revision_two:
                return -1
            elif revision_one > revision_two:
                return 1
        return 0
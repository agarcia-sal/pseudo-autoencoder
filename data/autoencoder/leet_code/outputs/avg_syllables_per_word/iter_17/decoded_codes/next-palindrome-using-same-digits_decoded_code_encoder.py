class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half = num[:n // 2]

        half_list = self.listFromString(half)
        k = -1
        l = -1
        # Find the largest index k such that half_list[k] < half_list[k+1]
        for index in range(len(half_list) - 2, -1, -1):
            if half_list[index] < half_list[index + 1]:
                k = index
                break
        if k == -1:
            return ""

        # Find the largest index l > k such that half_list[l] > half_list[k]
        for index in range(len(half_list) - 1, k, -1):
            if half_list[index] > half_list[k]:
                l = index
                break

        self.swapElements(half_list, k, l)
        half_list = self.sortSublistFromPosition(half_list, k + 1)
        new_half = self.joinListWithEmptyString(half_list)

        if n % 2 == 0:
            return new_half + new_half[::-1]
        else:
            return new_half + num[n // 2] + new_half[::-1]

    def listFromString(self, string_value: str) -> list:
        return list(string_value)

    def swapElements(self, list_value: list, index_one: int, index_two: int) -> None:
        list_value[index_one], list_value[index_two] = list_value[index_two], list_value[index_one]

    def sortSublistFromPosition(self, list_value: list, start_index: int) -> list:
        # Sort sublist from start_index to end in ascending order
        return list_value[:start_index] + sorted(list_value[start_index:])

    def joinListWithEmptyString(self, list_value: list) -> str:
        return "".join(list_value)
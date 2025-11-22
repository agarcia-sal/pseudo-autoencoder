class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half = num[: n // 2]
        half_list = list(half)
        k = -1
        l = -1

        for index in range(len(half_list) - 2, -1, -1):
            if half_list[index] < half_list[index + 1]:
                k = index
                break

        if k == -1:
            return ""

        for index in range(len(half_list) - 1, k, -1):
            if half_list[index] > half_list[k]:
                l = index
                break

        half_list[k], half_list[l] = half_list[l], half_list[k]
        half_list = half_list[: k + 1] + sorted(half_list[k + 1 :])
        new_half = "".join(half_list)

        if n % 2 == 0:
            return new_half + new_half[::-1]
        else:
            return new_half + num[n // 2] + new_half[::-1]
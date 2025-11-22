class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half = num[:n // 2]
        half_list = list(half)
        k = -1
        l = -1

        for i in range(len(half_list) - 2, -1, -1):
            if half_list[i] < half_list[i + 1]:
                k = i
                break

        if k == -1:
            return ""

        for i in range(len(half_list) - 1, k, -1):
            if half_list[i] > half_list[k]:
                l = i
                break

        half_list[k], half_list[l] = half_list[l], half_list[k]

        half_list = half_list[: k + 1] + sorted(half_list[k + 1 :])

        new_half = "".join(half_list)

        if n % 2 == 0:
            reversed_new_half = new_half[::-1]
            return new_half + reversed_new_half
        else:
            middle_character = num[n // 2]
            reversed_new_half = new_half[::-1]
            return new_half + middle_character + reversed_new_half
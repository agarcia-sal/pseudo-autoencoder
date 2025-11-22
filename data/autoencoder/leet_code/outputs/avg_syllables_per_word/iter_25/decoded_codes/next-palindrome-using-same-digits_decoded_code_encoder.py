class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half = num[:n // 2]
        half_list = list(half)
        k = -1
        l = -1

        # Find the largest index k such that half_list[k] < half_list[k + 1]
        for i in range(len(half_list) - 2, -1, -1):
            if half_list[i] < half_list[i + 1]:
                k = i
                break

        if k == -1:
            return ""

        # Find the largest index l > k such that half_list[l] > half_list[k]
        for i in range(len(half_list) - 1, k, -1):
            if half_list[i] > half_list[k]:
                l = i
                break

        # Swap half_list[k] and half_list[l]
        half_list[k], half_list[l] = half_list[l], half_list[k]
        # Sort the sublist after position k
        half_list = half_list[:k + 1] + sorted(half_list[k + 1:])
        new_half = "".join(half_list)

        if n % 2 == 0:
            return new_half + new_half[::-1]
        else:
            return new_half + num[n // 2] + new_half[::-1]
class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        if n == 0:
            return ""

        half_end = n // 2  # midpoint (not inclusive)

        # half is substring from position 0 to half_end - 1 (0-based indexing)
        # but if half_end == 0, half is empty
        half = num[:half_end]

        half_list = list(half)

        k = -1
        l = -1

        # Find k
        for i in range(len(half_list) - 2, -1, -1):
            if half_list[i] < half_list[i + 1]:
                k = i
                break

        if k == -1:
            return ""

        # Find l
        for i in range(len(half_list) - 1, k, -1):
            if half_list[i] > half_list[k]:
                l = i
                break

        # Swap half_list[k] and half_list[l]
        half_list[k], half_list[l] = half_list[l], half_list[k]

        # Sort the sublist after position k
        new_half_list = half_list[: k + 1] + sorted(half_list[k + 1 :])

        new_half = "".join(new_half_list)

        if n % 2 == 0:
            # even length: palindrome = new_half + reversed new_half
            return new_half + new_half[::-1]
        else:
            # odd length: palindrome = new_half + middle_char + reversed new_half
            middle_char = num[n // 2]
            return new_half + middle_char + new_half[::-1]
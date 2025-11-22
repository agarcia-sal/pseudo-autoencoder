class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half = num[:n // 2]

        half_list = list(half)
        k = -1
        l = -1

        # Find the rightmost character which is smaller than its next character
        for i in range(len(half_list) - 2, -1, -1):
            if half_list[i] < half_list[i + 1]:
                k = i
                break

        if k == -1:
            return ""

        # Find the rightmost character greater than half_list[k]
        for i in range(len(half_list) - 1, k, -1):
            if half_list[i] > half_list[k]:
                l = i
                break

        # Swap characters at positions k and l
        half_list[k], half_list[l] = half_list[l], half_list[k]

        # Sort the substring after position k
        half_list = half_list[:k+1] + sorted(half_list[k+1:])

        new_half = "".join(half_list)

        if (n // 2) * 2 == n:
            # Even length palindrome
            return new_half + new_half[::-1]
        else:
            # Odd length palindrome: keep middle character
            return new_half + num[n // 2] + new_half[::-1]
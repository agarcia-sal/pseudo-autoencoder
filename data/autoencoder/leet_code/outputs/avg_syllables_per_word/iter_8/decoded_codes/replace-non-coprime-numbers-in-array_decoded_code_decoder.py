from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = stack[-1] * num // g
                stack.pop()
            stack.append(num)
        return stack
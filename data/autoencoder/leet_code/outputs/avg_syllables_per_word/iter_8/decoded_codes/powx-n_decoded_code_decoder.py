class Solution:
    def myPow(self, x, n):
        def qpow(a, n):
            ans = 1
            while n != 0:
                if n & 1:
                    ans = ans * a
                a = a * a
                n = n // 2
            return ans

        if n >= 0:
            return qpow(x, n)
        else:
            return 1 / qpow(x, -n)
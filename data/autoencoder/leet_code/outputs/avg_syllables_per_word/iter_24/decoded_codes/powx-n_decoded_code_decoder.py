class Solution:
    def myPow(self, x, n):
        def qpow(a, n):
            ans = 1
            while n > 0:
                if n % 2 == 1:
                    ans *= a
                a *= a
                n //= 2
            return ans

        if n >= 0:
            return qpow(x, n)
        else:
            return 1 / qpow(x, -n)
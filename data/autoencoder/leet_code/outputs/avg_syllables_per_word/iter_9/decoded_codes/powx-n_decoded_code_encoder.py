class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            ans = 1.0
            while n != 0:
                if n % 2 == 1:
                    ans *= a
                a *= a
                n //= 2
            return ans

        return qpow(x, n) if n >= 0 else 1 / qpow(x, -n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            answer = 1.0
            while n > 0:
                if n % 2 == 1:
                    answer *= a
                a *= a
                n //= 2
            return answer

        if n >= 0:
            return qpow(x, n)
        else:
            return 1.0 / qpow(x, -n)
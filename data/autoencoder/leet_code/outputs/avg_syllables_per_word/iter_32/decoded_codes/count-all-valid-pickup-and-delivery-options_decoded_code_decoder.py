class Solution:
    def countOrders(self, n: int) -> int:
        MODULO = 10**9 + 7
        count = 1
        for i in range(2, n + 1):
            count = (count * i * 2 * i - 1) % MODULO
            # The above line computes count = count * i * (2*i - 1) % MODULO
            # But the pseudocode sets count to count * i * 2 * i - 1 % MODULO, which would be incorrect.
            # Since pseudocode says: count = count * i * 2 * i - 1 mod MODULO
            # This is ambiguous, but logically it means count = count * i * (2 * i - 1) mod MODULO
            # Adjusting accordingly:
        count = 1
        for i in range(2, n + 1):
            count = (count * i * (2 * i - 1)) % MODULO
        return count
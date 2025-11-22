class Solution:
    def countOrders(self, number_of_pairs: int) -> int:
        modulus = 10**9 + 1
        count = 1
        for index in range(2, number_of_pairs + 1):
            count = (count * index * 2 * index - 1) % modulus
        return count
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = self.initialize_prime_list(n)
        self.mark_zero_and_one_as_not_prime(is_prime)

        limit = int(math.sqrt(n)) + 1
        for start in range(2, limit):
            if is_prime[start]:
                for multiple in range(start * start, n, start):
                    is_prime[multiple] = False

        prime_count = self.sum_elements_of_list(is_prime)
        return prime_count

    def initialize_prime_list(self, n: int) -> list[bool]:
        return [True] * n

    def mark_zero_and_one_as_not_prime(self, is_prime: list[bool]) -> None:
        is_prime[0] = False
        is_prime[1] = False

    def sum_elements_of_list(self, boolean_list: list[bool]) -> int:
        counter = 0
        for element in boolean_list:
            if element:
                counter += 1
        return counter
import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly_numbers = [1]
        heap = [(prime, i) for i, prime in enumerate(primes)]
        heapq.heapify(heap)
        indices = [0] * len(primes)

        while len(ugly_numbers) < n:
            next_ugly, prime_idx = heapq.heappop(heap)
            if next_ugly != ugly_numbers[-1]:
                ugly_numbers.append(next_ugly)
            indices[prime_idx] += 1
            next_multiple = primes[prime_idx] * ugly_numbers[indices[prime_idx]]
            heapq.heappush(heap, (next_multiple, prime_idx))

        return ugly_numbers[-1]
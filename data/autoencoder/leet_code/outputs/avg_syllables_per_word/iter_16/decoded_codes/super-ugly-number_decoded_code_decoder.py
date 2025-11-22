import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly_numbers = [1]
        heap = [(p, i) for i, p in enumerate(primes)]
        heapq.heapify(heap)
        indices = [0] * len(primes)

        while len(ugly_numbers) < n:
            next_ugly, prime_index = heapq.heappop(heap)
            if next_ugly != ugly_numbers[-1]:
                ugly_numbers.append(next_ugly)
            indices[prime_index] += 1
            next_multiple = primes[prime_index] * ugly_numbers[indices[prime_index]]
            heapq.heappush(heap, (next_multiple, prime_index))

        return ugly_numbers[-1]
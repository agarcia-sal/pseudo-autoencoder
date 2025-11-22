import heapq

def nth_ugly_number(primes, n):
    ugly_numbers = [1]
    heap = [(p, i) for i, p in enumerate(primes)]
    heapq.heapify(heap)
    indices = [0] * len(primes)

    while len(ugly_numbers) < n:
        next_ugly, pi = heapq.heappop(heap)
        if next_ugly != ugly_numbers[-1]:
            ugly_numbers.append(next_ugly)
        indices[pi] += 1
        new_val = primes[pi] * ugly_numbers[indices[pi]]
        heapq.heappush(heap, (new_val, pi))

    return ugly_numbers[-1]
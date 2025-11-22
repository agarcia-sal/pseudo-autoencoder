import heapq

def can_construct(target):
    heap = [-x for x in target]
    heapq.heapify(heap)
    total = sum(target)

    while -heap[0] > 1:
        largest = -heapq.heappop(heap)
        rest = total - largest

        if largest <= rest or rest == 0:
            return False

        val = largest % rest
        if val == 0 and rest != 1:
            return False

        total = rest + val
        heapq.heappush(heap, -val)

    return True
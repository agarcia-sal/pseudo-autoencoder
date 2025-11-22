import heapq

class Solution:
    def medianSlidingWindow(self, list_of_numbers: list[int], window_size: int) -> list[float]:
        max_heap = []
        min_heap = []

        def balance_heaps():
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        def add_num(number: int):
            if not max_heap or number <= -max_heap[0]:
                heapq.heappush(max_heap, -number)
            else:
                heapq.heappush(min_heap, number)
            balance_heaps()

        def remove_num(number: int):
            # Remove number from appropriate heap and re-heapify
            # Since Python heaps do not support removal, we locate and remove the element by value.
            if number <= -max_heap[0]:
                try:
                    max_heap.remove(-number)
                    if max_heap:
                        heapq.heapify(max_heap)
                except ValueError:
                    pass
            else:
                try:
                    min_heap.remove(number)
                    if min_heap:
                        heapq.heapify(min_heap)
                except ValueError:
                    pass
            balance_heaps()

        def get_median() -> float:
            if len(max_heap) > len(min_heap):
                return float(-max_heap[0])
            return (-max_heap[0] + min_heap[0]) / 2

        # Initialize the heaps with the first window
        for index in range(window_size):
            add_num(list_of_numbers[index])

        medians = [get_median()]

        for index in range(window_size, len(list_of_numbers)):
            add_num(list_of_numbers[index])
            remove_num(list_of_numbers[index - window_size])
            medians.append(get_median())

        return medians
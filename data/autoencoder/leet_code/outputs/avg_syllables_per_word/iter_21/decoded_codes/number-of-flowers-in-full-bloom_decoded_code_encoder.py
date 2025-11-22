class Solution:
    def fullBloomFlowers(self, flowers, people):
        start_times = self.get_start_times(flowers)
        end_times = self.get_end_times(flowers)
        result = []
        for person in people:
            started = self.bisect_right(start_times, person)
            ended = self.bisect_left(end_times, person)
            count_in_bloom = started - ended
            result.append(count_in_bloom)
        return result

    def get_start_times(self, flowers):
        start_times = [start for start, _ in flowers]
        start_times.sort()
        return start_times

    def get_end_times(self, flowers):
        end_times = [end for _, end in flowers]
        end_times.sort()
        return end_times

    def bisect_right(self, sorted_list, value):
        low, high = 0, len(sorted_list)
        while low < high:
            mid = (low + high) // 2
            if sorted_list[mid] <= value:
                low = mid + 1
            else:
                high = mid
        return low

    def bisect_left(self, sorted_list, value):
        low, high = 0, len(sorted_list)
        while low < high:
            mid = (low + high) // 2
            if sorted_list[mid] < value:
                low = mid + 1
            else:
                high = mid
        return low
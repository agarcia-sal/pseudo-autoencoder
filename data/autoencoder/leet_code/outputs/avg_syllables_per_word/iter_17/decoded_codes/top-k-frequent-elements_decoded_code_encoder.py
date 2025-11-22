from collections import defaultdict

class Solution:
    def topKFrequent(self, list_of_numbers, integer_k):
        frequency_map = defaultdict(int)
        for number in list_of_numbers:
            frequency_map[number] += 1

        maximum_frequency = max(frequency_map.values()) if frequency_map else 0
        buckets = [[] for _ in range(maximum_frequency + 1)]

        for number, frequency in frequency_map.items():
            buckets[frequency].append(number)

        result_list = []
        for frequency in range(maximum_frequency, 0, -1):
            if buckets[frequency]:
                result_list.extend(buckets[frequency])
                if len(result_list) >= integer_k:
                    return result_list[:integer_k]
        return result_list
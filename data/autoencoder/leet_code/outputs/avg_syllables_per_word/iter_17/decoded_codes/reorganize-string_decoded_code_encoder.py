from collections import Counter
import heapq

def CreateMaxHeap(count):
    # Convert count dict into a max heap using negative frequencies
    return [(-freq, char) for char, freq in count.items()]

def ExtractMax(max_heap):
    # Pop element with maximum frequency (smallest negative number)
    freq, char = heapq.heappop(max_heap)
    return freq, char

def InsertMaxHeap(max_heap, freq, char):
    # Push element into max heap
    heapq.heappush(max_heap, (freq, char))

def JoinCharacters(list_of_characters):
    # Join list of characters into a single string
    return ''.join(list_of_characters)

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = CreateMaxHeap(count)
        heapq.heapify(max_heap)
        prev_char = None
        prev_freq = 0
        result = []

        # While there are characters to process in the heap or previous character frequency is negative
        while max_heap or prev_freq < 0:
            if not max_heap and prev_freq < 0:
                # Impossible to reorganize further without adjacent duplicates
                return ""
            freq, char = ExtractMax(max_heap)
            result.append(char)
            freq += 1  # increment frequency towards zero since freq is negative
            if prev_freq < 0:
                InsertMaxHeap(max_heap, prev_freq, prev_char)
            prev_char = char
            prev_freq = freq
        return JoinCharacters(result)
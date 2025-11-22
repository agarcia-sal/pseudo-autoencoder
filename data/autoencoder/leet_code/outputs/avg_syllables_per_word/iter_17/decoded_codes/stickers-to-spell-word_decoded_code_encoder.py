from collections import Counter, deque

class Solution:
    def minStickers(self, list_of_stickers, target_string):
        list_of_stickers = self.convert_stickers_to_counters(list_of_stickers)
        self.sort_stickers_by_max_frequency(list_of_stickers)

        queue = self.initialize_queue(target_string, 0)
        memoization_table = self.initialize_memo(target_string, 0)

        while queue:
            current_target, used_stickers = self.dequeue_element(queue)

            for sticker in list_of_stickers:
                if current_target[0] not in sticker:
                    continue
                remaining_characters_counter = self.counter_of_string(current_target)
                self.subtract_counter(remaining_characters_counter, sticker)

                new_target_string = self.string_from_sorted_elements_of_counter(remaining_characters_counter)

                if new_target_string == "":
                    return used_stickers + 1

                if new_target_string not in memoization_table:
                    memoization_table[new_target_string] = used_stickers + 1
                    self.enqueue_element(queue, new_target_string, used_stickers + 1)
        return -1

    def convert_stickers_to_counters(self, list_of_stickers):
        # Convert each sticker string into a Counter dictionary
        return [Counter(sticker) for sticker in list_of_stickers]

    def sort_stickers_by_max_frequency(self, list_of_stickers):
        # Sort stickers in descending order by their max character frequency
        list_of_stickers.sort(key=lambda c: max(c.values()) if c else 0, reverse=True)

    def initialize_queue(self, target_string, zero):
        # Initialize queue with a tuple (target_string, used_stickers_count)
        return deque([(target_string, zero)])

    def initialize_memo(self, target_string, zero):
        # Initialize memoization dict with target_string mapped to zero count
        return {target_string: zero}

    def dequeue_element(self, queue):
        # Pop element from the left side of the queue
        return queue.popleft()

    def counter_of_string(self, string_input):
        # Return Counter of characters in string_input
        return Counter(string_input)

    def subtract_counter(self, counter_one, counter_two):
        # Reduce counts in counter_one by counts in counter_two, no negatives allowed
        for char in counter_two:
            counter_one[char] = max(0, counter_one[char] - counter_two[char])
            if counter_one[char] == 0:
                del counter_one[char]

    def string_from_sorted_elements_of_counter(self, counter_input):
        # Convert Counter back to sorted string
        chars = []
        for char in sorted(counter_input):
            chars.append(char * counter_input[char])
        return "".join(chars)

    def enqueue_element(self, queue, new_target_string, used_stickers_count):
        # Add new element to the right side of the queue
        queue.append((new_target_string, used_stickers_count))
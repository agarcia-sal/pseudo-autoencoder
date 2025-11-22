from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, string_s: str, list_of_words: list[str]) -> int:
        waiting_dictionary = defaultdict(deque)
        for word in list_of_words:
            word_iterator = iter(word)
            first_character = next(word_iterator, None)
            if first_character is not None and first_character in string_s:
                waiting_dictionary[first_character].append(word_iterator)

        match_count = 0
        for c in string_s:
            if c in waiting_dictionary:
                current_iterators = waiting_dictionary[c]
                waiting_dictionary[c] = deque()
                while current_iterators:
                    it = current_iterators.popleft()
                    next_character = next(it, None)
                    if next_character is None:
                        match_count += 1
                    elif next_character in waiting_dictionary:
                        waiting_dictionary[next_character].append(it)
        return match_count
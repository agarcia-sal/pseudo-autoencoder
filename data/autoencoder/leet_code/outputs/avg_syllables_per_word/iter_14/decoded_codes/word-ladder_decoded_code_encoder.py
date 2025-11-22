from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        word_dict = defaultdict(list)
        word_length = len(beginWord)

        for word in wordList:
            for i in range(word_length):
                intermediate_word = word[:i] + '*' + word[i+1:]
                word_dict[intermediate_word].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, current_length = queue.popleft()

            for i in range(word_length):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]

                for word in word_dict.get(intermediate_word, []):
                    if word == endWord:
                        return current_length + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, current_length + 1))

                # Clear the intermediate list to prevent repeated processing
                word_dict[intermediate_word] = []

        return 0
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        word_dict = defaultdict(list)
        word_length = len(beginWord)

        for word in wordList:
            for index in range(word_length):
                intermediate_key = word[:index] + '_' + word[index+1:]
                word_dict[intermediate_key].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, current_length = queue.popleft()
            for index in range(word_length):
                intermediate_word = current_word[:index] + '_' + current_word[index+1:]
                for word in word_dict[intermediate_word]:
                    if word == endWord:
                        return current_length + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, current_length + 1))

        return 0
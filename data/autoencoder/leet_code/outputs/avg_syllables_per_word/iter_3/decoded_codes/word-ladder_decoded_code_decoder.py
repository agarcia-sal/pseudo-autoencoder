from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        word_dict = defaultdict(list)
        word_length = len(beginWord)

        for word in wordList:
            for i in range(word_length):
                key = word[:i] + "*" + word[i+1:]
                word_dict[key].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, length = queue.popleft()
            for i in range(word_length):
                intermediate = current_word[:i] + "*" + current_word[i+1:]
                for word in word_dict[intermediate]:
                    if word == endWord:
                        return length + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, length + 1))
                word_dict[intermediate] = []
        return 0
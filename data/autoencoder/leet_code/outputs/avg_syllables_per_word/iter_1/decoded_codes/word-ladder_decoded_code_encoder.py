from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    word_len = len(beginWord)
    word_dict = defaultdict(list)
    for w in wordList:
        for i in range(word_len):
            word_dict[w[:i] + "*" + w[i+1:]].append(w)

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        cur, dist = queue.popleft()
        for i in range(word_len):
            inter = cur[:i] + "*" + cur[i+1:]
            for w in word_dict[inter]:
                if w == endWord:
                    return dist + 1
                if w not in visited:
                    visited.add(w)
                    queue.append((w, dist + 1))

    return 0
from collections import defaultdict

def word_squares(words):
    prefix_map = defaultdict(list)
    word_len = len(words[0])
    for word in words:
        for i in range(word_len + 1):
            prefix_map[word[:i]].append(word)

    results = []

    def backtrack(square):
        if len(square) == word_len:
            results.append(square[:])
            return
        prefix = ''.join(word[len(square)] for word in square)
        for candidate in prefix_map.get(prefix, []):
            backtrack(square + [candidate])

    for word in words:
        backtrack([word])

    return results
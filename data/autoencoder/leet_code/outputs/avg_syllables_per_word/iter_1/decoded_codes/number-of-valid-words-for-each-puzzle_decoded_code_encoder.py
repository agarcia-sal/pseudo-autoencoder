from collections import defaultdict

def find_num_of_valid_words(words, puzzles):
    def to_mask(s):
        return sum(1 << (ord(c) - ord('a')) for c in s)

    word_count = defaultdict(int)
    for w in words:
        m = to_mask(w)
        if bin(m).count('1') <= 7:
            word_count[m] += 1

    res = []
    for p in puzzles:
        f = 1 << (ord(p[0]) - ord('a'))
        pm = to_mask(p[1:])
        c = word_count[f]
        sub = pm
        while sub != 0:
            c += word_count[sub | f]
            sub = (sub - 1) & pm
        res.append(c)

    return res
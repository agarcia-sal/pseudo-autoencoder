def longest_word(words):
    words.sort(key=lambda w: (len(w), w))
    valid = set()
    longest = ""
    for w in words:
        if len(w) == 1 or w[:-1] in valid:
            valid.add(w)
            if len(w) > len(longest):
                longest = w
    return longest
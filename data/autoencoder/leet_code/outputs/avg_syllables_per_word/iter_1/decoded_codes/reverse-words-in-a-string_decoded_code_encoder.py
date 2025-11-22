def reverse_words(s):
    words = s.split(' ')
    words.reverse()
    return ' '.join(words)
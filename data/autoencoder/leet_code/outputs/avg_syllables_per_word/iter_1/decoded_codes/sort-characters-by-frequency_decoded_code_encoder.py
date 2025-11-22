from collections import Counter

def frequency_sort(s):
    freq = Counter(s)
    sorted_chars = sorted(freq, key=lambda c: freq[c], reverse=True)
    return ''.join(char * freq[char] for char in sorted_chars)
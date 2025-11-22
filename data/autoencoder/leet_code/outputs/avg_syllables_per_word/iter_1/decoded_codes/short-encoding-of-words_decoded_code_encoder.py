rev_words = sorted(word[::-1] for word in words)
total = 0
for i in range(len(rev_words)):
    if i + 1 == len(rev_words) or not rev_words[i + 1].startswith(rev_words[i]):
        total += len(rev_words[i]) + 1
return total
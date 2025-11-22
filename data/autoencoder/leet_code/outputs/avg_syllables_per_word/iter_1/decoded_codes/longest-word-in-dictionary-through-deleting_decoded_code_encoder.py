def findLongestWord(s, dict):
    sorted_dict = sorted(dict, key=lambda w: (-len(w), w))
    for w in sorted_dict:
        if subseq(w, s):
            return w
    return ""

def subseq(word, s):
    it = iter(s)
    return all(c in it for c in word)
def replace_words(dictionary, sentence):
    dictionary.sort(key=len)
    words = sentence.split()

    def replace(w):
        for root in dictionary:
            if w.startswith(root):
                return root
        return w

    result = ' '.join(map(replace, words))
    return result
class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionary.sort(key=len)
        def replace(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word
        return ' '.join(replace(word) for word in sentence.split())
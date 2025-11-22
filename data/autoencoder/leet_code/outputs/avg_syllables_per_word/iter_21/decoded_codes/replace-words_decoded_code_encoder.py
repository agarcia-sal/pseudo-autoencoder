class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionary.sort(key=len)
        words = sentence.split()

        def replace(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word

        replaced_words = [replace(word) for word in words]
        result_sentence = ' '.join(replaced_words)
        return result_sentence
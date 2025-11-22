from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        words = sentence.split()

        def replace(word: str) -> str:
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word

        replaced_words = []
        for word in words:
            replaced_words.append(replace(word))
        result_sentence = ' '.join(replaced_words)
        return result_sentence
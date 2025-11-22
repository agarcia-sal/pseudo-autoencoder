from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)  # sort roots by length ascending
        words = sentence.split()

        def replace(word: str) -> str:
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word

        replaced_words = [replace(word) for word in words]
        return ' '.join(replaced_words)
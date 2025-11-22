class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        concatenated_sentence = " ".join(sentence) + " "
        total_length = len(concatenated_sentence)
        position = 0

        for _ in range(rows):
            position += cols
            if concatenated_sentence[position % total_length] == ' ':
                position += 1
            else:
                while position > 0 and concatenated_sentence[(position - 1) % total_length] != ' ':
                    position -= 1

        return position // total_length
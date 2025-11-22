class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        total_length = len(s)
        position = 0
        for _ in range(rows):
            position += cols
            if s[position % total_length] == " ":
                position += 1
            else:
                while position > 0 and s[(position - 1) % total_length] != " ":
                    position -= 1
        return position // total_length
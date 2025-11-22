class Solution:
    def boldWords(self, words: list[str], s: str) -> str:
        bold_marks = [False] * len(s)
        for word in words:
            start_position = s.find(word)
            while start_position != -1:
                for index in range(start_position, start_position + len(word)):
                    bold_marks[index] = True
                start_position = s.find(word, start_position + 1)

        result_collection = []
        i = 0
        while i < len(s):
            if bold_marks[i]:
                result_collection.append("<b>")
                while i < len(s) and bold_marks[i]:
                    result_collection.append(s[i])
                    i += 1
                result_collection.append("</b>")
            else:
                result_collection.append(s[i])
                i += 1

        return "".join(result_collection)
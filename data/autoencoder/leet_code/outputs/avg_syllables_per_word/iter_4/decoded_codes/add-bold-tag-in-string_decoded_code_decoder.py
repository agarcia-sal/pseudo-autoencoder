class Solution:
    def addBoldTag(self, s: str, words: list[str]) -> str:
        if not words:
            return s

        n = len(s)
        mask = [False] * n

        for word in words:
            start = 0
            word_len = len(word)
            while start <= n - word_len:
                pos = s.find(word, start)
                if pos == -1:
                    break
                for i in range(pos, pos + word_len):
                    mask[i] = True
                start = pos + 1

        result = []
        i = 0
        while i < n:
            if mask[i]:
                result.append("<b>")
                while i < n and mask[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1

        return "".join(result)
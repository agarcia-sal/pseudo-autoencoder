class Solution:
    def addBoldTag(self, s: str, words: list[str]) -> str:
        if len(words) == 0:
            return s

        n = len(s)
        mask = [False] * n

        for word in words:
            start = 0
            wl = len(word)
            while start <= n - wl:
                start = s.find(word, start)
                if start == -1:
                    break
                for i in range(start, start + wl):
                    mask[i] = True
                start += 1

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
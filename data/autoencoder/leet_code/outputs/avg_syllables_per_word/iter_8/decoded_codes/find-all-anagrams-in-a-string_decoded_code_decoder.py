class Solution:
    def findAnagrams(self, s, p):
        len_s = len(s)
        len_p = len(p)

        if len_p > len_s:
            return []

        p_count = {}
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        s_count = {}
        for i in range(len_p):
            ch = s[i]
            s_count[ch] = s_count.get(ch, 0) + 1

        anagrams = []

        if s_count == p_count:
            anagrams.append(0)

        for i in range(len_p, len_s):
            ch_in = s[i]
            s_count[ch_in] = s_count.get(ch_in, 0) + 1

            ch_out = s[i - len_p]
            s_count[ch_out] -= 1

            if s_count[ch_out] == 0:
                del s_count[ch_out]

            if s_count == p_count:
                anagrams.append(i - len_p + 1)

        return anagrams
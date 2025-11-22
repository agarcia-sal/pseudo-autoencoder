class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(p_i, s_i, mapping, used):
            if p_i == len(pattern) and s_i == len(s):
                return True
            if p_i == len(pattern) or s_i == len(s):
                return False

            c = pattern[p_i]
            if c in mapping:
                word = mapping[c]
                if not s.startswith(word, s_i):
                    return False
                return backtrack(p_i+1, s_i+len(word), mapping, used)
            else:
                for end in range(s_i+1, len(s)+1):
                    word = s[s_i:end]
                    if word in used:
                        continue
                    mapping[c] = word
                    used.add(word)
                    if backtrack(p_i+1, end, mapping, used):
                        return True
                    del mapping[c]
                    used.remove(word)
            return False

        return backtrack(0, 0, {}, set())
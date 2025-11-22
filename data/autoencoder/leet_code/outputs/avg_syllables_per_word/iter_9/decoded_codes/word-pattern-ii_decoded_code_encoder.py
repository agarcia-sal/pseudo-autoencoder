class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(p_index, s_index, mapping, used):
            if p_index == len(pattern) and s_index == len(s):
                return True
            if p_index == len(pattern) or s_index == len(s):
                return False

            current_char = pattern[p_index]
            if current_char in mapping:
                word = mapping[current_char]
                if s[s_index:s_index+len(word)] != word:
                    return False
                return backtrack(p_index + 1, s_index + len(word), mapping, used)
            else:
                for end in range(s_index + 1, len(s) + 1):
                    word = s[s_index:end]
                    if word in used:
                        continue
                    mapping[current_char] = word
                    used.add(word)
                    if backtrack(p_index + 1, end, mapping, used):
                        return True
                    del mapping[current_char]
                    used.remove(word)
                return False

        return backtrack(0, 0, {}, set())
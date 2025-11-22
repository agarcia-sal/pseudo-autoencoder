class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(p_idx, s_idx, mapping, used):
            if p_idx == len(pattern) and s_idx == len(s):
                return True
            if p_idx == len(pattern) or s_idx == len(s):
                return False

            current_char = pattern[p_idx]

            if current_char in mapping:
                word = mapping[current_char]
                if not s.startswith(word, s_idx):
                    return False
                return backtrack(p_idx + 1, s_idx + len(word), mapping, used)
            else:
                for end in range(s_idx + 1, len(s) + 1):
                    word = s[s_idx:end]
                    if word in used:
                        continue
                    mapping[current_char] = word
                    used.add(word)
                    if backtrack(p_idx + 1, end, mapping, used):
                        return True
                    del mapping[current_char]
                    used.remove(word)
                return False

        return backtrack(0, 0, {}, set())
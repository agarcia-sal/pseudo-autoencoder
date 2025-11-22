from typing import Dict, Set

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pattern_index: int, string_index: int, mapping: Dict[str, str], used: Set[str]) -> bool:
            if pattern_index == len(pattern) and string_index == len(s):
                return True
            if pattern_index == len(pattern) or string_index == len(s):
                return False

            current_char = pattern[pattern_index]
            if current_char in mapping:
                word = mapping[current_char]
                if s[string_index:string_index + len(word)] != word:
                    return False
                return backtrack(pattern_index + 1, string_index + len(word), mapping, used)
            else:
                for end in range(string_index + 1, len(s) + 1):
                    word = s[string_index:end]
                    if word in used:
                        continue
                    mapping[current_char] = word
                    used.add(word)
                    if backtrack(pattern_index + 1, end, mapping, used):
                        return True
                    del mapping[current_char]
                    used.remove(word)
                return False

        return backtrack(0, 0, {}, set())
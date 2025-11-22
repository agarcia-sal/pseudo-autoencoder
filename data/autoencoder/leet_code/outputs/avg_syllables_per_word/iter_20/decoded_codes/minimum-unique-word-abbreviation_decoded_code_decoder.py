from math import inf
from typing import List, Optional

class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        def is_valid_abbr(string_s: str, abbr: str) -> bool:
            i = 0
            j = 0
            n = len(string_s)
            m = len(abbr)
            while i < n and j < m:
                if abbr[j].isdigit():
                    if abbr[j] == '0':  # leading zero not allowed
                        return False
                    shift = 0
                    while j < m and abbr[j].isdigit():
                        shift = shift * 10 + int(abbr[j])
                        j += 1
                    i += shift
                else:
                    if i >= n or string_s[i] != abbr[j]:
                        return False
                    i += 1
                    j += 1
            return i == n and j == m

        def generate_abbrs(word: str, length: int, abbr: str = "", index: int = 0, skip_count: int = 0):
            if index == length:
                if skip_count > 0:
                    abbr += str(skip_count)
                abbrs.append(abbr)
                return
            # Abbreviate current char (increment skip_count)
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            # Keep current char (flush skip_count if > 0)
            new_abbr = abbr + (str(skip_count) if skip_count > 0 else "") + word[index]
            generate_abbrs(word, length, new_abbr, index + 1, 0)

        def find_unique_abbr() -> Optional[str]:
            length_target = len(target)
            for length in range(1, length_target + 1):
                abbrs.clear()
                generate_abbrs(target, length_target)
                min_abbr = None
                min_length = inf
                for abbr in abbrs:
                    # Check if abbr is unique abbreviation for target wrt filtered_dict
                    if all(not is_valid_abbr(word, abbr) for word in filtered_dict):
                        if len(abbr) < min_length:
                            min_length = len(abbr)
                            min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr
            return None

        filtered_dict = [word for word in dictionary if len(word) == len(target)]
        abbrs: List[str] = []
        result = find_unique_abbr()
        return result if result is not None else ""
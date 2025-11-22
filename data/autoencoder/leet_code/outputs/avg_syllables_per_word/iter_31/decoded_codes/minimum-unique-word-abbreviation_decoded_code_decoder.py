from math import inf
from typing import List

class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        def is_valid_abbr(s: str, abbr: str) -> bool:
            i, j = 0, 0
            n, m = len(s), len(abbr)
            while i < n and j < m:
                if abbr[j].isdigit():
                    if abbr[j] == '0':
                        return False
                    shift = 0
                    while j < m and abbr[j].isdigit():
                        shift = shift * 10 + int(abbr[j])
                        j += 1
                    i += shift
                else:
                    if s[i] != abbr[j]:
                        return False
                    i += 1
                    j += 1
            return i == n and j == m

        def generate_abbrs(word: str, length: int, abbr: str, index: int, skip_count: int):
            if index == length:
                if skip_count > 0:
                    abbr += str(skip_count)
                abbrs.append(abbr)
                return
            # Option 1: Abbreviate this character (increment skip_count)
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            # Option 2: Keep this character
            new_abbr = abbr + (str(skip_count) if skip_count > 0 else '') + word[index]
            generate_abbrs(word, length, new_abbr, index + 1, 0)

        def find_unique_abbr():
            length = len(target)
            for length_limit in range(1, length + 1):
                abbrs.clear()
                generate_abbrs(target, len(target), '', 0, 0)
                min_abbr = None
                min_length = inf
                for abbr in abbrs:
                    if len(abbr) > length_limit:
                        continue
                    is_unique = True
                    for word in filtered_dict:
                        if is_valid_abbr(word, abbr):
                            is_unique = False
                            break
                    if is_unique and len(abbr) < min_length:
                        min_length = len(abbr)
                        min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr
            return target  # fallback in edge cases

        filtered_dict = [word for word in dictionary if len(word) == len(target)]

        abbrs = []
        return find_unique_abbr()
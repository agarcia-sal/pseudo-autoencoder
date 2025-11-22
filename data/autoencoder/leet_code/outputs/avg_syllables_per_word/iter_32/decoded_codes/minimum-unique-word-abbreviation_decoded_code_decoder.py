from math import inf
from typing import List

class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        filtered_dict = [word for word in dictionary if len(word) == len(target)]
        abbrs = []

        def is_valid_abbr(s: str, abbr: str) -> bool:
            i, j = 0, 0
            len_s, len_abbr = len(s), len(abbr)
            while i < len_s and j < len_abbr:
                if abbr[j].isdigit():
                    if abbr[j] == '0':  # leading zero in number invalid
                        return False
                    shift = 0
                    while j < len_abbr and abbr[j].isdigit():
                        shift = shift * 10 + int(abbr[j])
                        j += 1
                    i += shift
                else:
                    if s[i] != abbr[j]:
                        return False
                    i += 1
                    j += 1
            return i == len_s and j == len_abbr

        def generate_abbrs(word: str, length: int, abbr: str = '', index: int = 0, skip_count: int = 0):
            if index == length:
                if skip_count > 0:
                    abbr += str(skip_count)
                abbrs.append(abbr)
                return
            # Skip current character
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            # Keep current character
            if skip_count > 0:
                generate_abbrs(word, length, abbr + str(skip_count) + word[index], index + 1, 0)
            else:
                generate_abbrs(word, length, abbr + word[index], index + 1, 0)

        def find_unique_abbr():
            length_target = len(target)
            for length in range(1, length_target + 1):
                abbrs.clear()
                generate_abbrs(target, length_target)
                min_abbr = None
                min_length = inf
                for abbr in abbrs:
                    # abbr length matches or smaller than length current loop iteration?
                    # Actually, no filtering in pseudocode on length of abbr here; just choose minimum length
                    if all(not is_valid_abbr(word, abbr) for word in filtered_dict):
                        if len(abbr) < min_length:
                            min_length = len(abbr)
                            min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr
            return None

        return find_unique_abbr() if filtered_dict else target